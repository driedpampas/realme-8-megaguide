import os
from telethon.sync import TelegramClient
from github import Github
import markdownify

# Telegram setup
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
bot_token = os.getenv('TELEGRAM_TOKEN')
channel_id = int(os.getenv('CHANNEL_ID'))  # Make sure this is an integer

with TelegramClient(bot_token, api_id, api_hash) as client:
    # Get posts from a specific channel
    channel_posts = client.get_messages(channel_id, limit=10)
    
    # Convert posts to Markdown
    markdown_posts = [markdownify.markdownify(post.message) for post in channel_posts]

    # GitHub setup
    g = Github(os.getenv('GITHUB_TOKEN'))
    repo = g.get_user().get_repo(os.getenv('GH_REPO'))

    # Create or update .md file in the repo
    file_path = "posts.md"
    if file_path in [file.path for file in repo.get_contents("")]:
        contents = repo.get_contents(file_path)
        repo.update_file(contents.path, "update posts", "\n".join(markdown_posts), contents.sha)
    else:
        repo.create_file(file_path, "create posts file", "\n".join(markdown_posts))