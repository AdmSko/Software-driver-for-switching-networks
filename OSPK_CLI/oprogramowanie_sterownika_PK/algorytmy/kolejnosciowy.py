from oprogramowanie_sterownika_PK.narzedzia.narzedzia import wyczysc_ekran, sprawdz_czy_kolumna_wiersz_wolne
from oprogramowanie_sterownika_PK.algorytmy.paull import algorytm_paulla


def algorytm_kolejnosciowy(typ_struktury, struktura, wl, wp, x, y, slownik_polaczen, czy_przestrojen):
    """
        Funkcja realizuje kolejnościowy algorytm sterowania dla 3-sekcyjnego pola Closa, w którym komutatory
        sekcji środkowej są sprawdzane w kolejności i, i+1, ...
    :param typ_struktury: (int) przyjmuje wartość 1-4, przechowuje informacje o wybranym typie struktury, Clos, Benes, ...
    :param struktura: Lista trójwymiarowych macierzy reprezentujących sekcje pola Closa.
    :param wl: (list) Lista rozmiarów komutatorów z lewej strony (wektor wejściowy).
    :param wp: (list) Lista rozmiarów komutatorów z prawej strony (wektor wyjściowy).
    :param x: Wejście zadanego połączenia.
    :param y: Wyjście zadanego połączenia.
    :param slownik_polaczen: Słownik istniejących połączeń.
    :param czy_przestrojen: Zmienna bool, czy stosować algorytm przestrojeń.

    :return: Zwraca zaktualizowany stan struktury i słownik z połączeniami.
    """

    # konfiguracja wejścia/wyjścia
    nr_komutatora_we = x // wl[0]     # dzielenie bez reszty określa nr komutatora
    nr_lacza_we = x % wl[0]     # dzielenie modulo określa nr lacza
    nr_komutatora_wy = y // wp[0]
    nr_lacza_wy = y % wp[0]
    sekcja_we = 0
    sekcja_wy = 2

    #algorytm kolejnościowy dla struktury Closa - dopisać if dla reszty typów przy implementacji
    if typ_struktury == 1:
        for kolumna in range(len(struktura[sekcja_we][nr_komutatora_we][nr_lacza_we])):
            # 1 sekcja sprawdzenie, czy wolny
            if sprawdz_czy_kolumna_wiersz_wolne(struktura, nr_komutatora_we, nr_lacza_we, kolumna, sekcja_we):
                # 3 sekcja sprawdzenie, czy wolny
                if sprawdz_czy_kolumna_wiersz_wolne(struktura, nr_komutatora_wy, kolumna, nr_lacza_wy, sekcja_wy):
                    # czyli komutator sekcji środkowej jest równy structure[1][kolumna, nr_komutatora_we, nr_komutatora_wy]
                    # wpisywanie '1'
                    struktura[sekcja_we][nr_komutatora_we, nr_lacza_we, kolumna] = 1
                    struktura[1][kolumna, nr_komutatora_we, nr_komutatora_wy] = 1
                    struktura[sekcja_wy][nr_komutatora_wy, kolumna, nr_lacza_wy] = 1
                    # zapisywanie zmian do słownika połączeń
                    id_polaczenia = f'({x},{y})'
                    if id_polaczenia not in slownik_polaczen:
                        slownik_polaczen[id_polaczenia] = []
                    slownik_polaczen[id_polaczenia].append((nr_komutatora_we, nr_lacza_we, kolumna))
                    slownik_polaczen[id_polaczenia].append((kolumna, nr_komutatora_we, nr_komutatora_wy))
                    slownik_polaczen[id_polaczenia].append((nr_komutatora_wy, kolumna, nr_lacza_wy))
                    print(f"\nZestawiono połączenie ({x},{y}) !")
                    id_klucz = f'({x},{y})'
                    pozycje = slownik_polaczen[id_klucz]
                    pozycje_str = ','.join([f"({k},{we},{wy})" for k, we, wy in pozycje])
                    print(f"d{id_klucz} = {{{pozycje_str}}}")
                    input("\nNaciśnij Enter, aby wrócić do menu operacji...")
                    wyczysc_ekran()
                    return struktura, slownik_polaczen

    # jeśli wybrano używanie algorytmu przestrojeń - Paull
    if czy_przestrojen:
        # sprawdzanie, czy w slowniku nie ma połączeń z x na cokolwiek ani z cokolwiek na y
        wejscie_zajete = any(str(x) in klucz.split(',')[0][1:] for klucz in slownik_polaczen)
        wyjscie_zajete = any(str(y) in klucz.split(',')[1][:-1] for klucz in slownik_polaczen)

        if not wejscie_zajete and not wyjscie_zajete:
            # wywołanie algorytmu przestrojeń
            algorytm_paulla(struktura, wl, wp, x, y, slownik_polaczen, nr_komutatora_we,
                            nr_komutatora_wy, nr_lacza_we, nr_lacza_wy)
            return struktura, slownik_polaczen
        else:
            if wejscie_zajete:
                print(f"Wejście {x} jest już zajęte!")
            if wyjscie_zajete:
                print(f"Wyjście {y} jest już zajęte!")

    # jeśli nie da się zestawić połączenia
    print(f"Nie można zostawić połączenia ({x},{y})")
    input("\nNaciśnij Enter, aby wrócić do menu operacji...")
    wyczysc_ekran()

    return struktura, slownik_polaczen


