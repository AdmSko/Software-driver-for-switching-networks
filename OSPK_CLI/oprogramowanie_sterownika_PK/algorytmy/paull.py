from oprogramowanie_sterownika_PK.narzedzia.narzedzia import wyczysc_ekran
from oprogramowanie_sterownika_PK.narzedzia.narzedzia import znajdz_klucz_w_slowniku
import copy


def algorytm_paulla(struktura, wl, wp, x, y, slownik_polaczen, nr_komutatora_we,
                    nr_komutatora_wy, nr_lacza_we, nr_lacza_wy):
    """
        Odpowiedzialna za algorytm przestrojeń Paull'a dla 3-sekcyjnego pola Closa.

        Funkcja realizuje algorytm przestrojeń paulla. Tworzy macierz stanu,
        przeprowadza na niej operacje wymagane do przestawienia połączeń, takie jak
        wypełnienie jej istniejącymi już połączeniami, zastąpienie ich poprzez symbole
        A i B, zamianę połączeń, które skutkuje odblokowaniem komutatorów dla zadanego połączenia.

    :param struktura: Lista trójwymiarowych macierzy reprezentujących sekcje pola Closa.
    :param wl: (list) Lista rozmiarów komutatorów z lewej strony (wektor wejściowy).
    :param wp: (list) Lista rozmiarów komutatorów z prawej strony (wektor wyjściowy).
    :param x: Wejście zadanego połączenia
    :param y: Wyjście zadanego połączenia
    :param slownik_polaczen: Słownik zawierający istniejące połączenia i ich drogi.
    :param nr_komutatora_we: Numer komutatora wejściowego.
    :param nr_komutatora_wy: Numer komutatora wyjściowego.
    :param nr_lacza_we: Numer łącza wejściowego.
    :param nr_lacza_wy: Numer łącza wyjściowego.

    :return: Zaktualizowana struktura stanu pola komutacyjnego i słownik z połączeniami
    """

    # KROK 1: tworzenie i aktualizacja macierz na podstawie słownika z połączeniami, macierz pomocnicza
    macierz_paulla, macierz_pomocnicza = utworz_macierz_paulla(wl[1], slownik_polaczen)
    macierz_pomocnicza_komutatory = copy.deepcopy(macierz_paulla)

    # KROK 2: denote - przypisanie symboli A i B, aktualizacja macierzy pomocniczych
    macierz_paulla, wartosc_A, wartosc_B = zamiana_wartosci_na_symbole(macierz_paulla, nr_komutatora_we, nr_komutatora_wy, wp[0])

    # dodanie zadanego połączenia do macierzy paulla
    macierz_paulla[nr_komutatora_we][nr_komutatora_wy] = 'A'

    # dodanie zadanego połączenia do macierzy pomocniczych - połączenia
    if macierz_pomocnicza[nr_komutatora_we][nr_komutatora_wy] is None:
        macierz_pomocnicza[nr_komutatora_we][nr_komutatora_wy] = f'({x},{y})'
    else:
        macierz_pomocnicza[nr_komutatora_we][nr_komutatora_wy] += f'({x},{y})'

    # dodanie zadanego połączenia do macierzy pomocniczych - nr_komutatora
    if macierz_pomocnicza_komutatory[nr_komutatora_we][nr_komutatora_wy] is None:
        macierz_pomocnicza_komutatory[nr_komutatora_we][nr_komutatora_wy] = wartosc_A
    else:
        macierz_pomocnicza_komutatory[nr_komutatora_we][nr_komutatora_wy] += wartosc_A

    # dodatkowa macierz pomocnicza zawierająca nr komutatorów dla połączeń przed przestrojeniami
    macierz_pomocnicza_komutatory_przed_przestrojeniem = copy.deepcopy(macierz_paulla)

    # KROK 3: przejście do zamiany symboli A i B, zawsze zadane połączenie przez symbol A

    # zamiany i aktualizacja macierzy pomocniczej z numerami komutatorów środkowych
    macierz_paulla, macierz_pomocnicza_komutatory, lista_zmian = przestrajanie_polaczen_w_macierzy(
        macierz_paulla, nr_komutatora_we, nr_komutatora_wy, macierz_pomocnicza_komutatory, wartosc_A, wartosc_B)

    # KROK 4: aktualizacja listy połączeń, stanu struktury na podstawie macierzy pomocniczych
    # aktualizacja słownika połączeń na podstawie info z macierzy pomocniczych
    slownik_polaczen, struktura = aktualizacja_slownika_po_przestrojeniach(
        slownik_polaczen, macierz_pomocnicza_komutatory, lista_zmian,
        wartosc_A, wartosc_B, macierz_pomocnicza_komutatory_przed_przestrojeniem, struktura)

    # KROK 5: wszystkie przestrojone, to dodać połączenie, które chcemy podstawowo zestawić.
    wartosc_A = int(wartosc_A)
    id_klucz = f'({x},{y})'
    slownik_polaczen[id_klucz] = [(nr_komutatora_we, nr_lacza_we, wartosc_A),
                                (wartosc_A, nr_komutatora_we, nr_komutatora_wy),
                                (nr_komutatora_wy, wartosc_A, nr_lacza_wy)]

    struktura[0][nr_komutatora_we, nr_lacza_we, wartosc_A] = 1
    struktura[1][wartosc_A, nr_komutatora_we, nr_komutatora_wy] = 1
    struktura[2][nr_komutatora_wy, wartosc_A, nr_lacza_wy] = 1

    print(f"\nZestawiono połączenie ({x},{y}) po przestrojeniach !")
    pozycje = slownik_polaczen[id_klucz]
    pozycje_str = ','.join([f"({k},{we},{wy})" for k, we, wy in pozycje])
    print(f"d{id_klucz} = {{{pozycje_str}}}")
    input("\nNaciśnij Enter, aby wrócić do menu operacji...")
    wyczysc_ekran()

    return struktura, slownik_polaczen


