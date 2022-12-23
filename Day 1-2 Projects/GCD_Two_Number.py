# GCD stands for Greatest Common Divisor
num1 = int(input("Enter Your First Number : "))
num2 = int(input("Enter Your second Number : "))
i = 1
while(i<=num1 and i<=num2):
  if(num1%i==0 and num2%i==0):
    gcd = i
  i = i + 1
print("The GCD of your number : ",gcd)
