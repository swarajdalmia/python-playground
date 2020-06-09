'''
Reference used : https://www.storybench.org/how-to-scrape-reddit-with-python/
Look at the documentation of PRAW for more details : https://praw.readthedocs.io/en/latest/index.html
'''
import praw
import pandas as pd 
import datetime as dt
import json

# change UNIX timestamp to readable format 
def get_date(created):
    return dt.datetime.fromtimestamp(created)

if __name__ == "__main__":

    # the config files contains the API settings 
    with open('./web-scraping/config.json', 'r') as f:
        config = json.load(f)

    # the configs entered 
    reddit = praw.Reddit(client_id=config['client_id'], client_secret=config['client_secret'], 
                     user_agent=config['user_agent'], username=config['username'], password=config['password'])

    # the subreddit has been accessed here. here 'r/comics' is used
    # one can also use .search("SEARCH_KEYWORDS") to get only results matching an engine search
    subred_comic = reddit.subreddit('comics')

    topics_dict = { "title":[], "score":[], "id":[], "url":[], "comms_num": [], "created": [], "body":[]}

    # one, can sort using: hot, new, controversial, top etc.
    for post in subred_comic.hot(limit=10):  # default limit is 100, one can also query entries uptill some date
        # this saves some of the details of the reddit entries in the dict
        topics_dict["title"].append(post.title)
        topics_dict["score"].append(post.score)
        topics_dict["id"].append(post.id)
        topics_dict["url"].append(post.url)
        topics_dict["comms_num"].append(post.num_comments)
        topics_dict["created"].append(post.created)
        topics_dict["body"].append(post.selftext)

    # the dict is changed to a pandas dataframe
    topics_data = pd.DataFrame(topics_dict)

    # a new timestamp col added 
    _timestamp = topics_data["created"].apply(get_date)
    topics_data = topics_data.assign(timestamp = _timestamp)

    # save the pandas dataframe to a csv file
    topics_data.to_csv('./web-scraping/comics_sub_reddit.csv', index=False)
    
    # to get a specific post using the post id. One can also use the URL
    example_post = reddit.submission(id=topics_dict["id"][0])

    # post the comments extracted from a post
    for top_level_comment in example_post.comments:
        print(top_level_comment.body)
        






