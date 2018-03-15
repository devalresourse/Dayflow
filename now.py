# user name
name = input("what is you name?:")

# user age
age = input("how old are you")



# ask user city
city = input("your city")

# ask questions
question = input("what you like")


# create output test
string = "Your name is {} and your age is {}. your is city {} you question{}"
output = string.format(name, age, city, question)

# print output

print(output)

