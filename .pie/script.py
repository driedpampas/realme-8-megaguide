from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from github import Github
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

# Get the latest message from the Telegram channel
channel_entity = client.get_entity(channel_username)
latest_message = next(client.iter_messages(channel_entity, limit=20))

# Get the date of the latest message
latest_message_date = latest_message.date

# Check if the file exists and get the date of the latest post in the file
latest_file_date = None
if os.path.exists(file_path):
    with open(file_path, 'r') as f:
        first_line = f.readline()
        date_str = first_line.split(' - ')[0].strip('# ')
        if date_str:
            latest_file_date = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S%z')

# If the file doesn't exist or the latest message is newer than the latest post in the file, update the file
if latest_file_date is None or latest_message_date > latest_file_date:
    # Convert the latest message to Markdown format
    markdown_content = f'# {latest_message.date} - {latest_message.sender.username}\n\n'
    markdown_content += f'{latest_message.text}\n\n'

    # Write markdown content to local file
    with open(file_path, 'w') as f:
        f.write(markdown_content)

# Close the Telegram client
client.disconnect()
