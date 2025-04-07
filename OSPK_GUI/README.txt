	Dodatek zawiera oprogramowanie sterownika pól komutacyjnych z graficznym interfejsem użytkownika GUI. Oprogramowanie zostało napisane w języku programowania Python dla wersji interpretera 3.10 z wykorzystaniem biblioteki Kivy, która realizuje graficzny interfejs użytkownika. OSPK_GUI jest głównym katalogiem projektu, wewnątrz którego znajdują się katalogi .idea, .venv. i oprogramowanie_sterownika_PK. Do pisania oprogramowania wykorzystano środowisko PyCharm, które generuje dodatkowo katalogi .idea i .venv. Pierwszy z nich zawiera metadane projektu, takie jak ustawienia projektu, konfiguracje środowiska uruchomieniowego oraz style kodowania, natomiast .venv odpowiada za ustawienia wirtualnego środowiska Pythona, które izoluje zależności projektu. Zawiera lokalną instalację Pythona i bibliotek wymaganych przez projekt, co pozwala uniknąć konfliktów związanych z wersjami. Katalog oprogramowanie_sterownika_PK zawiera pliki realizujące oprogramowanie sterownika pól komutacyjnych, które zostały omówione w rozdziale piątym.
Przed przystąpieniem do uruchomienia oprogramowania, niezależnie od metody, należy pobrać interpreter Python 3.10.11 ze strony https://www.python.org/downloads/release/python-31011/ . Rekomendowana wersją pliku jest Windows installer (64-bit). Następnie należy otworzyć pobrany plik .exe i przejść przez proces instalacji. Ważnym etapem jest zaznaczenie okna Add python.exe to PATH. Następnie można skorzystać z opcji Install Now. Po zainstalowaniu interpretera Python, wymagana jest instalacja bibliotek stosowanych w oprogramowaniu. W tym celu należy otworzyć wiersz poleceń w systemie Windows za pomocą Wyszukaj, wpisać cmd, otworzyć wiersz poleceń i wpisać komendy, która instaluje biblioteki NumPy i Kivy:
pip install numpy
pip install kivy
Uwaga! W przypadku posiadania na urządzeniu wielu interpreterów języka Python, należy sprecyzować, w którym interpreterze ma zostać zainstalowana dana biblioteka. Zrealizować można to za pomocą komendy:
{ścieżka}\Python310\python.exe -m pip install numpy
{ścieżka}\Python310\python.exe -m pip install kivy
gdzie {ścieżka} to lokalizacja pliku python.exe interpretera Python 3.10.11. Można ją otrzymać poprzez użycie komendy:
where python
	Aby poprawnie uruchomić oprogramowanie w środowisku PyCharm wpierw należy pobrać środowisko ze strony internetowej https://www.jetbrains.com/pycharm/ poprzez kliknięcie na stronie przycisku instaluj. Następnie należy wybrać pobranie wersji PyCharm Community, co spowoduje pobranie instalatora środowiska, w którym należy przejść przez proces instalacyjny, czyli wybór miejsca na dysku do instalacji i innych ustawień względem własnych preferencji. Kolejnym krokiem jest otworzenie tego środowiska, wybranie opcji Plik, następnie Otwórz, wyszukanie i zaznaczenie katalogu OSPK_GUI i kliknięcie przycisku OK.  W przypadku pierwszego włączenia środowiska wyświetlony zostanie ekran startowy, w którym należy wybrać opcję Open, wyszukać katalog OSPK_CLI i zatwierdzić poprzez przycisk OK. W ten sposób katalog projektowy zostanie otwarty w środowisku PyCharm. Na tym etapie środowisko może wyświetlić informację o braku interpretera lub „Invalid Python SDK”. W takiej sytuacji należy ustawić ręcznie interpreter dla projektu poprzez File > Settings > Python Interpreter > Add interpreter > Select existing i wybranie Python 3.10.11 pod ścieżką, gdzie został on wcześniej pobrany na urządzenie. Teraz należy wybrać z drzewa projektowego w środowisku plik main.py i uruchomić go poprzez skrót klawiszowy Shift+F10 lub przycisk z zieloną strzałką.
