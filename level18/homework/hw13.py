# 13) მომხმარბელს შემოატანინეთ რიცხვი შემდეგ კი მომხმარებლის შემოტანილ რიცხვამდე დაბეჭდეთ მხოლოდ ხუთის ჯერადი რიცხვები

number = int(input("enter number:"))



for i in range(1, number ):
    if i %5 == 0:
        print(i)