def utworz_macierz_paulla(r, slownik_polaczen):
    """
        Tworzy macierz Paull'a, która operuje na numerach komutatorów, gdzie:
        -wiersz odpowiada komutatorom sekcji wejściowej
        -kolumna odpowiada komutatorom sekcji wyjściowej
        -komórka zawiera informacje o komutatorach sekcji środkowej

    :param r: Liczba wejść i wyjść na komutator sekcji wewnętrznej (również liczba komutatorów w sekcji wejściowej i wyjściowej).
    :param slownik_polaczen: Słownik zawierający istniejące połączenia i ich drogi.

    :return: Stworzona macierz Paull'a i wartości symboli
    """
    # tworzenie macierzy paulla o wymiarach rxr
    macierz_paulla = [[None for _ in range(r)] for _ in range(r)]
    macierz_pomocnicza = [[None for _ in range(r)] for _ in range(r)]  # Tworzymy macierz pomocniczą

    for klucz, wartosc in slownik_polaczen.items():
        # znajdowanie numerów komutatorów dla każdego z połączeń
        pierwsza_sekcja = wartosc[0][0]
        trzecia_sekcja = wartosc[2][0]
        komutator_srodkowy = wartosc[1][0]

        # uzupełnienie macierzy Paull'a
        if macierz_paulla[pierwsza_sekcja][trzecia_sekcja] is not None:
            # Jeśli jest już wartość w komórce, to łączymy ją z nową wartością (numer komutatora)
            macierz_paulla[pierwsza_sekcja][trzecia_sekcja] = str(macierz_paulla[pierwsza_sekcja][trzecia_sekcja]) + f",{komutator_srodkowy}"
        else:
            # jeśli nie ma wartości, przypisujemy numer komutatora
            macierz_paulla[pierwsza_sekcja][trzecia_sekcja] = str(komutator_srodkowy)

        # Uzupełnienie macierzy pomocniczej (gdzie zapisujemy klucz połączenia)
        if macierz_pomocnicza[pierwsza_sekcja][trzecia_sekcja] is not None:
            # jeśli jest już wartość w komórce, to łączymy ją z nowym kluczem
            macierz_pomocnicza[pierwsza_sekcja][trzecia_sekcja] = str(macierz_pomocnicza[pierwsza_sekcja][trzecia_sekcja]) + f",{klucz}"
        else:
            # jeśli nie ma wartości, przypisujemy klucz połączenia
            macierz_pomocnicza[pierwsza_sekcja][trzecia_sekcja] = klucz

    return macierz_paulla, macierz_pomocnicza


