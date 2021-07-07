from .. import loader, utils

@loader.tds
class RPMod(loader.Module):
    """Модуль RPMod by недоСашка"""
    strings = {'name': 'RPMod by недоСашка'}

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

    async def рплистcmd(self, message):
        """Используй: .рплист чтобы посмотреть список рп команд."""
        await message.edit("<b>• чмок\n• чпок\n• кусь\n• обнять\n• шлеп\n• ударить\n• кинуть камень\n• выкинуть\n• закопать\n• выкопать\n• запопать\n• послать\n• сосать\n• отлизать\n• выебать\n• пожениться\n• развод\n• уложить/лечь спать\n• ❤️\n• рука и сердце\n• кинуть на карту\n• купить еду/чипсы\n• купить пиво\n• выпить пиво\n\nНовинка:\n\n• Связать\n• Придушить\n• Возбудить\n• Погладить\n• Утопить в молоке\n• Кончить на\n• Сделать чик-чик\n• Кастрировать\n• Пустить слюни на\n• Почесать за ухом\n• Поцеловать/чмокнуть в лобик\n• Плюнуть в лицо\n• Харкнуть\n•  Прогнать\n• Обсосать\n• Скинуть фотку\n• Обоссать\n• Рыгнуть в лицо\n• Показать жопу/сиськи/хуй\n\n Пока всё \n\n Есть идеи для модуля?\nПиши сюда: https://t.me/ideidlyamodulei18</b>")

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
                    if message.text.lower() == "купить пиво":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> купил(-а) пиво <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "выпить пиво":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> выпил(-а) пиво с <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "послать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> послал(-а) нахуй <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "сосать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> отсосал(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "пожениться":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> поженился(-а) на <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "развод":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> развёлся(-ась) с <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "уложить спать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> уложил(-а) спать <a href=tg://user?id={user.id}>{user.first_name}</a>")
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
                    if message.text.lower() == "Cвязать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> связал(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "Придушить":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> придушил(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "Возбудить":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> возбудил(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "Погладить":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> погладил(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "Утопить в молоке":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> утопил(-а) в молоке <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "Кончить на":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> кончил(-а) на <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "Сделать чик-чик":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> сделал(-а) чик-чик <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "Кастрировать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> кастрировал(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "Пустить слюни на":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> пустил(-а) слюни на <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "Почесать за ухом":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> почесал(-а) за ухом <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "Поцеловать в лобик":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> поцеловал(-а) в лобик <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "Плюнуть в лицо":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> плюнул(-а) в лицо <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "Чмокнуть в лобик":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> чмокнул(-а) в лобик <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "Харкнуть":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> харкнул(-а) в <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "Прогнать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> прогнал(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "Обсосать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> обсосал(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "Скинуть фотку":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> скинул(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "Обоссать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> обоссал(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "Рыгнуть в лицо":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> рыгнул(-а) в лицо  <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "Показать жопу":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> показал(-а) жопу <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "Показать сиськи":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> показала сиськи <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "Показать хуй":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> показал хуй <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "смех":
                        await message.edit(f"АХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХА")  
        except: pass
