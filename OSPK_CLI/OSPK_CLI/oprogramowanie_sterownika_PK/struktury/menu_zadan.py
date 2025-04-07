from oprogramowanie_sterownika_PK.algorytmy.kolejnosciowy import algorytm_kolejnosciowy
from oprogramowanie_sterownika_PK.algorytmy.quasi_przypadkowy import algorytm_quasi_przypadkowy
from oprogramowanie_sterownika_PK.algorytmy.benes import algorytm_benesa
from oprogramowanie_sterownika_PK.narzedzia.narzedzia import (sprawdz_dane_wejsciowe_od_do, wyczysc_ekran,
                                                              sprawdz_wartosci_we_wy, znajdz_klucz_id_polaczenia)
from oprogramowanie_sterownika_PK.struktury.clos import utworz_strukture_closa


def menu_zadan(typ_struktury, liczba_sekcji, wl, wp, algorytm, czy_przestrojen):
    """
        OFunkcja menu_zadan obsługuje menu interakcji użytkownika dla zarządzania polem o dowolnej strukturze z
        możliwych do wybrania w funkcji menu_glowne, której kod znajduje się w pliku main.py. W funkcji menu_zadan
        deklarowana jest pusta lista struktura, która następnie uzupełniana jest poprzez wywołanie funkcji
        utworz_pole_closa, oraz pusty słownik slownik_polaczen, do którego w ramach wykonywanych zadań będą dodawane
        lub usuwane zapisy o połączeniach. Z poziomu tego menu wywoływane są funkcje poszczególnych zadań,
        takich jak zadanie połączenia, rozłączenie połączenia, czy wyświetlenia tablicy połączeń.

        :param typ_struktury: parametr typu int, przyjmuje wartość 1-4, gdzie 1-struktura Closa, 2-struktura Benesa,
        3-struktura Cantora, 4-wyjście z programu,
        :param liczba_sekcji: parametr typu int, określa liczbę sekcji w polu komutacyjnym,
        :param wl: lista zawierająca wartości typu int, przedstawia lewostronny rozmiar komutatorów;
        każda komórka tej listy zawiera informacje o komutatorach jednej sekcji,
        :param wp: (list) lista zawierająca wartości typu int, przedstawia prawostronny rozmiar komutatorów;
        każda komórka tej listy zawiera informacje o komutatorach jednej sekcji,
        :param algorytm: Typ algorytmu zestawiania połączeń:
            - `1`: Algorytm sekwencyjny.
            - `2`: Algorytm quasi-przypadkowy.
            - `3`: Algorytm Benesa.
        :param czy_przestrojen: Flaga wskazująca, czy podczas zestawiania połączeń w przypadku blokady ma być używany algorytm przestrojeń (rearrange).
            - `True`: Stosowanie algorytmu przestrojeń
            - `False`: niestosowanie algorytmu przestrojeń

        Operacje dostępne w menu:
        1. Zestawienie połączenia:
           - Użytkownik podaje numer portu wejściowego i wyjściowego, a algorytm zestawia połączenie.
        2. Rozłączenie połączenia:
           - Usunięcie istniejącego połączenia.
        3. Wyświetlenie tablicy połączeń:
           - Pełna lista wszystkich aktywnych połączeń w polu.
        4. Wyświetlenie konkretnych połączeń:
           - Szczegółowe informacje o połączeniach dla wybranych portów.
        5. Wyświetlenie struktury pola:
           - przedstawienie obecnego stanu pola.
        6. Powrót do głównego menu:
           - Zakończenie pracy funkcji.

        Funkcja obsługuje następujące algorytmy:
        - **Algorytm sekwencyjny**: Wykorzystuje ustaloną kolejność przy zestawianiu połączeń.
        - **Algorytm quasi-przypadkowy**: Wybiera last+1 komutator do zestawienia połączenia.
        - **Algorytm Benesa**: Zestawienia połączeń poprzez najbardziej obciążone komutatory.
        - **Algorytm przestrojeń**: Przestrojenia w celu zestawienia zadanego połączenia.

        Struktura danych:
        - `struktura`: Lista trójwymiarowych macierzy reprezentujących sekcje pola Closa.
        - `slownik_polaczen`: Słownik przechowujący obecne połączenia w formacie `klucz: wartość`, gdzie klucz to `(wejście, wyjście)`, a wartość to lista połączeń na ścieżce.

        :return: Funkcja nie zwraca wartości, wywołuje odpowiednie procedury i modyfikuje strukturę pola oraz połączenia.
        """
    # stworzenie listy 3-wymiarowych macierzy przedstawiających stan pola - dla wdrożenie innych dopisać if
    if typ_struktury == 1:

        # tworzenie struktury dla Closa
        struktura = utworz_strukture_closa(liczba_sekcji, wl, wp)

    # tworzenie słownika, który pełni rolę listy połączeń
    slownik_polaczen = {}
    """
    # testy dla sprawdzenia algorytmu przestrojeń -> zestaw np. (3, 12)
    #1sekcja
    struktura[0][0, 0, 0] = 1 #0-0
    struktura[0][0, 1, 1] = 1 #1-1
    struktura[0][1, 0, 0] = 1 #4-8
    struktura[0][1, 1, 1] = 1 #5-9
    struktura[0][2, 2, 2] = 1 #10-6
    struktura[0][2, 3, 3] = 1 #11-7
    struktura[0][3, 0, 0] = 1 #12-4
    struktura[0][3, 2, 2] = 1 #14-14
    struktura[0][3, 3, 3] = 1 #15-15
    #2sekcja
    struktura[1][0, 0, 0] = 1 #0-0
    struktura[1][0, 1, 2] = 1 #4-8
    struktura[1][0, 3, 1] = 1 #12-4
    struktura[1][1, 0, 0] = 1 #1-1
    struktura[1][1, 1, 2] = 1 #5-9
    struktura[1][2, 2, 1] = 1 #10-6
    struktura[1][2, 3, 3] = 1 #14-14
    struktura[1][3, 2, 1] = 1 #11-7
    struktura[1][3, 3, 3] = 1 #15-15
    #3sekcja
    struktura[2][0, 0, 0] = 1 #0-0
    struktura[2][0, 1, 1] = 1 #1-1
    struktura[2][1, 0, 0] = 1 #12-4
    struktura[2][1, 1, 3] = 1 #11-7
    struktura[2][1, 2, 2] = 1 #10-6
    struktura[2][2, 0, 0] = 1 #4-8
    struktura[2][2, 1, 1] = 1 #5-9
    struktura[2][3, 2, 2] = 1 #14-14
    struktura[2][3, 3, 3] = 1 #15-15
    slownik_polaczen[f'({0},{0})'] = []
    slownik_polaczen[f'({1},{1})'] = []
    slownik_polaczen[f'({4},{8})'] = []
    slownik_polaczen[f'({5},{9})'] = []
    slownik_polaczen[f'({10},{6})'] = []
    slownik_polaczen[f'({11},{7})'] = []
    slownik_polaczen[f'({12},{4})'] = []
    slownik_polaczen[f'({14},{14})'] = []
    slownik_polaczen[f'({15},{15})'] = []
    slownik_polaczen[f'({0},{0})'].append((0, 0, 0))
    slownik_polaczen[f'({0},{0})'].append((0, 0, 0))
    slownik_polaczen[f'({0},{0})'].append((0, 0, 0))
    slownik_polaczen[f'({1},{1})'].append((0, 1, 1))
    slownik_polaczen[f'({1},{1})'].append((1, 0, 0))
    slownik_polaczen[f'({1},{1})'].append((0, 1, 1))
    slownik_polaczen[f'({4},{8})'].append((1, 0, 0))
    slownik_polaczen[f'({4},{8})'].append((0, 1, 2))
    slownik_polaczen[f'({4},{8})'].append((2, 0, 0))
    slownik_polaczen[f'({5},{9})'].append((1, 1, 1))
    slownik_polaczen[f'({5},{9})'].append((1, 1, 2))
    slownik_polaczen[f'({5},{9})'].append((2, 1, 1))
    slownik_polaczen[f'({10},{6})'].append((2, 2, 2))
    slownik_polaczen[f'({10},{6})'].append((2, 2, 1))
    slownik_polaczen[f'({10},{6})'].append((1, 2, 2))
    slownik_polaczen[f'({11},{7})'].append((2, 3, 3))
    slownik_polaczen[f'({11},{7})'].append((3, 2, 1))
    slownik_polaczen[f'({11},{7})'].append((1, 1, 3))
    slownik_polaczen[f'({12},{4})'].append((3, 0, 0))
    slownik_polaczen[f'({12},{4})'].append((0, 3, 1))
    slownik_polaczen[f'({12},{4})'].append((1, 0, 0))
    slownik_polaczen[f'({14},{14})'].append((3, 2, 2))
    slownik_polaczen[f'({14},{14})'].append((2, 3, 3))
    slownik_polaczen[f'({14},{14})'].append((3, 2, 2))
    slownik_polaczen[f'({15},{15})'].append((3, 3, 3))
    slownik_polaczen[f'({15},{15})'].append((3, 3, 3))
    slownik_polaczen[f'({15},{15})'].append((3, 3, 3))
    """



    # deklaracja zmiennej ostatnio_uzyty_komutator dla quasi-przypadkowy
    ostatnio_uzyty_komutator = -1

    while True:
        wyczysc_ekran()
        print("Menu operacji na polu:")
        print("1. Zestaw połączenie")
        print("2. Rozłącz połączenie")
        print("3. Wyświetl tablicę połączeń")
        print("4. Wyświetl konkretne połączenie")
        print("5. Wyświetl stan struktury pola")
        print("6. Powrót do głównego menu")
        wybor = input("Wybierz opcję: ")

        if wybor == '1':
            # zestawienie połączenia jest zależne od typu struktury, bo jeżeli inna struktura, to wymagana jest modyfikacja algorytmu
            if typ_struktury == 1:
                struktura, slownik_polaczen, ostatnio_uzyty_komutator = zestaw_polaczenie(typ_struktury, struktura, wl, wp, slownik_polaczen, algorytm, czy_przestrojen, ostatnio_uzyty_komutator)

        elif wybor == '2':
            # operacja rozłączenia połączenia
            struktura, slownik_polaczen = rozlacz_polaczenie(struktura, slownik_polaczen)

        elif wybor == '3':
            pokaz_tablice_polaczen(slownik_polaczen, True)

        elif wybor == '4':
            pokaz_tablice_polaczen(slownik_polaczen, False)

        elif wybor == '5':
            pokaz_stan_struktury(struktura)

        elif wybor == '6':
            wyczysc_ekran()
            return
        else:

            print("Nieprawidłowy wybór. Spróbuj ponownie.")
            input("Naciśnij Enter, aby spróbować ponownie...")


