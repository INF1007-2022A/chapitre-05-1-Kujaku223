#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
        if number < 0:
            return -1* number
       # return abs(number)
    return number



def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    SPACE = ' '
    noms = ''
    for lettre in prefixes:
        nom+= f"(lettre){suffixe}"
    return nom.split()
print (use_prefixes())

def prime_integer_summation() -> int:
    return 0


def factorial(number: int) -> int:
    for i in range(2, nombre):
    number *= i
    print(number)
    return number


def use_continue() -> None:
    or i in range(1, 10 + 1):
    if i == 5:
        continue
    print(i)
    pass


def verify_ages(groups: List[List[int]]) -> List[bool]:
    return []


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")
SPACE = " "
result = ""
for groupe  in groupes:
    print(groupe)
    if len(groupe)>10 or len(groupe)<3:
        result += str(False) + SPACE
        continue
    if 25 in groupe:
        result += str(True) + SPACE
        continue
    if min(groupe) < 18:
        result += str(False) + SPACE
        continue
    if max(groupe)>70 and 50 in groupe:
        result += str(False) + SPACE
        continue
    return result += str.split()
print verify_ages(groupes))

if __name__ == '__main__':
    main()
