import praw
import time

dir(praw) # so that i can see the methods inside praw

reddit = praw.Reddit(user_agent='reddevils tier1 bot',
              client_id='oi_wchrKkLQOCg',
              client_secret='nyV4T9DZYRtwDRl9iOHIVhgYDYQ',
              username='gokhanpictregeta',
              password='iamepic')

subredditHangManBot = reddit.subreddit("hangmanBot")
subredditReddevils = reddit.subreddit("reddevils")
posts = subredditReddevils.new()
while True :
    for post in posts:
        flair = post.link_flair_text
        title = post.title
        link = post.url

        if flair == "Tier 1":
            print "flair = " + flair
            print "title = " + title
            print "link = " + link
            subredditHangManBot.submit(title,selftext=link)
    time.sleep(200)







