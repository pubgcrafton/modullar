# meta developer: @netuzbfan

import asyncio
import time

from telethon.tl import functions

from .. import loader, utils


@loader.tds
class AutoSoatMod(loader.Module):
    """Profilingiz uchun avtomatik soat ⏱"""

    strings = {
        "name": "Avtomatik soat",
        "invalid_args": "<b>Nimadir xato ketdi iltimos o'rnatish qo'llanmasini o'qing!</b>",
        "missing_time": "<b>Oldin soatni bioga o'rnatishingiz kerak!</b>",
        "enabled_bio": "<b>Soat bioga muvoffaqiyatli o'rnatildi✅</b>",
        "bio_not_enabled": "<b>Soat bioga o'rnatilmadi❗️</b>",
        "disabled_bio": "<b>Biodagi soat bekor qilindi 🗑</b>",
        "enabled_name": "<b>Soat Nikga muvoffaqiyatli o'rnatildi✅</b>",
        "name_not_enabled": "<b>soat nikga o'rnatilmadi❗️</b>",
        "disabled_name": "<b>Nikdagi soat bekor qilindi🗑</b>",
    }

    def __init__(self):
        self.bio_enabled = False
        self.name_enabled = False
        self.raw_bio = None
        self.raw_name = None

    async def client_ready(self, client, db):
        self.client = client

    async def avtobiocmd(self, message):
        """Bioga soat o'rnatish | soat avtomatik o'zgaradi, Foydalanish:
        .avtobio '<bio uchun so'zlar, joriy vaqt {time}' joriy vaqtni anglatadi>'"""

        msg = utils.get_args(message)
        if len(msg) != 1:
            return await utils.answer(message, self.strings("invalid_args", message))
        raw_bio = msg[0]
        if "{time}" not in raw_bio:
            return await utils.answer(message, self.strings("missing_time", message))

        self.bio_enabled = True
        self.raw_bio = raw_bio
        await self.allmodules.log("start_autobio")
        await utils.answer(message, self.strings("enabled_bio", message))

        while self.bio_enabled:
            current_time = time.strftime("Sana %d.%m.%y | Soat %H:%M Daqiqa o'tdi ")
            bio = raw_bio.format(time=current_time)
            await self.client(functions.account.UpdateProfileRequest(about=bio))
            await asyncio.sleep(60)

    async def stopavtobiocmd(self, message):
        """Biodagi soatni Bekor qilish."""

        if self.bio_enabled is False:
            return await utils.answer(message, self.strings("bio_not_enabled", message))
        self.bio_enabled = False
        await self.allmodules.log("stop_autobio")
        await utils.answer(message, self.strings("disabled_bio", message))
        await self.client(
            functions.account.UpdateProfileRequest(about=self.raw_bio.format(time=""))
        )
    
    async def avtonamecmd(self, message):
        """Telegram nikga vaqt o'rnatish | vaqt avtomatik ravishda  o'zgaradi 
O'rnatish .avtoname 'nik uchun so'z {time}' joriy vaqtni anglatadi'"""

        msg = utils.get_args(message)
        if len(msg) != 1:
            return await utils.answer(message, self.strings("invalid_args", message))
        raw_name = msg[0]
        if "{time}" not in raw_name:
            return await utils.answer(message, self.strings("missing_time", message))

        self.name_enabled = True
        self.raw_name = raw_name
        await self.allmodules.log("start_autoname")
        await utils.answer(message, self.strings("enabled_name", message))

        while self.name_enabled:
            current_time = time.strftime("%H:%M")
            name = raw_name.format(time=current_time)
            await self.client(functions.account.UpdateProfileRequest(first_name=name))
            await asyncio.sleep(60)
    
    async def stopavtonamecmd(self, message):
        """Nikdagi soatni bekor qilish."""

        if self.name_enabled is False:
            return await utils.answer(
                message, self.strings("name_not_enabled", message)
            )
        self.name_enabled = False
        await self.allmodules.log("stop_autoname")
        await utils.answer(message, self.strings("disabled_name", message))
        await self.client(
            functions.account.UpdateProfileRequest(
                first_name=self.raw_name.format(time="")
            )
        )
