from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from oprogramowanie_sterownika_PK.gui.ekran_glowny.ekran_glowny import ekran_glowny
from oprogramowanie_sterownika_PK.gui.ekran_zadan.ekran_zadan import ekran_zadan


class aplikacja(App):
    """
        Główna klasa aplikacji, w której znajdują się ekrany realizujące
        poszczególne ekrany oraz funkcji z nimi związane
    """
    title = 'Oprogramowanie sterownika pól komutacyjnych'

    def build(self):
        """
            Funkcja obsługująca ekrany za pomocą ScreenManager'a,
            który zawiera informacje o możliwych do wywołania ekranów.

        :return: root - korzeń jako ScreenManager, zwraca aktualny ekran
        """
        root = ScreenManager()
        root.add_widget(ekran_glowny(name='-ekran_glowny-'))
        root.current = '-ekran_glowny-'
        root.add_widget(ekran_zadan(name='-ekran_zadan-'))

        return root


if __name__ == "__main__":
    aplikacja().run()