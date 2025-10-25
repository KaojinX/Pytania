Quiz Python
Opis

Jest to prosty program do wykonywania testów w konsoli. Program umożliwia zadawanie pytań użytkownikowi i liczenie wyników. Jest skalowalny – można łatwo dodawać nowe zestawy pytań w formacie JSON, a program automatycznie je odczyta i włączy do testu.

Program działa w pętli aż do momentu, gdy użytkownik odpowie na określoną liczbę pytań zdefiniowaną w pliku config.JSON. Na koniec oblicza wynik w procentach i zapisuje go do pliku tekstowego z nazwą użytkownika.

Struktura plików

main.py – główny plik programu, uruchamia quiz

config.JSON – ustawienia testu: liczba pytań do zaliczenia i próg procentowy

Pytania.JSON, Pytania2.JSON, … – pliki z pytaniami w formacie JSON

Każdy plik z pytaniami powinien mieć strukturę:

{
    "questions": [
        {
            "id": 1,
            "question": "Treść pytania",
            "options": ["Opcja1", "Opcja2", "Opcja3", "Opcja4"],
            "answer": "Poprawna odpowiedź"
        }
    ]
}


💡 Uwaga: wpisy w polu options nie są wymagane do działania programu, ale mogą być użyte w przyszłych aktualizacjach do prezentacji opcji użytkownikowi.

Konfiguracja (config.JSON)

Przykład:

{
    "config": {
        "amountofquestions": 5,
        "needtopass": 60
    }
}


amountofquestions – liczba pytań, które użytkownik ma rozwiązać

needtopass – minimalny procent poprawnych odpowiedzi, aby zaliczyć test

Zasady działania

Program losuje pytania ze wszystkich dostępnych plików JSON z pytaniami.

Użytkownik odpowiada na pytania w konsoli.

Program sprawdza odpowiedź i zlicza poprawne odpowiedzi.

Proces powtarza się aż do osiągnięcia liczby pytań określonej w config.JSON.

Na koniec program oblicza procent poprawnych odpowiedzi i zapisuje wynik do pliku <nazwa_użytkownika>.txt.

Skalowalność

Aby dodać nowe pytania, wystarczy utworzyć kolejny plik JSON w tym samym folderze.

Program automatycznie odczyta wszystkie pliki z pytaniami, ignorując pliki konfiguracyjne.

Nie jest wymagane wypełnianie pola options, ale można je dodać, aby w przyszłości wyświetlać listę możliwych odpowiedzi.

Instrukcja uruchomienia

Skopiuj wszystkie pliki (program, pliki z pytaniami i config.JSON) do jednego folderu.

Otwórz terminal lub konsolę w tym folderze.

Uruchom program:

python main.py


Odpowiadaj na pytania w konsoli.

Po zakończeniu testu wynik zostanie zapisany w pliku <nazwa_użytkownika>.txt.
