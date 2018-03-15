# here is a very long word

word = "antidisestablishmentarianism"

# use a slice to take out the word "establishment"
# and store it in the answer variable....
word = (word [word.index("estab") : word.index("arianism")])
answer = (word)
print (answer)
