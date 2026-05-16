from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
TOKEN="8927093512:AAFLQBYZfkzm2BIjogLf5j_RLYJhn6iwdgs"

async def hi(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hi {update.effective_user.first_name}')


async def news(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Recently, blah blah blah blah b-....")

async def chaos(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Shall we summon the Internet Chaos Or Scan the Digital Abyss?")

app=ApplicationBuilder().token(TOKEN).build()   
app.add_handler(CommandHandler("chaos", chaos))
app.add_handler(CommandHandler("hi", hi))
app.add_handler(CommandHandler("news", news))
app.run_polling()    