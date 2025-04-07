from oprogramowanie_sterownika_PK.narzedzia.narzedzia import wyczysc_ekran, sprawdz_czy_kolumna_wiersz_wolne
from oprogramowanie_sterownika_PK.algorytmy.paull import algorytm_paulla


def algorytm_benesa(typ_struktury, struktura, wl, wp, x, y, slownik_polaczen, czy_przestrojen):
    """
            Funkcja realizuje algorytm sterowania Benesa dla 3-sekcyjnego pola Closa, w którym komutatory
            sekcji środkowej są sprawdzane kolejno względem najbardziej obciążonego komutatora.
        :param typ_struktury: (int), przyjmuje wartość 1-4, przechowuje informacje o wybranym typie struktury, Clos, Benes, ...
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
    nr_komutatora_we = x // wl[0]  # dzielenie bez reszty określa nr komutatora
    nr_lacza_we = x % wl[0]  # dzielenie modulo określa nr lacza
    nr_komutatora_wy = y // wp[0]
    nr_lacza_wy = y % wp[0]
    sekcja_we = 0
    sekcja_wy = 2
    liczba_komutatorow_sekcji_srodkowej = len(struktura[1])  # liczba komutatorów środkowych

    # tworzenie wektora zajętości komutatorów sekcji środkowej
    lista_zajetosci = []
    for komutator_srodkowej in range(liczba_komutatorow_sekcji_srodkowej):
        zliczanie = sum(struktura[1][komutator_srodkowej, :, :].flatten())  # zliczanie jedynek w każdym komutatorze
        lista_zajetosci.append((komutator_srodkowej, zliczanie))

    # sortowanie komutatorów malejąco według zajętości
    lista_zajetosci.sort(key=lambda x: x[1], reverse=True)

    #algorytm Benesa dla pola o strukturze Closa
    if typ_struktury == 1:
        # Benesa, szukanie komutatorów sekcji środkowej od komutatora najbardziej obciążonego
        for komutator_srodkowej, _ in lista_zajetosci:

            # 1 sekcja sprawdzenie, czy wolny
            if sprawdz_czy_kolumna_wiersz_wolne(struktura, nr_komutatora_we, nr_lacza_we, komutator_srodkowej, sekcja_we):

                # 3 sekcja sprawdzenie, czy wolny
                if sprawdz_czy_kolumna_wiersz_wolne(struktura, nr_komutatora_wy, komutator_srodkowej, nr_lacza_wy, sekcja_wy):

                    # aktualizowanie struktury
                    struktura[sekcja_we][nr_komutatora_we, nr_lacza_we, komutator_srodkowej] = 1
                    struktura[1][komutator_srodkowej, nr_komutatora_we, nr_komutatora_wy] = 1
                    struktura[sekcja_wy][nr_komutatora_wy, komutator_srodkowej, nr_lacza_wy] = 1

                    # zapisywanie zmian do słownika połączeń
                    id_polaczenia = f'({x},{y})'
                    if id_polaczenia not in slownik_polaczen:
                        slownik_polaczen[id_polaczenia] = []
                    slownik_polaczen[id_polaczenia].append((nr_komutatora_we, nr_lacza_we, komutator_srodkowej))
                    slownik_polaczen[id_polaczenia].append((komutator_srodkowej, nr_komutatora_we, nr_komutatora_wy))
                    slownik_polaczen[id_polaczenia].append((nr_komutatora_wy, komutator_srodkowej, nr_lacza_wy))
                    print(f"\nZestawiono połączenie ({x},{y}) poprzez komutator środkowy {komutator_srodkowej}!")

                    # wyświetlanie drogi zestawionego połączenia
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
    print(f"Nie można zostawić połączenia ({x},{y})!")
    input("\nNaciśnij Enter, aby wrócić do menu operacji...")
    wyczysc_ekran()
    return struktura, slownik_polaczen
