import praw
import re
import time
import random

reddit = praw.Reddit('feelinbluebot')

listOfSubreddits = [
    'emojipasta',
    'copypasta',
    'testingground4bots',
]

# Target body
messages = ["depressed", "very sad", "bad day", "kill me", "end my life"]

# Array of youtube videos
possible_videos = [
                    "https://youtu.be/GVXCr6upWUo",
                    "https://www.youtube.com/watch?v=u3KF6DBRRik",
                    "https://youtu.be/MYfeSHgfK5s",
                    "https://youtu.be/vKSjydW2Ik0",
                    "https://youtu.be/9faqM-WvxBQ",
                    "https://youtu.be/ryxRN29ev3s",
                    "https://www.youtube.com/watch?v=7G_aaak-tDE",
                    "https://www.youtube.com/watch?v=e9x4o1gAzTc",
                    "https://youtu.be/C2ZRPz4KZfo",
                    "https://youtu.be/ngtzvZ1V0p8",
                    "https://youtu.be/pAebnJXbEHA",
                    "https://youtu.be/HJPDiFCo4Nc",
                    "https://youtu.be/_L-CYkXmJzw",
                    "https://youtu.be/EWeVKUAkgnw",
                    "https://www.youtube.com/watch?v=WwK3OK3ZqDE",
                    "https://youtu.be/kG-xi6Mx5i0",
                    "https://youtu.be/eEoMI9BwHp4",
                    "https://youtu.be/vwg-8mKaluE",
                    "https://youtu.be/wifBBIc2kIM",
                    "https://youtu.be/X1M69l7ZGlw",
                                                                ]

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

    for submission in subreddit.hot(limit=10):

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
                    current_comment.reply("Why so blue, kangaroo? \n\nHere's a catchy sea shanty, [just for you!]({}) \n\n \n\n \n\n^I ^am ^a ^bot ^and ^this ^was ^performed ^automatically!".format(random.choice(possible_videos)))
                    comments_file.write(str(current_comment.id)+"\n")

                    # Add the comment to the comment cache (temporary)
                    # comment_cache.append(str(current_comment.id))
                    # Close file when done and about to restart the loop, it will be opened again.

                    comments_file.close()

                    # Once we reply to a comment
                    # Suspend for 10 minutes to avoid reddit ratelimit (time allowed between posts).

                    print("Post Successful. Sleeping for 24 hours to refresh."+"\n")
                    time.sleep(86400)

                # Responds to comments with the word "very sad" contained in them.
                if re.search(messages[1], current_comment.body, re.IGNORECASE):

                    comments_file = open("logs/posts_replied_to.txt", "a+")
                    current_comment.reply(
                        "Why you feeling sad, comrade? \n\nHere's a rad tune, [to make you feel a lil' more glad!]({}) \n\n \n\n \n\n^I ^am ^a ^bot ^and ^this ^was ^performed ^automatically!".format(random.choice(possible_videos)))
                    comments_file.write(str(current_comment.id) + "\n")

                    comments_file.close()

                    print("Post Successful. Sleeping for 24 hours to refresh." + "\n")
                    time.sleep(86400)

                # Responds to comments with the phrase "bad day" contained in them.
                if re.search(messages[2], current_comment.body, re.IGNORECASE):

                    comments_file = open("logs/posts_replied_to.txt", "a+")
                    current_comment.reply(
                        "Having a horrible day, you incredible blue jay? \n\nHere's a groovy clip, [so you wont go astray!]({}) \n\n \n\n \n\n^I ^am ^a ^bot ^and ^this ^was ^performed ^automatically!".format(random.choice(possible_videos)))
                    comments_file.write(str(current_comment.id) + "\n")

                    comments_file.close()

                    print("Post Successful. Sleeping for 24 hours to refresh." + "\n")
                    time.sleep(86400)

                # Responds to comments with the phrase "kill me" contained in them.
                if re.search(messages[3], current_comment.body, re.IGNORECASE):

                    comments_file = open("logs/posts_replied_to.txt", "a+")
                    current_comment.reply(
                        "Feeling like your whole world is coming down? \n\nWell let me turn that frown. [right around!]({}) \n\n \n\n \n\n^I ^am ^a ^bot ^and ^this ^was ^performed ^automatically!".format(random.choice(possible_videos)))
                    comments_file.write(str(current_comment.id) + "\n")

                    comments_file.close()

                    print("Post Successful. Sleeping for 24 hours to refresh." + "\n")
                    time.sleep(86400)

                # Responds to comments with the phrase "end my life" contained in them.
                if re.search(messages[4], current_comment.body, re.IGNORECASE):

                    comments_file = open("logs/posts_replied_to.txt", "a+")
                    current_comment.reply(
                        "Feeling down in the dumps? \n\nLet me change your mind by showing you something funny, [ol' chum!]({}) \n\n \n\n \n\n^I ^am ^a ^bot ^and ^this ^was ^performed ^automatically!".format(random.choice(possible_videos)))
                    comments_file.write(str(current_comment.id) + "\n")

                    comments_file.close()

                    print("Post Successful. Sleeping for 24 hours to refresh." + "\n")
                    time.sleep(86400)


            # If this comment is in the comment cache, skip it.

            else:

                print("Encountered comment #"+str(current_comment.id)+" already. Skipping it in 12 hours.")
                time.sleep(43200)
                continue

    print("Loop starting over, starting new search for a comment.")
