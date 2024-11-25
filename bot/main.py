from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from my_info import API_KEY, BOT_USERNAME, SOCIAL_MEDIA, CONTACT, RESUME, PROJECTS, SKILLS

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_markdown_v2("👋 Welcome to *AymenDevBot*\! \n\n"
    "I can share my resume, projects, and contact info\. Use /help to see all commands\.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_markdown_v2(
        " *Help Menu* \n\n"
        "Here are the commands you can use:\n"
        "\- /start : Welcome message and introduction\.\n"
        "\- /resume : Get a copy of my resume\.\n"
        "\- /projects : View details of my projects\.\n"
        "\- /skills : See my technical skills\.\n"
        "\- /contact : Get my contact information\.\n"
        "\- /social\_media : Access my GitHub and LinkedIn links\.\n"
    )

async def resume_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    resume:str = ""
    for key,val in RESUME.items():
        resume += f'{key} : {val} \n'
    await update.message.reply_text(
        "Aymen Resume\n\n"
        f"{resume}"
    )

async def projects_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    projects_str:str = 'My Projects \n\n.' 
    for key0, val0 in PROJECTS.items():
        projects_str += f'{key0}\n'
        for key1, val1 in val0.items():
            projects_str += f'- {key1} : {val1}\n'
        projects_str += f'\n\n'
    await update.message.reply_text(projects_str)

async def skills_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(', '.join(SKILLS))
    
async def contact_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    cont = f'My contact info\n\n'
    for key, val in CONTACT.items():
        cont += f'{key} : {val}\n'
    await update.message.reply_text(cont)

async def social_media_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    cont = f'My Social Media\n\n'
    for key, val in SOCIAL_MEDIA.items():
        cont += f'{key} : {val}\n'
    await update.message.reply_markdown_v2(cont)

# Create the bot application
application = Application.builder().token(API_KEY).build()

# Add command handlers
application.add_handler(CommandHandler("start", start_command))
application.add_handler(CommandHandler("help", help_command))
application.add_handler(CommandHandler("resume", resume_command))
application.add_handler(CommandHandler("projects", projects_command))
application.add_handler(CommandHandler("skills", skills_command))
application.add_handler(CommandHandler("contact", contact_command))
application.add_handler(CommandHandler("social_media", social_media_command))

# Run the bot
if __name__ == "__main__":
    print("Bot is running...")
    application.run_polling(poll_interval=3)