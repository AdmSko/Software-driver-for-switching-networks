	Dodatek zawiera oprogramowanie sterownika pól komutacyjnych korzystające z interfejsu wiersza poleceń CLI. Oprogramowanie zostało napisane w języku programowania Python dla wersji interpretera 3.10. OSPK_CLI jest głównym katalogiem projektu, wewnątrz którego znajdują się katalogi .idea, .venv. i oprogramowanie_sterownika_PK. Do pisania oprogramowania wykorzystano środowisko PyCharm, które generuje katalogi .idea i .venv. Pierwszy z nich zawiera metadane projektu, takie jak ustawienia projektu, konfiguracje środowiska uruchomieniowego, czy style kodowania, natomiast .venv odpowiada za ustawienia wirtualnego środowiska Pythona, które izoluje zależności projektu. Zawiera lokalną instalację Pythona i bibliotek wymaganych przez projekt, co pozwala uniknąć konfliktów wersji bibliotek. W katalogu oprogramowanie_sterownika_PK zawarte są pliki realizujące oprogramowanie sterownika pól komutacyjnych, które zostały omówione w rozdziale piątym.
Przed przystąpieniem do uruchomienia oprogramowania, niezależnie od metody, należy pobrać interpreter Python 3.10.11 ze strony https://www.python.org/downloads/release/python-31011/ . Rekomendowana wersją pliku jest Windows installer (64-bit). Następnie należy otworzyć pobrany plik .exe i przejść przez proces instalacji. Ważnym etapem jest zaznaczenie okna Add python.exe to PATH. Następnie można skorzystać z opcji Install Now. Po zainstalowaniu interpretera Python, wymagana jest instalacja bibliotek stosowanych w oprogramowaniu. W tym celu należy otworzyć wiersz poleceń w systemie Windows za pomocą Wyszukaj, wpisać cmd, otworzyć wiersz poleceń i wpisać komendę, która instaluje bibliotekę NumPy:
pip install numpy
Uwaga! W przypadku posiadania na urządzeniu wielu interpreterów języka Python, należy sprecyzować, w którym interpreterze ma zostać zainstalowana dana biblioteka. Zrealizować można to za pomocą komendy:
{ścieżka}\Python310\python.exe -m pip install numpy
gdzie {ścieżka} to lokalizacja pliku python.exe interpretera Python 3.10.11. Można ją otrzymać poprzez użycie komendy:
where python
	Aby poprawnie uruchomić oprogramowanie w środowisku PyCharm wpierw należy pobrać środowisko ze strony internetowej https://www.jetbrains.com/pycharm/ poprzez kliknięcie na stronie przycisku instaluj. Następnie należy wybrać pobranie wersji PyCharm Community, co spowoduje pobranie instalatora środowiska, w którym należy przejść przez proces instalacyjny, czyli wybór miejsca na dysku do instalacji i innych ustawień względem własnych preferencji. Kolejnym krokiem jest otworzenie tego środowiska, wybranie opcji File, następnie Open, wyszukanie i zaznaczenie katalogu OSPK_CLI i kliknięcie przycisku OK.  W przypadku pierwszego włączenia środowiska wyświetlony zostanie ekran startowy, w którym należy wybrać opcję Open, wyszukać katalog OSPK_CLI i zatwierdzić poprzez przycisk OK. W ten sposób katalog projektowy zostanie otwarty w środowisku PyCharm. Na tym etapie środowisko może wyświetlić informację o braku interpretera lub „Invalid Python SDK”. W takiej sytuacji należy ustawić ręcznie interpreter dla projektu poprzez File > Settings > Python Interpreter > Add interpreter > Select existing i wybranie Python 3.10.11 pod ścieżką, gdzie został on wcześniej pobrany na urządzenie. Teraz należy wybrać z drzewa projektowego w środowisku plik main.py i uruchomić go poprzez skrót klawiszowy Shift+F10 lub przycisk z zieloną strzałką. 
