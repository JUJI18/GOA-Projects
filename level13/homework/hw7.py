#7) მომხმარებელს შემოატაინეთ 2 რიცხვი, და შემდეგ გამოიყენეთ შედარების 
# ოპერატორები რა რიცხვსაც შეიყვანს მომხმარებელი, მასე გამოიყენთ შედარების ოპერატორები ==,!=,<,>,<=,=>.

number1= input("დაწერე შენთვის სასურველი რიცხვი:")
print("შესანიშნავია👌")
number2 = input("ახლა კი განსხვავებული რიცხვი დაწერე:")

print(int(number1) > int(number2))
print(int(number2) > int(number1))
print(int(number1) == int(number2))
print(int(number1) <= int(number2))
print(int(number1) >= int(number2))
print(int(number2) != int(number1))