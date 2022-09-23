---
author: [Stanislaw Baranski]
bibliography: [bibliography.bib]
csl: chicago-author-date.csl
date: September 2022
title: Predykcja typu osobowości na podstawie aktywności cyfrowej za pomocą uczenia maszynowego
reference-section-title: References
---

Szwajcarski psychiatra Carl Jung zaobserwował pojawiające się wzorce zachowań u swoich pacjentów. Zaproponował on model, który opisuje preferencje ludzkich zachowań na trzech dychotomicznych skalach [@jungPsychologicalTypes2016]. Pierwsza skala opisuje, w jaki sposób człowiek preferuje zbierać informacje, gdzie na jednym końcu skali są zmysły, a na drugim intuicja. Druga skala opisuje, w jaki sposób dana osoba preferuje podejmować decyzję, kierując się uczuciami i wartościami czy racjonalnością i prawdą. Do tego Jung zaobserwował, że każda z funkcji kognitywnych (zmysły, intuicja, uczucia, racjonalność) występuje w dwóch odmianach: introwertyczna (subiektywna, wywoływana od obserwatora) i ekstrawertyczna (obiektywna, wywoływana od obiektu), dając w sumie osiem funkcji.

Myers–Briggs Type Indicator (MBTI)[@myersGiftsDifferingUnderstanding1995] rozszerza ten model o dodatkową skalę “lifestyle” opisująca, która z funkcji (zbieranie informacji czy podejmowanie decyzji) jest uzewnętrzniana przez człowieka. Niektórzy uzewnętrzniają zbieranie informacji - mówimy o nich, że dążą do spójności. Inni natomiast uzewnętrzniają podejmowanie decyzji - mówimy o nich, że są decyzyjni. Model MBTI wprowadza wygodne kodowanie typów osobowości za pomocą czterech liter I/E, S/N, F/T, oraz P/J . Pierwsza określa preferencje danej osoby do czerpania energii ze świata wewnętrznego (introwertyk) lub zewnętrznego (ekstrawertyk). Druga określa, czy dana osoba preferuje czerpać informacje za pomocą zmysłów (ang. senses) bądź intuicji (ang. intuition). Trzecia określa preferencje podejmowania decyzji, bazując głównie na uczuciach, wartości, etyce, dążeniu do harmonii (ang. feeling), czy raczej logiki, racjonalności, spójności, dążenia do prawdy (ang. thinking). Czwarta litera (P lub J) określa, która funkcja jest dominująca, zbieranie informacji (ang. perceiving), czy podejmowanie decyzji (ang. judging). Powstaje w ten sposób 16 typów osobowości, każdy określany czterema literami np. INTJ, ESFP, ISFP, ENFJ.

Model MBTI często nazywany jest pseudonauką z trzech głównych powodów:

1. Krytykuje się jego nienaukowe metody badawcze oraz sam sposób powstania modelu, który bazuje na niepotwierdzonych teoriach Carla Junga, a nie na empirycznych obserwacjach świata metodami naukowymi [@chalmersWhatThisThing2013].
2. Ponad 30% badań nad modelem jest prowadzonych przez jedną fundację, która czerpie zyski z popularności modelu poprzez sprzedaż szkoleń oraz narzędzi.
3. Brakuje mu skali neurotyczności, która uważana jest za cechę osobowości niezależną od pozostałych funkcji [@grantMBTIIfYou2013].  
4. Wykazuje niską statystyczną rzetelność. Wielokrotne wykonanie testu w odstępie pięciu tygodni skutkuje innym typem osobowości z 50% prawdopodobieństwem [@pittengerMeasuringMBTIComing1993].

Z tego powodu naukowcy stworzyli nowy model, oparty o empiryczne obserwacje oraz naukowe metody badawcze. Model Wielkiej piątki (ang. Big Five) powstał dzięki zebraniu ponad czterech tysięcy przymiotników określających ludzką osobowość [@allportTraitnamesPsycholexicalStudy1936], a następnie pogrupowaniu ich oraz zredukowaniu do pięciu niezależnych skal: ekstrawersji (ang. extraversion), otwartości na doświadczenie (ang. openness to experience), ugodowości (ang. agreeableness), sumienności (ang. conscientiousness), neurotyczności (ang. neuroticism).

Okazuje się, że pięć skal modelu BigFive, posiada zaskakująco wysoką korelację z funkcjami kognitywnymi MBTI. Skala ekstrawersji (E) pozostaje taka sama, skala otwartości (O) posiada wysoką korelację z typem intuicyjnym (I), skala ugodowości(A) ze skalą kierowania się uczuciami(F), skala sumienności (C) z typem uzewnętrzniania decyzyjności (J), natomiast skala neurotyczności nie posiada swojego odpowiednika w modelu MBTI.

