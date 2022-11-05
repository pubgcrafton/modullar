#           ▄▀█ █▀▄▀█ █▀█ █▀█ █▀▀
#           █▀█ █░▀░█ █▄█ █▀▄ ██▄
#
#             © Copyright 2022
#
#          https://t.me/the_farkhodov
#
# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# meta pic: https://te.legra.ph/file/388e1b26a46a8c439e479.png
# meta banner: https://raw.githubusercontent.com/AmoreForever/assets/master/Createlinks.jpg
# meta developer: @DONIYOR_TM


from .. import loader, utils, security



@loader.tds
class HavolaMod(loader.Module):
    """Kerakli ijtimoiy tarmoqqa havolalar yarating"""

    strings = {
        "name": "Havola",
        "youtube": "🫂 <b>Siz uchun maxsus YouTube havolasi.</b>\n\n",
        "google": "🫂 <b>Siz uchun maxsus Google havolasi.</b>\n\n",
        "github": "🫂 <b>Siz uchun maxsus Github havolasi.</b>\n\n",
        "pornhub": "🫂 <b>Siz uchun maxsus Pornhub havolasi.</b>\n\n",
        "telegram": "🫂 <b>Siz uchun maxsus Telegram havolasi.</b>\n\n",
        "4pda": "🫂 <b>Siz uchun maxsus 4pda havolasi.</b>\n\n",
        
    }

    async def ytcmd(self, message):
        """<matn> YouTube havolasini yarating"""
        text = utils.get_args_raw(message) 
        s = f"<b>✏ Kalit so'z: <code>{text}</code></b>"
        if await self.allmodules.check_security(
            message,
            security.OWNER | security.SUDO,
        ):
            
            try:
                await self.inline.form(
                    self.strings("youtube", message) + s,
                    reply_markup=[                        
                        [{"text": "♨️ Havola", "url": f"https://m.youtube.com/results?sp=mAEA&search_query={text}"}],
                        [{"text": "🔻 Yopish", "action": f"close"}],
                        
                    ],
                    message=message,
                )
            except Exception:
                await utils.answer(message, self.strings("join", message))
                

    async def gugcmd(self, message):
        """<matn> Google havolasini yarating"""
        text = utils.get_args_raw(message) 
        s = f"<b>✏ Kalit so'z: <code>{text}</code></b>"
        if await self.allmodules.check_security(
            message,
            security.OWNER | security.SUDO,
        ):
            
            try:
                await self.inline.form(
                    self.strings("google", message) + s,
                    reply_markup=[
                        [{"text": "🛰 Havola", "url": f"https://www.google.com/search?q={text}"}],
                        [{"text": "🔻 Yopish", "action": f"close"}],
                    ],
                    message=message,
                )
            except Exception:
                await utils.answer(message, self.strings("join", message))
                
    async def ghcmd(self, message):
        """<matn> GitHub havolasini yarating"""
        text = utils.get_args_raw(message) 
        s = f"<b>✏ Kalit so'z: <code>{text}</code></b>"
        if await self.allmodules.check_security(
            message,
            security.OWNER | security.SUDO,
        ):
            
            try:
                await self.inline.form(
                    self.strings("github", message) + s,
                    reply_markup=[
                        [{"text": "🛰 Havola", "url": f"https://github.com/search?q={text}"}],
                        [{"text": "🔻 Yopish", "action": f"close"}],
                    ],
                    message=message,
                )
            except Exception:
                await utils.answer(message, self.strings("join", message))
           
    async def phcmd(self, message):
        """<matn> PornHub havolasini yarating"""
        text = utils.get_args_raw(message) 
        s = f"<b>✏ Kalit so'z: <code>{text}</code></b>"
        if await self.allmodules.check_security(
            message,
            security.OWNER | security.SUDO,
        ):
            
            try:
                await self.inline.form(
                    self.strings("pornhub", message) + s,
                    reply_markup=[
                        [{"text": "🛰 Havola", "url": f"https://rt.pornhub.com/video/search?search={text}"}],
                        [{"text": "🔻 Yopish", "action": f"close"}],
                    ],
                    message=message,
                )
            except Exception:
                await utils.answer(message, self.strings("join", message))
                
    async def tgcmd(self, message):
        """<matn> Telegram havolasini yarating"""
        text = utils.get_args_raw(message) 
        s = f"<b>✏ Kalit so'z: <code>{text}</code></b>"
        if await self.allmodules.check_security(
            message,
            security.OWNER | security.SUDO,
        ):
            
            try:
                await self.inline.form(
                    self.strings("telegram", message) + s,
                    reply_markup=[
                        [{"text": "🛰 Havola", "url": f"tg://search?query={text}"}],
                        [{"text": "🔻 Yopish", "action": f"close"}],
                    ],
                    message=message,
                )
            except Exception:
                await utils.answer(message, self.strings("join", message))
 
    async def pdacmd(self, message):
        """<matn> 4pda havolasini yarating"""
        text = utils.get_args_raw(message) 
        s = f"<b>✏ Kalit so'z: <code>{text}</code></b>"
        if await self.allmodules.check_security(
            message,
            security.OWNER | security.SUDO,
        ):
            
            try:
                await self.inline.form(
                    self.strings("4pda", message) + s,
                    reply_markup=[
                        [{"text": "🛰 Havola", "url": f"https://4pda.to/forum/index.php?act=search&source=all&forums=316&subforums=1&query={text}"}],
                        [{"text": "🔻 Yopish", "action": f"close"}],
                    ],
                    message=message,
                )
            except Exception:
                await utils.answer(message, self.strings("join", message))               