from .. import loader, utils, main
from telethon.tl.types import Message, User, Channel


def get_link(user: User or Channel) -> str:
    return (
        f"tg://user?id={user.id}"
        if isinstance(user, User)
        else (
            f"tg://resolve?domain={user.username}"
            if getattr(user, "username", None)
            else ""
        )
    )


def get_full_name(user: User or Channel) -> str:
    return (
        user.title
        if isinstance(user, Channel)
        else (
            f"{user.first_name} "
            + (user.last_name if getattr(user, "last_name", False) else "")
        )
    )


@loader.tds
class OwonersMod(loader.Module):
    """Control permissions through userbot"""

    strings = {
        "name": "Владельцы",
        "owner": " <b>Вы стали владельцем.</b>",
        "not_owner": "<b>Вы больше не владелец.</b>",
        "no_owner": "<b>Вы не владелец.</b>",
        "no_reply": "<b>Реплей где?</b>",
        "owners": "<b>Владельцы:</b>\n{}",
    }

    async def client_ready(self, client, db) -> None:
        self.client = client
        self.db = db
        if getattr(main, "__version__", (0, 0, 0)) < (2, 0, 2):
            raise Exception("This module is compatible only with GeekTG 2.0.2+")

    @loader.owner
    async def owoneraddcmd(self, message: Message) -> None:
        """<reply> [-f] - Give user userbot's owner"""
        reply = await message.get_reply_message()
        if not reply:
            await utils.answer(message, self.strings("no_reply"))
            return

        user = reply.sender_id
        user = int(str(user)[4:]) if str(user).startswith("-100") else int(user)

        try:
            if user not in self.client.dispatcher.security._owner:
                self.client.dispatcher.security._owner = list(
                    set(self.client.dispatcher.security._owner + [user])
                )
        except Exception:
            pass

        if "-f" in utils.get_args_raw(message):
            self.db.set(
                "friendly-telegram.security",
                "owner",
                list(
                    set(self.db.get("friendly-telegram.security", "owner", []) + [user])
                ),
            )

        await utils.answer(message, self.strings("owner"))

    @loader.owner
    async def owonerlistcmd(self, message: Message) -> None:
        """List current userbot owners"""
        header = self.strings("owners")

        try:
            temp = self.client.dispatcher.security._owner
        except Exception:
            temp = []

        perm = self.db.get("friendly-telegram.security", "owner", [])
        result = ""

        for owner in list(set(temp + perm)):
            try:
                u = await self.client.get_entity(owner)
            except Exception:
                continue

            prefix = ("⏱" if owner in temp and owner not in perm else "⚱️") + (
                "👤" if isinstance(u, User) else "📣"
            )

            user = f'{prefix} <b><a href="{get_link(u)}">{get_full_name(u)}</a></b>\n'
            result += user

        await utils.answer(message, header.format(result))

    @loader.owner
    async def owonerrmcmd(self, message: Message) -> None:
        """<reply> - Remove sudo from user"""
        reply = await message.get_reply_message()
        if not reply:
            await utils.answer(message, self.strings("no_reply"))
            return

        user = reply.sender_id
        user = int(str(user)[4:]) if str(user).startswith("-100") else int(user)

        try:
            if user not in self.client.dispatcher.security._owner:
                await utils.answer(message, self.strings("no_owner"))
        except Exception:
            pass

        self.db.set(
            "friendly-telegram.security",
            "owner",
            list(
                set(self.db.get("friendly-telegram.security", "owner", []))
                - set([user])
            ),
        )

        try:
            await self.client.dispatcher.security.update_owners()
        except Exception:
            pass

        await utils.answer(message, self.strings("not_owner"))