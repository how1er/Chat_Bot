import telebot
import  aiogram


bot = telebot.TeleBot('5165580375:AAFErXRjKu9bBDsxeJwBgIgk37lSI4qr3AY')
channel_id= '@mychannel1502'

@bot.message_handler(commands=['start'])
def start_message(message):
   user_channel_status = bot.get_chat_member(chat_id=channel_id, user_id=message.from_user.id)
   if user_channel_status.status != 'left':
      bot.send_message(message.from_user.id, 'привет')
   else:
      bot.send_message(message.from_user.id, "t.me/" + channel_id[1:])

bot.polling(none_stop=True, interval=0)
