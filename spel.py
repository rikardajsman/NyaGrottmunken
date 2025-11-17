print("Hej spelet!")


print("Grottmunkenspelet")
print("")

score = 0

print("1. Vad är 2+7?")
answer1 = input("Ange ditt svar ")

if answer1 == "9":
    score += 1

print("Du fick " + str(score +"/1"))
