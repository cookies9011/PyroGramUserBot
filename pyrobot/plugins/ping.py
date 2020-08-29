"""Telegram Ping / Pong Speed
Syntax: .ping"""

from pyrogram import Client, Filters

from datetime import datetime

from pyrobot import COMMAND_HAND_LER


# -- Constants -- #
SPAM = "ZELOS & OXY REFILLING/n/n✅ Netflix, 1 mese di durata garantita, nessun tipo di blocco!/n/n📑 Prezzi bassissimi, e grandi quantita al giorno, massimo ordine di 200 netflix al giorno!/n/n👨‍💻 Per altre info contattare @ListaDeiDesideri o @Zelos00"
# -- Constants End -- #


@Client.on_message(Filters.command("alive", COMMAND_HAND_LER)  & Filters.me)
async def check_alive(client, message):
    await message.edit(ALIVE)


@Client.on_message(Filters.command("helpme", COMMAND_HAND_LER)  & Filters.me)
async def help_me(client, message):
    await message.edit(HELP)


@Client.on_message(Filters.command("ping", COMMAND_HAND_LER)  & Filters.me)
async def ping(client, message):
    start_t = datetime.now()
    await message.edit("Pong!")
    end_t = datetime.now()
    time_taken_s = (end_t - start_t).microseconds / 1000
    await message.edit(f"Pong!\n{time_taken_s}μs")


@Client.on_message(Filters.command("repo", COMMAND_HAND_LER)  & Filters.me)
async def repo(client, message):
    await message.edit(REPO)
