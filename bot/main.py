from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from my_info import API_KEY, BOT_USERNAME, SOCIAL_MEDIA, CONTACT, RESUME, PROJECTS, SKILLS

def log_user_interaction(update: Update, command_name: str):
    user_id = update.effective_user.id
    username = update.effective_user.username or "No username"
    print(f"User ID: {user_id}, Username: {username}, Command: {command_name}")

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log_user_interaction(update, "/start")
    await update.message.reply_markdown_v2("👋 Welcome to *AymenDevBot*\! \n\n"
    "I can share my resume, projects, and contact info\. Use /help to see all commands\.")

async def how_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log_user_interaction(update, "/help")
    await update.message.reply_markdown_v2(
        " *🚀 Full Stack Developer \| Python Developer* \n\n"
        "I’m Aymen Merad, a full\-stack developer with a Bachelor’s in Computer Science and currently pursuing a Master’s in Data Engineering and Web Technology\. I work across the stack, building scalable backend services with Python and FastAPI and creating responsive frontends\. My design skills, honed through freelance projects, have earned me a 5\-star rating for client satisfaction\.\n"
        " **📂 Projects ** : /projects \n"
        " **🔧 Technical Skills ** : /skills \n"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log_user_interaction(update, "/how")
    await update.message.reply_markdown_v2(
        " *Help Menu* \n\n"
        "Here are the commands you can use:\n"
        "\- /start : Welcome message and introduction\.\n"
        "\- /how : A brief summary about Aymen and his career journey\.\n"
        "\- /resume : Get a copy of my resume\.\n"
        "\- /projects : View details of my projects\.\n"
        "\- /skills : See my technical skills\.\n"
        "\- /contact : Get my contact information\.\n"
        "\- /social\_media : Access my GitHub and LinkedIn links\.\n"
    )

async def resume_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log_user_interaction(update, "/resume")
    resume:str = ""
    for key,val in RESUME.items():
        resume += f'{key} : {val} \n'
    await update.message.reply_text(
        "Aymen Resume\n\n"
        f"{resume}"
    )

async def projects_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log_user_interaction(update, "/projects")
    projects_str:str = 'My Projects \n\n.'
    for title, project_info in PROJECTS.items():
        projects_str += f'{title}\n'
        for key, val in project_info.items():
            projects_str += f'- {key} : {val}\n'
        projects_str += f'\n\n'
    await update.message.reply_text(projects_str)

async def skills_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log_user_interaction(update, "/skills")
    await update.message.reply_text(', '.join(SKILLS))

async def contact_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log_user_interaction(update, "/contact")
    cont = f'My contact info\n\n'
    for key, val in CONTACT.items():
        cont += f'{key} : {val}\n'
    await update.message.reply_text(cont)

async def social_media_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log_user_interaction(update, "/social_media")
    cont = f'My Social Media\n\n'
    for key, val in SOCIAL_MEDIA.items():
        cont += f'{key} : {val}\n'
    await update.message.reply_text(cont)

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
application.add_handler(CommandHandler("how", how_command))

# Run the bot
if __name__ == "__main__":
    print("Bot is running...")
    application.run_polling(poll_interval=3)