from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.widget import Widget


def popup_zestaw_polaczenie(self):
    """
     Funkcja obsługująca popup związany z zestawieniem połączenia
    :param self:
    :return:
    """
    # tworzenie popupu i ustawienie elementów
    self.popup = Popup(title="Wprowadź parametry", size_hint=(None, None), size=(400, 300))
    main_layout = BoxLayout(orientation="vertical", padding=20, spacing=10)
    main_layout.add_widget(BoxLayout(size_hint_y=None, height=20))
    input_layout = GridLayout(cols=2, padding=10, spacing=10)

    input_layout.add_widget(
        Label(text=f"Podaj numer wejścia: \n(0-{self.max_port_numer})", halign="center", valign="middle"))
    self.wejsciowe_x_in = TextInput(multiline=False, size_hint=(None, None), size=(100, 40), font_size=16)
    input_layout.add_widget(self.wejsciowe_x_in)

    input_layout.add_widget(
        Label(text=f"Podaj numer wyjścia: \n(0-{self.max_port_numer})", halign="center", valign="middle"))
    self.wejsciowe_y_out = TextInput(multiline=False, size_hint=(None, None), size=(100, 40), font_size=16)
    input_layout.add_widget(self.wejsciowe_y_out)
    main_layout.add_widget(input_layout)

    buttons_layout = BoxLayout(orientation="horizontal", size_hint_y=None, height=50, spacing=10)
    przycisk_zatwierdz = Button(text="Zatwierdź", size_hint=(None, None), size=(170, 50))
    przycisk_zatwierdz.bind(on_release=self.na_potwierdzenie_nowego_polaczenia)
    buttons_layout.add_widget(przycisk_zatwierdz)

    przycisk_anuluj = Button(text="Anuluj", size_hint=(None, None), size=(170, 50))
    przycisk_anuluj.bind(on_release=self.popup.dismiss)
    buttons_layout.add_widget(przycisk_anuluj)

    # Dodajemy layout z przyciskami do głównego layoutu
    main_layout.add_widget(buttons_layout)

    # Ustawiamy layout popupa
    self.popup.content = main_layout

    # Pokazujemy popup
    self.popup.open()


def pokaz_tablice_polaczen(self, wszystkie):
    """
     Funkcja wyswietlająca tablice połączeń w obiekcie text_input

    :param self: Aktualna instancja oprogramowania (App)
    :param wszystkie: True - wyswietlenie calej tablicy polaczen, False - konkretne polaczenie
    :return:
    """
    # wszystkie połączenia
    if wszystkie:
        message = self.pokaz_tablice_polaczen(wszystkie, None, None)
        text_window = self.ids.text_input
        text_window.text = message
        return

    # wybrane połączenie
    else:
        # popup na podanie x lub y
        self.popup = Popup(title="Wprowadź parametry", size_hint=(None, None), size=(400, 300))
        main_layout = BoxLayout(orientation="vertical", padding=20, spacing=10)
        main_layout.add_widget(BoxLayout(size_hint_y=None, height=20))  # Pusty BoxLayout na górze dla przestrzeni
        input_layout = GridLayout(cols=2, padding=10, spacing=10)

        input_layout.add_widget(
            Label(text=f"Podaj numer wejścia: \n(0-{self.max_port_numer})", halign="center", valign="middle"))
        self.input_x_in_show = TextInput(multiline=False, size_hint=(None, None), size=(100, 40), font_size=16)
        input_layout.add_widget(self.input_x_in_show)

        input_layout.add_widget(
            Label(text=f"Podaj numer wyjścia: \n(0-{self.max_port_numer})", halign="center", valign="middle"))
        self.input_y_out_show = TextInput(multiline=False, size_hint=(None, None), size=(100, 40), font_size=16)
        input_layout.add_widget(self.input_y_out_show)
        main_layout.add_widget(input_layout)

        # przyciski
        buttons_layout = BoxLayout(orientation="horizontal", size_hint_y=None, height=50, spacing=10)
        submit_button = Button(text="Zatwierdź", size_hint=(None, None), size=(170, 50))
        submit_button.bind(on_release=lambda instance: self.sprawdz_dane_do_wyswietlenia_jeden(wszystkie))
        buttons_layout.add_widget(submit_button)
        cancel_button = Button(text="Anuluj", size_hint=(None, None), size=(170, 50))
        cancel_button.bind(on_release=self.popup.dismiss)
        buttons_layout.add_widget(cancel_button)
        main_layout.add_widget(buttons_layout)
        self.popup.content = main_layout

        # wyswietlenie popupu
        self.popup.open()
        return


