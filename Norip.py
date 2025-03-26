from email.message import Message
import telebot

bot = telebot.TeleBot("7674690160:AAF3S5H_JdnPyXeIvzrIr7J0d6XfLaWMgJI")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "خوش امدید به ربات (gedbed) شما میتوانید به زودی با این ربات لوگوی رایگان خود را بسازید")
    bot.send_message(message.chat.id,"/help")

key_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
key_markup.add("راهنما","فونت", "فهرست", "نسخه پولی")


@bot.message_handler (commands=['help'])
def help_me(message):
  bot.reply_to(message, "انتخاب کنید", reply_markup=key_markup)


@bot.message_handler()
def keyboard(message):
   if message.text == "فونت":
       bot.send_message(message.chat.id,"بزودی")
   elif message.text == "فهرست":
       bot.send_message(message.chat.id,"بزودی")
   elif message.text == "نسخه پولی":
       bot.send_message(message.chat.id,"بزودئ")
   elif message.text == "راهنما":
       bot.send_message(message.chat.id,"soon")

bot.infinity_polling()
