from kivy.metrics import dp
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import os


class FileChooserPopup(Popup):
    """
     Klasa realizuje wybór scieżki oraz zapis stanu struktury pola komutacyjnego
     wykorzystując filechooser z biblioteki Kivy.
    """
    def __init__(self, callback, **kwargs):
        """
         Funkcja inicjalizacyjna
        """
        super(FileChooserPopup, self).__init__(**kwargs)
        self.filechooser = None
        self.callback = callback
        self.tytul = 'Wybierz ścieżkę'
        self.size_hint = (0.9, 0.9)
        self.content = self.utworz_zawartosc()

    def utworz_zawartosc(self):
        """
         Funkcja tworząca okno typu popup umozliwiające wybór ścieżki
         zapisu pliku
        """
        layout = BoxLayout(orientation='vertical')
        sciezka_pulpit = os.path.join(os.path.expanduser('~'), 'Desktop')
        if not os.path.exists(sciezka_pulpit):
            os.makedirs(sciezka_pulpit)
        self.filechooser = FileChooserIconView(path=sciezka_pulpit, dirselect=True)
        layout.add_widget(self.filechooser)

        layout_przyciski = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(60), spacing=dp(10))
        layout_przyciski.bind(minimum_width=layout_przyciski.setter('width'))

        lewa_przestrzen = BoxLayout(size_hint=(0.4, None), height=dp(50))
        layout_przyciski.add_widget(lewa_przestrzen)
        przycisk_wybierz = Button(
            text='Wybierz',
            size_hint=(None, None),
            size=(dp(100), dp(50)),
            pos_hint={'center_x': 0.5},
            background_color=(0.5, 0.7, 1, 1),
            color=(1, 1, 1, 1),
            font_size=dp(18),
        )
        przycisk_wybierz.bind(on_press=self.na_wybor)
        layout_przyciski.add_widget(przycisk_wybierz)

        przycisk_anuluj = Button(
            text='Anuluj',
            size_hint=(None, None),
            size=(dp(100), dp(50)),
            pos_hint={'center_x': 0.5},
            background_color=(0.5, 0.7, 1, 1),
            color=(1, 1, 1, 1),
            font_size=dp(18),
        )
        przycisk_anuluj.bind(on_press=self.dismiss)
        layout_przyciski.add_widget(przycisk_anuluj)
        layout.add_widget(layout_przyciski)

        return layout

    def na_wybor(self, instance):
        """
         Wywołanie funkcji tworzących scieżki dla zapisywanego pliku.
        """
        wybrana_sciezka = self.filechooser.path
        self.callback(wybrana_sciezka)
        self.dismiss()
