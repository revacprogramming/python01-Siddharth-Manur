# Conditional Execution
hrs = input("Enter Hours:")
h = float(hrs)
rate = float(input("Enter Rate:"))
pay=h*rate if h<40 else (40*rate)+((h-40)*1.5*rate)
print(pay)
