# Basketbola spēles rezultāta prognozēšana

## Ievads
### Problēmas nostādne
Basketbola spēļu rezultātu prognozēšana ir diezgan sarežģīta lieta, jo jāņem vērā ļoti daudz dažādu faktoru, un ne vienmēr visi ir skaidri saprotami vai viegli analizējami. Parasti, kad cilvēki cenšas prognozēt rezultātus, tas vairāk balstās uz intuīciju par pagājušajām spēlēm, kas parasti noved pie kļudainām prognozēm un ja tādas ir liktas - sliktām likmēm. Šī problēma ir īpaši aktuāla profesionālajā sportā, kur precīza prognoze var būt svarīga gan komandas stratēģijai, gan biznesa lēmumiem, piemēram, saistībā ar totalizatoriem vai sponsoriem.

### Darba un novērtēšanas mērķis
Šī darba galvenais mērķis ir izpētīt un izveidot prognozēšanas modeli, kas varētu efektīvi analizēt datus par pagājušām spēlēm un prognozēt spēles rezultātu ar pēc iespējas lielāku precizitāti. Novērtēšanas ietvaros būtu nepieciešams novērtēt cik precīzi modelis prognozē balstoties uz datiem un apmācības pieeju.

## Līdzīgo risinājumu pārskats
| Nr. | Risinājuma nosaukums | Īss apraksts | Svarīgākās iezīmes | Ierobežojumi |
| - | - | - | - | - |
| 1. | Forebet [1] | Bezmaksas prognozes vairākiem sporta veidiem izmantojot matemātiskos algoritmus, mašīnmācīšanos un mākslīgo intelektu, pamatojoties uz statistiku. | <li>Izmanto mākslīgo intelektu uz komandas snieguma rādītājiem, vēsturiskajiem datiem, spēlētāju statistiku un viens pret otru (head to head) datiem.</li><li>Var redzēt iepriekšējos spēļu rezultātus starp abām komandām (head to head).</li><li>Ir apskatāmi citu spēļu dati pret pārējām komandām.</li><li>Var salīdzināt prognozes rezultātus (vai prognoze piepildījās/kāds bija īstais rezultāts).</li><li>Var meklēt spēles kārtojot pēc valstīm un līgām.</li> | <li>Dati par laikapstākļiem nav noderīgi basketbolam (ja vien spēles nenotiek iekštelpu laukumos).</li><li>Tendences ir pieejamas tikai par futbolu nevis par basketbolu.</li> |
| 2. | Progsport [2]  | Platforma, kas ģenerē bezmaksas prognozes galvenokārt basketbolam, piedāvājot ieskatu, piemēram, uzvaras/zaudējuma iespējamību, punktu starpību un kopējo punktu skaitu spēlē. | <li>Salīdzināšana ar viņu modeļiem, ar "grāmatu" modeļiem kas ir no NBA partneriem, kā arī salīdzinājuma rezultējošā prognoze</li><li>Priekš saprotošiem lietotājiem parādīti specifiski ietekmējoši faktori uz rezultātiem</li> | <li> Nav moderns izskats mājaslapai </li><li> Nevar salīdzināt jebkuru komandu ar jebkuru - tikai parāda prognozes spēlēm kas notiks drīzumā</li>|
| 3. | Lineāras regresijas modeļu lietošana prognozešanai [3]| Zinātniskais papīrs kas apraksta basketbola rezultātu prognozēšanu izmantojot regresijas, analīzes un Puasona modeļus. | <li>Uz datiem balstīta precizitāte izmantojot regresijas analīzes un Puasona modeļus ļauj prognozēt, pamatojoties uz stingriem un uzticamiem datiem.</li><li>Pielāgojamība kas ļauj pielāgot konkrētām līgām vai komandām, pielāgojot parametrus, pamatojoties uz kontekstu (piemēram, mājas/izbraukuma spēles, traumu ietekme, vēsturiskie savstarpējie rezultāti).</li><li> Kvantifikējama nenoteiktība kas tiek iegūta ar varbūtības metodēm kas ļauj modelim nodrošināt ticamības intervālus ap prognozēm, sniedzot lietotājiem ieskatu par iespējamo rezultātu mainīgumu.</li> | <li> Ja tiek izmantots pārāk daudz vēsturisko datu vai pārāk daudz mainīgo, tad modelis var kļūt pārāk sarežģīts, iespējams, pārmērīgi pielāgojot datus.</li><li> Lai saglabātu precizitāti, modeļiem ir pastāvīgi jāatjaunina jaunākie dati (piemēram, pašreizējā spēlētāja forma, komandas izmaiņas, savainojumi utt.). Ja prognozes netiek regulāri atjauninātas, tās var kļūt novecojušas un mazāk ticamas.</li>|

## Tehniskais risinājums
### Prasības
1. Nepiereģistrēta lietotāja tiesības.
    1. Apskatīt publiski pieejamo informāciju (mājaslapas aprakstu).
    2. Reģistrēties kā jaunam lietotājam.
    3. Pieslēgties kā esošam klietam.
3. Reģistrēta lietotāja tiesības.
     1. Apskatīt publiski pieejamo informāciju (mājaslapas aprakstu).
     2. Apskatīt spēļu grafiku.
     3. Apskatīt spēļu prognozes (punktus un rezultātu ar norādītu varbūtību).
     4. Apskatīt detalizētāku informāciju par konkrētu spēli (spēlētāju sastāvu, iepriekšēju spēļu rezultātus starp esošajām komandām - ja tādas ir bijušas).
     5. Izrakstīties no profila.
