import json
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton



  
# returns JSON object as 
# a dictionary


btnProfile = KeyboardButton('check')
btnProfilef = KeyboardButton('Profilefgg')
profileKeyboard = ReplyKeyboardMarkup(resize_keyboard = True).add(btnProfile)



btnUrl = InlineKeyboardButton(text='Subscribe', url='https://t.me/binbeginner')
btnsubdone = InlineKeyboardButton(text='Check subscription', callback_data='subdone')
checkSubMenu = InlineKeyboardMarkup(row_width=3)

checkSubMenu.insert(btnUrl)
checkSubMenu.insert(btnsubdone)

ServerMenu = InlineKeyboardMarkup(row_width=3)
us = InlineKeyboardButton(text='🇺🇸 US', callback_data='usserver')
sg = InlineKeyboardButton(text='🇯🇵 JP', callback_data='jpserver')
india =  InlineKeyboardButton(text='🇮🇳 IN', callback_data='inserver')
ServerMenu.insert(us)
ServerMenu.insert(sg)
ServerMenu.insert(india)