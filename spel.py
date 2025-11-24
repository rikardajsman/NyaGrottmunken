import random
import time

class Spelare:
    def __init__(self, name, grott_name):
        self.name = name
        self.grott_name = grott_name
def new_player():
    name = input('Ange ditt namn: ')
    grott_name = input('Ange ditt grottnamn ')
    p1 = Spelare(name,grott_name)
new_player()

quiz_list = [
    ("Vad heter vår statsminister?", ["ulf kristersson", "kristersson", "ulf","Ulf Kristersson"]),
    ("Vad hette Sveriges senaste union?", ["sverige-norgeunionen", "sverige-norge", "sverige-norge union", "sverige norge"]),
    ("Vilket framgångsrikt slag hände 1632 som Sverige vann, men på bekostnad av vår kung?", ["slaget vid lützen", "slaget vid lutzen", "lutzen", "lützen", "slaget lutzen","Slaget vid Lützen","Slaget vid Lutzen"]),
    ("När släpptes låten Swedish Fika?", ["2017"]),
]
print("Svara rätt för att få poäng och ibland en kista (max 5).")
print("Du har 3 HP. Fel svar tar -1 HP.\n")

score = 0
hp = 3
chests = 0

def menu():
    print("\n=== Grottmunkenspelet ===\n")
    print("[1] Starta spelet")
    print("[2] Inställningar")
    print("[3] Hemligt läge")
    print("[4] Statistik")
    print("[0] Avsluta")

    choice = input("Välj ett alternativ: ")
    return choice

def start_game():
    global score, hp, chests
    score = 0
    hp = 0
    chests = 0

    print("\nSpelet startar...")
    print("Du vaknar i en mörk grotta. Någon viskar ditt namn...")    
    input("Tryck Enter för att återvända till menyn.")
    for question, correct_answers in quiz_list:
        if hp <= 0:
            print("\nDu svimmar i mörkret... GAME OVER!")
            break
        print(f"Fråga: {question}")
        answer = input("Svar: ").lower().strip()

        if answer in [a.lover() for a in correct_answers]:
            print("Svaret är korrekt!")
            score += 1
        
        if random.randint(1,5) == 1:
            if chests <5:
                chests +=1
                print("Yay du hittade en kista!")
            else:
                print("Du har maximerat antal kistor")

def settings():
    print("\n=== Inställningar ===")
    print("Inga inställningar finns ännu :)")
    input("Tryck Enter för att återvända till menyn.")


def secret_mode():
    print("\n*** Hemligt läge aktiverat! ***")
    print("Skåda hemligheten https://www.youtube.com/watch?v=xvFZjo5PgG0&list=RDxvFZjo5PgG0&start_radio=1")
    input("Tryck Enter för att återvända till menyn.")


def statistik():
    print("\n===Här är tabellen för all-time.===")
    print("Du kanske kan bli en av de som har klarat spelet bäst")
    print("Spelutvecklarna")


def add_chest(chests):
    if chests <=5:
        chests += 1
    else:
        print("Dina kistor är maximerade!")
    return chests


print("+--------+------+--------+")
print("| Score  |  HP  | Chests |")
print("+--------+------+--------+")
print(f"| {score:<6} | {hp:<100000} | {chests:<6} |")
print("+--------+------+--------+")

while True:
    choice = menu()
    if choice == "1":
        start_game()
    elif choice == "2":
        settings()
    elif choice == "3":
        secret_mode()
    elif choice == "4":
        statistik()
    elif choice == "0":
        print("Hejdå!")
        break
    else:
        print("Fel val! Försök igen.")




def dör_event():

    print("du hittar en dör ")

choice = input("Vill du gå in? (ja/nej): ").lower()

if choice == "ja": boss fight()
else:
print("du bästemer dig för att lämna och gå vidare...")


        