5. Administratora tiesības.
     1. Veikt visas darbības, ko spēj reģistrēts lietotājs.
     2. Atjaunot spēļu grafiku.
         1. Pievienot jaunas spēles starp komandām.
         2. Pievienot patiesos spēļu rezultātus (norādīt uzvarētāju un punktu skaitu).
     3. Veikt darbības ar reģistrēto lietotāju profiliem.
         1. Dzēst/deaktivizēt/aktivizēt reģistrētu lietotāju profilus.
         2. Apskatīt reģistrēto lietotāju statistiku (kuras spēles viņiem visvairāk interesē - pēc skatījumu skaita).

### Algoritms
1.	Ielādē un apstrādā datus no datu bāzes - nolasām spēļu datus un komandu statistiku, apvienojam tos, pārvēršot komandu nosaukumus skaitļos un pievienojot komandu sezonas datus. 
2.	Sagatavo ievaddatus un mērķus - izveido ievaddatus (komandu un spēļu statistiku) un mērķus (spēļu rezultātus), kas tiks izmantoti modeļa treniņam. 
3.	Izveido neironu tīkla modeli - konstruē modeli ar vairākiem slāņiem, kas spēj mācīties sarežģītas attiecības starp komandu statistiku un spēļu rezultātiem. 
4.	Apmāca modeli ar sagatavotajiem datiem - trenē modeli, izmantojot visus apstrādātos gadu datus, optimizējot tā spēju prognozēt spēļu rezultātus. 
5.	Saglabā un izmanto modeli prognozēm - saglabā apmācīto modeli un izmanto to, lai prognozētu spēļu rezultātus, ievadot jaunos komandu datus.

### Konceptu modelis
![Konceptu modelis](https://i.ibb.co/ZNDfQwL/PROLAB2-drawio.png)
### Tehnoloģiju steks
![Tehnologiju steks](https://i.ibb.co/gZmp4YW/Tehnolo-iju-steks-3.png)

### Programmatūras apraksts
Algoritma un modeļa izstrādē tika lietota Python programmēšanas valoda ar TensorFlow, Pandas un Numpy bibliotēkām - balstoties uz to ka bija vēlme veidot modeli ar neironu tīkliem. Priekš mājaslapas izveides tika lietotas HTML, CSS un JavaScript valodas kā arī Flask lai izveidotu mājas lapu priekš prognozes modeļa. Datu glabāšanai un lietošanai projektā tiek izmantota MySQL datu bāze un lai varētu izmantot mājaslapu jebkurš tiek lietoti PythonAnywhere pakalpojumi.

## Novērtējums
### Novērtēšanas plāns
#### Mērķis
Novērtēt basketbola spēļu prognozēšanas modeļa precizitāti (gan spēles iznākumam “kura komanda uzvarēs”, gan pašam punktu skaitam - abām komandām).
#### Ieejas mainīgie
Novērtējuma datu kopa sastāvēs no vairākiem prognozētajiem basketbola spēļu ierakstiem ar šādiem mainīgajiem:
- Prognozētais spēles iznākums (kura komanda uzvarēs).
- Prognozētā varbūtība, ka šī komanda uzvarēs.
- Prognozētais punktu skaits.
- Īstais spēles iznākums (kura komanda uzvarēs).
- Īstais spēles punktu skaits.

#### Novērtēšanas mēri
Risinājuma novērtēšanas plānā tiks pielietots prognozēšanas modeļa precizitātes koeficients, par spēles iznākumu “kura komanda uzvarēs” – cik spēles iznākumus modelis prognozēja pareizi. Modeļa novērtēšanai ir vajadzīgs arī modeļa precizitātes mērs par pašiem prognozētajiem spēles punktiem.

### Novērtēšanas rezultāti
|Modeļa numurs | Punktu prognozēšanas precizitāte (%) | Uzvarētāju prognozēšanas precizitāte (%)|
| - | - | - |
| 1. | 84.89 | 57.62|
| 2. | 82 | 62.91|
| 3. | 90.74 | 50.33|
| 4. | 90.54 | 58.28|
| 5. | 90.31 | 54.97|

![Novērtēšanas rezultāti](https://i.ibb.co/bQsb2N3/chart.png)

## Secinājumi
Var secināt, ka projekts ir izveidots pēc izvēlētās tēmas ietvariem, bet ir vietas kur varētu to pielabot un padarīt labāku. Izmantojot neirona tīklus lai varētu izveidot modeli priekš rezultātu prognozēšanas bija pareizā izvēle. Pilnviedošanai varētu uztrennēt efektīvāku modeli ar citādākiem parametriem un vairāk datiem, kas iespējams uzlabotu precizitāti prognozēm bet tas varētu prasīt savādāku pieeju un daudz lielāka līmeņa tehnoloģijas un daudz vairāk resursus.

## Informācijas avoti
1. Forebet - <https://www.forebet.com/en/what-is-forebet>
2. Progsport - <https://www.progsport.com/>
3. Lineāras regresijas piemērs ar basketbola statistiku - <https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1736184>
4. Flask dokumentācija - <https://flask.palletsprojects.com/en/stable/>
5. PythonAnywhere dokumentācija - <https://help.pythonanywhere.com/pages/>
6. MySQL dokumentācija - <https://dev.mysql.com/doc/>
7. Python 3 Dokumentācija - <https://docs.python.org/3/>
8. TensorFlow bibliotēkas dokumentācija - <https://www.tensorflow.org/api_docs>
