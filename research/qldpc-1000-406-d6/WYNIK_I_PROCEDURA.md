# MathemaSpace: dokładny wynik dla opublikowanego kodu kwantowego

Data badania: 28 października 2026.

**Wynik:** dla konkretnych macierzy kodu `[[1000,406,≤6]]` autorstwa @hirobumii wykazaliśmy `d_X=d_Z=d=6`. Publiczny katalog podawał świadectwa `d≤6`, a przy certyfikacie informację „none yet”. Uzupełnieniem jest dowód, że nie istnieje niezerowy błąd z zerowym syndromem o wadze od 1 do 5. Kod i operatory o wadze 6 nie są naszym wynalazkiem.

## Co jest nowe, a co było znane

- Znane: konstrukcja lifted product, grupa `C5⋊C20`, parametry 1000 i 406, macierze kontroli, waga kontroli 8 i operatory o wadze 6. Autor kodu: **@hirobumii**, PR #3863.
- Otrzymane w tym badaniu: jawny dowód dolnej granicy 6 dla dokładnie tych macierzy, sprawdzalny certyfikat i osobny weryfikator.
- Status nowości: w sprawdzonym wpisie, notatce autora, PR i komentarzach nie znalazłem takiego dowodu. Wyszukiwanie parametrów i identyfikatora nie znalazło wcześniejszego certyfikatu. To **kandydat na nowy wynik certyfikacyjny dla znanej instancji**, nie potwierdzone pierwszeństwo światowe ani nowa ogólna metoda matematyczna.
- Nie dowiedziono przewagi MathemaSpace nad pracą bez silnika. Drugi program potwierdza matematykę także bez niego. Jeden poprawny wynik nie dowodzi uniwersalnej poprawności całego procesu odkrywania.

## Znaczenie praktyczne

W standardowym modelu stabilizatorowym odległość 6 oznacza możliwość wykrycia dowolnego niezerowego błędu Pauliego o wadze do 5 oraz istnienie procedury korygującej dowolne błędy o wadze do 2. Nie jest to pomiar działania procesora, czas dekodowania ani ocena odporności na błędy obwodu. Wykluczenie wszystkich małych błędów daje mocniejsze uzasadnienie niż samo to, że losowa heurystyka nie znalazła kontrprzykładu.

## Proces: zależności przed poszukiwaniem reprezentacji

1. **Zamrożenie obiektu.** Ustalamy commit i sumę SHA-256 wejścia. Nie pracujemy na samej etykiecie `[[1000,406,6]]`, bo etykieta nie jest dowodem.
2. **Odtworzenie relacji.** Z definicji grupy i generatorów budujemy wszystkie 300 kontroli w każdym sektorze. Wykazujemy zgodność przestrzeni wierszy z 297 opublikowanymi kontrolami. Skrócenie macierzy nie może zmienić rozważanego jądra.
3. **Podział po strukturze, nie po dziedzinie danych.** Pierwsze 900 współrzędnych to krawędzie VV w trzech rozłącznych blokach syndromu; ostatnie 100 to CC, których każdy wybór wytwarza po dwa końce w każdym z trzech bloków.
4. **Minimalne zależności potrzebne do dolnej granicy.** Potrzebujemy: braku cykli VV krótszych niż 6, braku małych zbiorów niezmienniczych CC, kosztu co najmniej 5 krawędzi dla jednego CC oraz niezgodności warunków dla pary CC. Te cztery zobowiązania są osobno sprawdzane.
5. **Dostarczona silnikowi reprezentacja.** Podajemy 100 stanów grupy, sześć przejść i obserwacje `j mod m`. Sprawdzamy `m=1,2,4,5,10,20`. V13 buduje ilorazy i weryfikuje zachowanie przejść oraz obserwacji.
6. **Zbyt mało informacji.** Ilorazy do `m=10` zachowują swoje obserwacje, ale dają za słabą granicę długości ścieżek. Nie nazywamy tego dowodem niemożliwości zadania.
7. **Wystarczający iloraz.** `m=20` daje sumy kosztów VV co najmniej 7 i 5. Użycie tych wartości wymaga dowodu, że obraz każdej ścieżki jest ścieżką tej samej długości. Granica działa w kierunku: odległość w ilorazie ≤ odległość oryginalna.
8. **Dowód globalny.** Rozpatrujemy wszystkie możliwe liczby CC w błędzie wagi ≤5: 0,1,2,3,4,5. Każdy przypadek prowadzi do sprzeczności. Pełny argument jest w `PROOF.md`.
9. **Górna granica.** Oryginalne operatory wagi 6 sprawdzamy algebraicznie: zerowy syndrom i brak przynależności do przestrzeni stabilizatorów. Z `d≥6` i `d≤6` otrzymujemy `d=6`.
10. **Osobny sprawdzian.** Drugi program buduje kolumny zamiast wierszy, używa innej eliminacji GF(2), sprawdza brak krótkich cykli przez dwudzielność i wspólnych sąsiadów, wylicza odległości bez ilorazu i sprawdza wszystkie 4950 par CC. Oba programy zgadzają się co do wyniku.

## Co dokładnie zrobił silnik

Użyty oryginał to `V13.py`, SHA-256:

