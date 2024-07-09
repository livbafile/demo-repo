
#************************************************************
# scrabble letters with their point value                    *
#************************************************************
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]


#*************************************************************
#  zip the two dictionaries, letters and points together     *
#  dictionary comprehansion                                  *
#*************************************************************
letter_to_points = {letters:points for letters, points in zip(letters, points)}
letter_to_points[" "] = 0


#***************************************************************
# function that calculates the score of the word - when called *
#***************************************************************
def score_word(word):
    point_total = 0
    
    for letter in word.upper() or letter in word.lower():
        if letter not in letter_to_points:
            point_total += 0
        else:
            point_total += letter_to_points[letter]

    return point_total

#***************************************************************************
# creation of a new dictionary with player names and a list of their words *
#***************************************************************************
player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], 
                   "wordNerd": ["EARTH", "EYES", "MACHINE"], 
                   "Lexi Con": ["ERASER", "BELLY", "HUSKY"], 
                   "Prof Reader": ["ZAP", "COMA", "PERIOD"]
                   }

# create an empty dictionary to keep each name and score
player_to_points = {}

#================================================================================================================
#Iterate through the items in player_to_words. Call each player player and each list of words words.
#Within your loop, create a variable called player_points and set it to 0.
#
#Within the loop, create another loop that goes through each word in words and adds the value of score_word() 
#with word as an input.
#================================================================================================================
def update_point_totals():
    
    for player, words in player_to_words.items():
        player_points = 0
        for word in words:
            player_points += score_word(word)
        player_to_points[player] = player_points

#=====================================================================================
#play_word() — a function that would take in a player and a word, 
#and add that word to the list of words they’ve played
#=====================================================================================
def play_word(player, word):

    player_to_words[player].append(word)
        
    return "Player and Word Added"

#=====================================================================================

#=============== TESTING DATA ========================
#play_word('Lexi Con', 'ROCKING')
update_point_totals()
print(player_to_points)
print(player_to_words)
