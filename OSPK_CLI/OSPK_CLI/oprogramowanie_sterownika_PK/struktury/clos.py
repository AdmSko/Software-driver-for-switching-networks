import numpy as np


def utworz_strukture_closa(liczba_sekcji, wl, wp):
    """
        Tworzy strukturę pola Closa w postaci listy trójwymiarowych macierzy reprezentujących struktura pola.

        Sekcja pola Closa definiowana jest przez jej rozmiar i liczbę komutatorów:
        - Sekcja wejściowa: `wl[0] x wp[0]` (liczba wejść `wl[0]` na komutator, liczba wyjść `wp[0]` na komutator).
        - Sekcja wewnętrzna: `wl[1] x wl[1]` (liczba wejść i wyjść `wl[1]` na komutator).
        - Sekcja wyjściowa: `wp[0] x wl[0]` (liczba wejść `wp[0]` na komutator, liczba wyjść `wl[0]` na komutator).

        :param liczba_sekcji: Liczba sekcji w polu Closa.
        :param wl: Liczba wejść na komutator sekcji wejściowej.
        :param wp: Liczba wyjść na komutator sekcji wejściowej (również liczba wejść na komutator sekcji wyjściowej).
        :return: Lista trójwymiarowych macierzy reprezentujących strukturę sekcji pola Closa.
            - Indeks `0`: Sekcja wejściowa (macierz `wl[1] x wl[0] x wp[0]`).
            - Indeks `1` do `liczba_sekcji-2`: Sekcje wewnętrzne (macierze `wp[0] x wl[1] x wl[1]`).
            - Indeks `liczba_sekcji-1`: Sekcja wyjściowa (macierz `wl[1] x wp[0] x wl[0]`).
        """

    # tablica przechowująca wszystkie struktura
    struktura = []

    # tworzenie macierzy 3 wymiarowej, która będzie zawierać informacje o poszczególnych sekcjach,
    # dodawane do glownej listy
    for sekcja in range(liczba_sekcji):

        # sekcja pierwsza (sekcja -> wl[0] x wp[0])
        if sekcja == 0:
            struktura.append(np.zeros((wl[1], wl[0], wp[0])))

        # sekcja trzecia (sekcja -> wp[0] x wl[0])
        elif sekcja == liczba_sekcji-1:
            struktura.append(np.zeros((wl[1], wp[0], wl[0])))

        # struktura druga (sekcja -> wl[1] x wl[1])
        else:
            struktura.append(np.zeros((wp[0], wl[1], wl[1])))

    return struktura
