from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from github import Github
import os

# Telegram API credentials
api_id = os.environ.get('API_ID')
api_hash = os.environ.get('API_HASH')
channel_username = 'Realme8AOSP'
session_string = os.environ.get('SESSION_STRING')  # Get the session string from environment variables

# GitHub API credentials
github_token = os.environ.get('GITHUB_TOKEN')
repo_owner = 'driedpampas'
repo_name = 'realme-8-megaguide'
file_path = '.pie/temp.md'

# Initialize Telegram client with StringSession
client = TelegramClient(StringSession(session_string), api_id, api_hash)
client.start()

# Retrieve the last 10 posts from the Telegram channel
channel_entity = client.get_entity(channel_username)
posts = client.get_messages(channel_entity, limit=10)

# Convert posts to Markdown format
markdown_content = ''
for post in posts:
    markdown_content += f'# {post.date} - {post.sender.username}\n\n'
    markdown_content += f'{post.text}\n\n'

# Write markdown content to local file
with open(file_path, 'w') as f:
    f.write(markdown_content)

# Close the Telegram client
client.disconnect()