from oprogramowanie_sterownika_PK.narzedzia.narzedzia import (wyczysc_ekran, sprawdz_dane_wejsciowe_od_do,
                                 sprawdz_dlugosc_list)
from oprogramowanie_sterownika_PK.struktury.menu_zadan import menu_zadan


def menu_glowne():
    """
    Główne menu programu do obsługi struktur pól komutacyjnych.

    Funkcja obsługuje wybór struktury pola komutacyjnego (np. pole Closa)
    oraz pozwala wybrać algorytm sterowania.
    Użytkownik może skonfigurować parametry pola, takie jak liczba sekcji i
    wektory wejściowe/wyjściowe, a następnie przejść do dedykowanego menu.

    Zmienne lokalne:
        typ_struktury (int) = przyjmuje wartość 1-4, przechowuje informacje o wybranym typie struktury, Clos, Benes, ...
        wl (list): Lista rozmiarów komutatorów z lewej strony (wektor wejściowy).
        wp (list): Lista rozmiarów komutatorów z prawej strony (wektor wyjściowy).
        liczba_sekcji (int): Liczba sekcji w polu komutacyjnym.
        algorytm (int): Wybrany typ algorytmu sterowania:
            - 1: Kolejnościowy,
            - 2: Quasi-przypadkowy,
            - 3: Algorytm Benesa,
            - 4: Przestrajalny (z dodatkowym wyborem algorytmu).
        czy_przestrojen (bool): Flaga określająca, czy algorytm wymaga przestrajania.

    :return: None
    """
    wyczysc_ekran()
    while True:
        print("\--- Menu Główne ---")
        print("1. Utwórz pole o strukturze Closa")
        print("2. Utwórz pole o strukturze Benesa")
        print("3. Utwórz pole o strukturze Cantora")
        print("4. Wyjdź")
        typ_struktury = sprawdz_dane_wejsciowe_od_do("Wybierz opcję: ", 1,4)
        if typ_struktury == 1:
            while True:
                wyczysc_ekran()

                while True:
                    liczba_sekcji = sprawdz_dane_wejsciowe_od_do("\nPodaj liczbę sekcji pola: ", 1, 13)
                    if liczba_sekcji is None:
                        print("Niepoprawnie wpisano liczbę sekcji, spróbuj jeszcze raz.")
                    if liczba_sekcji % 2 == 0:
                        print("Liczba sekcji musi być nieparzystą liczbą całkowitą z zakresu <1,13>")

                    #dodatkowy warunek, bo wzdrożono rozwiązania dla 3sekcyjnego pola
                    if liczba_sekcji != 3:
                        print("W oprogramowaniu wdrożono jedynie rozwiązania dla struktury 3-sekcyjnej!")
                    else:
                        break

                # sprawdzenie, czy wektor wl i wp mają taki sam rozmiar i czy wartości > 0
                wl, wp = sprawdz_dlugosc_list(liczba_sekcji)

                czy_przestrojen = False

                # wybór algorytmu sterowania
                algorytm = sprawdz_dane_wejsciowe_od_do("\nPodaj z jakiego algorytmu sterowania chcesz korzystać:"
                                                             "\n 1. kolejnościowy"
                                                             "\n 2. quasi-przypadkowy"
                                                             "\n 3. Benesa"
                                                             "\n 4. przestrajalny"
                                                             "\n Wybierz algorytm: ", 1, 4)
                if algorytm == 4:
                    czy_przestrojen = True
                    algorytm = sprawdz_dane_wejsciowe_od_do("\nPodaj z jakiego algorytmu sterowania chcesz korzystać:"
                                                             "\n 1. kolejnościowy"
                                                             "\n 2. quasi-przypadkowy"
                                                             "\n 3. Benesa", 1, 3)

                # przejście do menu dla pola Closa, 3-sekcyjne
                menu_zadan(typ_struktury, liczba_sekcji, wl, wp, algorytm, czy_przestrojen)
                break

        elif typ_struktury == 2:
            print("\nW ramach oprogramowania sterownika PK, struktura Benesa nie została wdrożona")
            input("\nNaciśnij Enter, aby wrócić do menu struktury...")
            wyczysc_ekran()
            continue

        elif typ_struktury == 3:
            print("\nW ramach oprogramowania sterownika PK, struktura Cantora nie została wdrożona")
            input("\nNaciśnij Enter, aby wrócić do menu struktury...")
            wyczysc_ekran()
            continue

        elif typ_struktury == 4:
            print("Wyjście z programu...")
            break

        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")
            input("Naciśnij Enter, aby spróbować ponownie...")


if __name__ == "__main__":
    menu_glowne()
