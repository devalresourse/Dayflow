known_users=["Alice", "Bob", "Claire", "Dan", "Emma", "Shola", "Kemi", "Tomi"]

print(len(known_user))

while True:
    print("Hi!, My name is Travis")
    name=input("what is your name?:).strip().capitalize()

    if name is known_user:
        print("Hello {}!".format(name)
               
    else:
        print("name NOT recognised")
               
