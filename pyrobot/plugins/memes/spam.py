from telethon import events
import asyncio
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="spam (.*)"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.2
    animation_ttl = range(0, 16)
    input_str = event.pattern_match.group(1)
    if input_str == "netflix":
        await event.edit("<b>ZELOS & OXY REFILLING</b>/n/n✅ <b>Netflix</b>, 1 mese di durata garantita, nessun tipo di blocco!/n/n📑 Prezzi bassissimi, e grandi quantita al giorno, massimo ordine di 200 netflix al giorno!/n/n👨‍💻 Per altre <b>info</b> contattare @ListaDeiDesideri o @Zelos00")
