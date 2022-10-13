from dotenv import dotenv_values
import praw

config = dotenv_values(".env")

reddit = praw.Reddit(
    client_id=config["CLIENT"],
    client_secret=config["SECRET"],
    username=config["USERNAME"],
    password=config["PASSWORD"],
    user_agent=config["USER-AGENT"],
)

print("All flairs")
for template in reddit.subreddit("intj").flair.templates:
    print(template["text"])


for e in reddit.subreddit("intj").top(time_filter="all", limit=10):
    if e.author_flair_text:
        print(e.author_flair_text)

    print(e.title)
    e.comments.replace_more()
    print(len(e.comments.list()))
