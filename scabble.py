
#************************************************************
# scrabble letters with their point value                    *
#************************************************************
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]


#*************************************************************
#  zip the two dictionaries, letters and points together     *
#  dictionary comprehansion                                  *
#*************************************************************
letter_to_points = {key:value for key, value in zip(letters, points)}
letter_to_points[" "] = 0


#***************************************************************
# function that calculates the score of the word - when called *
#***************************************************************
def score_word(word):
  point_total = 0

  for letter in word:
      letter = letter.upper()
        
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

# iterate through player_to_words 
for player, words in player_to_words.items():
    player_points = 0
    # for each of the words
    for word in words:
        # call score_word function and pass each word to it
        # add up the points per word
        player_points += score_word(word)
    
    player_to_points[player] = player_points

print(player_to_points)

# function called play_word() that will take in a 'player' and a 'word', and add that word to the list of words they’ve played
def play_word(player, word):
    player_to_words[player].append(word)


#testing and adding other functions - 

# add to play_word dictionary
#print(player_to_words)
#play_word('Lexi Con', 'ORANGE')
#play_word('wordNerd', 'TRIANGLE')
#play_word('Prof Reader', 'UMBRELLA')
#play_word('player1', 'TORNADOE')
#print(player_to_words)

## function called update_point_totals() - call any time a word is played

def update_point_totals():
    #player_to_points = {}

    for player, words in player_to_words.items():
        player_points = 0
        for word in words:
            player_points += score_word(word)
    
        player_to_points[player] = player_points

print(player_to_points)

# call update_point_totals 
update_point_totals()

print(player_to_points)

print(player_to_words)
