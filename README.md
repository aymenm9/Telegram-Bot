# AymenDevBot

AymenDevBot is an open-source Telegram bot designed to showcase my resume, projects, technical skills, and social media links. You can use this bot as a personal assistant or customize it for your own needs.

![1732629212767](https://github.com/user-attachments/assets/b680c54f-04a5-437c-ba63-c785615bfbdd)

## Features

    - View my resume and contact information.
    - Explore my technical skills and completed projects.
    - Access links to my social media profiles.
    - Fully customizable and open source!

## Try It Out

Click the link below to chat with the bot directly on Telegram:

👉 [Start Chatting with AymenDevBot](https://t.me/aymenDevBot)

## Setup Instructions

    Follow these steps to set up your own instance of AymenDevBot.

### Prerequisites

    1. Install Python (version 3.9 or later recommended).
    2. Get your Telegram Bot API key:
    - Open Telegram and search for [BotFather](https://t.me/BotFather).
    - Use `/newbot` to create a bot and obtain the API key.

### Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/aymenDevBot.git
    cd aymenDevBot
    pip install -r req.txt
    cd bot

2. Create my_info.py

    ```bash
    touch my_info.py
or 
    ```bash
    code my_info.py

3. Add your info

    ```python
    API_KEY:str
    BOT_USERNAME:str
    SOCIAL_MEDIA:dict # {'name' : 'link'}
    CONTACT:dict # {'name' : 'val'}
    RESUME:dict # {'name' : 'link'}
    PROJECTS:dict # {'name' : {str : str}}
    SKILLS:list

4. Run the bot

    ```bash
    python3 main.py