def zestaw_polaczenie(typ_struktury, struktura, wl, wp, slownik_polaczen, algorytm, czy_przestrojen, ostatnio_uzyty_komutator):
    """
    Funkcja zestaw_polaczenie realizuje obsługę wprowadzenia zmiennych x i y,
    które przedstawiają odpowiednio wejście i wyjście zadanego połączenia.

    :param typ_struktury: parametr typu int, przyjmuje wartość 1-4, gdzie 1-struktura Closa, 2-struktura Benesa,
    3-struktura Cantora
    :param struktura: lista zawierająca macierze trójwymiarowe reprezentujące odwzorowanie stanu struktury pola
    :param wl: lista zawierająca wartości typu int, przedstawia lewostronny rozmiar komutatorów
    :param wp: lista zawierająca wartości typu int, przedstawia prawostronny rozmiar komutatorów
    :param slownik_polaczen: słownik przechowujący informacje o istniejących połączeniach
    :param algorytm: parametr typu int, przechowuje informacje o wybranym alg. sterowania
    :param czy_przestrojen: flaga określająca, czy wybrano algorytm przestrojeń,
    :param ostatnio_uzyty_komutator: zmienna przechowująca indeks ostatnio uzytego komutatora dla algorytmu quasi-przypadkowego
    :return:
    """
    # największy numer wejścia/wyjścia
    max_nr_komutatora = wl[0] * wl[1] - 1

    x = sprawdz_dane_wejsciowe_od_do(f"\nPodaj łącze wejściowe (0 - {max_nr_komutatora}):",0, max_nr_komutatora)
    y = sprawdz_dane_wejsciowe_od_do(f"Podaj łącze wyjściowe (0 - {max_nr_komutatora}):", 0, max_nr_komutatora)

    if algorytm == 1:
        # wywolanie zestawienia za pomocą algorytmu sekwencyjnego
        struktura, slownik_polaczen = (
            algorytm_kolejnosciowy(typ_struktury, struktura, wl, wp, x, y, slownik_polaczen, czy_przestrojen))

    elif algorytm == 2:
        # wywolanie zestawienia za pomocą quasi-przypadkowego
        struktura, slownik_polaczen, ostatnio_uzyty_komutator = (
            algorytm_quasi_przypadkowy(typ_struktury, struktura, wl, wp, x, y, slownik_polaczen, ostatnio_uzyty_komutator,
                                       czy_przestrojen))

    elif algorytm == 3:
        # wywolanie zestawienia za pomocą algorytmu Benesa
        struktura, slownik_polaczen = (
            algorytm_benesa(typ_struktury, struktura, wl, wp, x, y, slownik_polaczen, czy_przestrojen))
    return struktura, slownik_polaczen, ostatnio_uzyty_komutator