def zamiana_wartosci_na_symbole(macierz_paulla, nr_komutatora_we, nr_komutatora_wy, m):
    """
        Zamiana wartości macierzy Paull'a na symbole A lub B w zależności od warunku,
        który mówi o tym, że w żadnym wierszu ani kolumnie nie może się powtarzać ten sam symbol.

    :param macierz_paulla: Macierz Paull'a o rozmiarach rxr, główna macierz do przestrojeń.
    :param nr_komutatora_we: Numer komutatora wejściowego.
    :param nr_komutatora_wy: Numer komutatora wyjściowego.
    :param m: Liczba wyjść na komutator sekcji wejściowej (również liczba wejść na komutator sekcji wyjściowej).

    :return: Macierz Paull'a z zamienionymi danymi na symbole A i B, wartość symbolu A, wartość symbolu B.
    """
    # Krok 1: Zbieranie wszystkich wartości, które występują w wierszu nr_komutatora_we
    uzyte_w_wierszu = set()
    for j in range(len(macierz_paulla[nr_komutatora_we])):
        if macierz_paulla[nr_komutatora_we][j] is not None:
            # rozdzielenie ciągów, takich jak '0,1' na pojedyncze elementy
            for wartosc in macierz_paulla[nr_komutatora_we][j].split(','):
                uzyte_w_wierszu.add(wartosc.strip())

    # Krok 2: wybranie wartosc_B, czyli wartość, która nie występuje w wierszu
    wartosc_B = None
    for wartosc in range(m):  # Zakładając, że wartości w wierszu są w zakresie <0-m>
        wartosc_B_str = str(wartosc)  # Zamieniamy na string
        if wartosc_B_str not in uzyte_w_wierszu:
            wartosc_B = wartosc_B_str
            break

    # Krok 3: zamiana w całej macierzy wartości wartosc_B na "B"
    for i in range(len(macierz_paulla)):
        for j in range(len(macierz_paulla[i])):
            if macierz_paulla[i][j] is not None and wartosc_B in str(macierz_paulla[i][j]):
                # zamiana tylko, jeśli wartosc_B (np. '0', '1', ...) jest zawarte w komórce
                macierz_paulla[i][j] = 'B'

    # Krok 4: zebranie wszystkich wartości, które występują w kolumnie switch_nbr_out
    uzyte_w_kolumnie = set()
    for i in range(len(macierz_paulla)):
        if macierz_paulla[i][nr_komutatora_wy] is not None:
            # rozdzielenie ciągów, takie jak '0,1' na pojedyncze elementy
            for wartosc in macierz_paulla[i][nr_komutatora_wy].split(','):
                uzyte_w_kolumnie.add(wartosc.strip())

    # Krok 5: Wybieranie wartosc_A, czyli wartość, która nie występuje w kolumnie
    wartosc_A = None
    for wartosc in range(m):  # zakładając, że wartości w kolumnie są w zakresie 0-m
        wartosc_A_str = str(wartosc)  # zamiana na string
        if wartosc_A_str not in uzyte_w_kolumnie and wartosc_A_str != wartosc_B:
            wartosc_A = wartosc_A_str
            break

    # Krok 6: zamiana w całej macierzy wartości wartosc_A na "A"
    for i in range(len(macierz_paulla)):
        for j in range(len(macierz_paulla[i])):
            if macierz_paulla[i][j] is not None and wartosc_A in str(macierz_paulla[i][j]):
                # zamiana tylko, jeśli wartosc_A (np. '0', '1') jest zawarte w komórce
                macierz_paulla[i][j] = 'A'

    return macierz_paulla, wartosc_A, wartosc_B


