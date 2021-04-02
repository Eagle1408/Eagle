from .. import loader, utils

@loader.tds
class AntiTagMod(loader.Module):
    """Режим AntiTag."""
    strings = {'name': 'AntiTag'}

    async def client_ready(self, client, db):
        self.db = db

    async def atoncmd(self, message):
        """Включить режим AntiTag: .aton <текст или реплай>."""
        atst = self.db.get("AntiTag", "status", False)
        msg = self.db.get("AntiTag", "sets", {})
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        msg.update({"message": None})
        msg.update({"is_reply": None})
        if reply:
            msg.update({"message": f"{reply.chat_id}|{reply.id}"})
            msg.update({"is_reply": True})
        else:
            if args: msg.update({"message": args})
            else: msg.update({"message": "<b>Занят.</b>\n Статус обновлён: В сети. Причина: сработал антитег."})
            msg.update({"is_reply": False})
        self.db.set("AntiTag", "status", True)
        self.db.set("AntiTag", "sets", msg) 
        return await message.edit("<b>Арёл</b> Улетел.")

    async def atoffcmd(self, message):
        """Выключить режим AntiTag: .atoff."""
        self.db.set("AntiTag", "status", False)
        self.db.set("AntiTag", "sets", {})
        return await message.edit("<b>Арёл</b> Прилетел.")
        
    async def watcher(self, message):
        try:
            atst = self.db.get("AntiTag", "status", False)
            msg = self.db.get("AntiTag", "sets", {})
            if message.mentioned:
                if msg["is_reply"] == True:
                    chat = int(msg["message"].split("|")[0])
                    id = int(msg["message"].split("|")[1])
                    msg = await message.client.get_messages(chat, ids=id)
                else:
                    msg = msg["message"]
                await message.client.send_message(message.to_id, msg, reply_to=message)
        except: pass
