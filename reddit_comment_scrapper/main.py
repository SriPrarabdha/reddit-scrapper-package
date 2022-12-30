import typer
import json
import praw
import time
from rich.progress import track


app = typer.Typer()

def build_tree(comments):
    tree = []
    for comment in comments:
        # Add the comment to the tree
        
        tree.append({"id": comment.id, "body": comment.body, "replies": []})
        # Recursively build the tree for the replies to this comment
        if comment.replies:
            tree[-1]["replies"] = build_tree(comment.replies)
    return tree

@app.command()
def comment_graph(redditid:str , redditsecret:str , namesubreddit:str , post_category : str ,number_of_post:int ) :
    typer.echo("Please enter your Reddit ID , Reddit Secret , name of subreddit to parse , post-category , number of posts to parse in respective order")
    user_agent = "Scraper 1.0 by /u/MajesticPanic8917"
    reddit = praw.Reddit(
        client_id = redditid ,
        client_secret = redditsecret, 
        user_agent = user_agent
    )
    tree= []
    if number_of_post == 0:
        number_of_post = None

    if post_category == 'rising' :
        submissions = reddit.subreddit(namesubreddit).rising(limit=number_of_post)
    elif post_category == 'hot':
        submissions = reddit.subreddit(namesubreddit).hot(limit=number_of_post)
    elif post_category == 'new':
        submissions = reddit.subreddit(namesubreddit).new(limit=number_of_post)
    elif post_category == 'top':
        submissions = reddit.subreddit(namesubreddit).top(limit=number_of_post)
    else:
        print("ERROR!!!")
        print("Please choose with in hot, new, top, rising")
        return 
    
    try:
        for submission in submissions:
            print(submission.title)
            submission.comments.replace_more(limit=None)
    
            tree_submission = build_tree(submission.comments)
    
            tree.append({"Submission" : submission.title , "comments" : tree_submission})
    except:
        print("ERROR!!!")
        print(f'Please check the details provided REDDIT-ID - {redditid}, REDDIT-SECRET - {redditsecret}, SUBREDDIT-NAME - {namesubreddit}')

    json_data = json.dumps(tree)

    # Save the JSON string to a file
    with open("comments.json", "w") as f:
        f.write(json_data)



