import os
from aiogram import Bot, types
from github import Github
import markdownify
import asyncio

async def main():
    # Telegram setup
    bot = Bot(token=os.getenv('TELEGRAM_TOKEN'))
    updates = bot.get_updates()

    # Get posts from a specific channel
    channel_id = int(os.getenv('CHANNEL_ID'))  # Channel IDs are integers
    channel_posts = [update.channel_post.text for update in updates if update.channel_post.chat.id == channel_id]

    # Limit to the last 10 posts
    channel_posts = channel_posts[-10:]

    # Convert posts to Markdown
    markdown_posts = [markdownify.markdownify(post) for post in channel_posts]

    # GitHub setup
    g = Github(os.getenv('GITHUB_TOKEN'))
    repo = g.get_user().get_repo(os.getenv('GH_REPO'))

    # Create or update .md file in the repo
    file_path = ".pie/temp.md"
    if file_path in [file.path for file in repo.get_contents("")]:
        contents = repo.get_contents(file_path)
        repo.update_file(contents.path, "update posts", "\n".join(markdown_posts), contents.sha)
    else:
        repo.create_file(file_path, "create posts file", "\n".join(markdown_posts))

# Run the async function
asyncio.run(main())