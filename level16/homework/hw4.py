#4) გიორგიმ შექმნა ზოოპარკი სადაც შესვლა მხოლოდ კონკრეტული აღნაგობის ხალხს შეუძლიათ. 
# გიორგი ზოოპარკში უშვებს ხალხს რომელიც 180 სანტიმეტრზე მაღლები არიან და 50-90 კილოს შორის არიან წონით. 
# თქვენი მისიაა რომ მომხმარებელს შემოატანინოთ წონა და სიმაღლე და გაარკვიოთ შეუძლია თუ არა მომხმარებელს ზოოპარკის მონახულება.


user_weight = int(input("enter your weight here:"))
print("okay, now")
user_height = int(input("enter your height here:"))

if user_weight < 50 or user_weight > 90 or user_height < 180:
    print("you can't enter the zoo😒")

else: 
    print("you can enter to the zoo🙌")

