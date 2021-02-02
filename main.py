import praw
import re
from praw.models import MoreComments

enter_sub = input("Type a subbreddit name: ")
if len(enter_sub) < 1 : enter_sub = "nashua"

search_term = input("Search for a term: ")
if len(search_term) < 1 : search_term = "09876543211234567890"

try:
    post_limit = input("How many of the top posts would you like to look through?: ")
    if len(post_limit) < 1 : postlimit = 3
    post_limit = int(post_limit)
except:
    print("!!ERROR!! Please type in a positive number")
    post_limit = input("How many of the top posts would you like to look through?: ")
    if len(post_limit) < 0 : post_limit = 3
    post_limit = int(post_limit)

reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit(enter_sub)

ticker_total = 0
post_number = 1
for submission in subreddit.hot(limit = post_limit):
    url = submission.url
    url_title = submission.title
    print("\nReading r/", enter_sub, "post #",post_number,": ", url_title,"\nURL:", url, )
    post_number = post_number + 1

    ticker_count = 0
    submission.comments.replace_more(limit=0)
    for topcomments in submission.comments.list():
        topcomments = topcomments.body #string
        search = len(re.findall(search_term, topcomments))
        if search == True:
            ticker_count = ticker_count + 1

    print("'",search_term,"'", "was mentioned: ", ticker_count, " times \n")
    ticker_total = ticker_total + ticker_count

print(search_term, "was mentioned a total of", ticker_total, "times in the current top", post_limit ,"r/",enter_sub, "post comments.")