`d7b7a130d12432b6a6add9c65fee6195a8353cab21d335dcdc61600095c2ea54`.

Wywołaliśmy `minimize_moore` 12 razy oraz `verify_bridge` 12 razy. Pełne argumenty i odpowiedzi wszystkich 24 wywołań są w JSONL. Rodzinę obserwacji oraz twierdzenie o małych błędach przygotował asystent. V13 nie został przedstawiony jako generator dowolnych praw naukowych. W tym badaniu nie wykonywaliśmy V12, V14 ani CORE013; ich kopie w części prywatnej są materiałem pomocniczym wyraźnie oznaczonym jako nieużyty w dowodzie.

## Zakres zadania z GitHuba

Wybrano otwarte [#4162](https://github.com/unitaryfoundation/qldpc-challenge/issues/4162), dotyczące kodów o dużej liczbie kubitów logicznych. Sprawdzono jego stan: otwarte, bez komentarzy. Istniejący kod `[[1000,406,≤6]]` pasuje do wskazanego obszaru. Nasz wynik uzupełnia jego certyfikację, ale **nie stanowi nowego kodu, nowego punktu Pareto ani zamknięcia całego zgłoszenia**.

Pierwszy pomysł z prostym produktem hipergrafowym został odrzucony: znana konstrukcja dawała gorszy kod niż już istniejący wpis. To odrzucenie oraz pozostałe sprawdzone tropy zapisano w `RESEARCH_LOG.json`. Nie oznaczamy ich jako odkryć.

## Jak odtworzyć wynik bez wiedzy z tej rozmowy

W części pełnej:

```sh
python3 reproduce.py
python3 independent_check.py
```

W części publicznej:

```sh
python3 independent_check.py --math-only
```

Potrzebny jest Python ≥3.10. Bez instalowania bibliotek, internetu i kont. Pełna paczka ma też pojedynczy plik `.py`, który rozpakowuje wszystkie źródła i wykonuje oba programy. Końcowe wyniki, sumy plików i log odtworzenia są dołączone. Dowód nie polega na pełnym przeglądzie około `binom(1000,5)` podpór; wykorzystuje lemat grafowy wykluczający je jednocześnie.

## Prywatność i kompletność

Paczka **PUBLIC** zawiera publiczny kod kwantowy, nowy tekst dowodu, mój niezależny weryfikator i wyniki matematyczne. Nie zawiera źródeł prywatnego silnika, maili ani zawartości Drive. Można ją pokazać publicznie z zachowaniem dołączonych informacji o autorze i licencji materiału z repozytorium.

Paczka **PRIVATE_FULL** oraz pojedynczy pełny `.py` zawierają oryginalne kody MathemaSpace i pełne ślady ich wywołań. Traktuj je jako prywatne; sam wynik matematyczny nie wymaga ujawnienia tych kodów.

Kompletność dotyczy tego wyniku: wejścia, użytego V13, obu programów, wszystkich 24 wywołań silnika, odrzuconych ilorazów, dowodu, certyfikatu, środowiska i procedury. To nie jest kopia wszystkich Twoich kont, wszystkich poprzednich rozmów ani całego stanu wewnętrznego modelu. Nie wykonano nowego pełnego audytu Gmaila, Drive i wszystkich notatników Colab w ramach tego eksperymentu. Wstępne wyszukiwania i pierwszy test struktury nie mają pełnego surowego dziennika każdej czynności; luka jest jawna. Cały rdzeń końcowego wyniku odtwarza się z dołączonych źródeł.

## Źródła i sprawdzenie nowości

- [Zamrożony kod](https://github.com/unitaryfoundation/qldpc-challenge/blob/9587d1aa54e98aa49caacf4a2cb358424e70160e/codes/1000-406-6.json) i [notatka autora](https://github.com/unitaryfoundation/qldpc-challenge/blob/9587d1aa54e98aa49caacf4a2cb358424e70160e/notes/1000-406-6.md).
- [PR #3863 i przegląd](https://github.com/unitaryfoundation/qldpc-challenge/pull/3863): opublikowano `upper_bound`; komentarz zatwierdzający nie zawiera dowodu dolnej granicy.
- [Aktualna karta kodu](https://qecchallenge.com/codes/1000-406-6.html): `certificate none yet`, oba sektory `≤6` w dniu sprawdzenia.
- Panteleev–Kalachev, [arXiv:2111.03654v2](https://arxiv.org/abs/2111.03654v2): znane podstawy nieabelowego lifted product. Nie przypisujemy sobie tej konstrukcji.
- Bhardwaj i in., [arXiv:2607.28795v2](https://arxiv.org/html/2607.28795v2): znane nieabelowe kody, reprezentacje lewa/prawa i ograniczenia odległości. Nie znaleziono tam dokładnego rozpatrywanego certyfikatu; sam brak trafienia nie dowodzi pierwszeństwa.

Stan publicznego katalogu oraz odpowiedzi API zapisano w `provenance/`. Pełny tekst prac nie jest przedrukowywany. Nie wysłano publikacji ani komentarza na GitHubie. Wynik czeka na niezależny przegląd zewnętrzny i ewentualne przyjęcie certyfikatu przez organizatorów.