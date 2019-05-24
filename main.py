import random

words = ['giraffe', 'elefant', 'mustang']
word = random.choice(words)
blank = []
for l in word:
    blank.append("_")
guessed_letters = []
attempt = len(word)
game_state = True

while game_state:
    guess = input('Please, enter your guess: ')
    if guess.lower() in guessed_letters:
        print('You have already picked this letter. Please, try another')
    elif not guess.lower().isalpha():
        print('Numbers are forbidden. Please, pick a letter')
    elif len(guess.lower()) > 1:
        print('Too much letters. You should pick only one')
    else:
        guessed_letters.append(guess)
        if guess not in word:
            attempt -= 1
            print('Sorry, no such character in this word\n'
                  'Only {} attempts left'.format(attempt))
            print((" ").join(blank))
            if attempt == 0:
                print('Sorry, you have lost this game')
                game_state = False
        else:
            start_search = 0
            search_mode = True
            while search_mode:
                try:
                    found_at = word.index(guess, start_search)
                    blank[found_at] = guess
                    start_search = start_search + 1
                except:
                    search_mode = False
            print((" ").join(blank))
            if '_' not in blank:
                print("Felicidades, you have won this game")
                game_state = False