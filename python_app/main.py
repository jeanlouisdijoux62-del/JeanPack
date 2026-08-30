import sys

def menu():
    print("\n=== Logiciel Auto Jean ===")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quitter")

def get_number(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        print("Erreur : entre un nombre.")
        return None

def addition():
    a = get_number("A : ")
    b = get_number("B : ")
    if a is not None and b is not None:
        print("Résultat :", a + b)

def soustraction():
    a = get_number("A : ")
    b = get_number("B : ")
    if a is not None and b is not None:
        print("Résultat :", a - b)

def multiplication():
    a = get_number("A : ")
    b = get_number("B : ")
    if a is not None and b is not None:
        print("Résultat :", a * b)

def division():
    a = get_number("A : ")
    b = get_number("B : ")
    if a is None or b is None: return
    if b == 0:
        print("Division par zéro impossible.")
    else:
        print("Résultat :", a / b)

def main():
    while True:
        menu()
        choix = input("Choix : ").strip()
        if choix == "1": addition()
        elif choix == "2": soustraction()
        elif choix == "3": multiplication()
        elif choix == "4": division()
        elif choix == "5":
            print("Au revoir Jean.")
            sys.exit()
        else:
            print("Choix invalide.")

if __name__ == "__main__":
    main()
