import requests
from bs4 import BeautifulSoup
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
TOKEN = "8927093512:AAEJ0bq7Xcs7np7ADGcweAFYJErMIr91oP4"
current_index = 0

def get_news():
    global current_index
    
    response = requests.get("https://news.ycombinator.com/")
    soup = BeautifulSoup(response.content, "html.parser")
    titles = soup.select(".titleline > a")
    news = []

    start = current_index
    end = current_index + 5
    current_index += 5

    for item in titles:
        news.append({
            "title": item.get_text(),
            "link": item["href"]
        })
    return news[start:end]        

async def hi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"Hi {update.effective_user.first_name}"
    )

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):    
    await update.message.reply_text(
    """ ⚔️ Chaos Archive Initialized.

Two paths detected:

🧠 /journey
Explore the evolution logs.

🌐 /abyss
Scan the digital abyss."""
    )

async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Recently, blah blah blah..."
    )

async def journey(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Journey Archive opening soon..."
    )

async def abyss(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Digital abyss scan initializing..."
    )

async def chaos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Shall we summon the Internet Chaos Or Scan the Digital Abyss?"
    )

async def check_me(update: Update, context: ContextTypes.DEFAULT_TYPE):
    articles = get_news()
    message=""
    for article in articles:
        message +=(
        f"• {article['title']}\n"
        f"  Link: {article['link']}\n\n"
        )
    if articles:
        await update.message.reply_text(message)
    else:
        await update.message.reply_text("The Digital Abyss is silent... No news found.")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("hi", hi))
app.add_handler(CommandHandler("news", news))
app.add_handler(CommandHandler("chaos", chaos))
app.add_handler(CommandHandler("check_me", check_me))
app.add_handler(CommandHandler("journey", journey))
app.add_handler(CommandHandler("abyss", abyss))
print("Chaos Scraper is sprinting...")
app.run_polling()