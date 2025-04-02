from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import requests  # Import requests to call the backend

# Telegram bot token
BOT_TOKEN = "CREATE BOT TOKEN"

# Define backend URL
BACKEND_URL = "http://127.0.0.1:5000/fact-check"

# Command to start the bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
🚀 Welcome to the Misinformation Detection Bot!
Paste any text, and I'll analyze it for potential misinformation.
""")

# Handle text messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text

    # Send text to backend for analysis
    response = requests.post(BACKEND_URL, json={"text": user_input})

    if response.status_code == 200:
        result = response.json()
        formatted_result = "\n".join([f"{fact}: {check}" for fact, check in result.items()])
        reply_text = f"📢 **Fact-Checking Results:**\n\n{formatted_result}"
    else:
        reply_text = "⚠️ Error: Unable to process the request."

    # Send response to the user
    await update.message.reply_text(reply_text)

# Error handler
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")

# Main function to run the bot
if __name__ == "__main__":
    print("Starting bot...")
    app = Application.builder().token(BOT_TOKEN).build()

    # Add handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    app.add_error_handler(error)

    # Start the bot
    print("Polling...")
    app.run_polling(poll_interval=3)
