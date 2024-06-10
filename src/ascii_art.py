#  Defining Variable from the config.txt file
contOfHangmanStages = None
global countOfHangmanStages

with open("resources/config.txt", "r") as txtf:
    exec(txtf.read())

# My first Ascii-Arts for this project :^)

line_one = """------
     |
   /^^^|
  ( °,° )
   |___/"""

line_two_1 = """     |
 /---^---|
|#########|"""

line_two_2 = """|#########|
|#########|
 ~~~~~~~~~"""

line_three = """     |
     |
     |"""

line_four = """    '''
   '' ''
  ''   ''
 ''     ''"""

# ---------------------------------

hangman_stages = []

for x in range(0, countOfHangmanStages):
    f = open('resources/hangman_stage_{fx}.txt'.format(fx=x), 'r')
    hangman_stages.append(f.read())
    f.close()
