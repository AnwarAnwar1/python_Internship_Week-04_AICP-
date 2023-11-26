s=3 # last digit of my cnic
def calcArea():
 #length of one side of hexagon
    print("Area of Hexagon:",1.5*1.732*s)
def calcPeri():
    print("Perimeter of Hexagon is:", 6*s)
def calcAngleSum():
    a = 120 # one angle of Hexagon
    print("Sum of angles of Hexagon:",6*a)
def display():
    calcArea()
    calcPeri()
    calcAngleSum()
def calcAreaSquare():
    print("Area of Square is :",2*s)
def calcPeriSquare():
    print("Perimeter of square is:",4*s)
def displaySq():
    calcAreaSquare()
    calcPeriSquare()

while True:
    print('-------------------------------------------------------------------------')
    print('My CNIC number is: 30302-1235713-3')
    print("Enter 1 to calculate area,perimeter and sum of angles of hexagon")
    print("Enter 2 to calculate area and perimeter of square")
    choice=input("Press any other key to exit : ")
    if choice == "1":
        display()
    elif choice == "2":
        displaySq()
    else:
        break