def popup_informacja(self, tytul, wiadomosc):
    """
     Funkcja tworzy okno popup w przypadku wystąpienia
     błędu lub informacji zwrotnej z wykonywanej operacji.

    :param self: Aktualna instancja oprogramowania (App).
    :param tytul: Tytuł okna.
    :param wiadomosc: Wiadomość wyświetlana jako zawartość okna.
    """
    popup_blad = Popup(
        title=tytul,
        size_hint=(None, None),
        size=(400, 200),
    )
    layout = GridLayout(cols=1, padding=10, spacing=10)

    zawartosc_popup = Label(text=wiadomosc, halign="center", valign="middle")
    zawartosc_popup.bind(size=zawartosc_popup.setter("text_size"))  # Automatyczne łamanie tekstu
    layout.add_widget(zawartosc_popup)

    ok_przycisk = Button(text="OK", size_hint=(None, None), size=(100, 50), pos_hint={"center_x": 0.5})
    ok_przycisk.bind(on_release=popup_blad.dismiss)
    layout.add_widget(ok_przycisk)

    popup_blad.content = layout

    popup_blad.open()


def pokaz_informacje_o_polaczeniu(self, wiadomosc):
    """
     Funkcja wyświetla informacje po operacji na połączeniu.

    :param self: Aktualna instancja oprogramowania (App)
    :param wiadomosc: Informacja wyświetlana jako zawartość okna.
    """
    info_popup = Popup(title="Informacje o połączeniu", size_hint=(None, None), size=(500, 300))
    info_layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
    info_layout.add_widget(Widget(size_hint_y=0.5))  # Spacer w górnej części

    info_label = Label(text=wiadomosc, halign="center", valign="middle", size_hint_y=None, height=40)
    info_layout.add_widget(info_label)
    info_layout.add_widget(Widget(size_hint_y=0.5))  # Spacer w dolnej części

    close_button = Button(text="Zamknij", size_hint=(None, None), size=(200, 50))
    close_button.bind(on_release=info_popup.dismiss)

    close_button.pos_hint = {'center_x': 0.5}
    info_layout.add_widget(close_button)
    info_popup.content = info_layout

    info_popup.open()


def popup_rozlacz_polaczenie(self):
    """
     Funkcja obsługująca przygotowanie do zadania rozłączenia połączenia.
     Wprawdzanie parametrów wstępnych.

    :param self: Aktualna instancja oprogramowania (App)
    """
    self.popup = Popup(title="Wprowadź parametry", size_hint=(None, None), size=(400, 300))
    main_layout = BoxLayout(orientation="vertical", padding=20, spacing=10)
    main_layout.add_widget(BoxLayout(size_hint_y=None, height=20))
    input_layout = GridLayout(cols=2, padding=10, spacing=10)

    # dodanie etykiet i pól tekstowych
    input_layout.add_widget(
            Label(text=f"Podaj numer wejścia: \n(0-{self.max_port_numer})", halign="center", valign="middle"))
    self.wejsciowe_x_in = TextInput(multiline=False, size_hint=(None, None), size=(100, 40), font_size=16)
    input_layout.add_widget(self.wejsciowe_x_in)
    input_layout.add_widget(
        Label(text=f"Podaj numer wyjścia: \n(0-{self.max_port_numer})", halign="center", valign="middle"))
    self.wejsciowe_y_out = TextInput(multiline=False, size_hint=(None, None), size=(100, 40), font_size=16)
    input_layout.add_widget(self.wejsciowe_y_out)
    main_layout.add_widget(input_layout)

    # przyciski
    przyciski_layout = BoxLayout(orientation="horizontal", size_hint_y=None, height=50, spacing=10)
    zatwierdz_button = Button(text="Zatwierdź", size_hint=(None, None), size=(170, 50))
    zatwierdz_button.bind(on_release=self.na_rozlaczenie_polaczenia)  # Correct binding here
    przyciski_layout.add_widget(zatwierdz_button)

    anuluj_button = Button(text="Anuluj", size_hint=(None, None), size=(170, 50))
    anuluj_button.bind(on_release=self.popup.dismiss)
    przyciski_layout.add_widget(anuluj_button)
    main_layout.add_widget(przyciski_layout)
    self.popup.content = main_layout

    self.popup.open()
