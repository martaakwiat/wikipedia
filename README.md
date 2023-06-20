# wikipedia
Projekt zaliczeniowy- testowanie aplikacji webowej(wikipedii) z wykorzystaniem Selenium w Pythonie

Środowisko testowe:
-Windows 11
-Visual Studio Code, version 1.79.1 
-Python 3.11.3
-Chromedriver 114.0.5735.90 
-Chrome web browser 114.0.5735.110 version

Niezbędne pakiety:
-Biblioteka Selenium
-unittest

Projekt : 
Testowanie aplikacji webowej (Wikipedii) z wykorzystaniem Selenium w 
Pythonie

Scenariusz testowy: 
Logowanie się do aplikacji webowej


Przypadek 001 (przypadek negatywny):
Użytkownik próbuje zalogować się do aplikacji, podając złe hasło

Warunki wstępne:
1. Użytkownik posiada aktywne konto w aplikacji
2. Otwarta strona internetowa

Kroki:
1. Kliknij "Zaloguj się"
2. Wprowadź poprawną nazwę użytkownika w polu "Nazwa Użytkownika"
3. Wprowadź błędne hasło użytkownia w polu "Hasło"
4. Zaznacz checkbox "Nie wylogowuj mnie"
5. Kliknij przycisk "Zaloguj się"

Oczekiwany rezultat:
1. Użytkownik otrzymuje komunikat „Podany login lub hasło są 
nieprawidłowe. Spróbuj jeszcze raz."

Warunki końcowe:
1. Użytkownik nie zostaje zalogowany


Przypadek 002 (przypadek negatywny):
Użytkownik próbuje zalogować się do aplikacji, nie podając hasła

Warunki wstępne:
1. Użytkownik posiada aktywne konto w aplikacji
2. Otwarta strona internetowa

Kroki:
1. Kliknij "Zaloguj się"
2. Wprowadź poprawną nazwę użytkownika w polu "Nazwa Użytkownika"
3. Pomiń pole hasło użytkownika, pozostawiając je puste
4. Zaznacz checkbox "Nie wylogowuj mnie"
5. Kliknij przycisk "Zaloguj się"
   
Oczekiwany rezultat:
1. Użytkownik otrzymuje komunikat „Wypełnij to pole" pod hasłem

Warunki końcowe:
1. Użytkownik jest niezalogowany


Przypadek 003 (przypadek pozytywny):
Użytkownik poprawnie loguje się do aplikacji

Warunki wstępne:
1. Użytkownik posiada aktywne konto w aplikacji
2. Otwarta strona internetowa

Kroki:
1. Kliknij "Zaloguj się"
2. Wprowadź poprawną nazwę użytkownika w polu "Nazwa Użytkownika"
3. Wprowadź poprawne hasło użytkownika w polu "Hasło"
4. Zaznacz checkbox "Nie wylogowuj mnie"
5. Kliknij przycisk "Zaloguj się"

Oczekiwany rezultat:
1. Użytkownik zostaje pomyślnie zalogowany

Warunki końcowe:
1. Użytkownik jest zalogowany
