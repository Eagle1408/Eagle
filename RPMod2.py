from .. import loader, utils

@loader.tds
class RPMod(loader.Module):
    """Модуль RPMod by недоСашка 2"""
    strings = {'name': 'RPMod недоСашка v2.0'}

    async def client_ready(self, client, db):
        self.db = db
        self.db.set("RPMod", "status", True)

    async def rpmod2cmd(self, message):
        """Используй: .rpmod чтобы включить/выключить RP режим."""
        status = self.db.get("RPMod", "status")
        if status is not False:
            self.db.set("RPMod", "status", False)
            await message.edit("<b>RP Режим <code>выключен</code></b>")
        else:
            self.db.set("RPMod", "status", True)
            await message.edit("<b>RP Режим <code>включен</code></b>")

    async def рплист2cmd(self, message):
        """Используй: .рплист2 чтобы посмотреть список рп команд."""
        await message.edit("<b>•Представь что тут ссылка на эти команды•</b>")

    async def watcher(self, message):
        status = self.db.get("RPMod", "status")
        reply = await message.get_reply_message()
        try:
            user = await message.client.get_entity(reply.sender_id)
            me = (await message.client.get_me())
            if status is not False:
                if message.sender_id == me.id:
                    if message.text.lower() == "обидется на":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> обиделся(-ась) на <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "уебать об стенку":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> уебал(-ала) об стенку <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "послать додому":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> послал(-а) додому <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "послать до хаты":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> послал(-а) до хаты <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "дать в попку":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> дал(-а) в попку <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "прийти к":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> пришёл(-шла) к <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "чмокнуть в попку":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> чмокнул(-а) в попку <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "чмок в пупок":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> чмокнул(а) в пупок <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "облизать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> облизал(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "позвать на турнир":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> позвал(-а) на турнир <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "похвалить":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> похвалил(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "сделать могилу для":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> сделал(-а) могилу для <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "спать рядом с":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> спит рядом с <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "выбросить на улицу":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> выбросил(-а) на улицу <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "выгнать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> выгнал(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "ударить тапком":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> ударил(-а) тапком <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "попросить деньги у":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> попросил(-а) деньги у <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "пожелать спокойной ночи":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> пожелал(-а) спокойной ночи <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "подарить носок":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> подарил(-а) носок <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "приручить":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> приручил(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "присвоить":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> присвоил(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "подарить свободу":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> подарил(-а) свободу <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "взять в рабство":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> взял(-а) в рабство <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "поклонится":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> поклонился(-ась) перед <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "извинится":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> извиняеться перед <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "собрать вещи":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> собрал(-а) вещи <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "больше не общаться":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> больше не общаеться с <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "захотеть выебать в очко":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> захотел(-а) выебать в очко <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "накормить пельменями":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> накормил(-а) пельменями <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "одеть штаны":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> одел(-а) штаны на <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "снять штаны":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> снял(-а) штаны с <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "снять кофту":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> снял(-а) кофту с <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "связать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> связал(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                           except: pass
