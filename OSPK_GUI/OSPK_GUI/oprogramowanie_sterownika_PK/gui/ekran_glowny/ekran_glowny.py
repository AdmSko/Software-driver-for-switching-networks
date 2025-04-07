from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from oprogramowanie_sterownika_PK.narzedzia.program_tools import sprawdz_dlugosc_list, sprawdz_dane_wejsciowe_od_do
from oprogramowanie_sterownika_PK.narzedzia.pop_upy_ekran_glowny import popup_parametry, zamknij_popup, popup_informacja, pokaz_niewdrozony_benes, pokaz_niewdrozony_cantor

Builder.load_file('ekran_glowny/ekran_glowny.kv')


class ekran_glowny(Screen):
    """
     Klasa realizuje ekran główny, który jest piewszym ekranem oprogramowania.
     W ramach ekranu realizowany jest wybór typu struktury oraz zadanie
     parametrów pola komutacyjnego za pomocą obiektów w oknie typu popup.
    """
    def __init__(self, **kwargs):
        """
         Funkcja inicjalizacyjna, dekladracja wstępnych wartości parametrów

        """
        super(ekran_glowny, self).__init__(**kwargs)
        self.typ_struktury = None
        self.liczba_sekcji = None
        self.param_wl = None
        self.param_wp = None
        self.wl = []
        self.wp = []
        self.param_popup = None  # popup główny
        self.popup_informacja = None  # popup błędu
        self.algorithm_choice = None
        self.param_algorytm = None
        self.param_czy_przestrojen = False

    def przygotuj_popup_wprowadzenie_danych(self):
        """
         obsługuje wyświetlenie funkcji popup_parameters, która
         służy do określenia parametrów zadanego pola
        :return:
        """

        #tu zmienic w przypadku dodania innych struktur pola
        self.typ_struktury = 1
        popup_parametry(self)

    def na_wyborze_algorytmu(self, instance, x):
        """
            Funkcja obsługująca wybór algorytmu sterowania
        :param x: ciąg znaków zawierający informacje o wybranym alg. sterowania
        :return:
        """

        # funkcja wywoływana, gdy użytkownik wybierze algorytm z listy rozwijanej
        if x == "przestrajalny" or self.param_czy_przestrojen == True:
            self.param_czy_przestrojen = True
            # Odblokowujemy drugi dropdown
            self.algorytm_przycisk1.disabled = False
            self.algorytm_przycisk1.text = "Wybierz algorytm sterowania"  # aktualizacja tekstu przycisku
        else:
            self.param_czy_przestrojen = False
            # ukrycie drugiego dropdown listy, jeśli wybrano inny algorytm
            self.algorytm_przycisk1.disabled = True

            self.algorytm_przycisk1.text = "Wybierz algorytm sterowania"  # aktualizacja tekstu przycisku
        if self.algorytm_przycisk.text != f"Algorytm: przestrajalny":
            self.algorytm_przycisk.text = f"Algorytm: {x}"
            self.param_algorytm = x
        else:
            self.algorytm_przycisk1.text = f"Algorytm: {x}"
            self.param_algorytm = x

    def sprawdz_wartosci_we_wy(self, instance):
        """
          Sprawdza wartosprawdści wpisane przez użytkownika
        """
        try:
            wiadomosc, liczba_sekcji = sprawdz_dane_wejsciowe_od_do(self.liczba_sekcji.text, 1, 13)

            if wiadomosc:
                popup_informacja(self, wiadomosc)
                return
            if liczba_sekcji % 2 == 0:
                popup_informacja(self, "Liczba sekcji musi być nieparzystą liczbą całkowitą z zakresu <1,13>")
                return

            # na potrzeby aktualnie istniejacych rozwiazan jedynie dla 3sekcyjnych:
            if liczba_sekcji != 3:
                popup_informacja(self, "W oprogramowaniu wdrożono jedynie rozwiązania dla struktury 3-sekcyjnej!")
                return

            wl_wartosci = self.param_wl.text.split()
            wp_wartosci = self.param_wp.text.split()
            try:
                wl_wartosci = [int(value) for value in wl_wartosci]
                wp_wartosci = [int(value) for value in wp_wartosci]
            except ValueError:
                popup_informacja(self, "Wektory wl i wp muszą zawierać tylko liczby.")
                return
            # sprawdzenie długość listy
            wiadomosc = sprawdz_dlugosc_list(liczba_sekcji, wl_wartosci, wp_wartosci)

            if wiadomosc:
                popup_informacja(self, wiadomosc)
                return

            if self.param_algorytm is None or self.param_algorytm == "przestrajalny":
                popup_informacja(self, "Wybierz algorytm sterowania")
                return

            self.wl = wl_wartosci
            self.wp = wp_wartosci
            zamknij_popup(self)

        except ValueError:
            popup_informacja("Nieprawidłowe dane wejściowe.")

    # funkcje wywolujace popupy dla niewdrozonych
    def pokaz_popup_benes(self):
        pokaz_niewdrozony_benes(self)

    def pokaz_popup_cantor(self):
        pokaz_niewdrozony_cantor(self)
