# Basketbola spēles rezultāta prognozēšana

## Ievads
### Problēmas nostādne
### Darba un novērtēšanas mērķis

## Līdzīgo risinājumu pārskats
| Nr. | Risinājuma nosaukums | Īss apraksts | Svarīgākās iezīmes | Ierobežojumi |
| - | - | - | - | - |
| 1. | Forebet [1] | Bezmaksas prognozes vairākiem sporta veidiem izmantojot matemātiskos algoritmus, mašīnmācīšanos un mākslīgo intelektu, pamatojoties uz statistiku. | <li>Izmanto mākslīgo intelektu uz komandas snieguma rādītājiem, vēsturiskajiem datiem, spēlētāju statistiku un viens pret otru (head to head) datiem.</li><li>Var redzēt iepriekšējos spēļu rezultātus starp abām komandām (head to head).</li><li>Ir apskatāmi citu spēļu dati pret pārējām komandām.</li><li>Var salīdzināt prognozes rezultātus (vai prognoze piepildījās/kāds bija īstais rezultāts).</li><li>Var meklēt spēles kārtojot pēc valstīm un līgām.</li> | <li>Dati par laikapstākļiem nav noderīgi basketbolam (ja vien spēles nenotiek iekštelpu laukumos).</li><li>Tendences ir pieejamas tikai par futbolu nevis par basketbolu.</li> |
| 2. | Progsport [2]  | Platforma, kas ģenerē bezmaksas prognozes galvenokārt basketbolam, piedāvājot ieskatu, piemēram, uzvaras/zaudējuma iespējamību, punktu starpību un kopējo punktu skaitu spēlē. | <li>Salīdzināšana ar viņu modeļiem, ar "grāmatu" modeļiem kas ir no NBA partneriem, kā arī salīdzinājuma rezultējošā prognoze</li><li>Priekš saprotošiem lietotājiem parādīti specifiski ietekmējoši faktori uz rezultātiem</li> | <li> Nav moderns izskats mājaslapai </li><li> Nevar salīdzināt jebkuru komandu ar jebkuru - tikai parāda prognozes spēlēm kas notiks drīzumā</li>|
| 3. | Lineāras regresijas modeļu lietošana prognozešanai [3]| Zinātniskais papīrs kas apraksta basketbola rezultātu prognozēšanu izmantojot regresijas, analīzes un Puasona modeļus. | <li>Uz datiem balstīta precizitāte izmantojot regresijas analīzes un Puasona modeļus ļauj prognozēt, pamatojoties uz stingriem un uzticamiem datiem.</li><li>Pielāgojamība kas ļauj pielāgot konkrētām līgām vai komandām, pielāgojot parametrus, pamatojoties uz kontekstu (piemēram, mājas/izbraukuma spēles, traumu ietekme, vēsturiskie savstarpējie rezultāti).</li><li> Kvantifikējama nenoteiktība kas tiek iegūta ar varbūtības metodēm kas ļauj modelim nodrošināt ticamības intervālus ap prognozēm, sniedzot lietotājiem ieskatu par iespējamo rezultātu mainīgumu.</li> | <li> Ja tiek izmantots pārāk daudz vēsturisko datu vai pārāk daudz mainīgo, tad modelis var kļūt pārāk sarežģīts, iespējams, pārmērīgi pielāgojot datus.</li><li> Lai saglabātu precizitāti, modeļiem ir pastāvīgi jāatjaunina jaunākie dati (piemēram, pašreizējā spēlētāja forma, komandas izmaiņas, savainojumi utt.). Ja prognozes netiek regulāri atjauninātas, tās var kļūt novecojušas un mazāk ticamas.</li>|
| 4. | - | - | - | - |
| 5. | - | - | - | - |

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
     5. Salīdzināt patieso spēles rezultātu ar prognozi.
     6. Atlasīt spēles pēc basketbola kluba un līgas.
     7. Izrakstīties no profila.
5. Administratora tiesības.
     1. Veikt visas darbības, ko spēj reģistrēts lietotājs.
     2. Atjaunot spēļu grafiku.
         1. Pievienot jaunas spēles starp komandām.
         2. Pievienot patiesos spēļu rezultātus (norādīt uzvarētāju un punktu skaitu).
     3. Veikt darbības ar reģistrēto lietotāju profiliem.
         1. Dzēst/deaktivizēt/aktivizēt reģistrētu lietotāju profilus.
         2. Apskatīt reģistrēto lietotāju statistiku (kuras spēles viņiem visvairāk interesē - pēc skatījumu skaita).
### Algoritms
### Konceptu modelis
![Konceptu modelis](https://i.ibb.co/ZNDfQwL/PROLAB2-drawio.png)
### Tehnoloģiju steks
### Programmatūras apraksts

## Novērtējums
### Novērtēšanas plāns
### Novērtēšanas rezultāti

## Secinājumi

## Informācijas avoti
1. https://www.forebet.com/en/what-is-forebet
2. https://www.progsport.com/
3. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1736184
4.
5.
