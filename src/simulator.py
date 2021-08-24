import praw
import markovify
import os


def simulate_reply(post_url):
    client_id = os.environ['client_id']
    secret = os.environ['secret']
    user_agent = os.environ['user_agent']

    reddit = praw.Reddit(client_id= client_id, client_secret= secret , user_agent= user_agent)
    post = reddit.submission(url=  post_url)

    reply_list = []

    # Depth First Search Algorithm
    def dfs(reply):
        for i in range(len(reply.replies)):
            reply_list.append(reply.replies[i].body)
            dfs(reply.replies[i])

    post.comments.replace_more(limit=0)

    for i in range(len(post.comments)):
        queue = list()
        queue.append(post.comments[i])
        while queue:
            reply = queue.pop(0)
            reply_list.append(reply.body)
            dfs(reply)


    text = post.selftext
    for r in reply_list:
        text += r + "." + "\n"

    text_model = markovify.Text(text)

    return text_model.make_sentence()

