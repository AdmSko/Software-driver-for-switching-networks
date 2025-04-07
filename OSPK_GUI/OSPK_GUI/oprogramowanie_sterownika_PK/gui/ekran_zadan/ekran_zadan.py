from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
import os
from oprogramowanie_sterownika_PK.narzedzia.program_tools import znajdz_klucz_id_polaczenia
from oprogramowanie_sterownika_PK.algorytmy.kolejnosciowy import algorytm_kolejnosciowy
from oprogramowanie_sterownika_PK.algorytmy.quasi_przypadkowy import algorytm_quasi_random
from oprogramowanie_sterownika_PK.algorytmy.benes import algorytm_Benesa
from oprogramowanie_sterownika_PK.struktury.clos import stworz_strukture_closa
from oprogramowanie_sterownika_PK.narzedzia.struktura_do_pliku import FileChooserPopup
from oprogramowanie_sterownika_PK.narzedzia.pop_upy_ekran_zadan import pokaz_tablice_polaczen, popup_zestaw_polaczenie, pokaz_informacje_o_polaczeniu, popup_rozlacz_polaczenie, popup_informacja
Builder.load_file('ekran_zadan/ekran_zadan.kv')


class ekran_zadan(Screen):
    def __init__(self, **kwargs):
        """
        Funkcja inicjalizacyjna, deklaracja podstawowych wartości zmiennych
        """
        super(ekran_zadan, self).__init__(**kwargs)
        self.typ_struktury = None
        self.liczba_sekcji = None
        self.wl = []
        self.wp = []
        self.wejsciowe_x_in = None
        self.wejsciowe_y_out = None
        self.param_algorytm = None
        self.struktura = None
        self.max_port_numer = None
        self.param_czy_przestrojen = False
        self.ostatnio_uzyty_komutator = -1
        self.slownik_polaczen = {}
        self.wybrana_sciezka = None

    def uaktualnij_parametry(self, typ_struktury, liczba_sekcji, wl, wp, algorytm, czy_przestrojen):
        """
            Funkcja aktualizująca parametry wykorzystywane w klasie po zamianie ekranu na nowy

        :param typ_struktury:
        :param liczba_sekcji:
        :param wl:
        :param wp:
        :param algorytm:
        :param czy_przestrojen:
        :return:
        """
        self.typ_struktury = typ_struktury
        self.liczba_sekcji = liczba_sekcji
        self.wl = wl
        self.wp = wp
        self.param_algorytm = algorytm
        self.param_czy_przestrojen = czy_przestrojen
        self.max_port_numer = self.wl[0] * self.wp[0] - 1

        # wywolanie stworzenia odwzorowania pola Closa
        if self.typ_struktury == 1:
            self.struktura = stworz_strukture_closa(self.liczba_sekcji, self.wl, self.wp)

            # przykladowy zbior polaczen do sprawdzenia poprawnosci dzialania algorytmu Paulla
            """
            # 1sekcja
            self.struktura[0][0, 0, 0] = 1  # 0-0
            self.struktura[0][0, 1, 1] = 1  # 1-1
            self.struktura[0][1, 0, 0] = 1  # 4-8
            self.struktura[0][1, 1, 1] = 1  # 5-9
            self.struktura[0][2, 2, 2] = 1  # 10-6
            self.struktura[0][2, 3, 3] = 1  # 11-7
            self.struktura[0][3, 0, 0] = 1  # 12-4
            self.struktura[0][3, 2, 2] = 1  # 14-14
            self.struktura[0][3, 3, 3] = 1  # 15-15
            # 2sekcja
            self.struktura[1][0, 0, 0] = 1  # 0-0
            self.struktura[1][0, 1, 2] = 1  # 4-8
            self.struktura[1][0, 3, 1] = 1  # 12-4
            self.struktura[1][1, 0, 0] = 1  # 1-1
            self.struktura[1][1, 1, 2] = 1  # 5-9
            self.struktura[1][2, 2, 1] = 1  # 10-6
            self.struktura[1][2, 3, 3] = 1  # 14-14
            self.struktura[1][3, 2, 1] = 1  # 11-7
            self.struktura[1][3, 3, 3] = 1  # 15-15
            # 3sekcja
            self.struktura[2][0, 0, 0] = 1  # 0-0
            self.struktura[2][0, 1, 1] = 1  # 1-1
            self.struktura[2][1, 0, 0] = 1  # 12-4
            self.struktura[2][1, 1, 3] = 1  # 11-7
            self.struktura[2][1, 2, 2] = 1  # 10-6
            self.struktura[2][2, 0, 0] = 1  # 4-8
            self.struktura[2][2, 1, 1] = 1  # 5-9
            self.struktura[2][3, 2, 2] = 1  # 14-14
            self.struktura[2][3, 3, 3] = 1  # 15-15
            self.slownik_polaczen[f'({0},{0})'] = []
            self.slownik_polaczen[f'({1},{1})'] = []
            self.slownik_polaczen[f'({4},{8})'] = []
            self.slownik_polaczen[f'({5},{9})'] = []
            self.slownik_polaczen[f'({10},{6})'] = []
            self.slownik_polaczen[f'({11},{7})'] = []
            self.slownik_polaczen[f'({12},{4})'] = []
            self.slownik_polaczen[f'({14},{14})'] = []
            self.slownik_polaczen[f'({15},{15})'] = []
            self.slownik_polaczen[f'({0},{0})'].append((0, 0, 0))
            self.slownik_polaczen[f'({0},{0})'].append((0, 0, 0))
            self.slownik_polaczen[f'({0},{0})'].append((0, 0, 0))
            self.slownik_polaczen[f'({1},{1})'].append((0, 1, 1))
            self.slownik_polaczen[f'({1},{1})'].append((1, 0, 0))
            self.slownik_polaczen[f'({1},{1})'].append((0, 1, 1))
            self.slownik_polaczen[f'({4},{8})'].append((1, 0, 0))
            self.slownik_polaczen[f'({4},{8})'].append((0, 1, 2))
            self.slownik_polaczen[f'({4},{8})'].append((2, 0, 0))
            self.slownik_polaczen[f'({5},{9})'].append((1, 1, 1))
            self.slownik_polaczen[f'({5},{9})'].append((1, 1, 2))
            self.slownik_polaczen[f'({5},{9})'].append((2, 1, 1))
            self.slownik_polaczen[f'({10},{6})'].append((2, 2, 2))
            self.slownik_polaczen[f'({10},{6})'].append((2, 2, 1))
            self.slownik_polaczen[f'({10},{6})'].append((1, 2, 2))
            self.slownik_polaczen[f'({11},{7})'].append((2, 3, 3))
            self.slownik_polaczen[f'({11},{7})'].append((3, 2, 1))
            self.slownik_polaczen[f'({11},{7})'].append((1, 1, 3))
            self.slownik_polaczen[f'({12},{4})'].append((3, 0, 0))
            self.slownik_polaczen[f'({12},{4})'].append((0, 3, 1))
            self.slownik_polaczen[f'({12},{4})'].append((1, 0, 0))
            self.slownik_polaczen[f'({14},{14})'].append((3, 2, 2))
            self.slownik_polaczen[f'({14},{14})'].append((2, 3, 3))
            self.slownik_polaczen[f'({14},{14})'].append((3, 2, 2))
            self.slownik_polaczen[f'({15},{15})'].append((3, 3, 3))
            self.slownik_polaczen[f'({15},{15})'].append((3, 3, 3))
            self.slownik_polaczen[f'({15},{15})'].append((3, 3, 3))
            """
            # zestaw np. (3,12)

        # tu należałoby dodać warunki na inne typy struktury jak Benes itd. po wdrożeniu ich

    def pokaz_popup_nowe_polaczenie(self):
        """
         Funkcja wyświetlająca okno popup w ramach wprowadzania
         danych wejściowych zadania zestawienia połączenia
        :return:
        """
        popup_zestaw_polaczenie(self)

    def pokaz_popup_rozlacz_polaczenie(self):
        popup_rozlacz_polaczenie(self)

    def na_potwierdzenie_nowego_polaczenia(self, instance):
        """
         Funkcja realizująca pobranie parametrów (x,y) oraz wywołanie funkcji
         odpowiedzialnej za zestawienia połączenia
        :param instance:
        :return:
        """
        try:
            # Pobieramy wartości z pól tekstowych
            x = int(self.wejsciowe_x_in.text)
            y = int(self.wejsciowe_y_out.text)

            # tu algorytmy sterowania dla Closa, czyli typ_struktury == 1
            if self.typ_struktury == 1:
                if not (0 <= x <= self.max_port_numer and 0 <= y <= self.max_port_numer):
                    raise ValueError(f"Wartości muszą być w zakresie od 0 do {self.max_port_numer}.")
                if self.param_algorytm == "kolejnościowy":
                    # Wywołujemy algorytm sekwencyjny
                    self.struktura, self.slownik_polaczen, wiadomosc = algorytm_kolejnosciowy(
                        self.struktura, self.wl, self.wp, x, y, self.slownik_polaczen,
                        self.param_czy_przestrojen)
                elif self.param_algorytm == "quasi-przypadkowy":
                    (self.struktura, self.slownik_polaczen,
                     self.ostatnio_uzyty_komutator, wiadomosc) = algorytm_quasi_random(
                        self.struktura, self.wl, self.wp, x, y,
                        self.slownik_polaczen, self.ostatnio_uzyty_komutator,self.param_czy_przestrojen)
                elif self.param_algorytm == "Benesa":
                    self.struktura, self.slownik_polaczen, wiadomosc = algorytm_Benesa(
                        self.struktura, self.wl, self.wp, x, y, self.slownik_polaczen,
                        self.param_czy_przestrojen)
                # Pokazujemy popup z informacją o połączeniu
            pokaz_informacje_o_polaczeniu(self, wiadomosc)

            # Zamykamy popup
            self.popup.dismiss()

        except ValueError as e:
            pokaz_informacje_o_polaczeniu(self, "Błąd: Niepoprawnie wprowadzono dane")

    def na_rozlaczenie_polaczenia(self, instance):
        """
         Funkcja realizująca zebranie parametrów podanych przez użytkownika
         oraz sprawdzająca ich poprawność, spełnienie warunków
        """
        # Pobieramy wartości z pól tekstowych
        x = self.wejsciowe_x_in.text.strip()
        y = self.wejsciowe_y_out.text.strip()

        # Sprawdzamy, czy oba pola są puste
        if not x and not y:
            popup_informacja(self, "Błąd", "Wprowadź wartości dla wejścia i wyjścia !")
            return

        # Jeśli jedno z pól jest puste, ustawiamy na None
        if not x:
            x = None
        elif not y:
            y = None

        # Walidacja, czy wartości są liczbami
        if x and not x.isdigit():
            popup_informacja(self, "Błąd", "Podaj prawidłowy numer wejścia !")
            return
        if y and not y.isdigit():
            popup_informacja(self, "Błąd", "Podaj prawidłowy numer wyjścia !")
            return

        # Konwertujemy wartości na int, jeśli są liczbami
        if x:
            x = int(x)
        if y:
            y = int(y)

        # Wywołujemy funkcje rozłączająca
        message = self.rozlacz_polaczenie(x, y)

        # Pokazujemy popup z informacją o połączeniu
        pokaz_informacje_o_polaczeniu(self, message)

        # Zamykamy popup
        self.popup.dismiss()

    def rozlacz_polaczenie(self, x, y):
        """
            Realizacja operacji rozłączania połączenia.

        :param struktura: Lista 3-wymiarowych macierzy ze stanem struktury pola.
        :param slownik_polaczen: Słownik z połączeniami.
        :return:
        """
        numer_sekcji = 0

        if x is None and y is None:
            wiadomosc = "\nNieprawidłowa wartość: Nie można pozostawić x i y pustych."
            return wiadomosc

        else:
            # identyfikator polaczenia do rozlaczenia
            id_klucz = znajdz_klucz_id_polaczenia(x, y, self.slownik_polaczen)

        if id_klucz in self.slownik_polaczen:

            for polaczenie in self.slownik_polaczen[id_klucz]:
                # czytanie slownika
                nr_komutatora, wiersz, kolumna = polaczenie
                # usuwanie polaczen ze struktury
                self.struktura[numer_sekcji][nr_komutatora, wiersz, kolumna] = 0
                numer_sekcji += 1

            # usuwanie rekordu z slownika
            wiadomosc = f"\nUsunięto połączenie {id_klucz} !\n"
            pozycje = self.slownik_polaczen[id_klucz]
            pozycje_str = ','.join([f"({k},{we},{wy})" for k, we, wy in pozycje])
            wiadomosc += f"d{id_klucz} = {{{pozycje_str}}}"
            del self.slownik_polaczen[id_klucz]
            return wiadomosc

        wiadomosc = f'\nNie ma takiego połączenia'
        return wiadomosc

    def pokaz_popup_tablica_polaczen(self, czy_przestrojen):
        """
        Wywołanie okna pop-up do wyświetlenia istniejących polaczen w polu
        :param czy_przestrojen: określa czy wyświetlić jedno polaczenie, czy wszystkie
        :return:
        """
        pokaz_tablice_polaczen(self, czy_przestrojen)

    def pokaz_tablice_polaczen(self, wszystkie_czy_jedno, x, y):
        """
        Funkcja realizująca wyświetlenie tablicy połączeń w obiekcie TextInput
        :param wszystkie_czy_jedno: flaga okreslająca, czy wyświetlić jedno,
        czy wszystkie połączenia zawarte w słowniku połączeń
        :param x: zadane wejście połączenia
        :param y: zadane wyjście połączenia

        :return wiadomosc: zawiera informację o wyniku operacji w postaci ciągu znaków
        """
        wiadomosc = ""

        if x is None and y is None and wszystkie_czy_jedno:

            # wyswietlenie wszystkich polaczen
            wiadomosc += '==========Tablica zestawionych połączeń=========\n'
            wiadomosc += 'format drogi: d(x,y) = {(komutator,we,wy), ...}\n\n'

            # petla dla wszystkich polaczen w slowniku
            for id_polaczenia, pozycje in self.slownik_polaczen.items():
                # format przedstawienia
                pozycje_str = ','.join([f"({k},{we},{wy})" for k, we, wy in pozycje])
                # wyswietlanie
                wiadomosc += f"d{id_polaczenia} = {{{pozycje_str}}}\n"
            return wiadomosc
        if not wszystkie_czy_jedno:
            # sprawdzenie, czy połączenie istnieje w słowniku połączeń
            id_klucz = znajdz_klucz_id_polaczenia(x, y, self.slownik_polaczen)

            if id_klucz in self.slownik_polaczen:
                wiadomosc = 'format drogi: d(x,y) = {(komutator,we,wy),(komutator,we,wy),...}\n\n'
                pozycje = self.slownik_polaczen[id_klucz]
                pozycje_str = ','.join([f"({k},{we},{wy})" for k, we, wy in pozycje])
                wiadomosc += f"d{id_klucz} = {{{pozycje_str}}}"
                return wiadomosc
            else:
                wiadomosc = 'Nie ma takiego połączenia'
                return wiadomosc
        else:
            wiadomosc = f'Błąc: Niepoprawnie wprowadzone dane'
        return wiadomosc

    def sprawdz_dane_do_wyswietlenia_jeden(self, wszystkie):
        """
        Funkcja obsługująca pobranie parametrów x i y, które
        następnie wykorzystywane są do wyświetlenia połączenia (x,y)
        :param wszystkie: flaga określająca, czy wyświetlić jedno, czy wszystkie połączenia ze słownika
        """
        # pobierz wartości z pól tekstowych
        x = self.input_x_in_show.text.strip()
        y = self.input_y_out_show.text.strip()

        # sprawdź, czy oba pola są puste
        if not x and not y:
            popup_informacja(self, "Błąd", "Wprowadź wartości dla wejścia i wyjścia !")
            return

        # jeśli jedno z pól jest puste, ustawiamy na None
        if not x:
            x = None
        elif not y:
            y = None

        # walidacja, czy wartości są liczbami
        if x and not x.isdigit():
            popup_informacja(self, "Błąd", "Podaj prawidłowy numer wejścia !")
            return
        if y and not y.isdigit():
            popup_informacja(self, "Błąd", "Podaj prawidłowy numer wyjścia !")
            return

        # konwertowanie wartości na int, jeśli są liczbami
        if x:
            x = int(x)
        if y:
            y = int(y)

        # wywolanie funkcje pokazującą połączenie
        message = self.pokaz_tablice_polaczen(wszystkie, x, y)

        # pokaz popup z informacją o połączeniu
        pokaz_informacje_o_polaczeniu(self, message)

        # zamkniej popup
        self.popup.dismiss()

    def pokaz_stan_struktury(self):
        """
        Funkcja do wyświetlania struktury sieci
        w obiekcie TextInput znajdującym się w GridLayout.
        """

        tekst = ""  # zmienna do przechowywania tekstu, który zostanie wyświetlony w TextInput

        # przygotowanie nagłówków dla sekcji
        naglowki = "    ".join([f"Sekcja {i + 1}:" for i in range(len(self.struktura))])
        tekst += naglowki + "\n"

        # maksymalna liczba komutatorów w strukturze (dla wyrównania wierszy)
        max_komutatory = max(len(sekcja) for sekcja in self.struktura)

        # iteracja przez komutatory (macierze 2D) w sekcjach
        for komutator in range(max_komutatory):
            # przygotowanie wierszy do wyświetlenia dla każdej sekcji
            macierze_wiersze = []
            for sekcja in self.struktura:
                if komutator < len(sekcja):  # Jeśli sekcja ma dany komutator
                    # rozbicie macierzy 2D na wiersze i zapisujemy jako listę stringów
                    wiersze = [" ".join(map(str, map(int, wiersz))) for wiersz in sekcja[komutator]]
                    macierze_wiersze.append(wiersze)
                else:
                    # dodanie pustych wierszy, jeśli komutatora brak w danej sekcji
                    macierze_wiersze.append([" " * 30] * len(self.struktura[0][0]))

            # wyświetlenie wiersze macierzy obok siebie
            for wiersz_idx in range(len(macierze_wiersze[0])):  # Dla każdego wiersza
                linia = "         ".join(macierze[wiersz_idx] for macierze in macierze_wiersze)
                tekst += linia + "\n"  # Dodajemy linię tekstu do zmiennej tekst

            # dodanie linię odstępu między kolejnymi macierzami
            tekst += "\n"

        # Ustawiamy tekst w TextInput
        self.ids.text_input.text = tekst

        self.zapisz_plik()

    def zapisz_plik(self):
        """
         Funkcja obsługująca pop-up, który umożliwia wybranie scieżki
         do zapisania pliku
        """
        file_chooser_popup = FileChooserPopup(callback=self.finalizuj_zapis)
        file_chooser_popup.open()

    def finalizuj_zapis(self, folder_path):
        """
        Funkcja realizująca zapis wartosci self.text do pliku o rozszerzeniu .txt

        :param folder_path: sciezka pliku
        """
        # stała nazwa pliku
        base_filename = "struktura.txt"
        self.wybrana_sciezka = os.path.join(folder_path, base_filename)

        # jeśli plik istnieje, generuj nową nazwę z numerem
        if os.path.exists(self.wybrana_sciezka):
            name, ext = os.path.splitext(base_filename)
            counter = 1
            while os.path.exists(os.path.join(folder_path, f"{name}({counter}){ext}")):
                counter += 1
            self.wybrana_sciezka = os.path.join(folder_path, f"{name}({counter}){ext}")

        # tworzenie folderu, jeśli nie istnieje
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # próba zapisu pliku
        try:
            with open(self.wybrana_sciezka, 'w') as file:
                tekst = ""  # zmienna do przechowywania tekstu, który zostanie wyświetlony w TextInput

                # przygotowanie nagłówków dla sekcji
                naglowki = "    ".join([f"Sekcja {i + 1}:" for i in range(len(self.struktura))])
                tekst += naglowki + "\n"

                # maksymalna liczba komutatorów w strukturze (dla wyrównania wierszy)
                max_komutatory = max(len(sekcja) for sekcja in self.struktura)

                # iteracja przez komutatory (macierze 2D) w sekcjach
                for komutator in range(max_komutatory):
                    # przygotowanie wierszy do wyświetlenia dla każdej sekcji
                    macierze_wiersze = []
                    for sekcja in self.struktura:
                        if komutator < len(sekcja):  # meśli sekcja ma dany komutator
                            # rozbicie macierz 2D na wiersze i zapisujemy jako listę stringów
                            wiersze = [" ".join(map(str, map(int, wiersz))) for wiersz in sekcja[komutator]]
                            macierze_wiersze.append(wiersze)
                        else:
                            # dodanie puste wiersze, jeśli komutatora brak w danej sekcji
                            macierze_wiersze.append([" " * 30] * len(self.struktura[0][0]))

                    # wyświetlenie wierszy macierzy obok siebie
                    for wiersz_idx in range(len(macierze_wiersze[0])):  # Dla każdego wiersza
                        linia = "      ".join(macierze[wiersz_idx] for macierze in macierze_wiersze)
                        tekst += linia + "\n"  # Dodajemy linię tekstu do zmiennej tekst

                    # dodanie linii odstępu między kolejnymi macierzami
                    tekst += "\n"

                file.write(tekst)
            popup_informacja(self, "Poprawnie zapisano plik", f'Plik zapisany w ścieżce {self.wybrana_sciezka}')
        except Exception as e:
            popup_informacja(self, "Błąd", f'Błąd podczas zapisywanie pliku: {e}')

    def restartowanie_ekranu(self):
        """
        Przywrócenie podstawowych wartości parametrom przed zmianą ekranów
        """
        self.struktura = []  # Resetowanie jakiejś zmiennej
        self.liczba_sekcji = None
        self.wl = []
        self.wp = []
        self.wejsciowe_x_in = None
        self.wejsciowe_y_out = None
        self.param_algorytm = None
        self.struktura = None
        self.max_port_numer = None
        self.param_czy_przestrojen = False
        self.ostatnio_uzyty_komutator = -1
        self.slownik_polaczen = {}
        self.wybrana_sciezka = None

        # przechowanie referencji do TextInput
        text_input = self.ids.text_input

        # sprawdzenie, czy TextInput ma rodzica
        if text_input.parent:
            # usuniecie jesli istnieje
            text_input.parent.remove_widget(text_input)

        # wyczyszczenie GridLayout
        grid_layout = self.ids.grid_layout
        grid_layout.clear_widgets()  # Usuwamy wszystkie widgety z layoutu

        # dodanie TextInput z powrotem do GridLayout
        new_box_layout = BoxLayout(orientation='vertical', spacing=15, padding=15)
        text_input.text = ""  # wyczyszczenie tekstu
        new_box_layout.add_widget(text_input)  # dodanie do BoxLayout
        grid_layout.add_widget(new_box_layout)  # dodanie do GridLayout
