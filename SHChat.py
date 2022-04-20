"""

█▀ █░█ ▄▀█ █▀▄ █▀█ █░█░█
▄█ █▀█ █▀█ █▄▀ █▄█ ▀▄▀▄▀

    Copyleft 2022 t.me/shadow_modules
    This module is free software
    You can edit this module
"""
"""
======================================================================
Admin Tools for Friendly-Telegram UserBot.
Copyright (C) 2020 @Fl1yd, @AtiksX.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
======================================================================
"""

import io, logging, time
from .. import loader, utils
from telethon.tl.types import Message
from telethon.errors import (ChatAdminRequiredError, UserAdminInvalidError, FloodWaitError, PhotoCropSizeSmallError)
from telethon.tl.types import (ChatAdminRights, ChatBannedRights)
from telethon.tl.functions.channels import (EditAdminRequest, EditBannedRequest, EditPhotoRequest)
from telethon.tl.functions.messages import EditChatAdminRequest
import asyncio
logger = logging.getLogger(__name__)

# meta developer: @shadow_geektg, @CakesTwix, @Fl1yd

# ================== КОНСТАНТЫ ========================

PROMOTE_RIGHTS = ChatAdminRights(post_messages=True,
                                 add_admins=None,
                                 invite_users=True,
                                 change_info=None,
                                 ban_users=True,
                                 delete_messages=True,
                                 pin_messages=True,
                                 edit_messages=True)

DEMOTE_RIGHTS = ChatAdminRights(post_messages=None,
                                add_admins=None,
                                invite_users=None,
                                change_info=None,
                                ban_users=None,
                                delete_messages=None,
                                pin_messages=None,
                                edit_messages=None)

UNMUTE_RIGHTS = ChatBannedRights(until_date=None,
                                 view_messages=None,
                                 send_messages=False,
                                 send_media=False,
                                 send_stickers=False,
                                 send_gifs=False,
                                 send_games=False,
                                 send_inline=False,
                                 embed_links=False)

BANNED_RIGHTS = ChatBannedRights(until_date=None,
                                 view_messages=True,
                                 send_messages=True,
                                 send_media=True,
                                 send_stickers=True,
                                 send_gifs=True,
                                 send_games=True,
                                 send_inline=True,
                                 embed_links=True)

UNBAN_RIGHTS = ChatBannedRights(until_date=None,
                                view_messages=None,
                                send_messages=None,
                                send_media=None,
                                send_stickers=None,
                                send_gifs=None,
                                send_games=None,
                                send_inline=None,
                                embed_links=None)

# =====================================================

