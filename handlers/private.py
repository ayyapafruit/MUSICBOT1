from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""**Hey, I'm {bn} 🎵

I can play music in your group's voice call. Developed by [Professor](https://t.me/sensibleguy).

Add me to your group and play music freel!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
               
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ Join our Group ➕", url="https://t.me/english_hindi_chattingg"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Group Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/english_hindi_chattingg")
                ]
            ]
        )
   )


