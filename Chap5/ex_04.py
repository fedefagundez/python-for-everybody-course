def computeGrade(score):
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


try:
    scoreInput = input("Enter Score: ")
    score = float(scoreInput)

    computeGrade(score)

except:
    print("Bad Score")
