from pyrogram import Client, filters
from asyncio import sleep
from art import tprint
from pathlib import Path
from config import api_id, api_hash, phone_number
from random import randint

app = Client("my_account", api_id=api_id,
             api_hash=api_hash, phone_number=phone_number)



def spam_message():#Текст отправки сообщение
    if Path('./spam_files/text.md').is_file():
        md_str = ''
        with open(r"./spam_files/text.md", "r", encoding="utf-8") as file:
            for line in file:
                md_str += line
        return md_str
    elif Path('./spam_files/text.txt').is_file():
        txt_str = ''
        with open(r"./spam_files/text.txt", "r", encoding="utf-8") as file:
            for line in file:
                txt_str += line
        return txt_str
    else:
        print('[ERROR] Текстовый файл не найден!')


def check_image():
    path = './spam_files/image3.png'
    if Path(path).is_file() and (Path(path).suffix == ".png" or Path(path).suffix == ".jpg"
                                 or Path(path).suffix == ".jpeg"):
        return True
    else:
        return False


@app.on_message(filters.command('start', prefixes='/') & filters.me)
async def start_spamming(client, message):
    # Получение всех пользователей и чатов
    spam_msg = spam_message()
    chats = []
    async for dialog in app.get_dialogs():
        chats.append({'dialog': dialog.chat.first_name or dialog.chat.title, 'id': dialog.chat.id})

    # Проход по всем пользователям и отправка спам сообщения
    if not check_image():
        print('[+] Розпочати спам-розсилку без зображення')
        for chat in chats:
            await app.send_message(chat['id'], spam_msg)
            chat_name = chat['dialog']
            print(f'[+] {chat_name} отримав спам')
            await sleep(randint(10, 20)) # Кулдаун на отправку сообщений
    else:
        print('[+] Розпочати спам із зображення')
        for chat in chats:
            await app.send_photo(chat['id'], "./spam_files/image.png", caption=spam_msg)
            chat_name = chat['dialog']
            print(f'[+] {chat_name} отримав спам')
            await sleep(randint(10, 20))  # Кулдаун на отправку сообщений


@app.on_message(filters.command('test', prefixes='/') & filters.me)
async def check_msg(client, message):
    spam_msg = spam_message()
    if not check_image():
        await message.reply(spam_msg)
    else:
        await message.reply_photo("./spam_files/image.png", caption=spam_msg)


@app.on_message(filters.command('help', prefixes='/') & filters.me)
async def help_msg(client, message):
    text = f"**[1]** /start почати відправлення спаму\n" \
           f"**[2]** /test переглянути текст відправки \n " \
           f"**[3]**, /help допомога"
    await message.reply(text)





if __name__ == '__main__':
    tprint("""Byziz""")
    app.run()
