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

for x in range(0, 5):
    f = open('resources/hangman_stage_{fx}'.format(fx=x), 'r')
    hangman_stages.append(f.read())
    f.close()