def przestrajanie_polaczen_w_macierzy(macierz_paulla, nr_komutatora_we, nr_komutatora_wy, macierz_pomocnicza_komutatory, wartosc_A, wartosc_B):
    """
        Zamienia wartości w macierzy, aby rozwiązać konflikty, bazując na podanym wierszu i kolumnie.

    :param macierz_paulla: Lista dwuwymiarowa (macierz).
    :param nr_komutatora_we: Indeks wiersza początkowego.
    :param nr_komutatora_wy: Indeks kolumny początkowej.
    :param macierz_pomocnicza_komutatory: Macierz pomocnicza, wypełniona danymi o wykorzystywanych komutatorach przez połączenia.
    :param wartosc_A: Wartość string, która należy do symbolu A
    :param wartosc_B: Wartość string, która należy do symbolu B

    :return: Zaktualizowana macierz Paull'a, zaktualizowana macierz pomocnicza,
        lista_zmian zawiera informacje, w jakich komórkach zaszły zmiany.
    """
    # jeżeli licznik mod 2 == 0 to wstawia za 'A' -> 'B', jeżeli 1 to 'B' -> 'A'
    licznik = 0

    # lista przechowująca (wiersz, kolumna) informacje gdzie dokonano zamiany
    lista_zmian = []

    # rozpoczęcie od dodanego połączenia macierz_paulla[nr_komutatora_we, nr_komutatora_wy]
    wiersz = nr_komutatora_we
    kolumna = nr_komutatora_wy

    # zamiana, dopóki konflikt
    while wiersz is not None and kolumna is not None:
        wiersz, kolumna = sprawdz_czy_konflikt_wiersz_kolumna(macierz_paulla, wiersz, kolumna, licznik)

        # jeśli nie znaleziono konfliktów, przerwij
        if wiersz is None or kolumna is None:
            break
        lista_zmian.append(f'{wiersz}, {kolumna}')
        # zamiana wartości w macierzy
        if licznik % 2 == 0:
            macierz_paulla[wiersz][kolumna] = 'B'

            # aktualizacja auxiliary_matrix_switches
            if macierz_pomocnicza_komutatory[wiersz][kolumna] is not None:
                # podział stringa na listę, zamiana wartości, połączenie z powrotem w string
                wartosci = macierz_pomocnicza_komutatory[wiersz][kolumna].split(',')
                if str(wartosc_A) in wartosci:
                    wartosci[wartosci.index(str(wartosc_A))] = str(wartosc_B)
                macierz_pomocnicza_komutatory[wiersz][kolumna] = ','.join(wartosci)
            else:
                macierz_pomocnicza_komutatory[wiersz][kolumna] = str(wartosc_B)

        else:
            macierz_paulla[wiersz][kolumna] = 'A'

            # aktualizacja auxiliary_matrix_switches
            if macierz_pomocnicza_komutatory[wiersz][kolumna] is not None:
                # podział stringa na listę, zamiana wartości, połączenie z powrotem w string
                wartosci = macierz_pomocnicza_komutatory[wiersz][kolumna].split(',')
                if str(wartosc_B) in wartosci:
                    wartosci[wartosci.index(str(wartosc_B))] = str(wartosc_A)
                macierz_pomocnicza_komutatory[wiersz][kolumna] = ','.join(wartosci)
            else:
                macierz_pomocnicza_komutatory[wiersz][kolumna] = str(wartosc_A)

        licznik += 1  # zwiększenie licznika dla następnej iteracji

    print(f"\nOdblokowano komutator dla nowego połączenia po {licznik} iteracjach!")
    return macierz_paulla, macierz_pomocnicza_komutatory, lista_zmian


def sprawdz_czy_konflikt_wiersz_kolumna(macierz_paulla, wiersz, kolumna, licznik):
    """
    Znajduje drugie wystąpienie 'A' lub 'B' w wierszu i w kolumnie, pomijając pierwsze wystąpienie.

    :param macierz_paulla: Macierz Paull'a wykorzystywana do przestrojeń.
    :param wiersz: Indeks wiersza.
    :param kolumna: Indeks kolumny.
    :param licznik: Licznik iteracji (wybór symbolu).

    :return: Tuple (wiersz_konflikt, kolumna_konflikt) lub (None, None), jeśli brak konfliktów.
    """
    # ustalenie szukanego symbolu
    symbol = 'A' if licznik % 2 == 0 else 'B'

    # inicjalizacja wyników
    wiersz_konflikt = None
    kolumna_konflikt = None

    # sprawdzenie wiersza
    wiersz_dane = macierz_paulla[wiersz]
    for kol in range(len(wiersz_dane)):
        if kol != kolumna and wiersz_dane[kol] == symbol:  # pomijamy początkową kolumnę
            wiersz_konflikt = (wiersz, kol)
            break

    # sprawdzenie kolumny
    for r in range(len(macierz_paulla)):
        if r != wiersz and macierz_paulla[r][kolumna] == symbol:  # pomijamy początkowy wiersz
            kolumna_konflikt = (r, kolumna)
            break

    # zwracanie wyniku
    if wiersz_konflikt:
        return wiersz_konflikt[0], wiersz_konflikt[1]

    if kolumna_konflikt:
        return kolumna_konflikt[0], kolumna_konflikt[1]

    return None, None


