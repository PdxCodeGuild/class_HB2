# https://pypi.org/project/emoji/ emoji 2.0.0
# pip install emoji
# emoji list https://carpedm20.github.io/emoji/

# https://pypi.org/project/word2emoji/ word2emoji 0.1.5
# pip install word2emoji

import emoji
import word2emoji

# Using emoji package to help describe my understanding of Python lessons:


print(emoji.emojize(f'Learning Python is :downcast_face_with_sweat: sometimes it can even make me feel like :exploding_head: !!!'))

# emojize takes the code and displays the emoji


learning = []
while True:

    word = input(f'Enter a word to describe learning Python: ')
    wordemoji = word2emoji(word)
    wordtwo = input(f'Enter another word: ')
    wordtwoemoji = word2emoji(wordtwo)



    # word2emoji takes a word and turns it into an emoji
    
    # emoji.demojize takes the emoji and displays the code for it

    learning.append ({
        'Learning Python is' : wordemoji,
        'sometimes it can make me feel like' : wordtwoemoji
        })

    # The user inputed word is turned into an emoji

    emojicode = emoji.demojize(wordemoji)
    emojicodetwo= emoji.demojize(wordtwoemoji)

    # The emojis are turned into a message and the codes are displayed to user

    learningprint = pprint.Pre(learning)

    print(learningprint, 'Your emoji codes are ',emojicode, 'and ',emojicodetwo)

    
    # Add support for entering own emoji codes

    