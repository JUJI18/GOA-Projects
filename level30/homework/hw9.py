#9) გამოიყენეთ append და pop რომ დაატრიალოთ ლისტი და დაპრინტეთ შემდეგ 


my_list = ["ვაშლი", "მსხალი", "ატამი", "ალუბალი"]




reversed_fruit = []


while my_list:
    item = my_list.pop()  # ამოიღე ბოლო ელემენტი
    reversed_fruit.append(item)  # დაამატე გადატრიალებულ სიაში

print(reversed_fruit)