def rozlacz_polaczenie(struktura, slownik_polaczen):
    """
        Realizacja operacji rozłączania połączenia.

    :param struktura: Lista 3-wymiarowych macierzy ze stanem struktury pola.
    :param slownik_polaczen: Słownik z połączeniami.
    :return:
    """
    numer_sekcji = 0
    # structure[sekcja][nr_komutatora, wiersz, kolumna] < -- [nr_komutatora, we, wy]
    x = sprawdz_wartosci_we_wy(f"\nPodaj łącze wejściowe:")
    y = sprawdz_wartosci_we_wy(f"Podaj łącze wyjściowe:")

    if x is None and y is None:
        print("\nNieprawidłowa wartość: Nie można pozostawić x i y pustych.")
        input("\nNaciśnij Enter, aby wrócić do menu operacji...")
        return struktura, slownik_polaczen

    else:
        # identyfikator polaczenia do rozlaczenia
        id_klucz = znajdz_klucz_id_polaczenia(x, y, slownik_polaczen)

    if id_klucz in slownik_polaczen:

        for polaczenie in slownik_polaczen[id_klucz]:
            # czytanie slownika
            nr_komutatora, wiersz, kolumna = polaczenie
            # usuwanie polaczen ze struktury
            struktura[numer_sekcji][nr_komutatora, wiersz, kolumna] = 0
            numer_sekcji += 1

        # usuwanie rekordu z slownika
        print(f"\nUsunięto połączenie {id_klucz} !")
        pozycje = slownik_polaczen[id_klucz]
        pozycje_str = ','.join([f"({k},{we},{wy})" for k, we, wy in pozycje])
        print(f"d{id_klucz} = {{{pozycje_str}}}")
        del slownik_polaczen[id_klucz]

    else:
        print(f'\nNie ma takiego połączenia')
    input("\nNaciśnij Enter, aby wrócić do menu operacji...")
    return struktura, slownik_polaczen


