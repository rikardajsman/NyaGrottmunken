import random

class Spelare:
    def __init__(self, name, grott_name):
        self.name = name
        self.grott_name = grott_name

def new_player():
    name = input('Ange ditt namn: ')
    grott_name = input('Ange ditt grottnamn: ')
    return Spelare(name, grott_name)

p1 = new_player()

quiz_list = [
    ("Vad heter vår statsminister?",
     ["ulf kristersson", "kristersson", "ulf", "ulf kristersson"]),

    ("Vad hette Sveriges senaste union?",
     ["sverige-norgeunionen", "sverige-norge", "sverige-norge union", "sverige norge"]),

    ("Vilket framgångsrikt slag hände 1632 som Sverige vann, men på bekostnad av vår kung?",
     ["slaget vid lützen", "slaget vid lutzen", "lutzen", "lützen", "slaget lutzen"]),

    ("När släpptes låten Swedish Fika?",
     ["2017"]),
]

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
    hp = 3
    chests = 0

    for question, correct_answers in quiz_list:

        if hp <= 0:
            print("\nDu svimmar i mörkret... GAME OVER!")
            return

        print(f"\nFråga: {question}")
        answer = input("Svar: ").lower().strip()

        if answer in [a.lower() for a in correct_answers]:
            print("Rätt svar! Du får 1 poäng!")
            score += 1

            if random.randint(1, 5) == 1:
                if chests < 5:
                    chests += 1
                    print("🎁 Du hittade en kista!")
                else:
                    print("Du har redan max antal kistor.")
        else:
            hp -= 1
            print(f"Fel svar! -1 HP. Du har {hp} HP kvar.")

    if hp > 0:
        print("\n🎉 Du klarade grottmunkens utmaningar!")
        print("Slutresultat:")
        print(f"Poäng: {score}")
        print(f"HP: {hp}")
        print(f"Kistor: {chests}")


        boss_fight()

    input("\nTryck Enter för att återvända till menyn.")


def dor_event():
    print("\nDu hittar en gammal dörr...")
    choice = input("Vill du gå in? (ja/nej): ").lower()
    if choice == "ja":
        print("Du öppnar dörren och fortsätter djupare in...")
    else:
        print("Du ignorerar dörren och går vidare.")


def boss_fight():
    global hp, score, chests
    boss_hp = 6
    print("\nDu möter en boss! Striden börjar...")

    while boss_hp > 0 and hp > 0:
        action = input("Vill du attackera eller försvara? (attack/försvar): ").lower()
        if action == "attack":
            damage = random.randint(1, 3)
            boss_hp -= damage
            print(f"Du skadar bossen med {damage} HP! Boss HP: {max(boss_hp,0)}")
        elif action == "försvar":
            heal = random.randint(1,2)
            hp += heal
            print(f"Du återhämtar {heal} HP. Din HP: {hp}")
        else:
            print("Ogiltigt val!")

        if boss_hp > 0:
            boss_damage = random.randint(1,2)
            hp -= boss_damage
            print(f"Bossen attackerar och skadar dig med {boss_damage} HP. Din HP: {hp}")

    if hp <= 0:
        print("\nBossen besegrade dig... GAME OVER!")
    else:
        print("\n🎉 Du besegrade bossen! Grattis!")
        score += 5
        if chests < 5:
            chests += 1
            print("Du hittar en extra kista som belöning!")

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

# ---------------- MENYVAL ----------------
def settings():
    print("\n=== Inställningar ===")
    print("Inga inställningar finns ännu :)")
    input("Tryck Enter för att återvända till menyn.")

def secret_mode():
    print("\n*** Hemligt läge aktiverat! ***")
    print("Skåda hemligheten: https://www.youtube.com/watch?v=xvFZjo5PgG0")
    print("Där uppe är hemligheten.")
    input("Tryck Enter för att återvända till menyn.")

def statistik():
    print("\n=== Här är tabellen för all-time. ===")
    print("Du kanske kan bli en av de som har klarat spelet bäst!")
    print("Spelutvecklarna")
    input("Tryck Enter för att återvända till menyn.")
