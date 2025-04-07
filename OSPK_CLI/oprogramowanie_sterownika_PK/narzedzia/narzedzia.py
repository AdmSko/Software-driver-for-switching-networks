import os
import math


def wyczysc_ekran():
    """
        Funkcja wykonująca instrukcję czyszczenia ekranu (CLI)

    :return:
    """
    os.system('cls||clear')


def sprawdz_dane_wejsciowe_od_do(wartosc, od, do):
    """
        Sprawdzenie, czy poprawne (x, y) z uwzględnieniem ilości łączy wejściowych/wyjściowych.

    :param wartosc:
    :param od: Liczba, która określa dolną granicę zakresu dla wartości wpisywanej.
    :param do: Liczba, która określa górną granicę zakresu dla wartości wpisywanej.

    :return: Zwraca sprawdzoną wartość.
    """
    while True:

        try:
            wartosc_int = int(input(wartosc))

            if wartosc_int < od or wartosc_int > do:
                print("Nieprawidłowa wartość. Spróbuj ponownie.")

            else:
                return wartosc_int

        except ValueError:
            print("Nieprawidłowa wartość. Spróbuj ponownie.")


def sprawdz_wartosci_we_wy(wartosc):
    """
        Funkcja sprawdza poprawność wprowadzonych wartości x, y,
        które odpowiadają wejściu i wyjściu zadanego połączenia.

    :param wartosc: Wartość wprowadzona przez użytkownika.
    :return:
    """
    while True:

        try:
            wejsciowe = input(wartosc)

            # jeżeli użytkownik nie wpisał żadnej wartości, to zwraca None, aby można było zadać tylko x lub y
            if wejsciowe == "":
                return None

            wejsciowe = int(wejsciowe)

            # inaczej sprawdza, czy nie jest liczbą ujemną
            if wejsciowe < 0:
                print("Nieprawidłowa wartość. Spróbuj ponownie.")

            else:
                return wejsciowe

        except ValueError:
            print("Nieprawidłowa wartość. Spróbuj ponownie.")


def otrzymaj_liste_z_wejscia(wartosc):
    """
        Pobiera od użytkownika ciąg liczb oddzielonych spacjami i zwraca listę liczb całkowitych.

    :param wartosc: Wartość wpisana przez użytkownika.

    :return: Zwraca podzielone wartości z listy np. wl i wp.
    """
    while True:
        try:

            # pobranie danych od użytkownika
            wejsciowe = input(wartosc)

            # podzielenie ciągu na listę i konwersja na liczby całkowite
            wartosci = [int(x) for x in wejsciowe.split()]
            return wartosci

        except ValueError:
            print("Nieprawidłowe dane. Upewnij się, że wpisujesz liczby oddzielone spacjami.")


def sprawdz_dlugosc_list(liczba_sekcji):
    """
        Pobiera dwie listy od użytkownika, sprawdza ich długości oraz wartości elementów.
        W razie potrzeby umożliwia poprawienie danych.

        :return: Zwraca listy wl i wp.
    """
    while True:

        # pobranie list od użytkownika
        wl = otrzymaj_liste_z_wejscia("Podaj wektor wl (oddzielone spacjami): ")
        wp = otrzymaj_liste_z_wejscia("Podaj wektor wp (oddzielone spacjami): ")

        # sprawdzenie poprawnosci wpisania do listy
        if len(wl) != len(wp):
            print("Listy mają różną liczbę elementów!")
            print(f"Wektor Wl ma {len(wl)} elementów, a wektor Wp ma {len(wp)} elementów.")
            print("Muszą mieć tyle samo elementów! Spróbuj ponownie.")
            continue

        # sprawdzenie, czy wszystkie elementy są z zakresu <1,100>
        if any(x <= 0 for x in wl) or any(x <= 0 for x in wp) or any(x > 128 for x in wl) or any(x > 128 for x in wp):
            print("Wszystkie elementy w wektorach muszą być liczbami z zakresu <1,100>!")
            print(f"Wprowadzono: Wl = {wl}, Wp = {wp}")
            print("Spróbuj ponownie.")
            continue

        if len(wl) != math.ceil(liczba_sekcji/2) or len(wp) != math.ceil(liczba_sekcji/2):
            if len(wl) == 0 or len(wp) == 0:
                print("Wektory nie mogą być puste!")
                continue
            print(f"Wektory mają długość {len(wl)}, co wskazuje zadanie pola {len(wl)*2 - 1} sekcyjnego!")
            print(f"W oprogramowaniu wdrożono rozwiązania jedynie w oparciu o pole 3-sekcyjne")
            print("Dla pola 3-sekcyjnego o strukturze gs=g*g^-1 wektory powinny posiadać 2 elementy (długość 2)\n")
            continue

        # jeśli wszystkie warunki są spełnione, zwracane są listy
        return wl, wp


