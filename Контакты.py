# -*- coding: utf-8 -*-

# Module author: @Yahikor0

from telethon import functions

from .. import loader, utils


@loader.tds
class Контакты недоСашка(loader.Module):
    """
    Commands:
    """

    strings = {
        "name": "Conthelper",
        "блок": "<b>{} теперь в ЧС.</b>",
        "анблок": "<b>{} теперь не в ЧС.</b>",
        "удалитьконтакт": "<b>{} удалён с контактов.</b>",
        "who_to_block": "<b>Кого блокать то?.</b>",
        "who_to_unblock": "<b>Кого разблокать то?.</b>",
        "who_to_delcontact": "<b>Кого удалить с контактов то?.</b>",
    }

    def __init__(self):
        self.me = None

    async def client_ready(self, client, db):
        self.db = db
        self.client = client
        self.me = await client.get_me(True)

    async def reportcmd(self, message):
        """User report for spam."""
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        if message.chat_id != (await message.client.get_me()).id and message.is_private:
            user = await message.client.get_entity(message.chat_id)
        else:
            if args:
                user = await message.client.get_entity(
                    args if not args.isnumeric() else int(args)
                )
            if reply:
                user = await message.client.get_entity(reply.sender_id)
            else:
                return await message.edit("<b>Who I must report?</b>")

        await message.client(functions.messages.ReportSpamRequest(peer=user.id))
        await message.edit("<b>You get report for spam!</b>")

    async def блокcmd(self, message):
        """Use: .блок to block this user."""
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        if message.chat_id != (await message.client.get_me()).id and message.is_private:
            user = await message.client.get_entity(message.chat_id)
        else:
            if reply:
                user = await message.client.get_entity(reply.sender_id)
            else:
                user = await message.client.get_entity(
                    int(args) if args.isnumeric() else args
                )
            if not user:
                await utils.answer(message, self.strings["who_to_block"])
                return
        await message.client(functions.contacts.BlockRequest(user))
        await utils.answer(message, self.strings["blocked"].format(user.first_name))

    async def анблокcmd(self, message):
        """Use: .unblock to unblock this user."""
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        if message.chat_id != (await message.client.get_me()).id and message.is_private:
            user = await message.client.get_entity(message.chat_id)
        else:
            if reply:
                user = await message.client.get_entity(reply.sender_id)
            else:
                user = await message.client.get_entity(
                    int(args) if args.isnumeric() else args
                )
            if not user:
                await utils.answer(message, self.strings["who_to_unblock"])
                return
        await message.client(functions.contacts.UnblockRequest(user))
        await utils.answer(message, self.strings["unblocked"].format(user.first_name))

    async def удалитьконтактcmd(self, message):
        """Use: .delcont to remove a user from contacts."""
        args = utils.get_args(message)
        reply = await message.get_reply_message()
        if message.chat_id != (await message.client.get_me()).id and message.is_private:
            user = await message.client.get_entity(message.chat_id)
        else:
            if reply:
                user = await message.client.get_entity(reply.sender_id)
            else:
                user = await message.client.get_entity(
                    int(args) if args.isnumeric() else args
                )
            if not user:
                await utils.answer(message, self.strings["who_to_delcontact"])
                return
        await message.client(functions.contacts.DeleteContactsRequest(id=[user.id]))
        await utils.answer(message, self.strings["delcontact"].format(user.first_name))

    async def добавитьcmd(self, message):
        """Use: .addcont to add somebody in contacts."""
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        if not args:
            return await message.edit("<b>Where args?.</b>")
        if not reply:
            return await message.edit("<b>Where reply?</b>")
        else:
            user = await message.client.get_entity(reply.sender_id)
        try:
            await message.client(
                functions.contacts.AddContactRequest(
                    id=user.id,
                    first_name=args,
                    last_name=" ",
                    phone="phone",
                    add_phone_privacy_exception=False,
                )
            )
            await message.edit(
                f"<code>{user.id}</code> теперь в контактах <code>{args}</code>"
            )
        except:
            return await message.edit(
                "<b>Something went wrong (come up with different reasons).</b>"
            )
