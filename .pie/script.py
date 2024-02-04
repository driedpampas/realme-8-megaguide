from telethon.sync import TelegramClient
from github import Github
import os

# Telegram API credentials
api_id = os.environ.get('API_ID')
api_hash = os.environ.get('API_HASH')
channel_username = 'Realme8AOSP'

# GitHub API credentials
github_token = os.environ.get('GITHUB_TOKEN')
repo_owner = 'driedpampas'
repo_name = 'realme-8-megaguide'
file_path = '.pie/temp.md'

# Initialize Telegram client
client = TelegramClient('session_name', api_id, api_hash)
client.start()

# Retrieve the last 10 posts from the Telegram channel
channel_entity = client.get_entity(channel_username)
posts = client.get_messages(channel_entity, limit=10)

# Convert posts to Markdown format
markdown_content = ''
for post in posts:
    markdown_content += f'# {post.date} - {post.sender.username}\n\n'
    markdown_content += f'{post.text}\n\n'

# Initialize GitHub client
github_client = Github(github_token)
repo = github_client.get_repo(f'{repo_owner}/{repo_name}')

# Create or update the .md file in the GitHub repository
file = repo.get_contents(file_path)
repo.update_file(file_path, 'Updated posts', markdown_content, file.sha)

# Close the Telegram client
client.disconnect()