@loader.tds
class SHChatMod(loader.Module):
    """✉ Module for chat rules"""

    strings = {"name": "SHChat",
    'rules_n': '<b>😪 You didnt make the rules</b>',
    'clicks': '😗 Click', 
    'rulesch': '<b>👾 Rules for this chat</b>',
    'upd_rul': '<b>✅ Rules updated</b>',
    'promote_none': '<b>🛑 No one to promote</b>',
    'who': '<b>❔ Who is it?</b>',
    'not_admin': '<b>🚫 Im not an admin here</b>',
    'promoted': '<b>💥 {} elevated as an administrator.\nRank: {}</b>',
    'wtf_is_it': '<b>❔ What is this?</b>',
    'this_isn`t_a_chat': '<b>❗ This is not a chat!</b>',
    'demote_none': '<b>🛑 No one to demote</b>',
    'demoted': '<b>😥 {} Demoted in admin privileges</b>',
    'pinning': '<b>✉ Pin...</b>',
    'pin_none': '<b>📛 Reply to a message to pin it</b>',
    'unpinning': '<b>💨 Unpin...</b>',
    'unpin_none': '<b>🚫 Nothing to unpin</b>',
    'no_rights': '<b>⚖ I do not have rights</b>',
    'pinned': '<b>✔ Pinned successfully</b>',
    'unpinned': '<b>💚 Unpinned successfully</b>',
    'can`t_kick': '<b>❗ Cant kick user</b>',
    'kicking': '<b>⏳ Kick...</b>',
    'kick_none': '<b>✌ Nobody to kick</b>',
    'kicked': '<b>👨‍⚖️ {} kicked from chat</b>',
    'kicked_for_reason': '🌧<b>{} kicked from chat\n🚔 Reason {}.</b>',
    'banning': '<b>🥱 Ban...</b>',
    'banned': '<b>😰 {} banned from chat</b>',
    'ban_none': '<b>🚫 No one to give a ban</b>',
    'unban_none': '<b>❗ Someone to unban</b>',
    'unbanned': '<b>😊 {} unbanned in chat</b>',
    'mute_none': '<b>😥 No one to give mute</b>',
    'muted': '😗 <b>{} now in mute on </b>',
    'no_args': '<b>🚫 Invalid arguments</b>',
    'unmute_none': '<b>🛑 There is no one to unmute</b>',
    'unmuted': '<b>✔ {} no longer in the mute</b>',
    'no_reply': '<b>❗ No replay</b>',
    'deleting': '<b>🧹 Deletion...</b>',
    'no_args_or_reply':'<b>📛 No arguments or replay</b>',
    'deleted': '<b>✨ All messages from {} removed</b>',
    'del_u_search': '<b>👀 Search for deleted accounts...</b>',
    'del_u_kicking': '<b>🔰 Kick deleted accounts...</b>'
    }
    
    strings_ru = {
    'rules_n': '<b>😪 Вы не ввели правила</b>',
    'clicks': '😗 Клик',
    'rulesch': '👾 Правила этого чата',
    'upd_rul': '<b>✅ Правила обновлены</b>',
    'promote_none': '<b>🛑 Некого повышать</b>',
    'who': '<b>❔ Кто это?</b>',
    'not_admin': '<b>🚫 Я здесь не админ</b>',
    'promoted': '<b>💥 {} повышен в правах администратора.\nРанг: {}</b>',
    'wtf_is_it': '<b>❔ Что это?</b>',
    'this_isn`t_a_chat': '<b>❗ Это не чат!</b>',
    'demote_none': '<b>🛑 Некого понижать</b>',
    'demoted': '<b>😥 {} понижен в правах администратора</b>',
    'pinning': '<b>✉ Пин...</b>',
    'pin_none': '<b>📛 Ответь на сообщение чтобы закрепить его</b>',
    'unpinning': '<b>💨 Анпин...</b>',
    'unpin_none': '<b>🚫 Нечего откреплять</b>',
    'no_rights': '<b>⚖ У меня нет прав</b>',
    'pinned': '<b>✔ Закреплено успешно!</b>',
    'unpinned': '<b>💚 Откреплено успешно!</b>',
    'can`t_kick': '<b>❗ Не могу кикнуть пользователя</b>',
    'kicking': '<b>⏳ Кик...</b>',
    'kick_none': '<b>✌ Некого кикать</b>',
    'kicked': '<b>👨‍⚖️ {} кикнут из чата</b>',
    'kicked_for_reason': '🌧<b>{} кикнут из чата\n🚔 Причина: {}.</b>',
    'banning': '<b>🥱 Бан...</b>',
    'banned': '<b>😰 {} забанен в чате</b>',
    'banned_for_reason': '<b>🥺 {} забанен в чате\n🕳 Причина: {}</b>', 
    'ban_none': '<b>🚫 Некому давать бан</b>',
    'unban_none': '<b>❗ Некого разбанивать</b>',
    'unbanned': '<b>😊 {} разбанен в чате</b>',
    'mute_none': '<b>😥 Некому давать мут</b>',
    'muted': '😗 <b>{} теперь в муте на </b>',
    'no_args': '<b>🚫 Неверно указаны аргументы</b>',
    'unmute_none': '<b>🛑 Некого размучивать</b>',
    'unmuted': '<b>✔ {} теперь не в муте</b>',
    'no_reply': '<b>❗ Нет реплая</b>',
    'deleting': '<b>🧹 Удаление...</b>',
    'no_args_or_reply':'<b>📛 Нет аргументов или реплая</b>',
    'deleted': '<b>✨ Все сообщения от {} удалены</b>',
    'del_u_search': '<b>👀 Поиск удалённых аккаунтов...</b>',
    'del_u_kicking': '<b>🔰 Кик удалённых аккаунтов...</b>'
    }

    def __init__(self):
        self.config = loader.ModuleConfig("rules", "", lambda: "You rules")

    async def client_ready(self, client, db):
        self._db = db
        self._client = client

    @loader.unrestricted
    async def rulescmd(self, message: Message) -> None:
        """Command to display the rules that have been added"""
        if len(self.config["rules"]) == 0:
            await utils.answer(message, self.strings("rules_n", message))
            return
        await self.inline.form(
            text=self.strings("rulesch"),
            message=message,
            disable_security=True,
            reply_markup=[
                [
                    {
                        "text": self.strings("clicks"),
                        "callback": self.inline__callAnswer,
                    }
                ]
            ],
        )
    
    async def inline__callAnswer(self, call) -> None:
        rules = self._db.get("Rules", "rules")
        if rules != 0:
            await call.answer(rules[0], show_alert=True)
        else:
            await call.answer(self.strings("rules_n"), show_alert=True)


    async def crulescmd(self, message: Message) -> None:
        """Add or changing rules"""
        args = utils.get_args_raw(message)
        self.rules = [args]
        self._db.set("Rules", "rules", self.rules)
        await utils.answer(message, self.strings("upd_rul"))
        await asyncio.sleep(3)
        await message.delete()
        return

    
    async def promotecmd(self, promt):
        """The .promote command elevates the user to admin rights.\nUsage: .promote <@ or replay> <rank>."""
        if promt.chat:
            try:
                args = utils.get_args_raw(promt).split(' ')
                reply = await promt.get_reply_message()
                rank = 'admin'
                chat = await promt.get_chat()
                if not chat.admin_rights and not chat.creator:
                    return await utils.answer(promt, self.strings('not_admin', promt))
                if reply:
                    args = utils.get_args_raw(promt)
                    if args:
                        rank = args
                    else:
                        rank = rank
                    user = await utils.get_user(reply)
                else:
                    user = await promt.client.get_entity(args[0])
                    if len(args) == 1:
                        rank = rank
                    elif len(args) >= 2:
                        rank = utils.get_args_raw(promt).split(' ', 1)[1]
                try:
                    await promt.client(EditAdminRequest(promt.chat_id, user.id, PROMOTE_RIGHTS, rank))
                except ChatAdminRequiredError:
                    return await utils.answer(promt, self.strings('no_rights', promt))
                else:
                    return await utils.answer(promt, self.strings('promoted', promt).format(user.first_name, rank))
            except ValueError:
                return await utils.answer(promt, self.strings('no_args', promt))
        else:
            return await utils.answer(promt, self.strings('this_isn`t_a_chat', promt))


    async def demotecmd(self, demt):
        """The .demote command demotes a user in administrative privileges.\nUsage: .demote <@ or replay>."""
        if demt.chat:
            try:
                reply = await demt.get_reply_message()
                chat = await demt.get_chat()
                if not chat.admin_rights and not chat.creator:
                    return await utils.answer(demt, self.strings('not_admin', demt))
                if reply:
                    user = await utils.get_user(await demt.get_reply_message())
                else:
                    args = utils.get_args(demt)
                    if not args:
                        return await utils.answer(demt, self.strings('demote_none', demt))
                    user = await demt.client.get_entity(args[0])
                if not user:
                    return await utils.answer(demt, self.strings('who', demt))
                try:
                    if demt.is_channel:
                        await demt.client(EditAdminRequest(demt.chat_id, user.id, DEMOTE_RIGHTS, ""))
                    else:
                        await demt.client(EditChatAdminRequest(demt.chat_id, user.id, False))
                except:
                    return await utils.answer(demt, self.strings('no_rights', demt))
                else:
                    return await utils.answer(demt, self.strings('demoted', demt).format(user.first_name))
            except:
                return await utils.answer(demt, self.strings('wtf_is_it'))
        else:
            return await utils.answer(demt, self.strings('this_isn`t_a_chat', demt))


    async def pincmd(self, pint):
        """The .pin command pins a message in the chat.\nUsage: .pin <replay>"""
        if pint.chat:
            reply = await pint.get_reply_message()
            if not reply:
                return await utils.answer(pint, self.strings('pin_none', pint))
            await utils.answer(pint, self.strings('pinning', pint))
            try:
                await pint.client.pin_message(pint.chat, message=reply.id, notify=False)
            except ChatAdminRequiredError:
                return await utils.answer(pint, self.strings('no_rights', pint))
            await utils.answer(pint, self.strings('pinned', pint))
        else:
            await utils.answer(pint, self.strings('this_isn`t_a_chat', pint))


    async def unpincmd(self, unpon):
        """The .unpin command unpins a pinned message in a chat.\nUsage: .unpin <replay>"""
        if unpon.chat:
            await utils.answer(unpon, self.strings('unpinning', unpon))
            try:
                await unpon.client.pin_message(unpon.chat, message=None, notify=None)
            except ChatAdminRequiredError:
                await utils.answer(unpon, self.strings('no_rights', unpon))
                return
            await utils.answer(unpon, self.strings('unpinned', unpon))
        else:
            await utils.answer(unpon, self.strings('this_isn`t_a_chat', unpon))
    

    async def kickcmd(self, kock):
        """The .kick command kicks the user.\nUsage: .kick <@ or replay>."""
        if kock.chat:
            try:
                args = utils.get_args_raw(kock).split(' ')
                reason = utils.get_args_raw(kock)
                reply = await kock.get_reply_message()
                chat = await kock.get_chat()
                reason = False
                if not chat.admin_rights and not chat.creator:
                    return await utils.answer(kock, self.strings('not_admin', kock))
                if reply:
                    user = await utils.get_user(reply)
                    args = utils.get_args_raw(kock)
                    if args:
                        reason = args
                else:
                    user = await kock.client.get_entity(args[0])
                    if args:
                        if len(args) == 1:
                            args = utils.get_args_raw(kock)
                            user = await kock.client.get_entity(args)
                            reason = False
                        elif len(args) >= 2:
                            reason = utils.get_args_raw(kock).split(' ', 1)[1]
                try:
                    await utils.answer(kock, self.strings('kicking', kock))
                    await kock.client.kick_participant(kock.chat_id, user.id)
                except ChatAdminRequiredError:
                    return await utils.answer(kock, self.strings('no_rights', kock))
                else:
                    if reason:
                        return await utils.answer(kock, self.strings('kicked_for_reason', kock).format(user.first_name, reason))
                    if reason == False:
                        return await utils.answer(kock, self.strings('kicked', kock).format(user.first_name))
            except ValueError:
                return await utils.answer(kock, self.strings('no_args', kock))
        else:
            return await utils.answer(kock, self.strings('this_isn`t_a_chat', kock))
            

    async def bancmd(self, bon):
        """The .ban command will ban the user.\nUsage: .ban <@ or replay>."""
        if bon.chat:
            try:
                args = utils.get_args_raw(bon).split(' ')
                reason = utils.get_args_raw(bon)
                reply = await bon.get_reply_message()
                chat = await bon.get_chat()
                reason = False
                if not chat.admin_rights and not chat.creator:
                    return await utils.answer(bon, self.strings('not_admin', bon))
                if reply:
                    user = await utils.get_user(reply)
                    args = utils.get_args_raw(bon)
                    if args:
                        reason = args
                else:
                    user = await bon.client.get_entity(args[0])
                    if args:
                        if len(args) == 1:
                            args = utils.get_args_raw(bon)
                            user = await bon.client.get_entity(args)
                            reason = False
                        elif len(args) >= 2:
                            reason = utils.get_args_raw(bon).split(' ', 1)[1]
                try:
                    await utils.answer(bon, self.strings('banning', bon))
                    await bon.client(EditBannedRequest(bon.chat_id, user.id, ChatBannedRights(until_date=None, view_messages=True)))
                except ChatAdminRequiredError:
                    return await utils.answer(bon, self.strings('no_rights', bon))
                except UserAdminInvalidError:
                    return await utils.answer(bon, self.strings('no_rights', bon))
                if reason:
                    return await utils.answer(bon, self.strings('banned_for_reason', bon).format(user.first_name, reason))
                if reason == False:
                    return await utils.answer(bon, self.strings('banned', bon).format(user.first_name))
            except ValueError:
                return await utils.answer(bon, self.strings('no_args', bon))
        else:
            return await utils.answer(bon, self.strings('this_isn`t_a_chat', bon))


    async def unbancmd(self, unbon):
        """The .unban command to unban a user.\nUsage: .unban <@ or replay>."""
        if unbon.chat:
            reply = await unbon.get_reply_message() 
            chat = await unbon.get_chat()
            if not chat.admin_rights and not chat.creator:
                return await utils.answer(unbon, self.strings('not_admin', unbon))
            if reply:
                user = await utils.get_user(reply)
            else:
                args = utils.get_args(unbon)
                if not args:
                    return await utils.answer(unbon, self.strings('unban_none', unbon))
                user = await unbon.client.get_entity(args[0])
            if not user:
                return await utils.answer(unbon, self.strings('who', unbon))
            logger.debug(user)
            try:
                await unbon.client(EditBannedRequest(unbon.chat_id, user.id, ChatBannedRights(until_date=None, view_messages=False)))
            except:
                return await utils.answer(unbon, self.strings('no_rights', unbon))
            else:
                return await utils.answer(unbon, self.strings('unbanned', unbon).format(user.first_name))
        else:
            return await utils.answer(unbon, self.strings('this_isn`t_a_chat', unbon))


    async def mutecmd(self, mot):
        """The .mute command mutes the user.\nUsage: .mute <@ or replay> <time (1m, 1h, 1d)>."""
        if mot.chat:
            try:
                reply = await mot.get_reply_message()
                chat = await mot.get_chat()
                if not chat.admin_rights and not chat.creator:
                    return await utils.answer(mot, self.strings('not_admin', mot))
                if reply:
                    user = await utils.get_user(reply)

                else:
                    who = utils.get_args_raw(mot).split(' ')
                    user = await mot.client.get_entity(who[0])

                    if len(who) == 1:
                        timee = ChatBannedRights(until_date=True, send_messages=True)
                        await mot.client(EditBannedRequest(mot.chat_id, user.id, timee))
                        await mot.edit('<b>🌧 {} now in mute</b>'.format(user.first_name))
                        return

                    if not user:
                        return await utils.answer(mot, self.strings('mute_none', mot))
                    if user:
                        tim = who[1]
                        if tim:
                            if len(tim) != 2:
                                return await utils.answer(mot, self.strings('no_args', mot))
                            num = ''
                            t = ''
                            for q in tim:
                                if q.isdigit():
                                    num += q
                                else:
                                    t += q

                            text = f'<b>{num}'
                            if t == 'm':
                                num = int(num) * 60
                                text += ' minute(-s).</b>'
                            elif t == 'h':
                                num = int(num) * 3600
                                text += ' day(-s/).</b>'
                            elif t == 'd':
                                num = int(num) * 86400
                                text += ' hour(-s).</b>'
                            else:
                                return await utils.answer(mot, self.strings('no_args', mot))
                            timee = ChatBannedRights(until_date=time.time() + int(num), send_messages=True)
                            try:
                                await mot.client(EditBannedRequest(mot.chat_id, user.id, timee))
                                await utils.answer(mot, self.strings('muted', mot).format(utils.escape_html(user.first_name)) + text)
                                return
                            except:
                                await utils.answer(mot, self.strings('no_rights', mot))
                        else:
                            timee = ChatBannedRights(until_date=True, send_messages=True)
                            await mot.client(EditBannedRequest(mot.chat_id, user.id, timee))
                            await mot.edit('<b>🌧 {} now in mute</b>'.format(user.first_name))
                            return

                logger.debug(user)
                tim = utils.get_args(mot)
                if tim:
                    if len(tim[0]) < 2:
                        return await utils.answer(mot, self.strings('no_args', mot))
                    num = ''
                    t = ''
                    for q in tim[0]:
                        if q.isdigit():
                            num += q
                        else:
                            t += q

                    text = f'<b>{num}'
                    if t == 'm':
                        num = int(num) * 60
                        text += ' minute(-s).</b>'
                    elif t == 'd':
                        num = int(num) * 86400
                        text += ' day(-s) .</b>'
                    elif t == 'h':
                        num = int(num) * 3600
                        text += ' hour(-s).</b>'
                    else:
                        return await utils.answer(mot, self.strings('no_args', mot))
                    timee = ChatBannedRights(until_date=time.time() + int(num), send_messages=True)
                    try:
                        await mot.client(EditBannedRequest(mot.chat_id, user.id, timee))
                        await utils.answer(mot, self.strings('muted', mot).format(utils.escape_html(user.first_name)) + text)
                        return
                    except:
                        await utils.answer(mot, self.strings('no_rights', mot))
                else:
                    timee = ChatBannedRights(until_date=True, send_messages=True)
                    await mot.client(EditBannedRequest(mot.chat_id, user.id, timee))
                    await mot.edit('<b>🌧 {} now in mute</b>'.format(user.first_name))
                    return
            except:
                await utils.answer(mot, self.strings('mute_none', mot))
                return
        else:
            await utils.answer(mot, self.strings('this_isn`t_a_chat', mot))


    async def unmutecmd(self, unmot):
        """The .unmute command to unmute the user.\nUsage: .unmute <@ или реплай>."""
        if unmot.chat:
            try:
                reply = await unmot.get_reply_message() 
                chat = await unmot.get_chat()
                if not chat.admin_rights and not chat.creator:
                    return await utils.answer(unmot, self.strings('not_admin', unmot))
                if reply:
                    user = await utils.get_user(reply)
                else:
                    args = utils.get_args(unmot)
                    if not args:
                        return await utils.answer(unmot, self.strings('unmute_none', unmot))
                    user = await unmot.client.get_entity(args[0])
                if not user:
                    return await utils.answer(unmot, self.strings('who', unmot))
                try:
                    await unmot.client(EditBannedRequest(unmot.chat_id, user.id, UNMUTE_RIGHTS))
                except:
                    return await utils.answer(unmot, self.strings('not_admin', unmot))
                else:
                    return await utils.answer(unmot, self.strings('unmuted', unmot).format(user.first_name))
            except:
                return await utils.answer(unmot, self.strings('wtf_is_it', unmot))
        else:
            return await utils.answer(unmot, self.strings('this_isn`t_a_chat', unmot))


    async def deluserscmd(self, delus):
        """The .delusers command shows a list of all deleted accounts in a chat.\nUsage: .delusers <clean>."""
        if not delus.is_group:
            await utils.answer(delus, self.strings('this_isn`t_a_chat', delus))
            return
        con = utils.get_args_raw(delus)
        del_u = 0
        del_status = '<b>😊 No deleted accounts, chat cleared</b>'
        if con != "clean":
            await utils.answer(delus, self.strings('del_u_search', delus))
            async for user in delus.client.iter_participants(delus.chat_id):
                if user.deleted:
                    del_u += 1
            if del_u == 1:
                del_status = f"<b>😥 Found {del_u} deleted chat account, clear them with </b><code>.delusers clean</code><b>.</b>"
            if del_u > 0:
                del_status = f"<b>😥 Found {del_u} deleted chat accounts, clear them with</b><code>.delusers clean</code><b>.</b>"
            await delus.edit(del_status)
            return
        chat = await delus.get_chat()
        if not chat.admin_rights and not chat.creator:
            return await utils.answer(delus, self.strings('not_admin', delus))
        await utils.answer(delus, self.strings('del_u_kicking', delus))
        del_u = 0
        del_a = 0
        async for user in delus.client.iter_participants(delus.chat_id):
            if user.deleted:
                try:
                    await delus.client(EditBannedRequest(delus.chat_id, user.id, BANNED_RIGHTS))
                except ChatAdminRequiredError:
                    return await utils.answer(delus, self.strings('no_rights', delus))
                except UserAdminInvalidError:
                    del_u -= 1
                    del_a += 1
                await delus.client(EditBannedRequest(delus.chat_id, user.id, UNBAN_RIGHTS))
                del_u += 1
        if del_u == 1:
            del_status = f"<b>Kicked {del_u} remote account</b>"
        if del_u > 0:
            del_status = f"<b>Kicked {del_u} remote accounts</b>"

        if del_a == 1:
            del_status = f"<b>Kicked {del_u} remote account\n"
            f"{del_a} remote admin account not kicked"
        if del_a > 0:
            del_status = f"<b>Kicked {del_u} remote accounts\n"
            f"{del_a} deleted admin accounts are not kicked</b>"
        await delus.edit(del_status)