def znajdz_klucz_id_polaczenia(x, y, slownik_polaczen):
    """
    Funkcja wyszukuje klucz w słowniku connected_dictionary na podstawie x lub y.
    Klucz w słowniku jest w formacie '({x},{y})'.

    :param x: Łącze wejściowe (może być None).
    :param y: Łącze wyjściowe (może być None).
    :param slownik_polaczen: Słownik z połączeniami.
    :return: Klucz w formacie '({x},{y})' lub None, jeśli klucz nie istnieje.
    """
    for klucz in slownik_polaczen.keys():

        # pozbicie klucz w formacie '({x}, {y})' na liczby klucz_x i klucz_y
        klucz_x, klucz_y = eval(klucz)  # Używamy eval, aby przekonwertować string na tuple

        # sprawdzenie, czy podany x lub y pasuje do klucza
        if (x is None or x == klucz_x) and (y is None or y == klucz_y):
            return klucz

    # jeśli nie znaleziono klucza, zwracane None
    return None


def znajdz_klucz_w_slowniku(slownik_polaczen, pierwsza_wartosc, druga_wartosc, trzecia_wartosc):
    """
        Funkcja odpowiada za znalezienie wartości klucza w connected_dictionary na podstawie
        zadanych parametrów first_value, second_value, third_value.

    :param slownik_polaczen: Słownik zawierający połączenia.
    :param pierwsza_wartosc: Numer komutatora wykorzystywanego przez połączenie w pierwszej sekcji.
    :param druga_wartosc: Numer komutatora wykorzystywanego przez połączenie w drugiej sekcji.
    :param trzecia_wartosc: Numer komutatora wykorzystywanego przez połączenie w trzeciej sekcji.

    :return: Klucz lub None, jeżeli taki nie istnieje w liście.
    """
    for klucz, wartosci in slownik_polaczen.items():
        for wartosc_tuple in wartosci:
            if wartosc_tuple[0] == pierwsza_wartosc and wartosc_tuple[1] == druga_wartosc and wartosc_tuple[2] == trzecia_wartosc:
                #print(f"Znaleziono klucz: {klucz} dla wartości {pierwsza_wartosc}, {druga_wartosc}, {trzecia_wartosc}")
                return klucz
    return None  # jeśli nie znaleziono pasującego klucza


def sprawdz_czy_kolumna_wiersz_wolne(struktura, nr_komutatora, wiersz, kolumna, sekcja):
    """
        Sprawdzanie, czy dana komórka jest wolna, czy można zestawić połączenie.

    :param struktura: Lista 3-wymiarowych macierzy ze stanem struktury pola.
    :param nr_komutatora: Numer sprawdzanego komutatora.
    :param wiersz: Numer wiersza sprawdzanego komutatora.
    :param kolumna: Numer kolumny sprawdzanego komutatora.
    :param sekcja: Sekcja, w której znajduje się sprawdzany komutator.
    :return:
    """
    # structure[sekcja[switch_nbr,row,column] <-- [switch_nbr, we, wy]
    wiersz_sprawdzenie = all(komorka == 0 for komorka in struktura[sekcja][nr_komutatora][wiersz])
    kolumna_sprawdzenie = all(struktura[sekcja][nr_komutatora][r][kolumna] == 0
                       for r in range(len(struktura[sekcja][nr_komutatora])))

    # jeżeli nie ma 1 nigdzie to true, inaczej false, zajęte
    return wiersz_sprawdzenie and kolumna_sprawdzenie

