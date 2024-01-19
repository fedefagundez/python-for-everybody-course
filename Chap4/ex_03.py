try:
    scoreInput = input("Enter Score: ")
    # La siguiente línea devuelve un error si
    # scoreInput no es un número
    score = float(scoreInput)

    if score < 0 or score > 1:
        print("Bad Score")

    else:
        if score >= 0.9:
            print("A")
        elif score >= 0.8:
            print("B")
        elif score >= 0.7:
            print("C")
        elif score >= 0.6:
            print("D")
        else:
            print("F")

except:
    print("Bad Score")