BigFive uogólnia model MBTI przez wprowadzenie skali dla każdej cechy. W BigFive mówimy, że osoba jest w 54% ekstrawertykiem, podczas gdy w MBTI mogliśmy jedynie powiedzieć, że osoba jest typu ekstrawertyka. O ile model BigFive wydaje być się bliższy rzeczywistości, w praktyce łatwiej operować jest na typach osobowości. 

Dlatego, najpopularniejszy serwis do badania typu osobowości www.16personalities.com, korzysta zarówno z BigFive, jak i MBTI[^NERIS]. Tworzy on psychometryczny model przy użyciu pięciu cech BigFive, a następnie w zależności czy dana cecha była większa lub mniejsza od 50%, kategoryzuje wynik do 16 typów osobowości znanych z modelu MBTI. Dodatkowo rozszerza model o skale neurotyczności, tworząc w ten sposób 32 typów osobowości.

Pomimo że istnieje wiele innych modeli opisujących wzorce ludzkich zachowań — przykładowo, Enneagram, Socionics, MAPP3, HEXACO, Objective Personality — modele MBTI/BigFive cieszą się największą popularnością.

---

Znajomość typów osobowości pozwala na lepsze poznanie zarówno samego siebie, jak i innych ludzi. Każdy typ osobności przejawia zestaw silnych i słabych stron. Z tego faktu, korzystają agencję HR, oraz kadry zasobów ludzkich, początkowo w procesie rekrutacji, a następnie w procesie tworzenia dopasowanych zespołów. W konsekwencji czego oszczędzają zarówno pieniądze, jak i frustrację kandydata, oraz wszystkich współpracowników. 
Przykładowo, badanie [@capretzMakingSenseSoftware2010] sugeruje, że wymagane kompetencje, w branży IT, na pozycje:

- **analityka systemowego**, odpowiadają silnym stronom typów E\_F\_, np. ENFJ, ESFP;
- **architekta**, odpowiadają silnym stronom typów \_NT\_, np. INTJ, ENTP;
- **programisty**, odpowiadają silnym stronom typów IST\_, np. ISTJ, ISTP;
- **testera**, odpowiadają silnym stronom typów \_S\_J, np. ISTJ, ESFJ;
- **inżyniera utrzymania**, odpowiadają silnym stronom typów \_S\_P, np. ISTP, ESFP;

Innym przykładem jest PrinciplesUs[^PrinciplesUs] stworzone przez Ray Dalio oraz Adam Grant. Narzędzie pozwala na lepsze zrozumienie siebie oraz współpracowników, a co za tym idzie, poprawę wydajności w pracy. PrinciplesUs koordynuje proces podejmowania kolektywnych decyzji; każda decyzja, opinia, argumentacja, opatrzona jest dodatkową informacją o danym typie osobowości, dając szerszą informacje o danej wypowiedzi.

---

Wyznaczenie typu osobowości najczęściej sprowadza się do samodzielnego wykonania kwestionariusza online, przykładowo https://www.16personalities.com, który wyznacza nasz typ na podstawie udzielonych odpowiedzi. Samobadanie posiada wiele wad:

1. Pytania często są niejednoznaczne, a co za tym idzie udzielone na nie odpowiedzi.
2. Pytania w testach tłumaczone są na różne języki. Powoduje to, że sens pytania często różni się od oryginału. 
3. Badani często nie znają samych siebie na tyle dobrze, aby poprawnie odpowiedzieć na zadane im pytania.
4. Samobadanie podatne jest wiele błędów poznawczych, zwłaszcza heurystyka dostępności, która sprawia, że odpowiedzi badanych odzwierciedlają ich aktualny stan, a nie powtarzające się przez lata wzorce zachowań.
5. Badani porównują się z sobą z przeszłości. Powoduje to przekonanie, że skoro kiedyś byłem bardziej intowertyczny to teraz jestem ekstrawertykiem.
6. Badani porównują się z osobami ze swojego najbliższego otoczenia, a nie z ogólem społeczeństwa. Przykładowo, introwertyczna osoba, otaczająca się silnie introwertycznymi osobami może mieć poczucie bycia ekstrawertykiem.
7. Badani mogą chcieć odtworzyć obraz swojego idealnego ja [@SelfdiscrepancyTheory2022], odpowiadając na pytania tak jak chcieliby być odbierani, a nie jak faktycznie się zachowują (tzw. efekt wanna-be).

Istnieje wiele metod pozbycia się wymienionych błędów poznawczych. Jedną z nich jest skonstruowanie pytań w taki sposób, aby badany nie domyślał się, jaki aspekt jego osobowości jest oceniany. Inną metodą jest wykonywanie oceny przez wyspecjalizowanego operatora. Inną metodą jest wykonywanie testów grupowo i dochodzenie do decyzji metodą konsensusu.

---

W tym badaniu proponujemy nową metodę, pozbawioną ludzkich błędów poznawczych, pozwalającą na predykcje typu osobowości za pomocą uczenia maszynowego na podstawie aktywności cyfrowej.

