# Capturing data
inputHours = input("Enter Hours: ")
inputRate = input("Enter Rate: ")

# Converting to float
hours = float(inputHours)
rate = float(inputRate)

# Computing the pay
if hours <= 40:
    pay = hours * rate

pay = 40 * rate + (hours - 40) * (rate * 1.5)

# Printing results
print("Pay:",pay)