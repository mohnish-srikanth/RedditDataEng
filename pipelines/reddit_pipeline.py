from etls.reddit_etl import connect_reddit
from etls.reddit_etl import extract_posts
from utils.constants import CLIENT_ID, SECRET

def reddit_pipeline(file_name: str, subreddit: str, time_filter = 'day', limit = None):
    # connnecting to reddit instance
    instance = connect_reddit(CLIENT_ID, SECRET, 'Airscholar Agent')

    # extraction
    posts = extract_posts(instance, subreddit, time_filter, limit)
    # transformation

    # loading into csv