import os
import telegram
from github import Github

TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
GITHUB_TOKEN = os.environ['GITHUB_TOKEN']
GITHUB_REPO = os.environ['REPO']
FILE_PATH = os.environ['FILE_PATH']
CHANNEL_ID = os.environ['CHANNEL_ID']

# Initialize Telegram Bot
bot = telegram.Bot(token=TELEGRAM_TOKEN)

# Get Channel ID
channel_id = -100123456789  # Replace with your channel ID

# Fetch Posts
messages = bot.get_chat_history(chat_id=channel_id, limit=5)

# Convert to Markdown
markdown_content = ""
for message in messages:
    markdown_content += f"**{message.date}**: {message.text}\n\n"

# Initialize GitHub
github = Github(GITHUB_TOKEN)
repo = github.get_repo(GITHUB_REPO)

# Push to GitHub
file = repo.get_contents(FILE_PATH)
repo.update_file(FILE_PATH, "Update posts", markdown_content, file.sha)
