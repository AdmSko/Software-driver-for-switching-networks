from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget


def popup_parametry(self):
    """
     Funkcja realizuje okno typu popup umożliwiające wprowadzenie
     parametrów okreslających zadane pole komutacyjne, takich jak
     liczba sekcji, wektor wl, wp i algorytm sterowania.

     :param self: Aktualna instancja aplikacji. (App)
    """
    # tworzenie głównego okna popup
    self.param_popup = Popup(title="Wprowadź parametry", size_hint=(None, None), size=(400, 400))

    # logika związana z dodaniem do layoutu okna
    main_layout = BoxLayout(orientation="vertical", padding=20, spacing=10)
    input_layout = GridLayout(cols=2, padding=10, spacing=10)

    input_layout.add_widget(Label(text="Liczba sekcji:"))
    self.liczba_sekcji = TextInput(multiline=False)
    input_layout.add_widget(self.liczba_sekcji)

    input_layout.add_widget(Label(text="Wektor wl:"))
    self.param_wl = TextInput(multiline=False)
    input_layout.add_widget(self.param_wl)

    input_layout.add_widget(Label(text="Wektor wp:"))
    self.param_wp = TextInput(multiline=False)
    input_layout.add_widget(self.param_wp)

    main_layout.add_widget(input_layout)

    # realizacja wyboru algorytmu
    algorytm_layout = BoxLayout(orientation="horizontal", size_hint_y=None, height=50, spacing=10)

    self.algorytm_wybor = DropDown()
    for i, alg_nazwa in enumerate(["kolejnościowy", "quasi-przypadkowy", "Benesa", "przestrajalny"], 1):
        przycisk = Button(text=f"{alg_nazwa}", size_hint_y=None, height=44)
        przycisk.bind(on_release=lambda btn: self.algorytm_wybor.select(btn.text))
        self.algorytm_wybor.add_widget(przycisk)

    self.algorytm_przycisk = Button(text="Wybierz algorytm sterowania", size_hint=(1, None), height=44)
    self.algorytm_przycisk.bind(on_release=self.algorytm_wybor.open)
    self.algorytm_wybor.bind(on_select=self.na_wyborze_algorytmu)

    algorytm_layout.add_widget(self.algorytm_przycisk)
    main_layout.add_widget(algorytm_layout)

    # Layout dla drugiego wyboru algorytmu (przestrojen) - początkowo ukryty
    self.algorytm_wybor1 = DropDown()
    for i, alg_nazwa in enumerate(["kolejnościowy", "quasi-przypadkowy", "Benesa"], 1):
        przycisk = Button(text=f"{alg_nazwa}", size_hint_y=None, height=44)
        przycisk.bind(on_release=lambda btn: self.algorytm_wybor1.select(btn.text))
        self.algorytm_wybor1.add_widget(przycisk)

    self.algorytm_przycisk1 = Button(text="Wybierz algorytm sterowania", size_hint=(1, None), height=44)
    self.algorytm_przycisk1.bind(on_release=self.algorytm_wybor1.open)
    self.algorytm_wybor1.bind(on_select=self.na_wyborze_algorytmu)
    self.algorytm_przycisk1.disabled = True
    main_layout.add_widget(self.algorytm_przycisk1)

    przycisk_zamknij = Button(text="Zatwierdź", size_hint=(None, None), size=(200, 50), pos_hint={"center_x": 0.5})
    przycisk_zamknij.bind(on_release=self.sprawdz_wartosci_we_wy)
    main_layout.add_widget(przycisk_zamknij)
    self.param_popup.content = main_layout
    self.param_popup.open()


