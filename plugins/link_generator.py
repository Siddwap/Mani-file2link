#(©)NovaXTG

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from bot import Bot
from config import *
from shortzy import Shortzy
from helper_func import encode, get_message_id

@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('batch'))
async def batch(client: Client, message: Message):
    while True:
        try:
            first_message = await client.ask(text = "Forward the First Message from DB Channel (with Quotes)..\n\nor Send the DB Channel Post Link", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        f_msg_id = await get_message_id(client, first_message)
        if f_msg_id:
            break
        else:
            await first_message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is taken from DB Channel", quote = True)
            continue

    while True:
        try:
            second_message = await client.ask(text = "Forward the Last Message from DB Channel (with Quotes)..\nor Send the DB Channel Post link", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        s_msg_id = await get_message_id(client, second_message)
        if s_msg_id:
            break
        else:
            await second_message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is taken from DB Channel", quote = True)
            continue


    string = f"get-{f_msg_id * abs(client.db_channel.id)}-{s_msg_id * abs(client.db_channel.id)}"
    base64_string = await encode(string)
    link = await get_shortlink(f"https://t.me/{client.username}?start={base64_string}")
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("💸 Yᴏᴜ ᴄᴀɴ sʜᴀʀᴇ ᴛʜɪs ᴛᴏ ᴀɴʏ ᴄʜᴀᴛs 💸", url=f'https://telegram.me/share/url?url={link}')]])
    await second_message.reply_text(f"<b>ʏᴏᴜʀ ʟɪɴᴋ ɢᴇɴᴇʀᴀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ❗️</b>\n\n<b>💎 ғɪʟᴇ ɴᴀᴍᴇ : </b> \n\n<b>💫 ғɪʟᴇ sɪᴢᴇ : </b>\n\n<b>🦋 ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ : </b><i><b>{link}</b></i>\n\n<a href=https://t.me/tnlinkdown/6><b>「 Tᴜᴛᴏʀɪᴀʟ ᴠɪᴅᴇᴏ 」</b></a>\n\n<i>© @RolexMoviesOXO</i>", quote=True, reply_markup=reply_markup)

async def get_shortlink(link):
    url = 'https://tnshort.net/api'
    params = {'api': SHORTENER_API, 'url': link}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, raise_for_status=True, ssl=False) as response:
            data = await response.json()
            return data["shortenedUrl"]
    
@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('genlink'))
async def link_generator(client: Client, message: Message):
    while True:
        try:
            channel_message = await client.ask(text = "Forward Message from the DB Channel (with Quotes)..\nor Send the DB Channel Post link", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        msg_id = await get_message_id(client, channel_message)
        if msg_id:
            break
        else:
            await channel_message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is not taken from DB Channel", quote = True)
            continue

    base64_string = await encode(f"get-{msg_id * abs(client.db_channel.id)}")
    link = get_shortlink(f"https://t.me/{client.username}?start={base64_string}")
    await channel_message.reply_text(f"<b>ʏᴏᴜʀ ʟɪɴᴋ ɢᴇɴᴇʀᴀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ❗️</b>\n\n<b>💎 ғɪʟᴇ ɴᴀᴍᴇ : </b> \n\n<b>💫 ғɪʟᴇ sɪᴢᴇ : </b>\n\n<b>🦋 ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ : </b><i><b>{link}</b></i>\n\n<a href=https://t.me/tnlinkdown/6><b>「 Tᴜᴛᴏʀɪᴀʟ ᴠɪᴅᴇᴏ 」</b></a>\n\n<i>© @RolexMoviesOXO</i>", quote=True, reply_markup=reply_markup)
