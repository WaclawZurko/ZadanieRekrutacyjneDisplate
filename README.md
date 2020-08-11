# ZadanieRekrutacyjneDisplate
test sciezki sprzedazowej z usa na potrzeby rekrutacji

Aby uruchomic test potrzebujemy:
- Python (tworzone na 3.7.2)
- pip dla zainstalowania selenium i behave
- selenium - pip install selenium
- behave - pip install behave
- zainstalowanej przegladarki chrome oraz chromedriver dodany do zmiennych srodowiskowych (PATH)
- ustawic sie w terminalu na folderze displaiotesty i wpisac --> behave features/zadanierekrutacyjne.feature


Po poprawnym skonfigurowaniu test powinien trwac okolo 15-20 sekund

Dla lepszej czytelnosci zadania nie dodawalem trybu headless 

Tresc zadania jest w pliku zadanierekrutacyjne.feature

Dlaczego behave?
- BDD - jest calkiem zrozumiale dla "biznesu" czy innych osob nietechnicznych, scenariusze moga byc pisane przez osoby nie znajace "bebechow"
- latwo wpiac takie testy do browserstacka/crossbrowsertesting czy innych podonych (docelowo tak bym proponowal zrobic, latwiej utrzymac sterowniki, latwa obsluga roznych przegladarek itp)
- jest czytelniejszy niz samo selenium
- mialem wczesniej stycznosc ;)
