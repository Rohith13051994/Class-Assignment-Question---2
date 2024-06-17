class SubfieldsInAI():
    def Subfields():
        AI_list=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        print("Sub-fields in AI are:")  
        for list in AI_list:
            print(list)

    def OddEven():
        Num = int(input("Enter a number: "))
        if((Num%2)==0):
            print(Num," is Even number")
        else:
            print(Num," is Odd number")

    def Eligible():
        sex=input("Your Gender:")
        age=int(input("Your Age:"))

        if(sex=="Female"):
            if(age>=18):
                print("Eligible")
            else:
                print("Not Eligible")

        elif(sex=="Male"):
            if(age>=21):
                print("Eligible")
            else:
                print("Not Eligible")

    def percentage():
        Sub1= int(input("Subject1:"))
        Sub2= int(input("Subject2:"))
        Sub3= int(input("Subject3:"))
        Sub4= int(input("Subject4:"))
        Sub5= int(input("Subject5:"))

        total = Sub1 + Sub2 + Sub3 + Sub4 + Sub5
        print("Total :", total)

        percentage = total / 5
        print("Percentage : ", percentage)

    def triangle():
        Height = int(input("Height: "))
        Breadth = int(input("Breadth: "))
        Area_of_Tri = (Height * Breadth) / 2
        print("Area formula: (Height * Breadth) / 2")
        print("Area of Triangle: ", Area_of_Tri)

        Height1 = int(input("Height1: "))
        Height2 = int(input("Height2: "))
        Breadth = int(input("Breadth: "))
        Perimeter_of_Tri = Height1 + Height2 + Breadth
        print("Perimeter formula: Height1 + Height2 + Breadth")
        print("Perimeter of Triangle: ", Perimeter_of_Tri)

