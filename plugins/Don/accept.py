from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import Client, filters, errors, enums
from asyncio import sleep
from approvedb import add_user, add_group, all_users, all_groups, users, remove_user
from pyrogram.errors import UserNotParticipant
from pyrogram.errors.exceptions.flood_420 import FloodWait
import random, asyncio
from pyrogram.types import Message, User, ChatJoinRequest
from info import LOG_CHANNEL, ACC_SND_LOG

gif = [
    'https://telegra.ph/file/7e38c0e9a6b6051199f92.mp4',
    'https://telegra.ph/file/6d6ad78238403648013c4.mp4',
    'https://telegra.ph/file/7e38c0e9a6b6051199f92.mp4',
    'https://telegra.ph/file/6d6ad78238403648013c4.mp4',
    'https://telegra.ph/file/7e38c0e9a6b6051199f92.mp4',
    'https://telegra.ph/file/6d6ad78238403648013c4.mp4',
    'https://telegra.ph/file/7e38c0e9a6b6051199f92.mp4',
    'https://telegra.ph/file/6d6ad78238403648013c4.mp4',
    'https://telegra.ph/file/7e38c0e9a6b6051199f92.mp4',
    'https://telegra.ph/file/6d6ad78238403648013c4.mp4',
    'https://telegra.ph/file/7e38c0e9a6b6051199f92.mp4'
]


@Client.on_chat_join_request(filters.group | filters.channel & ~filters.private)
async def approve(client: Client, message: Message):
    chat=message.chat # Chat
    add_group(chat.id)
    user=message.from_user # User
    print(f"{user.first_name} 𝙹𝙾𝙸𝙽𝙴𝙳 ⚡") # Logs
    await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
    img = random.choice(gif)
    add_user(user.id)
    #nothingenter
    await client.send_video(user.id,img, "**Hello {}!\nYour Request To Join {} was approved👍\n\n⚠️click /start to see my power Powered By @sinimapremi **".format(message.from_user.mention, message.chat.title))
    if ACC_SND_LOG == "on":
        await client.send_message(
            chat_id=LOG_CHANNEL
            text="*#New_Approval\n\nName: {}\n\nChat: {} \n\n Join @sinimapremi**".format(message.from_user.mention, message.chat.title))
        )
        
        
    

