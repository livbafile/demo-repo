#scrabble letters with there point value
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# dictionary comprehension to create dictionary with latters and there values
letter_to_points = {key:value for key, value in zip(letters, points)}
letter_to_points[" "] = 0




# calcuate each words score
def score_word(word):
  point_total = 0

  for letter in word:
      letter = letter.upper()
        
      if letter not in letter_to_points:
          point_total += 0
      else:
          point_total += letter_to_points[letter]

  return point_total



#scabble game : dictionary with 4 players and there words
player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

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
