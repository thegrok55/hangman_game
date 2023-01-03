import random

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    
    num_of_letters=len(secret_word)
    
    
    correct_letters_counter=0
           
    for char in secret_word:
        for char_2 in letters_guessed:
            if char == char_2:
                correct_letters_counter+=1
    if correct_letters_counter >= num_of_letters :
        return True
    else :
        return False

def get_available_letters(letters_guessed):
    
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
        returns: string (of letters), comprised of letters that represents which letters have not
          yet been guessed.
    '''
    
    letters='qwertyuiopasdfghjklzxcvbnm'
    availabe_letters='a b c d e f g h i j k l m n i p q r s t u v w x y z'
    for c in letters_guessed:
        if c in letters:
            availabe_letters = availabe_letters.replace(c,'')

        
    return availabe_letters

   
def same_letter(letters_guessed):
    for i in range(len(letters_guessed)-1):
        for j in range(i+1,len(letters_guessed)):
            if letters_guessed[i]  == letters_guessed [j] :
                print('you can\'t guess the same letter twice')
                old_letter=letters_guessed[j]
                new_letter=input('please enter a new letter ')
                letters_guessed=letters_guessed.replace(old_letter,new_letter,1)
                x=True
                break
            else:
                x=False
        else:
            continue
        break  
    if x is True:
       letter_guessed=same_letter(letters_guessed)
       return letter_guessed
    return letters_guessed
        
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    print('the secret word contains',len(secret_word),'letters')
    print('you start with 6 guesses')
    letters_guessed=''
    partially_guessed_word=[]

    for i in range(len(secret_word)):
        partially_guessed_word.append("_")
    counter = 0 
    while (counter <= 5):
        if counter == 0 :
            counter += 1
            letters_guessed=input('guess your first letter ')
            while letters_guessed not in 'abcdefghijklmnopqrstuvwxyz':
                print('please enter a letter')
                letters_guessed=input('guess your first letter ')
            if letters_guessed in secret_word:
                print('you guessed right!')
                for i in range(len(secret_word)):
                    if letters_guessed == secret_word[i] :
                        partially_guessed_word[i]=letters_guessed
                        
            else:
                print('you guessed wrong :( ')
            print(' '.join(partially_guessed_word))       
        else :
            print('you have',6-counter,'guesses left')
            counter += 1
            unguessed_letters=get_available_letters(letters_guessed)
            print(unguessed_letters)
            this_round_letter=input('guess another letter ')
            if this_round_letter == '*':
                show_possible_matches(partially_guessed_word)
                counter -= 1
                continue
            else:
                while this_round_letter not in 'abcdefghijklmnopqrstuvwxyz':
                    this_round_letter=input('please enter a letter ')
            letters_guessed=letters_guessed+this_round_letter
            correction=same_letter(letters_guessed)
            if letters_guessed != correction:
                
                letters_guessed = correction
                letter_index=letters_guessed.index(this_round_letter)
                this_round_letter = letters_guessed[letter_index-1]
                
            wrong_guissing = 1        

            for i in range(len(secret_word)):
                if this_round_letter == secret_word[i] :
                    partially_guessed_word[i]=secret_word[i]
                    wrong_guissing=0
                    
            if wrong_guissing == 1 :
                print('you guessed wrong')
            else : 
                print('you guessed right !')
                counter -= 1
            print(' '.join(partially_guessed_word))
            if is_word_guessed(secret_word, letters_guessed) == True:
                return 'congratulations you solved it :) '
    else :
        print ('the man got hanged and it is your fault \n    ----------------------------')            
                            
                                
def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    guessed_letters_counter = len(my_word)
    correct_letters_counter = 0
    for c in my_word :
        if c == '_' :
            guessed_letters_counter -= 1
    if len(my_word) == len(other_word):
        for i in range(len(my_word)) : 
            if my_word[i] == '_':
                continue
            elif my_word[i] == other_word[i]:
                correct_letters_counter += 1
        if correct_letters_counter == guessed_letters_counter :
            return True
        else : 
            return False
    else:
        return False
    

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    for word in wordlist :
        if match_with_gaps(my_word, word) == True :
            print(word)
        else:
            continue
        
  
secret_word = choose_word(wordlist)
hangman(secret_word)
play_again = input('do you want to play again ? (y/n) ')
while play_again == 'y' : 
    secret_word = choose_word(wordlist)
    hangman(secret_word)
    play_again = input('do you want to play again ? (y/n) ')
    
    
    
    
