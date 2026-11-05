"""Reads Telegram updates (button presses and replies) and records approvals in approvals/<id>.json.
Also remembers the group chat id in config/telegram.json the first time the bot sees a group."""
import json, os, time, urllib.request, urllib.parse, pathlib

TOKEN = os.environ.get("TOKEN", "")
API = f"https://api.telegram.org/bot{TOKEN}/"
ROOT = pathlib.Path(".")
CFG = ROOT / "config/telegram.json"
STATE = ROOT / "config/telegram_offset.txt"

ERRORS = []
def call(method, **params):
    data = urllib.parse.urlencode({k: (json.dumps(v) if isinstance(v, (dict, list)) else v) for k, v in params.items()}).encode()
    try:
        with urllib.request.urlopen(API + method, data=data, timeout=30) as r:
            return json.loads(r.read())
    except Exception as e:
        body = getattr(e, "read", lambda: b"")().decode(errors="ignore")
        ERRORS.append(f"{method}: {e} {body}")
        return {"ok": False, "result": {"message_id": None} if method == "sendMessage" else []}

def load(p, default):
    return json.loads(p.read_text()) if p.exists() else default

def name_of(u):
    n = (u.get("first_name", "") + " " + u.get("last_name", "")).strip()
    return n or u.get("username", str(u.get("id")))

def main():
    if not TOKEN:
        print("no token"); return
    cfg = load(CFG, {})
    offset = int(STATE.read_text()) if STATE.exists() else 0
    upd = call("getUpdates", offset=offset + 1 if offset else 0, timeout=0,
               allowed_updates=["message", "callback_query", "my_chat_member", "channel_post"])
    for u in upd.get("result", []):
        offset = u["update_id"]
        # remember group / channel id when bot is added
        mcm = u.get("my_chat_member")
        if mcm and mcm["chat"]["type"] in ("group", "supergroup", "channel"):
            if not cfg.get("chat_id"):
                cfg["chat_id"] = mcm["chat"]["id"]; cfg["chat_title"] = mcm["chat"].get("title", "")
                call("sendMessage", chat_id=cfg["chat_id"],
                     text="✅ Reels agent ulandi. Tasdiq xabarlari shu yerga keladi.")
        msg = u.get("message") or u.get("channel_post")
        if msg and msg["chat"]["type"] in ("group", "supergroup", "channel") and not cfg.get("chat_id"):
            cfg["chat_id"] = msg["chat"]["id"]; cfg["chat_title"] = msg["chat"].get("title", "")
        # button press
        cq = u.get("callback_query")
        if cq:
            action, _, aid = cq.get("data", "").partition(":")
            f = ROOT / f"approvals/{aid}.json"
            rec = load(f, {"id": aid, "status": "pending", "comments": []})
            who = name_of(cq["from"])
            if rec["status"] in ("approved",):
                call("answerCallbackQuery", callback_query_id=cq["id"], text="Allaqachon tasdiqlangan")
                continue
            if action == "ok":
                rec.update(status="approved", by=who, at=int(time.time()))
                call("answerCallbackQuery", callback_query_id=cq["id"], text="Tasdiqlandi ✅")
                call("sendMessage", chat_id=cq["message"]["chat"]["id"], reply_to_message_id=cq["message"]["message_id"],
                     text=f"✅ {who} tasdiqladi. Agent keyingi qadamga o'tadi.")
            elif action == "edit":
                rec.update(status="changes_requested", by=who, at=int(time.time()))
                call("answerCallbackQuery", callback_query_id=cq["id"], text="Nima o'zgarsin? Xabarga javob (reply) yozing")
                m = call("sendMessage", chat_id=cq["message"]["chat"]["id"], reply_to_message_id=cq["message"]["message_id"],
                         text=f"✏️ {who}: nima o'zgarishi kerak? Shu xabarga javob (reply) qilib yozing.")
                rec["ask_message_id"] = m["result"]["message_id"]
            rec["message_id"] = cq["message"]["message_id"]
            f.parent.mkdir(exist_ok=True); f.write_text(json.dumps(rec, ensure_ascii=False, indent=1))
        # new topic request: "/mavzu <topic>" (empty = agent picks a topic)
        if msg and msg.get("text", "").split()[0:1] and msg["text"].split()[0].split("@")[0].lower() == "/mavzu":
            topic = msg["text"].partition(" ")[2].strip()
            q = load(ROOT / "queue/topics.json", [])
            item = {"id": f"t{msg['date']}", "topic": topic or "(agent tanlaydi)", "by": name_of(msg.get("from", {})),
                    "at": msg["date"], "status": "new"}
            q.append(item)
            (ROOT / "queue").mkdir(exist_ok=True)
            (ROOT / "queue/topics.json").write_text(json.dumps(q, ensure_ascii=False, indent=1))
            call("sendMessage", chat_id=msg["chat"]["id"], reply_to_message_id=msg["message_id"],
                 text=f"📝 Qabul qilindi: {item['topic']}\nSsenariy tayyor bo'lgach shu guruhga tasdiqqa keladi.")
        # reply with change comments
        if msg and msg.get("reply_to_message") and msg.get("text"):
            rid = msg["reply_to_message"]["message_id"]
            for f in (ROOT / "approvals").glob("*.json"):
                rec = load(f, {})
                if rid in (rec.get("message_id"), rec.get("ask_message_id")):
                    rec.setdefault("comments", []).append({"by": name_of(msg.get("from", {})), "text": msg["text"], "at": msg["date"]})
                    if rec.get("status") != "approved":
                        rec["status"] = "changes_requested"
                    f.write_text(json.dumps(rec, ensure_ascii=False, indent=1))
    STATE.write_text(str(offset))
    CFG.write_text(json.dumps(cfg, ensure_ascii=False, indent=1))

try:
    main()
except Exception:
    import traceback; ERRORS.append(traceback.format_exc())
pathlib.Path("config").mkdir(exist_ok=True)
pathlib.Path("config/poll_status.txt").write_text(time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()) + "\n" + ("\n".join(ERRORS) or "OK"))