def pokaz_tablice_polaczen(slownik_polaczen, wszystkie_czy_jedno):
    """
    Wyświetla tablicę połączeń w formacie ‘d(x,y) = {(nr_komutatora,we,wy),…}’
    w osobnej linijce dla każdego połączenia lub jedynie wyświetla konkretne
    połączenie w zależności od wartości zmiennej wszystkie_czy_jedno.

    :param slownik_polaczen: słownik przechowujący informacje o istniejących połączeniach
    :param wszystkie_czy_jedno: flaga określająca, czy wyświetlone ma zostać
    konkretne połączenie - False, czy cała tablica, czyli wszystkie połączenia - True,
    :return:
    """

    wyczysc_ekran()

    if wszystkie_czy_jedno:

        # wyswietlenie wszystkich polaczen
        print('========Tablica zestawionych połączeń========')
        print('format drogi: d(x,y) = {(komutator,we,wy), (komutator,we,wy), ...}\n')

        # petla dla wszystkich polaczen w slowniku
        for id_polaczenia, pozycje in slownik_polaczen.items():
            # format przedstawienia
            pozycje_str = ','.join([f"({k},{we},{wy})" for k, we, wy in pozycje])
            # wyswietlanie
            print(f"d{id_polaczenia} = {{{pozycje_str}}}")

    else:

        # wyswietlenie pojedynczego polaczenia
        x = sprawdz_wartosci_we_wy(f"Podaj łącze wejściowe:")
        y = sprawdz_wartosci_we_wy(f"Podaj łącze wyjściowe:")

        if x is None and y is None:
            print("\nNieprawidłowa wartość: Nie można pozostawić obu wejść pustych.")

        else:
            # sprawdzenie, czy połączenie istnieje w słowniku połączeń
            id_klucz = znajdz_klucz_id_polaczenia(x, y, slownik_polaczen)

            if id_klucz in slownik_polaczen:
                print('format drogi: d(x,y) = {(komutator,we,wy),(komutator,we,wy), ...}\n')
                pozycje = slownik_polaczen[id_klucz]
                pozycje_str = ','.join([f"({k},{we},{wy})" for k, we, wy in pozycje])
                print(f"d{id_klucz} = {{{pozycje_str}}}")

            else:
                print(f'Nie ma takiego połączenia')
    input("\nNaciśnij Enter, aby wrócić do menu operacji...")
    return


