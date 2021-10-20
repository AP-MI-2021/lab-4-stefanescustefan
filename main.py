def acelasi_numar_de_pare(l1, l2):
    """
    Determina daca doua liste au acelasi numar de elemente pare

    :param l1: Prima lista de numere intregi
    :param l2: A doua lista de numere intregi
    :return: True, daca listele au acelasi numar de elemente pare, False in caz contrar
    """
    nr1 = 0
    nr2 = 0
    for x in l1:
        if x % 2 == 0:
            nr1 = nr1 + 1
    for x in l2:
        if x % 2 == 0:
            nr2 = nr2 + 1
    return nr1 == nr2


def test_acelasi_numar_de_pare():
    assert acelasi_numar_de_pare([], [5, 7]) is True
    assert acelasi_numar_de_pare([0, 5], [13, 9, 24]) is True
    assert acelasi_numar_de_pare([1, 7], [3, 33, 9, 25]) is True
    assert acelasi_numar_de_pare([2, 7, 8], [1, 5, 4]) is False
    assert acelasi_numar_de_pare([24, 2, 6], [7, 9, 10, 12]) is False


def intersectie(l1: list, l2: list):
    """
    Determina intersectia a doua multimi de numere intregi

    :param l1: Prima multime
    :param l2: A doua multime
    :return: O lista reprezentand intersectia celor doua multimi
    """
    lista_intersectie = []
    for x in l1:
        if l2.count(x) > 0 and lista_intersectie.count(x) == 0:
            lista_intersectie.append(x)
    return lista_intersectie


def test_intersectie():
    assert intersectie([], [4, 5]) == []
    assert intersectie([5, 9, 10, 17], [3, 4, 20]) == []
    assert intersectie([10, 6, 9], [13, 9]) == [9]
    assert intersectie([1, 5, 9, 10], [4, 10, 2, 5]) == [5, 10]
    assert intersectie([5, 25, 29, 30], [30, 4, 1, 7, 29]) == [29, 30]


def palindroame_concat(l1: list, l2: list):
    """
    Determina palindroamele rezultate din concatenarea a elemente de pe aceeasi pozitie

    :param l1: Prima lista
    :param l2: A doua lista
    :return: Lista de palindroame obtinute prin concatenarea elementelor aflate pe aceeasi pozitie
    """
    lista_palindroame = []
    i = 0
    while i < len(l1) and i < len(l2):
        numar_concatenat = str(l1[i]) + str(l2[i])
        if numar_concatenat == numar_concatenat[::-1]:
            lista_palindroame.append(int(numar_concatenat))
        i = i + 1
    return lista_palindroame


def test_palindroame_concat():
    assert palindroame_concat([12, 22, 36, 11], [21, 23, 63, 55, 424]) == [1221, 3663]
    assert palindroame_concat([35, 8, 90, 7, 10, 15], [53, 4, 9, 7]) == [3553, 909, 77]
    assert palindroame_concat([9, 20, 98, 17], [8, 0]) == []
    assert palindroame_concat([15, 20, 12], [16, 2, 9, 19, 245]) == [202]
    assert palindroame_concat([32, 49, 202, 15, 7], [23, 95, 2]) == [3223]


def este_divizibil_cu_toate_elementele(x, l):
    """
    Verifica daca numarul x este divizibil cu toate elementele listei l

    :param x: Un numar intreg
    :param l: O lista de numere intregi nenule
    :return: True, daca x este divizibil cu toate elementele listei l, False in caz contrar
    """
    for divizor in l:
        if x % divizor != 0:
            return False
    return True


def test_este_divizibil_cu_toate_elementele():
    assert este_divizibil_cu_toate_elementele(9, [5]) is False
    assert este_divizibil_cu_toate_elementele(8, [1, 2, 4, 9]) is False
    assert este_divizibil_cu_toate_elementele(10, [2, 5]) is True
    assert este_divizibil_cu_toate_elementele(24, [1,2,3,4,6,12]) is True
    assert este_divizibil_cu_toate_elementele(25, [5, 25]) is True


def oglindire_elemente_divizibile(l1, l2, l3):
    """
    Oglindeste elementele din l1 si l2 care sunt divizibile cu toate elementele din l3

    :param l1: Prima lista
    :param l2: A doua lista
    :param l3: Lista ce contine divizorii care impun conditia de oglindire
    :return: Tuplu de listele l1 si l2 dupa modificare
    """
    l1_nou = []
    l2_nou = []
    for x in l1:
        if este_divizibil_cu_toate_elementele(x, l3):
            l1_nou.append(int(str(x)[::-1]))
        else:
            l1_nou.append(x)
    for x in l2:
        if este_divizibil_cu_toate_elementele(x, l3):
            l2_nou.append(int(str(x)[::-1]))
        else:
            l2_nou.append(x)
    return l1_nou, l2_nou


def test_oglindire_elemente_divizibile():
    assert oglindire_elemente_divizibile([], [23, 55], [9]) == ([], [23, 55])
    assert oglindire_elemente_divizibile([12, 22, 36, 363], [22, 23, 36, 55, 363], [1, 2, 3, 4]) == (
        [21, 22, 63, 363],
        [22, 23, 63, 55, 363])
    assert oglindire_elemente_divizibile([32, 8, 20, 57], [10, 128, 78], [2, 4]) == (
        [23, 8, 2, 57],
        [10, 821, 78])
    assert oglindire_elemente_divizibile([23, 57, 40], [81, 5, 16], [1, 3]) == (
        [23, 75, 40],
        [18, 5, 16])


def citire_liste():
    """
    Citeste doua liste de numere intregi

    :return: Un tuple format din listele de numere intregi
    """
    lista_A = [int(x) for x in input("Dati lista A: ").split(",")]
    lista_B = [int(x) for x in input("Dati lista B: ").split(",")]
    return lista_A, lista_B


def print_menu():
    print("1. Citire doua liste")
    print("2. Au cele doua liste acelasi numar de elemente pare?")
    print("3. Intersectia celor doua multimi")
    print("4. Afisare palindroame obtinute prin concatenarea elementelor de pe pozitii egale")
    print("5. Inlocuire cu oglinditul daca este divizibil cu toate elementele din a treia lista")
    print("x. Iesire")


def main():
    test_acelasi_numar_de_pare()
    test_intersectie()
    test_palindroame_concat()
    test_este_divizibil_cu_toate_elementele()
    test_oglindire_elemente_divizibile()

    lista_A = []
    lista_B = []
    end = False
    while not end:
        print_menu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            lista_A, lista_B = citire_liste()
        elif optiune == "2":
            if acelasi_numar_de_pare(lista_A, lista_B):
                print("Listele A si B au acelasi numar de elemente pare")
            else:
                print("Listele A si B nu au acelasi numar de elemente pare")
        elif optiune == "3":
            print(f"Intersectia multimilor A si B este: {intersectie(lista_A, lista_B)}")
        elif optiune == "4":
            print(f"Lista de palindroame: {palindroame_concat(lista_A, lista_B)}")
        elif optiune == "5":
            lista_C = [int(x) for x in input("Dati lista C: ").split(",")]
            lista_noua_A, lista_noua_B = oglindire_elemente_divizibile(lista_A, lista_B, lista_C)
            print(lista_noua_A)
            print(lista_noua_B)
        elif optiune == "a":
            print(lista_A)
            print(lista_B)
        elif optiune == "x":
            end = True


if __name__ == "__main__":
    main()
