#Calc 0.6 Alpha
print ("Calculator Alpha 0.8 Build 186")
def add(num, num2):
    return num + num2
def substract (num, num2):
    return num - num2
def multiply(num,num2):
    return num*num2
def divide(num,num2):
    return num/num2
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
while True:
    choice = input("Enter choice(1/2/3/4)(Note:If you tipe any other,the script will be restarted.): ")

    if choice in ('1', '2','3','4'):
        num = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

    if choice == '1':
            print("=", add(num, num2))
            
    elif choice == '2':
        print("=", substract(num, num2))

    elif choice=='3':
        print("=",multiply(num,num2))

    elif choice=='4':
        print("=",divide(num,num2))
            

    else:
        print ("Reseting...")
