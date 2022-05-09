# Conditional Execution

hrs = float(input("Enter hours? "))
rate = float(input("Enter Rate:"))
pay=hrs*rate if hrs<40 else (40*rate)+((hrs-40)*1.5*rate)
print(pay)
