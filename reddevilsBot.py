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
postsInReddevils = subredditReddevils.new()
postsInHangManBot = subredditHangManBot.new()
usedPosts = []

while True :


    for post in postsInHangManBot:
        title = post.title
        usedPosts.append(title)


    for post in postsInReddevils:
        flair = post.link_flair_text
        title = post.title
        link = post.url

        if flair == "Tier 1" and title not in usedPosts:
            print "flair = " + flair
            print "title = " + title
            print "link = " + link
            subredditHangManBot.submit(title,selftext=link)
    time.sleep(200)