Co więcej, w naszym narzędziu predykcja dotyczyć będzie, nie samych czterech liter typu osobowości (jak ma to miejsce w innych tego typu metodach [@amirhosseiniMachineLearningApproach2020; @hernandezPredictingMyersBriggsType2017]), ale poszczególnych funkcji kognitywnych. Na poziomie funkcji kognitywnych, istnieje dużo większa różnica, pomiędzy typami INTJ i INTP, niż np, INTJ i ENTJ. Czwarta litera typu, jest traktowana specjalnie i tak samo powinna być traktowana podczas predykcji. Oczekujemy, że predykcja na poziomie każdej funkcji kognitywnej, osiągnie dużo lepsze rezultaty niż predykcja na poziomie samych liter.

Celem badania jest stworzeniu narzędzia uczenia maszynowego do predykcji typu osobowości na podstawie aktywności cyfrowej. Aktywnością cyfrową mogą być polubienia na Facebooku, obserwacje na Tweeterze, posty na social media, re-tweety, zdjęcia na Instagramie, a nawet prywatne korespondencję. Każda z informacji wymaga dobrania innego algorytmu. 

Docelowo powstać ma usługa certyfikująca psychometryczny typ osobowości badanej osoby, który następnie może zostać użyty zarówno przez rekruterów do znalezienia odpowiedniego kandydata, jak i kandydatom dopasowanie odpowiednich stanowisk pracy.

Typy osobowości są wyjątkowo wrażliwą informacją personalną, dlatego nasz serwis gwarantować będzie prywatność przez zastosowanie nieświadomych obliczeń, oraz dowodów wiedzy zerowej.

---

##### Tezy badawcze:

1. Predykcja typu osobowości za pomocą uczenia maszynowego osiąga wyższą rzetelność statystyczną niż metody samobadania.
	- Wykonanie predykcji w kilkutygodniowych odstępach czasu nie powinno wpłynąć na zmianę predykcji typu.

2. Predykcja typu osobowości za pomocą uczenia maszynowego osiąga nie gorszą dokładność statystyczną niż metody samobadania.
	- Wykonanie predykcji za pomocą ML powinno odzwierciedlać faktyczny typ danej osoby. Gdzie faktyczny typ definiowany jest przez silniejsze rezonowanie z opisem danego typu w porównaniu z opisami innych typów.
- Predykcja typu osobowości za pomocą ML powinna przewidywać typ wykonany samo badaniem z dokładnością do 0.2.

##### State-of-the-art:
- [Recent Trends in Deep Learning Based Personality Detection](https://arxiv.org/pdf/1908.03628.pdf)

- [Predicting Myers-Briggs type indicator with text]()

- [Machine learning approach to personality type prediction based on the myers–briggs type indicator®](https://www.mdpi.com/2414-4088/4/1/9)

- [Personality Type Based on Myers-Briggs Type Indicator with Text Posting Style by using Traditional and Deep Learning](https://arxiv.org/abs/2201.08717)

- [Natural Language Processing | Classification Models | Scikit Learn | NLTK | Sentiment Analyzer | Pipeline | Imbalance Learn | TF-IDF](https://github.com/esharma3/myers-briggs-personality-prediction)

- [MBTI Personality Classifier](https://github.com/TGDivy/MBTI-Personality-Classifier)

- [Social BERTerfly](https://github.com/MLH-Fellowship/Social-BERTerfly)

##### Zadania do wykonania:
 
 1. Przegląd literatury.
 2. Zbadanie sposobów typowania przez wytrenowanych typologów.
 3. Zbadanie korelacji pomiędzy modelami MBTI/BigFive/Enneagram
 4. Zebranie zbioru treningowego z wymienionych poniżej źródeł
	 1. Zbudowanie scraperów/parserów.
	 2. Oczyszczenie danych.
	 3. Dodanie niepewności do zbioru uczącego
4. Przetestowanie wielu metod uczenia maszynowego.
5. Wzmocnienie modelu uczenia maszynowego sposobami typologów.


##### Zbiory uczące:

- [https://www.kaggle.com/datasets/datasnaek/mbti-type](https://www.kaggle.com/datasets/datasnaek/mbti-type)

- [https://www.personality-database.com/](https://www.personality-database.com/)

- [https://www.personalitycafe.com/forums/](https://www.personalitycafe.com/forums/)

- [https://www.reddit.com/r/mbti/](https://www.reddit.com/r/mbti/)

- [https://www.reddit.com/r/mbtimemes/](https://www.reddit.com/r/mbtimemes/)

- [https://www.reddit.com/r/intj/](https://www.reddit.com/r/intj/)

- [https://www.reddit.com/r/INTP/](https://www.reddit.com/r/INTP/)

- każdy typ ma swojego subreddita

[^NERIS]: https://www.16personalities.com/articles/our-theory
[^PrinciplesUs]: https://principlesus.com