def hangman (word):
    wrong = 0
    stages = ["",
              "                       ",
                __________
              "|                      ",
              "|         |            ",
              "|         0            ",
              "|        /|\           ",
              "|        / \           ",
              "|                      "
              ]
    rletters = list(word)
    board = ["___"] * len(word)
    win = false
    print("Welcome to Hangman")
