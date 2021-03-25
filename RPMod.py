from .. import loader, utils

@loader.tds
class RPMod(loader.Module):
    """Модуль RPMod by недоСашка"""
    strings = {'name': 'RPMod недоСашка Edition'}

    async def client_ready(self, client, db):
        self.db = db
        self.db.set("RPMod", "status", True)

    async def rpmodcmd(self, message):
        """Используй: .rpmod чтобы включить/выключить RP режим."""
        status = self.db.get("RPMod", "status")
        if status is not False:
            self.db.set("RPMod", "status", False)
            await message.edit("<b>RP Режим <code>выключен</code></b>")
        else:
            self.db.set("RPMod", "status", True)
            await message.edit("<b>RP Режим <code>включен</code></b>")

    async def rplistcmd(self, message):
        """Используй: .rplist чтобы посмотреть список рп команд."""
        await message.edit("<b>• чмок\n• чпок\n• кусь\n• обнять\n• шлеп\n• ударить\n• закопать\n• послать\n• сосать\n• отлизать\n• выебать\n• пожениться\n• уложить/лечь спать\n• ❤️\n• рука и сердце\n• кинуть на карту\n• купить еду/чипсы\n• купить пиво\n• выпить пиво.</b>")

    async def watcher(self, message):
        status = self.db.get("RPMod", "status")
        reply = await message.get_reply_message()
        try:
            user = await message.client.get_entity(reply.sender_id)
            me = (await message.client.get_me())
            if status is not False:
                if message.sender_id == me.id:
                    if message.text.lower() == "чмок":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> чмокнул(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "чпок":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> чпокнул(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "кусь":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> кусьнул(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "обнять":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> обнял(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "шлеп":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> шлепнул(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "ударить":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> ударил(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "закопать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> запопал(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")    
                    if message.text.lower() == "выебать":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> выебал(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")    
                    if message.text.lower() == "купить пиво":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> купил(-а) пиво <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "выпить пиво":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> выпил(-а) пиво с <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "послать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> послал(-а) нахуй <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "сосать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> отсосал(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "отлизать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> отлизал(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")    
                    if message.text.lower() == "пожениться":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> поженился(-а) на <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "уложить спать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> уложил(-ла) спать <a href=tg://user?id={user.id}>{user.first_name}</a>")    
                    if message.text.lower() == "лечь спать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> лег(-ла) спать с <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "купить еду":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> купил(-а) еду для <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "❤️":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> признался(-ась) в любви <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "рука и сердце":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> просит руку и сердце у <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "кинуть на карту":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> отправил(-а) деньги на карту <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "купить чипсы":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> купил(-а) чипсы <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "смех":
                        await message.edit(f"АХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХА")  
        except: pass

