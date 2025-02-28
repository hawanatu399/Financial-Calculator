# python compound interest calculatotor

principle = 0
rate = 0
time = 0

while principale <= 0:
   principle = float(input("Enter the principal amount: "))
   if principale <= 0:
       print("principle can't be less than or equal to zero")
print(principale)

#Run
Enter the principle amount: -1000
Principle can't be less than or equal to zero
Enter the principle amount: 0
Principle can't be less than or equal to zero
Enter the principle amount: 1000

while rate <= 0:
   rate = float(input("Enter the interest rate: "))
   if rate <= 0:
       print("rate can't be less than or equal to zero")

while time <= 0:
   rate = float(input("Enter the time in years: "))
   if time <= 0:
       print("time can't be less than or equal to zero")


print(principle)
print(rate)
print(time)
#Run

total = principale * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: ${total:.2f}")
#Run


OR


while principale < 0:
   principle = float(input("Enter the principal amount: "))
   if principale < 0:
       print("principle can't be less than zero")
print(principale)

while rate < 0:
   rate = float(input("Enter the interest rate: "))
   if rate < 0:
       print("rate can't be less than zero")

while time < 0:
   rate = float(input("Enter the time in years: "))
   if time < 0:
       print("time can't be less than zero")


print(principle)
print(rate)
print(time)

It will not work 


while True < 0:
   principle = float(input("Enter the principal amount: "))
   if principale < 0:
       print("principle can't be less than zero")
print(principale)
   else:
       break

while True < 0:
   rate = float(input("Enter the interest rate: "))
   if rate < 0:
       print("rate can't be less than zero")
   else:
       break

while True < 0:
   rate = float(input("Enter the time in years: "))
   if time < 0:
       print("time can't be less than zero")
   else:
       break


print(principle)
print(rate)
print(time)
#Run
