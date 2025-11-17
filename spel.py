print("Hej spelet!")
print("* Välkommen till grottan, munk. *")
print("Du vaknar ensam i mörkret och måste klura dig ut…\n")
print("Du har 3 liv. Misslyckas du tre gånger skickas du tillbaka till början.\n")
input("Tryck ENTER för att börja...")

print("Grottmunkenspelet")
print("")

score = 0

print("1. Vad är 2+7?")
answer1 = input("Ange ditt svar ")

if answer1 == "9":
    score += 1

print("Du fick " + str(score +"/1"))

