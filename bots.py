import logging
from aiogram import Bot, Dispatcher, executor, types
import markups as nav
import random
import json
import os.path
#from servergen import genserver
from subprocess import Popen
from checker import new_func
import re

TOKEN = '1952639092:AAHZ6p4FlhaIDO3E55eKKumu2twBMf3NvtE'
CHANNEL_ID = '@binbeginner'
NOT_SUB = 'Subscribe to this channel first'
ANOTHER_NOT_SUB = 'Subscription not found'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

#return True if user is subscribed
def check_sub(chat_member):
    if chat_member['status'] != 'left':
        return True
    else:
        return False

@dp.message_handler(content_types=types.ContentType.DOCUMENT)
async def scan_message(message: types.Message):
    user_id=message.from_user.id
    print("downloading document")
    destination = f"download/{user_id}.txt"
    if os.path.exists(destination):
        os.remove(destination)
    await message.document.download(destination)
    await bot.send_message(message.from_user.id, 'Successfully Downloaded👋')
    

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if message.chat.type == 'private':
        if check_sub(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
            await bot.send_message(message.from_user.id, 'Hi there👋', reply_markup=nav.profileKeyboard)
        else:
            await message.reply(NOT_SUB, reply_markup=nav.checkSubMenu)

@dp.message_handler(commands=['server'])
async def start(message: types.Message):
    if message.chat.type == 'private':
        if check_sub(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
            await bot.send_message(message.from_user.id, 'Hi there👋', reply_markup=nav.profileKeyboard)
        else:
            await message.reply(NOT_SUB, reply_markup=nav.checkSubMenu)

@dp.message_handler()
async def bot_message(message: types.Message):
    if message.chat.type == 'private':
        #if user will try to write 'Profile' without subscription
        if check_sub(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
            if message.text == 'check':
                user_id=message.from_user.id        
                destination = f"download/{user_id}.txt"
                if os.path.exists(destination):
                    await bot.send_message(message.from_user.id, 'Start to Check👋')
                    #new_func( cc, cvv, mes, ano)
                    user_id=message.from_user.id
                    file1 = open(f'download/{user_id}.txt', 'r')
                    Lines = file1.readlines()
                    count = 0

                    for line in Lines:
                        #count += 1
                        #print("Line{}: {}".format(count, line.strip()))
                        x = re.findall(r'\d+', line)
                        ccn = x[0]
                        mm = x[1]
                        yy = x[2]
                        cvv = x[3]
                        result = new_func( ccn, cvv, mm, yy)
                        await bot.send_message(message.from_user.id, f'👋{result}')
                else:
                    await bot.send_message(message.from_user.id, 'Please Send Me CC👋')
            else:
                #await bot.send_message(message.from_user.id, 'Unknown command')
                pass
        else:
            await message.reply(NOT_SUB, reply_markup=nav.checkSubMenu)






@dp.callback_query_handler(text='subdone')
async def subdone(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    if check_sub(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
        await bot.send_message(message.from_user.id, 'Hi there👋', reply_markup=nav.profileKeyboard)
    else:
        await bot.send_message(message.from_user.id, ANOTHER_NOT_SUB, reply_markup=nav.checkSubMenu)

@dp.callback_query_handler(text='checks')#change this
async def inserver(message: types.Message):

    await bot.delete_message(message.from_user.id, message.message.message_id)
    
    no = random.randint(0,99)
    USERNAME = str(message.from_user.id)
    PASSWORD = message.from_user.first_name + str(no) + '@Sktool'
    if check_sub(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
        provider = []
        f = open('servers.json')
        data = json.load(f)
        for i in data['servers']:
            if i['serverName'] == "IN": # change this 
                provider.append(i)
        if not provider == []:
            randomerver = random.choice(provider)   
            SERVER_ID = randomerver['serverId']
            APP_ID = randomerver['appId']
            API_KEY = randomerver['apiKey']
            EMAIL= randomerver['email']
            DESCRIP = randomerver['description']
            IPADD = randomerver['serverIp']
           # create = genserver(int(SERVER_ID),int(APP_ID),API_KEY,EMAIL,USERNAME,PASSWORD,DESCRIP,IPADD)
           # await bot.send_message(message.from_user.id, f'Hi there👋 {create}')
        else:
            await bot.send_message(message.from_user.id, "Hi there👋 Currently we don't have any provider yet.")
    else:
        await bot.send_message(message.from_user.id, ANOTHER_NOT_SUB, reply_markup=nav.checkSubMenu)





#Popen(f"gunicorn server.server:app --bind 0.0.0.0:8080", shell=True)



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
