#3) შეადარეთ თქვენი ასაკი მომხმარებლის შემოტანილ ასაკს, თუ თქვენი ასაკი მეტია მომხმარებლის ასაკზე უთხარით 
# რომ თქვენ მასზე დიდი ხართ, თუ მასზე პატარა ხართ დაუპრინტეთ რომ მასზე პატარა ხართ და სხვა შემთხვევაში დაუპრინტეთ რომ ტოლები ხართ.

my_age = 16

user_age = int(input("Enter your age here:"))


if my_age > user_age:
    print("I'm older than you🦉")
elif my_age < user_age:
    print("You are older than me👴")

else:
    print("we are the same age😍")