def aktualizacja_slownika_po_przestrojeniach(slownik_polaczen,
                                             macierz_pomocnicza_komutatory, lista_zmian, wartosc_A, wartosc_B,
                                             macierz_pomocnicza_komutatory_przed_zamiana, struktura):
    """
        Na podstawie zamian w macierzy Paull'a, aktualizacja
        słownika z połąceniami wraz ze stanem struktury pola.

    :param slownik_polaczen: Słownik zawierający istniejące połączenia.
    :param macierz_pomocnicza_komutatory: Macierz pomocnicza, wypełniona danymi o wykorzystywanych komutatorach przez połączenia.
    :param lista_zmian: Lista zawierająca informacje o wierszach i kolumnach, w których zaszło przestrojenie.
    :param wartosc_A: Wartość odpowiadająca symbolowi A.
    :param wartosc_B: Wartość odpowiadająca symbolowi A.
    :param macierz_pomocnicza_komutatory_przed_zamiana: Macierz pomocnicza,
        wypełniona danymi o wykorzystywanych komutatorach przez połączenia, stan przed przestrojeń.
    :param struktura: Lista trójwymiarowych macierzy reprezentujących sekcje pola Closa.

    :return: Zwraca zaktualizowany stan struktury pola i słownik połączeń.
    """
    # licznik do sprawdzenia, czy porównać z a_value, czy b_value
    licznik = 0

    # przygotowanie listy change_log do szukania połączenia, które miało modyfikacje
    for zmiana in lista_zmian:
        # podzielenie ciągu na dwie części
        pierwsza_wartosc, trzecia_wartosc = zmiana.split(',')  # split dzieli ciąg na podstawie ', '
        # konwertowanie na liczby całkowite
        pierwsza_wartosc = int(pierwsza_wartosc)
        trzecia_wartosc = int(trzecia_wartosc)
        druga_wartosc = None  # Zmienna do przechowywania wynik

        # wyciągniecie informacji o komutatorze sekcji środkowej z macierzy pomocniczej
        if macierz_pomocnicza_komutatory[pierwsza_wartosc][trzecia_wartosc] is not None:
            # jeśli komórka zawiera ciąg (np. '2,1')
            wartosc_komorka = macierz_pomocnicza_komutatory[pierwsza_wartosc][trzecia_wartosc]

            # podzielenie ciągu na dwie liczby
            podzielone_wartosci = wartosc_komorka.split(',')  # dzielenie ciągu na podstawie przecinka

            # konwertowanie wartości na liczby całkowite
            wartosci = [int(val) for val in podzielone_wartosci]
            # sprawdzenie każdej wartość w liście
            if licznik % 2 == 1:
                for wartosc in wartosci:
                    if wartosc == int(wartosc_A):
                        druga_wartosc = wartosc  # zapisanie wartości do trzecia_wartosc
                        break  # przerwanie pętli, jeśli znaleziona pasująca wartość
            else:
                for wartosc in wartosci:
                    if wartosc == int(wartosc_B):
                        druga_wartosc = wartosc  # zapisanie wartości do trzecia_wartosc
                        break  # przerwanie pętli, jeśli znaleziona pasująca wartość
            licznik += 1

            # pierwsza_wartosc - nr komutatora 1 sekcji, druga_wartosc - 2 sekcji, trzecia_wartosc - 3 sekcji,
            if druga_wartosc is not None:

                # na odwrót, b_value i a_value, bo trzeba znaleźć połączenie PRZED przestrojeniem
                if druga_wartosc == int(wartosc_B):
                    klucz = znajdz_klucz_w_slowniku(slownik_polaczen, pierwsza_wartosc, int(wartosc_A), trzecia_wartosc)
                else:
                    klucz = znajdz_klucz_w_slowniku(slownik_polaczen, pierwsza_wartosc, int(wartosc_B), trzecia_wartosc)
                if klucz:

                    # rozpakowanie na in i out
                    klucz2 = klucz.strip('()')
                    wartosc_we, wartosc_wy = map(int, klucz2.split(','))

                    # teraz jak znalezione połączenie to trzeba usunąć je ze struktury
                    nr_sekcji = 0
                    for polaczenie in slownik_polaczen[klucz]:
                        # czytanie slownika
                        nr_komutatora, wiersz, kolumna = polaczenie
                        # usuwanie polaczen ze struktury
                        struktura[nr_sekcji][nr_komutatora, wiersz, kolumna] = 0
                        nr_sekcji += 1

                    # nadpisać słownik połączeń PRZED przestrojeniem na PO
                    slownik_polaczen[klucz] = [(pierwsza_wartosc, wartosc_we, druga_wartosc),
                                             (druga_wartosc, pierwsza_wartosc, trzecia_wartosc),
                                             (trzecia_wartosc, druga_wartosc, wartosc_wy)]

                    # po nadpisaniu słownika - aktualizacja struktury
                    struktura[0][pierwsza_wartosc, wartosc_we, druga_wartosc] = 1
                    struktura[1][druga_wartosc, pierwsza_wartosc, trzecia_wartosc] = 1
                    struktura[2][trzecia_wartosc, druga_wartosc, wartosc_wy] = 1


                else:
                    print("Nie znaleziono klucza")

            else:
                print(f'Brak pasującej wartości w komórce [{pierwsza_wartosc}][{trzecia_wartosc}]')
        else:
            print(f'Brak wartości w komórce [{pierwsza_wartosc}][{trzecia_wartosc}]')

    return slownik_polaczen, struktura


