# 12)  მომხმარბელს შემოატანინეთ 
# რიცხვი შემდეგ კი მომხმარებლის შემოტანილ რიცხვამდე დაბეჭდეთ რიცხვები და გვერძე მიუწერეთ ლუწია თუ კენტი


number1 = int(input("დაწერე რიცხვი:"))

for i in range(1, number1 + 1):
    if i %2 == 0:
        print(str(i)+" ლუწი!")
    else:
        print(str(i)+ " კენტი")