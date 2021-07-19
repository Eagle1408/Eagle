from .. import loader, utils

@loader.tds
class RPMod(loader.Module):
    """Модуль RPMod by недоСашка"""
    strings = {'name': 'RPMod недоСашка'}

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
        await message.edit("<b>• чмок\n• чпок\n• кусь\n• обнять\n• шлеп\n• ударить\n• кинуть камень\n• выкинуть\n• закопать\n• выкопать\n• запопать\n• послать\n• сосать\n• отлизать\n• выебать\n• пожениться\n• развод\n• уложить/лечь спать\n• ❤️\n• рука и сердце\n• кинуть на карту\n• купить еду/чипсы\n• купить пиво\n• выпить пиво\n\nНовинка:\n\n• Связать\n• Придушить\n• Возбудить\n• Погладить\n• Утопить в молоке\n• Кончить на\n• Сделать чик-чик\n• Кастрировать\n• Пустить слюни на\n• Почесать за ухом\n• Поцеловать/чмокнуть в лобик\n• Плюнуть в лицо\n• Харкнуть\n• Прогнать\n• Бросить в канаву\n• Обсосать\n• Скинуть фотку\n• Обоссать\n• Рыгнуть в лицо\n• Показать жопу/сиськи/хуй\n\n Пока всё \n\n Есть идеи для модуля?\nПиши сюда: https://t.me/ideidlyamodulei18</b>")

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
                    if message.text.lower() == "связать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> связал(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "придушить":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> придушил(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "возбудить":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> возбудил(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "погладить":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> погладил(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "утопить в молоке":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> утопил(-а) в молоке <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "кончить на":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> кончил(-а) на <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "сделать чик-чик":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> сделал(-а) чик-чик <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "кастрировать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> кастрировал(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "пустить слюни на":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> пустил(-а) слюни на <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "почесать за ухом":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> почесал(-а) за ухом <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "поцеловать в лобик":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> поцеловал(-а) в лобик <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "плюнуть в лицо":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> плюнул(-а) в лицо <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "чмокнуть в лобик":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> чмокнул(-а) в лобик <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "харкнуть":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> харкнул(-а) в <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "прогнать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> прогнал(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "обсосать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> обсосал(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "скинуть фотку":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> скинул(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "обоссать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> обоссал(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "рыгнуть в лицо":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> рыгнул(-а) в лицо  <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "показать жопу":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> показал(-а) жопу <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "показать сиськи":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> показала сиськи <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "показать хуй":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> показал хуй <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "бросить в канаву":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> бросил(-а) в канаву <a href=tg://user?id={user.id}>{user.first_name}</a>")
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
                    if message.text.lower() == "уебать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> уебал(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "отсосать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> отсосал(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "отлизать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> отлизал(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "задушить":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> задушил(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "украсть":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> украл(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "погладить":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> погладил(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "притянуть":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> притянул(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "изнасиловать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "отпороть":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "отнести":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "кастрировать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "научить сосать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "обмануть":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "отрезать пипиську":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "утонуть в глазах":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "станцевать для":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "обматерить":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "обхуесосить":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "подарить девственность":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "забрать девственность":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "лешить девственности":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "покрестить":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "наказать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "пригласить на поминки":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "возбудить":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "пригласить на свадьбу":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "бухнуть с:
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "потанцевать с":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "пыпить час с":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "позвать в гости":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> позвал(-а) в гости <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "похоронить":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> похоронил(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "выгнать из свадьбы":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> выгнал(-а) из свадьбы <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "пригласить на др":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> пригласил(-а) на др <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "выгнать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> выгнал(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "отнести домой":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> отнёс(-ла) домой <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "родить детей от":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> родил(-а) детей от <a href=tg://user?id={user.id}>{user.first_name}</a>")
 
        except: pass
