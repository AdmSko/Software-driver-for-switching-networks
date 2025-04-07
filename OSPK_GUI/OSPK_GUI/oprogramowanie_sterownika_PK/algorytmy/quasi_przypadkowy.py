from oprogramowanie_sterownika_PK.narzedzia.program_tools import sprawdz_czy_kolumna_wiersz_wolne
from oprogramowanie_sterownika_PK.algorytmy.paull import algorytm_paulla


# algorytm quasi-przypadkowy dla 3 sekcyjnego pola Closa
def algorytm_quasi_random(struktura, wl, wp, x, y, slownik_polaczen, ostatnio_uzyty_komutator, czy_przestrojen):
    """
           Funkcja realizuje algorytm sterowania quasi-random dla 3-sekcyjnego pola Closa, w którym komutatory
           sekcji środkowej są sprawdzane w kolejności last_middle_switch+1, aż do
           momentu przejścia do komutatora, który umożliwia zestawienia połączenia.

       :param struktura: Lista trójwymiarowych macierzy reprezentujących sekcje pola Closa.
       :param wl: (list) Lista rozmiarów komutatorów z lewej strony (wektor wejściowy).
       :param wp: (list) Lista rozmiarów komutatorów z prawej strony (wektor wyjściowy).
       :param x: Wejście zadanego połączenia.
       :param y: Wyjście zadanego połączenia.
       :param slownik_polaczen: Słownik istniejących połączeń.
       :param ostatnio_uzyty_komutator: Zmienna zawierająca ostatnio użyty numer komutatora do zestawienia połączenia.
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
    wiadomosc = ""

    # quasi-przypadkowy, szukanie komutatorów sekcji środkowej od komutatora, przez którego ostatnio zestawiono + 1
    for i in range(liczba_komutatorow_sekcji_srodkowej):
        aktualny_komutator_srodkowej = (ostatnio_uzyty_komutator + 1 + i) % liczba_komutatorow_sekcji_srodkowej

        # 1 sekcja sprawdzenie czy wolny
        if sprawdz_czy_kolumna_wiersz_wolne(struktura, nr_komutatora_we, nr_lacza_we, aktualny_komutator_srodkowej, sekcja_we):

            # 3 sekcja sprawdzenie czy wolny
            if sprawdz_czy_kolumna_wiersz_wolne(struktura, nr_komutatora_wy, aktualny_komutator_srodkowej, nr_lacza_wy, sekcja_wy):

                # czyli komutator sekcji środkowej jest równy structure[1][aktualny_komutator_srodkowej, nr_komutatora_we, nr_komutatora_wy]
                # wpisywanie '1'
                struktura[sekcja_we][nr_komutatora_we, nr_lacza_we, aktualny_komutator_srodkowej] = 1
                struktura[1][aktualny_komutator_srodkowej, nr_komutatora_we, nr_komutatora_wy] = 1
                struktura[sekcja_wy][nr_komutatora_wy, aktualny_komutator_srodkowej, nr_lacza_wy] = 1

                # zapisywanie zmian do slownika polaczen
                id_polaczenia = f'({x},{y})'
                if id_polaczenia not in slownik_polaczen:
                    slownik_polaczen[id_polaczenia] = []
                slownik_polaczen[id_polaczenia].append((nr_komutatora_we, nr_lacza_we, aktualny_komutator_srodkowej))
                slownik_polaczen[id_polaczenia].append((aktualny_komutator_srodkowej, nr_komutatora_we, nr_komutatora_wy))
                slownik_polaczen[id_polaczenia].append((nr_komutatora_wy, aktualny_komutator_srodkowej, nr_lacza_wy))
                wiadomosc = f"\nZestawiono połączenie ({x},{y}) poprzez komutator środkowy {aktualny_komutator_srodkowej}!\n"

                # wyświetlenie drogi połączenia i zwrócenie zaktualizowanych struktur
                id_klucz = f'({x},{y})'
                pozycje = slownik_polaczen[id_klucz]
                pozycje_str = ','.join([f"({k},{we},{wy})" for k, we, wy in pozycje])
                wiadomosc += f"d{id_klucz} = {{{pozycje_str}}}"
                print("uzyty komutator sekc srod:", aktualny_komutator_srodkowej)
                return struktura, slownik_polaczen, aktualny_komutator_srodkowej, wiadomosc

        # jeśli wybrano używanie algorytmu przestrojeń - Paull
    if czy_przestrojen:

        # sprawdzanie, czy w slowniku nie ma połączeń z x na cokolwiek ani z cokolwiek na y
        wejscie_zajete = any(str(x) in klucz.split(',')[0][1:] for klucz in slownik_polaczen)
        wyjscie_zajete = any(str(y) in klucz.split(',')[1][:-1] for klucz in slownik_polaczen)

        if not wejscie_zajete and not wyjscie_zajete:
            # wywołanie algorytmu przestrojeń
            slownik_polaczen,struktura, wiadomosc = algorytm_paulla(struktura, wl, wp, x, y, slownik_polaczen, nr_komutatora_we,
                            nr_komutatora_wy, nr_lacza_we, nr_lacza_wy)
            return struktura, slownik_polaczen, ostatnio_uzyty_komutator, wiadomosc
        else:
            if wejscie_zajete:
                wiadomosc = f"Wejście {x} jest już zajęte!\n"

            if wyjscie_zajete:
                wiadomosc = f"Wyjście {y} jest już zajęte!\n"

    # jeśli nie da się zestawić połączenia
    wiadomosc = f"Nie można zostawić połączenia ({x},{y}) !"
    return struktura, slownik_polaczen, ostatnio_uzyty_komutator, wiadomosc