def pokaz_stan_struktury(struktura):
    """
        Wyświetla odwzorowanie stanu struktury pola na interfejsie
        wiersza poleceń poprzez odczytanie listy struktura i wypisanie jej sformatowanej zawartości

    :param struktura: Lista zawierająca 3-wymiarowe macierze ze stanem struktury pola.

    :return:
    """
    wyczysc_ekran()
    # przygotowanie nagłówków dla sekcji
    naglowki = "    ".join([f"Sekcja {i + 1}:" for i in range(len(struktura))])
    print(naglowki)

    # maksymalna liczba komutatorów w strukturze (dla wyrównania wierszy)
    max_komutatory = max(len(sekcja) for sekcja in struktura)

    # iteracja przez komutatory (macierze 2D) w sekcjach
    for komutator in range(max_komutatory):
        # przygotowanie wierszy do wyświetlenia dla każdej sekcji
        macierze_wiersze = []
        for sekcja in struktura:
            if komutator < len(sekcja):
                # pozbijanie macierz 2D na wiersze i zapisujemy jako listę stringów
                wiersze = [" ".join(map(str, map(int, wiersz))) for wiersz in sekcja[komutator]]
                macierze_wiersze.append(wiersze)
            else:
                # dodanie pustych wierszy, jeśli koniec komutatorów w sekcji
                macierze_wiersze.append([" " * 30] * len(struktura[0][0]))

        # wyświetlenie wierszy macierzy obok siebie
        for wiersz_idx in range(len(macierze_wiersze[0])):  # dla każdego wiersza
            linia = "      ".join(macierze[wiersz_idx] for macierze in macierze_wiersze)
            print(linia)

        # dodanie linii odstępu między kolejnymi macierzami
        print()

    # linie oddzielające dla czytelności
    print("\n" + "-" * 80)
    input("\nNaciśnij Enter, aby wrócić do menu operacji...")