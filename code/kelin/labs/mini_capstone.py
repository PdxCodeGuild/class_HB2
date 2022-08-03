# https://pypi.org/project/emoji/ emoji 2.0.0
# pip install emoji
# emoji list https://carpedm20.github.io/emoji/

# https://pypi.org/project/word2emoji/ word2emoji 0.1.5
# pip install word2emoji

import emoji
import word2emoji

# using emoji list adding emoji codes to a string


print(emoji.emojize(f'Learning Python is :downcast_face_with_sweat: sometimes it can even make me feel like :exploding_head: !!!'))

# emojize takes the code and displays the emoji

def user_prompt_get_emoji(phrase):
    word = input(phrase)
    wordemoji = word2emoji(word)
    return wordemoji

    # deployed a function to take the user input for the emoji
learning = []
while True:
    wordemoji = user_prompt_get_emoji('Enter a word to describe learning Python: ')

    # word = input(f'Enter a word to describe learning Python: ')
    # wordemoji = word2emoji(word)

    wordtwoemoji = user_prompt_get_emoji('Enter another word: ')

    # word2emoji takes a word and turns it into an emoji

    learning.append ({
        'Learning Python is' : wordemoji,
        'sometimes it can make me feel like' : wordtwoemoji
        })

    # The user inputed word is turned into an emoji
    
    # emoji.demojize takes the emoji and displays the code for it

    emojicode = emoji.demojize(wordemoji)
    emojicodetwo= emoji.demojize(wordtwoemoji)

    # The emojis are turned into a message and the codes are displayed to user

    print(learning, 'The text consists of 2 emoji codes and their translations.', emojicode, 'and', emojicodetwo, emoji.emojize(emojicode), emoji.emojize(emojicodetwo))
    
    with open('emojicodes.csv', 'w') as emojicodefile:
        emojicodefile.write(emojicode)
        emojicodefile.write(emojicodetwo)
        
    # write the user emoji codes to a csv file
    
    # Add support for entering own emoji codes to display

    # Add support for all emoji codes


    # find support for AI generated content