def popup_informacja(self, wiadomosc):
    """
     Funkcja tworzy okno typu popup zawierający informację.
     Informacją może być błąd lub wynikim danej operacji.

    :param self: Aktualna instancja aplikacji
    :param wiadomosc: wiadomość, która zostanie wyświetlona na ekran
    :return:
    """
    # zamykamy poprzedni popup błędu, jeśli istnieje
    if self.popup_informacja:
        self.popup_informacja.dismiss()
        self.popup_informacja = None
    # tworzenie nowego popup
    self.popup_informacja = Popup(
        title="Błąd",
        size_hint=(None, None), size=(600, 250)
    )

    # logika związana z dodaniem do layoutu okna
    layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
    layout.add_widget(Widget(size_hint_y=0.5))  # Spacer w górnej części
    layout.add_widget(
        Label(text=wiadomosc, halign="center", valign="middle", size_hint_y=None, height=40))
    layout.add_widget(Widget(size_hint_y=0.5))  # Spacer w dolnej części
    przycisk_zamknij = Button(text="OK", size_hint=(None, None), size=(200, 50))
    przycisk_zamknij.bind(on_release=self.popup_informacja.dismiss)
    przycisk_zamknij.pos_hint = {'center_x': 0.5}
    layout.add_widget(przycisk_zamknij)
    self.popup_informacja.content = layout
    self.popup_informacja.open()


def pokaz_niewdrozony_benes(self):
    """
     Funkcja realizuje tworzenie okna typu popup z informacją
     o niewdrożonym polu o strukturze Benesa.

     W przypadku dodania funkcjonalności związanych ze strukturą Cantora należy usunąć
     tę funkcję i dodać warunki w głównej funkcji ekranu.

     :param self: Aktualna instancja aplikacji
    """
    message = "Struktura Benesa nie została wdrożona"
    # tworzenie nowego okna popup
    self.popup_informacja = Popup(
        title="Błąd",
        size_hint=(None, None), size=(600, 250)
    )

    # logika związana z dodaniem do layoutu okna
    layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
    layout.add_widget(Widget(size_hint_y=0.5))
    layout.add_widget(
        Label(text=message, halign="center", valign="middle", size_hint_y=None, height=40))
    layout.add_widget(Widget(size_hint_y=0.5))
    przycisk_zamknij = Button(text="OK", size_hint=(None, None), size=(200, 50))
    przycisk_zamknij.bind(on_release=self.popup_informacja.dismiss)
    przycisk_zamknij.pos_hint = {'center_x': 0.5}
    layout.add_widget(przycisk_zamknij)
    self.popup_informacja.content = layout
    self.popup_informacja.open()


def pokaz_niewdrozony_cantor(self):
    """
     Funkcja realizuje tworzenie okna typu popup z informacją
     o niewdrożonym polu o strukturze Cantora.

     W przypadku dodania funkcjonalności związanych ze strukturą Cantora należy usunąć
     tę funkcję i dodać warunki w głównej funkcji ekranu.

     :param self: Aktualna instancja aplikacji
    """
    wiadomosc = "Struktura Cantora nie została wdrożona"
    # tworzenie nowego okna popup
    self.popup_informacja = Popup(
        title="Błąd",
        size_hint=(None, None), size=(600, 250)
    )

    # logika związana z dodaniem do layoutu okna
    layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
    layout.add_widget(Widget(size_hint_y=0.5))
    layout.add_widget(
        Label(text=wiadomosc, halign="center", valign="middle", size_hint_y=None, height=40))
    layout.add_widget(Widget(size_hint_y=0.5))
    close_button = Button(text="OK", size_hint=(None, None), size=(200, 50))
    close_button.bind(on_release=self.popup_informacja.dismiss)
    close_button.pos_hint = {'center_x': 0.5}
    layout.add_widget(close_button)
    self.popup_informacja.content = layout
    self.popup_informacja.open()


def zamknij_popup(self):
    """
     Funkcja wykorzystywana do wywołania ekranu ekran_zadan,
     po prawidłowym wprowadzeniu wszystkich wymaganch parametrów.

    :param self: aktualna instancja aplikacji
    """
    if self.param_popup:
        self.param_popup.dismiss()

    # przekazanie parametrów do ekranu -ekran_zadan-
    self.manager.current = '-ekran_zadan-'
    ekran_zadan = self.manager.get_screen('-ekran_zadan-')
    ekran_zadan.uaktualnij_parametry(
        int(self.typ_struktury),
        int(self.liczba_sekcji.text),
        list(self.wl),
        list(self.wp),
        self.param_algorytm,
        self.param_czy_przestrojen
    )