Opracowano również sposób uruchamiania oprogramowania wykorzystując inne popularne środowiska. Przykładowym z nich jest Visual Studio Code, w którym wymagane jest wykonanie następujących kroków:
1. otworzenie w środowisku głównego katalogu projektu - należy wybrać z paska narzędzi opcję Plik, następnie Otwórz Katalog i wybrać katalog OSPK_CLI,
2. uruchomienie programu - wykorzystując wbudowany w środowisko terminal (skrót Ctrl+Shift+`) wpisać komendę:
python -m oprogramowanie_sterownika_PK.main
W przypadku, gdy podstawowo w terminalu użytkownik nie znajduje się w katalogu OSPK_CLI, należy przez wyżej przedstawioną komendą wpisać:
cd {ścieżka}\OSPK_CLI
gdzie {ścieżka} należy zastąpić rzeczywistą ścieżką pliku, która określa położenie głównego katalogu projektu oprogramowania sterownika pól komutacyjnych,
Uwaga! W przypadku posiadania na urządzeniu wielu interpreterów języka Python, należy sprecyzować, za pomocą którego interpretera ma zostać uruchomione oprogramowanie. Zrealizować można to za pomocą komendy:
{ścieżka}\Python310\python.exe -m oprogramowanie_sterownika_PK.main
gdzie {ścieżka} to lokalizacja pliku python.exe interpretera Python 3.10.11. Pełną ścieżkę do interpretera można otrzymać poprzez użycie komendy:
where python
	Oprogramowanie również może być uruchomione z poziomu wiersza poleceń dla systemu operacyjnego Windows, w takim przypadku należy wykonać kroki:
1. uruchomienie wiersza poleceń CMD i przejście do katalogu OSPK_CLI za pomocą komendy:
cd {ścieżka}\OSPK_CLI
gdzie {ścieżka} należy zastąpić rzeczywistą ścieżką pliku, która określa położenie głównego katalogu projektu oprogramowania sterownika pól komutacyjnych,
2. uruchomienie oprogramowania - wykorzystując komendę:
python -m oprogramowanie_sterownika_PK.main
Uwaga! W przypadku posiadania na urządzeniu wielu interpreterów języka Python, należy sprecyzować, za pomocą którego interpretera ma zostać uruchomione oprogramowanie. Zrealizować można to za pomocą komendy:
{ścieżka}\Python310\python.exe -m oprogramowanie_sterownika_PK.main
gdzie {ścieżka} to lokalizacja pliku python.exe interpretera Python 3.10.11. Pełną ścieżkę do interpretera można otrzymać poprzez użycie komendy:
where python

Zawartość kartoteki \OSPK_CLI:
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
			wyczysc_ekran						// funkcja czyszcząca okno CLI
			sprawdz_dane_wejsciowe_od_do				// funkcja sprawdzająca poprawność wpisywanych danych z zakresem
			sprawdz_wartosci_we_wy					// funkcja sprawdzająca poprawność wpisywanych danych
			otrzymaj_liste_z_wejscia				// funkcja formatująca dane od użytkownika w listę
			sprawdz_dlugosc_list					// funkcja sprawdzająca długość podanych list
			znajdz_klucz_id_polaczenia				// funkcja znajdująca klucz połączenia w strukturze slownik_polaczen na podstawie podanego wejścia i wyjścia
			znajdz_klucz_w_slowniku					// funkcja znajdująca klucz połączenia w strukturze slownik_polaczen na podstawie wykorzystywanych komutatorów
			sprawdz_czy_kolumna_wiersz_wolne			// funkcja sprawdzająca, czy wiersz i kolumna są wolne, czyli sprawdzenie czy nie występuje wartość 1
	struktury								// katalog zawierający plik realizujący menu zadań oraz utworzenie pól o danej strukturze
		menu_zadan.py							// plik zawierający funkcje realizujące menu zadań
			menu_zadan						// główna funkcja realizująca menu zadań
			zestaw_polaczenie					// funkcja realizująca zadanie rozłączenia połączenia
			rozlacz_polaczenie					// funkcja realizująca zadanie rozłączenia połączenia
			pokaz_tablice_poalczen					// funkcja realizująca zadanie wyświetlenia tablicy połączeń oraz konkretnego połączenia
			pokaz_stan_struktury					// funkcja realizująca wyświetlenie stanu struktury pola
		clos.py								// plik zawierający funkcje realizujące utworzenie struktury Closa
			utworz_strukture_closa					// funkcja realizująca utworzenie struktury Closa
	main.py									// plik zawierający funkcję realizującą menu główne, które rozpoczyna pracę oprogramowania
		menu_glowne							// funkcja realizująca menu główne oprogramowania 
			