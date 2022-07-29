num1=float(input("entrer the first number: "))
op=input("entrer the operation: ")
num2=float(input("entrer the second number: "))
if op=="+":
    print(num1+num2)
elif op=="-":
    print(num1-num2)
elif op=="*":
    print(num1*num2)
elif op=="/" and num2!=0:
    print(num1/num2)
else:
    print("error")