Sprawdzono również sposób uruchamiania oprogramowania wykorzystując inne popularne środowiska. Przykładowym z nich jest Visual Studio Code, w którym wymagane jest wykonanie następujących kroków:
1. otworzenie w środowisku głównego katalogu projektu - należy wybrać z paska narzędzi opcję Plik, następnie Otwórz Katalog i wybrać katalog OSPK_GUI,
2. uruchomienie programu - wykorzystując wbudowany w środowisko terminal (skrót Ctrl+Shift+`) wpisać komendę:
python -m oprogramowanie_sterownika_PK.gui.main
W przypadku, gdy podstawowo w terminalu użytkownik nie znajduje się w katalogu OSPK_GUI, należy przez wyżej przedstawioną komendą wpisać:
cd {ścieżka}\OSPK_GUI
gdzie {ścieżka} należy zastąpić rzeczywistą ścieżką pliku, która określa położenie głównego katalogu projektu oprogramowania sterownika pól komutacyjnych.
Uwaga! W przypadku posiadania na urządzeniu wielu interpreterów języka Python, należy sprecyzować, za pomocą którego interpretera ma zostać uruchomione oprogramowanie. Zrealizować można to za pomocą komendy:
{ścieżka}\Python310\python.exe -m oprogramowanie_sterownika_PK.gui.main
gdzie {ścieżka} to lokalizacja pliku python.exe interpretera Python 3.10.11. Pełną ścieżkę do interpretera można otrzymać poprzez użycie komendy:
where python
	Oprogramowanie również może być uruchomione z poziomu wiersza poleceń dla systemu operacyjnego Windows, w takim przypadku należy wykonać kroki:
1. uruchomienie wiersza poleceń CMD i przejście do katalogu OSPK_GUI za pomocą komendy:
cd {ścieżka}\OSPK_GUI
gdzie {ścieżka} należy zastąpić rzeczywistą ścieżką pliku, która określa położenie głównego katalogu projektu oprogramowania sterownika pól komutacyjnych,
2. uruchomienie oprogramowania - wykorzystując komendę:
python -m oprogramowanie_sterownika_PK.gui.main
Uwaga! W przypadku posiadania na urządzeniu wielu interpreterów języka Python, należy sprecyzować, za pomocą którego interpretera ma zostać uruchomione oprogramowanie. Zrealizować można to za pomocą komendy:
{ścieżka}\Python310\python.exe -m oprogramowanie_sterownika_PK.gui.main
gdzie {ścieżka} to lokalizacja pliku python.exe interpretera Python 3.10.11. Pełną ścieżkę do interpretera można otrzymać poprzez użycie komendy:
where python

Zawartość kartoteki \OSPK_GUI:
.idea										// katalog zawierający metadane projektu
.venv										// katalog zawierający ustawienia środowiska wirtualnego
Oprogramowanie_sterownika_PK							// katalog zawierający realizację oprogramowania
	algorytmy								// katalog zawierający pliki, których funkcje realizują algorytmy sterowania
		kolejnosciowy.py						// plik zawierający realizację kolejnościowego algorytmu sterowania
			algorytm_kolejnosciowy					// funkcja realizująca kolejnościowy algorytm sterowania
		quasi_przypadkowy.py						// plik zawierający realizację quasi-przypadkowego algorytmu sterowania
			algorytm_quasi_przypadkowy				// funkcja realizująca quasi-przypadkowy algorytm sterowania
		benes.py							// plik zawierający realizację algorytmu sterowania Benesa
			algorytm_Benesa						// funkcja realizująca algorytm sterowania Benesa
		paull.py							// plik zawierający realizację algorytmu przestrojeń Paulla
			algorytm_paulla						// główna funkcja algorytmu Paulla, odpowiednio wywołuje funkcje realizujące algorytm
			utworz_macierz_paulla					// funkcja tworząca macierz Paulla
			zamiana_wartosci_na_symbole				// funkcja zamieniająca wartości w macierzy Paulla na odpowiednie symbole
			przestrajanie_polaczen_w_macierzy			// funkcja realizująca przestrojenia w macierzy Paulla
			sprawdz_czy_konflikt_wiersz_kolumna			// funkcja sprawdzająca, czy dla sprawdzanej komórki nadal występuje konflikt
			aktualizacja_slownika_po_przestrojeniach		// funkcja aktualizująca po przestrojeniach struktury stosowane w oprogramowaniu
	narzędzia								// katalog zawierający pliki z funkcjami pomocniczymi
		narzędzia.py							// plik zawierający funkcje pomocnicze
			wyczysc_ekran						// funkcja czyszcząca okno
			sprawdz_dane_wejsciowe_od_do				// funkcja sprawdzająca poprawność wpisywanych danych z zakresem
			sprawdz_wartosci_we_wy					// funkcja sprawdzająca poprawność wpisywanych danych
			otrzymaj_liste_z_wejscia				// funkcja formatująca dane od użytkownika w listę
			sprawdz_dlugosc_list					// funkcja sprawdzająca długość podanych list
			znajdz_klucz_id_polaczenia				// funkcja znajdująca klucz połączenia w strukturze slownik_polaczen na podstawie podanego wejścia i wyjścia
			znajdz_klucz_w_slowniku					// funkcja znajdująca klucz połączenia w strukturze slownik_polaczen na podstawie wykorzystywanych komutatorów
			sprawdz_czy_kolumna_wiersz_wolne			// funkcja sprawdzająca, czy wiersz i kolumna są wolne, czyli sprawdzenie czy nie występuje wartość 1
		pop_upy_ekran_glowny.py						// plik zawierający funkcje realizujące okna popup dla ekranu głównego
			popup_parametry						// funkcja wyświetlająca okno popup dla podania parametrów pola
			popup_informacja					// funkcja wyświetlająca okno z podana do niej wiadomością
			popup_niewdrozony_benes					// funkcja wyświetlająca okno informujące o niewdrożeniu pola Benesa
			popup_niewdrozony_cantor				// funkcja wyświetlająca okno informujące o niewdrożeniu pola Cantora
			zamknij_popup						// funkcja realizująca zamykanie okien popup
		pop_upy_ekran_zadan.py						// plik zawierający funkcje realizujące okna popup dla ekranu zadań
			popup_zestaw_polaczenie					// funkcja wyświetlająca popup dla zadania zestawienia połączenia
			pokaz_tablice_polaczen					// funkcja wyświetlająca na ekran wynik operacji wyświetlenia tablicy połączeń
			popup_informacja					// funkcja tworząca popup z przekazaną wiadomością
			pokaz_informacje_o_polaczeniu				// funkcja zwracająca informacje o poprawności wprowadzonych danych
			popup_rozlacz_polaczenie				// funkcja wyświetlająca okno popup z informacją o poprawności wykonania zadania rozłączenia połączenia
		struktura_do_pliku.py						// plik zawierający funkcje realizujące zapis stanu struktury do pliku
			Klasa - FileChooserPopup				// klasa opisująca FileChooser, narzędzie wyświetlające okno popup do wyboru ścieżki zapisu
				__init__					// funkcja inicjalizacyjna
				utworz_zawartosc				// funkcja formatująca ciąg znaków, który zostanie zapisy w pliku
				na_wybor					// funkcja formatująca ciąg znaków, który zostanie zapisany do pliku
	struktury								// katalog zawierający pliki realizujące utworzenie pól o danej strukturze
		clos.py								// plik zawierający funkcje realizujące utworzenie struktury Closa
			utworz_strukture_closa					// funkcja realizująca utworzenie struktury Closa
	gui									// katalog zawierający katalogi realizujące ekrany oprogramowania GUI
		ekran_glowny							// katalog zawierający pliki realizujące ekran główny oprogramowania
			ekran_glowny.kv						// plik zawierający układ graficzny ekranu głównego w formacie .kv
			ekran_glowny.py						// plik zawierający funkcje realizujące ekran główny - obsługa elementów ekranu
				Klasa - ekran_glowny				// klasa opisująca ekran główny, w której zawarte są jej funkcje 
					__init__				// funkcja inicjalizacyjna
					przygotuj_popup_wprowadzanie_danych	// funkcja realizująca okno popup do wprowadzenia danych pola
					na_wyborze_algorytmu			// funkcja realizująca operacje wykonywane podczas wyboru algorytmu sterowania
					sprawdz_wartosci_we_wy			// funkcja sprawdzająca poprawność wpisanych wartości z wejścia
					pokaz_popup_benes			// funkcja pełniąca rolę uchwytu na funkcję wyświetlającą popup informacyjny o polu Benesa
					pokaz_popup_cantor			// funkcja pełniąca rolę uchwytu na funkcję wyświetlającą popup informacyjny o polu Cantora
		ekran_zadan							// katalog zawierający pliki realizujące ekran zadań oprogramowania
			ekran_zadan.kv						// plik zawierający układ graficzny ekranu zadań w formacie .kv
			ekran_zadan.py						// plik zawierający funkcje realizujące ekran zadań - obsługa elementów ekranu
				Klasas - ekran_zadan				// klasa opisująca ekran zadań, w której zawarte są jej funkcje
					__init__				// funkcja inicjalizacyjna
					uaktualnij_parametry			// funkcja realizująca uaktualnienie parametrów zadanego pola
					pokaz_popup_nowe_polaczenie		// funkcja realizująca uchwyt na funkcję wyświetlającą okno popup dla zadania zestawienia nowego połączenia
					pokaz_popup_rozlacz_polaczenie		// funkcja realizująca uchwyt na funkcję wyświetlającą okno popup dla zadani rozłączenia połączenia
					na_potwierdzenie_nowego_polaczenia	// funkcja wyświetlająca popup informujący o poprawności zadania zestawienia połączenia
					na_rozlaczenie_polaczenia		// funkcja wyświetlająca popup informujący o poprawności zadania rozłączenia połączenia
					rozlacz_polaczenie			// funkcja realizująca zadanie rozłączenie połączenia
					pokaz_popup_tablica_polaczen		// funkcja realizująca wyświetlenie okna popup w celu podania danych wejścia i wyjścia połączenia do wyświetlenia
					pokaz_tablice_polaczen			// funkcja realizująca zadanie wyświetlenia tablicy połączeń
					sprawdz_dane_do_wyswietlenia_jeden	// funkcja sprawdzająca dane wprowadzone w ramach wyświetlenia konkretnego połączenia
					pokaz_stan_struktury			// funkcja realizująca zadanie wyświetlenia stanu struktury pola
					zapisz_plik				// funkcja wywołująca zadanie zapisania stanu struktury pola do pliku
					finalizuj_zapis				// funkcja finalizująca zadanie zapisania stanu struktury pola do pliku
					resetowanie_ekranu			// funkcja przywracająca parametry okna do wartości podstawowych w przypadku powrotu do menu głównego
		main.kv								// plik zawierający ustawienia związane z możliwymi do wyboru ekranami oprogramowania
		main.py								// plik zawierający ustawienia związane z wyborem aktualnego ekranu oprogramowania
			Klasa - aplikacja					// główna klasa oprogramowania, w której znajdują się deklaracje ekranów realizujących poszczególne funkcje
				build 						// funkcja obsługująca ekrany za pomocą narzędzia ScreenManager
