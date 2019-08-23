import praw
import re
import time
import random

reddit = praw.Reddit('feelinbluebot')

listOfSubreddits = [
    'FellowKids',
    'terriblefacebookmemes',
    'emojipasta',
    'roblox',
    'fffffffuuuuuuuuuuuu',
    'copypasta',
    'Surrealmemes'
]

# Target body
messages = ["depressed", "very sad", "bad day"]

# First task:
# Create an array, and take the line in posts_replied_to.txt and split by " ".
# Store each split word into that array
with open('logs/posts_replied_to.txt') as file_read:
    comment_cache = file_read.readlines()

# print("Comment cache" + "\n")
# print(comment_cache)


# Main entry post.

while True:

    randNum = random.randint(0, len(listOfSubreddits)-1)

    subreddit = reddit.subreddit(listOfSubreddits[randNum])

    # Loop through submissions in the hot section of chosen subreddit.
    print("Indexing through: r/"+str(listOfSubreddits[randNum]))

    for submission in subreddit.hot(limit=15):

        # Now loop through all comments in the submission, top-level and all below.

        submission.comments.replace_more(limit=None)
        for current_comment in submission.comments.list():

            # Open comments_file for appending/reading
            # comments_file = open("posts_replied_to.txt", "r")
            # print("Comments file opened for reading.\nContents of .readline():")
            # print(comments_file.readlines())
            # If we have not replied to this comment before, search it for our keyword.

            if str(current_comment.id)+"\n" not in comment_cache:

                # Do a case-insensitive search on the body of all comments.
                # Close the file and reopen for appending
                # comments_file.close()

                # If comment.author returns None, we have a deleted comment.
                # Skip it.
                if current_comment.author is None:
                    continue

                # Prevent the bot from replying to itself.
                if current_comment.author.name == 'FeelinBlueBot':
                    continue

                # Responds to comments with the word "depressed" contained in them.
                if re.search(messages[0], current_comment.body, re.IGNORECASE):

                    comments_file = open("logs/posts_replied_to.txt", "a+")
                    current_comment.reply("Why so blue, kangaroo? \n\nHere's a catchy sea shanty, [just for you!](https://youtu.be/GVXCr6upWUo) \n\n \n\n \n\n^I ^am ^a ^bot ^and ^this ^was ^performed ^automatically!")
                    comments_file.write(str(current_comment.id)+"\n")

                    # Add the comment to the comment cache (temporary)
                    # comment_cache.append(str(current_comment.id))
                    # Close file when done and about to restart the loop, it will be opened again.

                    comments_file.close()

                    # Once we reply to a comment
                    # Suspend for 10 minutes to avoid reddit ratelimit (time allowed between posts).

                    print("Post Successful. Sleeping for 30 minutes to refresh."+"\n")
                    time.sleep(600)
                    time.sleep(600)
                    time.sleep(600)

                # Responds to comments with the word "sad" contained in them.
                if re.search(messages[1], current_comment.body, re.IGNORECASE):

                    comments_file = open("logs/posts_replied_to.txt", "a+")
                    current_comment.reply(
                        "Why you feeling sad, comrade? \n\nHere's a rad tune, [to make you feel a lil' more glad!](https://www.youtube.com/watch?v=u3KF6DBRRik) \n\n \n\n \n\n^I ^am ^a ^bot ^and ^this ^was ^performed ^automatically!")
                    comments_file.write(str(current_comment.id) + "\n")

                    comments_file.close()

                    print("Post Successful. Sleeping for 30 minutes to refresh." + "\n")
                    time.sleep(600)
                    time.sleep(600)
                    time.sleep(600)

                # Responds to comments with the phrase "bad day" contained in them.
                if re.search(messages[2], current_comment.body, re.IGNORECASE):

                    comments_file = open("logs/posts_replied_to.txt", "a+")
                    current_comment.reply(
                        "Having a horrible day, you incredible blue jay? \n\nHere's a groovy clip, [so you wont go astray!](https://youtu.be/MYfeSHgfK5s) \n\n \n\n \n\n^I ^am ^a ^bot ^and ^this ^was ^performed ^automatically!")
                    comments_file.write(str(current_comment.id) + "\n")

                    comments_file.close()

                    print("Post Successful. Sleeping for 30 minutes to refresh." + "\n")
                    time.sleep(600)
                    time.sleep(600)
                    time.sleep(600)


            # If this comment is in the comment cache, skip it.

            else:

                print("Encountered comment #"+str(current_comment.id)+" already. Skipping it in one minute.")
                time.sleep(60)
                continue

    print("Loop starting over, starting new search for a comment.")

    # -------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------

'''

    # Have we run this code before? If not, create an empty list
    if not os.path.isfile("posts_replied_to.txt"):
        posts_replied_to = []

    # If we have run the code before, load the list of posts we have replied to
    else:
        # Read the file into a list and remove any empty values
        with open("posts_replied_to.txt", "r") as f:
            posts_replied_to = f.read()
            posts_replied_to = posts_replied_to.split("\n")

            # This is the actual line to filter out empty entries.
            posts_replied_to = list(filter(None, posts_replied_to))

        # If we haven't replied to this post before
        # posts_replied_to will store a number string for the id of the post
        # not the actual submission as a whole.
        # so use submission.id.
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            if re.search("hello", submission.title, re.IGNORECASE):
                # Reply to the post
                submission.reply("Test successful")
                print("Bot replying to : ", submission.title)

                # Store the current id into our list
                posts_replied_to.append(submission.id)

    # Write our updated list back to the file
    with open("posts_replied_to.txt", "w") as f:
        for post_id in posts_replied_to:
            f.write(post_id + "\n")
            

    for submission in subreddit.hot(limit=5):
        print("Title: ", submission.title)
        print("Text: ", submission.selftext)
        print("Score: ", submission.score)
        print("---------------------------------\n")
        
'''
