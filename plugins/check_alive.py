import random
from pyrogram import Client, filters
from info import ADMINS 

@Client.on_message(filters.new_chat_members)
async def welcome(bot, message):
	await message.delete()	
	
@Client.on_message(filters.left_chat_member)
async def goodbye(bot, message):
	await message.delete()

@Client.on_message(filters.regex("http") & filters.regex("www") | filters.regex("https") | filters.regex("t.me") & filters.incoming)
async def nolink(bot, message):
	await message.delete()
