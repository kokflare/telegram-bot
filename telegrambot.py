from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from telegram import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
import emoji
import random

btn1 = KeyboardButton(text='Share my contact', request_contact=True)
btn2 = KeyboardButton(text='Share my location', request_contact=True)
btn3 = KeyboardButton(text='Play game')
kb1 = ReplyKeyboardMarkup(resize_keyboard=True,keyboard=[[btn1, btn2],[btn3]], one_time_keyboard=True)


btn2_1=KeyboardButton(emoji.emojize(' ✌'))
btn2_2=KeyboardButton(emoji.emojize("🖐"))
btn2_3=KeyboardButton(emoji.emojize("👊"))
kb2 = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[btn2_1,btn2_2,btn2_3]])
list=[' ✌',"🖐","👊"]

TOKEN: Final='6619375626:AAEUk7lq4EJny3NrMg_DNABeC_X9WChSSX0'

BOT_USERNAME: Final='@qandaydirrr_bot'

async def start_command(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Salom {update.effective_user.first_name}, men bilan suxbatlashayotganingiz uchun raxmat!', reply_markup=kb1)

async def help_command(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Men shunchaki botman, marhamat nimadir yozsangiz javob beraman')

async def func_command(update:Update, context: ContextTypes.DEFAULT_TYPE):
    text=update.message.text
    j=0
    if text == 'Play game':
        await update.message.reply_text(random(list), reply_markup=kb2)

    elif text!=random(list):
        await update.message.reply_text(random(list),reply_markup=kb2)
        if text == "👊":
            await update.message.reply_text(j)


async def handle_message(update:Update, context:ContextTypes):
    message_type: str=update.message.chat.type
    text: str=update.message.text

    print(f"User ({update.message.chat.id}) in {message_type}:'{text}'")






if __name__ == '__main__':
    print('Starting bot..')
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(MessageHandler(filters.TEXT,func_command))


    print('Polling..')
    app.run_polling(poll_interval=2)

