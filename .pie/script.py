from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
from datetime import datetime

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

# Get all messages from the Telegram channel
channel_entity = client.get_entity(channel_username)
messages = client.iter_messages(channel_entity, limit=20)

# Accumulate markdown content for all messages
markdown_content = ''
for message in messages:
    # Convert the message to Markdown format
    message_date = message.date
    markdown_content += f'# {message_date} - {message.sender.username}\n\n'
    markdown_content += f'{message.text}\n\n'

# Write markdown content to local file
with open(file_path, 'w') as f:
    f.write(markdown_content)

# Close the Telegram client
client.disconnect()