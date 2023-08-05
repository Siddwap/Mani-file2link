#(©)NovaXTG

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b><i>👨‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href=https://t.me/JonSnow11><b>ᴊᴏɴ sɴᴏᴡ</b></a>\n📝 ʟᴀɴɢᴜᴀɢᴇ : <a href=https://www.python.org><b>ᴘʏᴛʜᴏɴ</b></a>\n📚 ꜰʀᴀᴍᴇᴡᴏʀᴋ : <a href=https://github.com/pyrogram/pyrogram><b>ᴘʏʀᴏɢʀᴀᴍ</b></a>\n📡 ʜᴏsᴛᴇᴅ ᴏɴ : <a href=heroku.com><b>ʜᴇʀᴏᴋᴜ</b></a>\n👥 sᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/RolexMoviesOX><b>ʀᴏʟᴇx ᴄᴏᴍᴍᴜɴɪᴛʏ</b></a>\n",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('∙ Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ ∙', url='https://t.me/+ZPpcbtCV204yYWU1'),
                        InlineKeyboardButton('∙ ᴄᴏɴᴛᴀᴄᴛ ∙', url='https://t.me/JonSnow11')
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
