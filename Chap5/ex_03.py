def computepay(hours, rate):
    if hours <= 40:
        pay = hours * rate
    else:
        pay = 40 * rate + (hours - 40) * (rate * 1.5)
        
    return pay

# Capture hours data and check
try:
    inputHours = input("Enter Hours: ")
    hours = float(inputHours)
    inputRate = input("Enter Rate: ")
    rate = float(inputRate)
    
    # Compute pay
    pay = computepay(hours, rate)
    
    # Printing results
    print("Pay:",pay)
    
except:
    print("Please, enter numerico input")
    
    