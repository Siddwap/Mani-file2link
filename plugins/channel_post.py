#(©)NovaXTG

import asyncio
import aiohttp
from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait
from bot import Bot
from config import *
from helper_func import encode
from shortzy import Shortzy

@Bot.on_message(filters.private & filters.user(ADMINS) & ~filters.command(['start','users','broadcast','batch','genlink','stats']))
async def channel_post(client: Client, message: Message):
    reply_text = await message.reply_text("Please Wait...!", quote = True)
    try:
        post_message = await message.copy(chat_id = client.db_channel.id, disable_notification=True)
    except FloodWait as e:
        await asyncio.sleep(e.x)
        post_message = await message.copy(chat_id = client.db_channel.id, disable_notification=True)
    except Exception as e:
        print(e)
        await reply_text.edit_text("Something went Wrong..!")
        return
    converted_id = post_message.id * abs(client.db_channel.id)
    string = f"get-{converted_id}"
    base64_string = await encode(string)
    link = f"https://t.me/{client.username}?start={base64_string}"

    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("💸 Yᴏᴜ ᴄᴀɴ sʜᴀʀᴇ ᴛʜɪs ᴛᴏ ᴀɴʏ ᴄʜᴀᴛs 💸", url=f'https://telegram.me/share/url?url={link}')]])

    await reply_text.edit(f"<b>ʏᴏᴜʀ ʟɪɴᴋ ɢᴇɴᴇʀᴀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ❗️</b>\n\n<b>💎 ғɪʟᴇ ɴᴀᴍᴇ : </b> \n\n<b>💫 ғɪʟᴇ sɪᴢᴇ : </b>\n\n<b>🦋 ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ : </b><i><b>{link}</b></i>\n\n<i>© @Monaserials</i>", reply_markup=reply_markup, disable_web_page_preview = True)

    if not DISABLE_CHANNEL_BUTTON:
        await post_message.edit_reply_markup(reply_markup)

@Bot.on_message(filters.channel & filters.incoming & filters.chat(CHANNEL_ID))
async def new_post(client: Client, message: Message):

    if DISABLE_CHANNEL_BUTTON:
        return

    converted_id = message.id * abs(client.db_channel.id)
    string = f"get-{converted_id}"
    base64_string = await encode(string)
    link = f"https://t.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("💸 Yᴏᴜ ᴄᴀɴ sʜᴀʀᴇ ᴛʜɪs ᴛᴏ ᴀɴʏ ᴄʜᴀᴛs 💸", url=f'https://telegram.me/share/url?url={link}')]])
    try:
        await message.edit_reply_markup(reply_markup)
    except Exception as e:
        print(e)
        pass
    
async def get_shortlink(link):
    url = 'https://tnshort.net/api'
    params = {'api': SHORTENER_API, 'url': link}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, raise_for_status=True, ssl=False) as response:
            data = await response.json()
            return data["shortenedUrl"]
