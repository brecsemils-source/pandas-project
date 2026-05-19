# Pandas bibliotekas analizes projekts

Skolas projekts, kura mērķis ir izpētīt Python bibliotēku "pandas", izveidot 15 praktiskus kodu piemērus un uztaisīt vienkāršu lietotāja saskarni (GUI) datu apskatei.

## Kāpēc tieši Pandas?
Izvēlējos pandas bibliotēku, jo tā ir populārākais rīks Python vidē, kad vajag strādāt ar tabulām (piemēram, CSV vai Excel failiem). Standarta Python rīki šādiem uzdevumiem prasa rakstīt pārāk daudz koda rindiņu, bet pandas ļauj ielasīt, filtrēt un kārtot datus ar dažām komandām. Tas ievērojami paātrina darbu un palīdz vieglāk saprast datu struktūru.

## Projekta struktūra
* main.py - Galvenā programma ar CustomTkinter vizuālo logu, kur var apskatīt datus.
* students.csv - Testa dati (skolēnu vārdi, vecumi, klases un atzīmes), kas tiek izmantoti piemēros.
* requirements.txt - Vajadzīgās bibliotēkas (pandas, customtkinter).
* example_01_read_csv.py līdz example_15_plot.py - 15 atsevišķi faili, kur katrā ir parādīta viena konkrēta funkcija ar komentāriem.

## Izpētītās 15 funkcijas

1. pd.read_csv() - Izmanto, lai ielādētu datus no CSV faila un pārvērstu tos DataFrame objektā.
2. pd.DataFrame() - Ļauj manuāli izveidot datu tabulu no Python sarakstiem vai vārdnīcām.
3. df.head() - Parāda pirmās 5 tabulas rindiņas, lai ātri apskatītu faila saturu.
4. df.tail() - Parāda pēdējās 5 tabulas rindiņas, lai pārbaudītu faila beigas.
5. df.info() - Sniedz tehnisko informāciju par tabulu (kolonnu nosaukumi, datu tipi, aizpildītās vērtības).
6. df.describe() - Aprēķina pamata statistiku ciparu kolonnām (vidējo vērtību, min, max, mediānu).
7. df.sort_values() - Sakārto tabulas rindiņas pēc izvēlētās kolonnas (augošā vai dilstošā secībā).
8. df[df['kolonna'] > x] (Filtrēšana) - Atlasa tikai tās rindiņas, kas atbilst konkrētam nosacījumam.
9. df.groupby() - Sagrupē datus pēc kādas pazīmes (piemēram, pa klasēm) un aprēķina kopējos rādītājus.
10. pd.merge() - Apvieno divas dažādas tabulas vienā, izmantojot kopīgu kolonnu (ID).
11. df.fillna() - Aizpilda tukšās vai trūkstošās vērtības tabulā ar norādīto tekstu vai skaitli.
12. df.dropna() - Izmet no tabulas visas rindiņas, kurās trūkst kādi dati.
13. df.apply() - Ļauj izpildīt kādu specifisku funkciju vai formulu uzreiz visai kolonnai.
14. df.to_csv() - Saglabā apstrādāto tabulu atpakaļ jaunā CSV failā.
15. df.plot() - Izveido vienkāršu vizuālu grafiku vai diagrammu, balstoties uz tabulas datiem.

## Secinājumi par Pandas

Ieguvumi:
Ļoti ātri strādā ar lieliem datu apjomiem. Tam ir milzīga dokumentācija un internetā ir viegli atrast risinājumus kļūdām. Viena rinda koda var aizstāt veselu ciklu, ko vajadzētu rakstīt parastā Python.

Ierobežojumi:
Patērē diezgan daudz operatīvās atmiņas (RAM), jo visi dati tiek ielādēti uzreiz atmiņā. Sākumā ir grūti pierast pie sintakses (piemēram, loc un iloc atšķirībām), un kļūdu paziņojumi mēdz būt ļoti gari un grūti salasāmi.