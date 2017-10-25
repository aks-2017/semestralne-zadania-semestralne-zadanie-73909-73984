# 1.	Softvérovo definované siete
Inicializova, kontrolova, meni a manaova správanie siete dynamicky cez rozhranie.

![alt text](https://github.com/aks-2017/semestralne-zadania-semestralne-zadanie-73909-73984/blob/master/docs/obr1.png)

Obrázok 1 Tradièná sie(v¾avo) a SDN(vpravo) [6]

Tradièné hardvérové siete nezodpovedajú neustále sa meniacim potrebám v oblasti vıpoètovej techniky a úloiska v prostrediach dátovıch centier a poskytovate¾ov sluieb. SDN (Software-Defined Networking) poskytuje lepšie monosti v takıch situáciách, kde mnohé vlastnosti vyadujú flexibilnejší a dynamickejší prístup. Vlastnosti SDN sú [10]:
* Priamo programovate¾né – sieová kontrola je priamo programovate¾ná pretoe je oddelená od smerovacích funkcií
* Agilná – oddelenie kontroly od smerovania umoòuje administrátorom dynamicky prispôsobova sieovú premávku aby spåòala meniace sa potreby
* Centrálne manaovate¾ná – sieová inteligencia je centralizovaná v SDN kontroléroch, ktoré udrujú celkovı poh¾ad na sie. 
* Programovate¾ná – umoòuje rıchlo meni konfiguráciu, manaova, zabezpeèi alebo optimalizova sie rıchlo cez automatické SDN programy, ktoré si môu ¾udia písa sami, pretoe nie sú proprietárne

Oproti tradiènej sieti je SDN sie riadená kontrolérom, ktorı má nieko¾ko rovín. Medzi základné roviny patria [10]:
* Riadiaca rovina ovláda to kam sa budú posiela správy
* Dátová rovina u len posiela pod¾a toho, èo mu riadiaca rovina povie

## 1.1.	Prostredie Mininet

Mininet je sieovı emulátor, ktorı umoòuje vytvára koncové zariadenia, prepínaèe, smerovaèe, a linky medzi nim. Mininet host sa správa rovnako ako reálna mašina a je moné sa naò pripoji pomocou SSH. Èo sa tıka OpenFlow kontrolérov, Mininet je ve¾mi flexibilnı a umoòuje prida do simulácie mnostvo typov kontrolérov. Siete Mininetu pracujú so skutoènım kódom vrátane štandardnıch sieovıch aplikácií Unix / Linux, ako aj na skutoènom jadre Linuxu a sieovom zásobníku. Hlavné funkcie nástroja Mininet sú [1]: 
* poskytuje jednoduché a lacné sieové testovacie médium pre vıvoj aplikácií nad protokolom OpenFlow
* umoòuje viacerım súbenım vıvojárom pracova nezávisle na tej istej topológii
* podporuje regresné testy na úrovni systému, ktoré sú opakovate¾né a ¾ahko zabalené
* umoòuje zloité testovanie topológie bez nutnosti prepojenia fyzickej siete
* podporuje ¾ubovo¾né vlastné topológie a obsahuje základnú sadu parametrizovanıch topológií
* je pouite¾nı mimo krabice bez programovania a tie poskytuje priamu a rozšírite¾nú Python API pre vytváranie a experimentovanie so sieami
* sluba Mininet poskytuje jednoduchı spôsob, ako dosiahnu správne správanie systému (a v rozsahu podporovanom vaším hardvérom, vıkonom) a experimentova s topológiami.

Mininet kombinuje mnohé z najlepších funkcií emulátorov a špecializovanıch simulátorov. V porovnaní s prístupmi zaloenımi na úplnej virtualizácii systému, spoloènos Mininet vyniká v [1]:
* rıchlejšom bootovaní
* umoòuje spravova stovky hostite¾ov a prepínaèov
* poskytuje väèšiu šírku pásma
* Jednoducho sa inštaluje

V porovnaní s hardvérovımi testovacími doskami, Mininet vyniká v [1]:
* je rıchlo rekonfigurovate¾nı a reštartovate¾nı

V porovnaní so simulátormi, Mininet vyniká v [1]:
* beí na reálnom, nemodifikovanom kóde vrátane aplikaèného kódu
* ¾ahko sa pripája k reálnym sieam

## 1.2.	Kontrolér

OpenFlow kontrolér je typ SDN kontroléra, ktorı pouíva OpenFlow protokol. OpenFlow kontrolér pouíva OpenFlow protokol aby spojil a konfiguroval sieové zariadenia, ako smerovaèe a prepínaèe, na nájdenie najlepšej cesty v premávke. SDN kontroléry teda u¾ahèujú riadenie siete a dokáu riadi celú komunikáciu medzi aplikáciami a zariadeniami, tak aby sa èo najefektívnejšie upravil tok premávky, tak ako je v danom momente potrebné. Keï nie je riadiaca rovina implementovaná vo firmvéri, ale je implementovaná v softvéri, administrátori dokáu manaova sie ove¾a jednoduchšie, viac dynamicky a s lepšou granularitou. OpenFlow kontrolér teda tvorí centrálnu kontrolnú jednotku v sieti, ktorá riadi všetku premávku, všetky zariadenia v sieti vykonávajú akcie tak ako od nich poaduje kontrolér a podporuje OpenFlow. [5]

### 1.2.1.	Kontrolér Ryu

Ryu poskytuje ve¾mi silnı pomer medzi jeho vıhodami a nevıhodami, v prospech vıhod. Ryu si stavia medzi jej hlavne piliere vıhod tri charakteristiky: kvalita kódu, funkcionalita a pouite¾nos. Podporuje nieko¾ko protokolov, pre správu sieovıch zariadení, tımi sú napr. Netconf, OF-config, no primárne OpenFlow vo verziách a po aktuálnu 1.5. Je napísanı v jazyku Python. [4]

## 1.3.	Protokol Openflow

Je protokol medzi kontrolérom a sieovımi zariadeniami, ako aj nástroj pre špecifikáciu logickej štruktúry siete. Pracuje v rámci TCP (Transmission Control Protocol), kde by mal poèúva na porte 6653. Môe vykona rôzne akcie [2]: 
* pridávanie, zmena alebo vyraïovanie paketov, pod¾a vopred definovanıch pravidiel a akcií
* smerovanie akceptovanıch paketov prepínaèom
* neakceptované pakety sú smerované do kontroléra, ktorı môe:
  * zmeni pravidlá smerovacej tabu¾ky na jednom alebo viacerıch prepínaèoch
  * nastavi nové pravidlá, aby tak predišiel ve¾kej komunikácií medzi prepínaèom a kontrolérom

![alt text](https://github.com/aks-2017/semestralne-zadania-semestralne-zadanie-73909-73984/blob/master/docs/obr2.png)

Obrázok 2 Openflow prepínaè [2]

Obrázok popisuje priblinú komunikáciu v rámci OpenFlow protokolu [2]: 
* SDN kontrolér komunikuje s prepínaèmi, ktoré sú kompatibilné s OpenFlow, pomocou OpenFlow protokolu beiaceho cez SSL (Secure Sockets Layer)
* kadı prepínaè sa pripojí k zariadeniam cie¾ového pouívate¾a, ktoré sú zdrojmi a cie¾mi paketovıch tokov
* kadı prepínaè má nieko¾ko tabuliek (spomenutıch vyššie), implementovanıch hardvérom alebo firmvérom, ktoré sa pouívajú na riadenie toku cez prepínaèe

## 1.4.	Prepínaè

Preposielacie zariadenie v SDN sa nazıva forwarder a pozostáva z dvoch èastí [3]:
* prietokovej tabu¾ky (flow table) obsahujúcej záznam a akciu na prijímanie aktívnych tokov
* abstrakènej vrstvy, ktorá bezpeène komunikuje s riadiacou jednotkou (kontrolérom) o novıch vstupoch, ktoré sa v danom momente nenachádzajú v tokovej tabu¾ke. 

OpenFlow prepínaè pozostáva z jednej alebo viacerıch tabuliek tokov, ktoré ukladajú záznamy pre vyh¾adanie alebo presmerovanie paketov. [3]

Po príchode paketov na OpenFlow prepínaè sa hlavièka paketu extrahuje a porovná s políèkom zhody (match field) z tabu¾ky tokov. Ak sa zhoduje hlavièka paketu s políèkom v tabu¾ke, tak prepínaè pouije príslušnú sadu inštrukcií spojenú s danım tokom. V prípade, e sa nenájde iadna zhoda s tabu¾kou tokov, tak nasledujúca akcia prepínaèa bude závisie od inštrukcií definovanıch v tabu¾ke chıbajúcich tokov (table-miss flow entry), napr. zahodenie paketu. [3]
 
## 1.5.	Dynamické adaptívne streamovanie

Hlavná myšlienka Dynamic adaptive streaming (MPEG-DASH) je rozdeli súbor s mediálnym obsahom na segmenty, ktoré môu by enkódované na rôznych bitratoch. Segmenty sú poskytnuté na webovom servery a môu by stiahnuté cez HTTP (GET request). Segmenty sú referencované pomocou URL (definované v RFC3986). Segmenty sa ïalej môu deli aj na menšie subsegmenty. Moné obsahy segmentov [8] [9]: 
* SegmentBase - najzákladnejšia reprezentácia
* SegmentList – obsahuje zoznam SegmentURL
* SegmentTemplate – vyskladáva zoznam segmentov

Na vysvetlenie vzahov medzi segmentami, MPEG-DASH zadefinovalo Media Presentation Description (MPD). MPD je XML súbor, ktorı reprezentuje rôzne vlastnosti mediálneho obsahu a jednotlivé segmenty pre kadú vlastnos. Táto štruktúra prezentuje spojenie medzi segmentami a bitratom. [8] [9]

Na obrázku je moné vidie princíp MPEG-DASH. Server rozdelí mediálny obsah na segmenty podla kvality na Low, Medium a Best. Klient pod¾a aktuálneho bandwidthu a CPU kapacity vyberá medzi kvalitou mediálneho obsahu. [8] [9] 

![alt text](https://github.com/aks-2017/semestralne-zadania-semestralne-zadanie-73909-73984/blob/master/docs/obr3.png)

Obrázok 3 Princíp fungovania MPEG-DASH [8]


# 2.	Návrh

## 2.1.	Topológia
V našom prevedení budeme pouíva rovnakú topológiu, aká bola uvedená v èlánku. Bude obsahova server, switch, virutálny switch, klientské PC a VM v ktorej bude bea Mininet. Pre zlúèite¾nos riešenia budú pouíté rovnaké rozsahy IP adries ako v èlánku:
* adresy v rozsahu-192.168.1.0/24
* adresy v rozsahu-192.168.2.0/24

![alt text](https://github.com/aks-2017/semestralne-zadania-semestralne-zadanie-73909-73984/blob/master/docs/obr4.png)

Obrázok 4 Návrh topológie [6]
 
## 2.2.	Technológie

Porovnanie pouitıch technológií v èlánku a návrhu našich technológií:

|Pouítá technológia v èlánku|Naša navrhnutá technológia|
|-------------|:-------------:|
|Server Apache HTTP| Server Nginx |
|Klientskı PC (Win 8, I7, 8GB RAM)|Klientskı PC (Win 10, I5, 8GB RAM)|
|Prehrávaè - Bitmovin|Prehrávaè – VLC|
|Kontrélér - nespomenutı|Kontrolér - Ryu|
|Codec - nespomenutı|Codec - H.264|
|Virtuálny switch - OpenVSwitch|Virtuálny switch - OpenVSwitch|
|Mininet verzie 2.2.1|Mininet verzie 2.2.2|
|Databáza - MySQL|Databáza - PostgreSQL|	

Rozhodli sme sa od èlánku odlíši inou vo¾bou HTTP servera, prehrávaèa, klientského PC, vo¾bou vlastného kontroléra, codecom, verziou Mininetu a inou databázou. V prípade zistenia vzájomnej nekompatibility alebo nekompatibility s technikou MPEG-DASH skúsime poui inı kompatibilné zariadenia alebo technológie. Tım by sme chceli dokáza univerzálnos prostredia Mininet aj v novšej verzií s pouitím inıch technológií.

## 2.3.	Princíp testovania

Testova budeme podobnım princípom, ako je pouitı v èlánku. Video v codecu H.264 bude streamované pomocou VLC media player s vyuítím techniky MPEG-DASH. Bandwidth bude menenı cez framework Mininetu minievents, ktorı umoòuje meni bandwidth a iné vlastnosti dynamicky. 

Na nasledujúcom obrázku môme vidie ukáku JSONu, ktorı bude meni bandwidth na linke medzi rozhraním root-eth0 a virtuálnym switchom (Link1).

![alt text](https://github.com/aks-2017/semestralne-zadania-semestralne-zadanie-73909-73984/blob/master/docs/obr5.png)

Obrázok 5 Ukáka JSONu [6]

Kadı test bude trva 120 sekúnd a kadıch 30 sekúnd budeme na linke Link1 meni bandwidth napríklad na hodnoty 1024 kb/s, 2048 kb/s a 3072 kb/s, pod¾a nasledujúceho grafu. 

![alt text](https://github.com/aks-2017/semestralne-zadania-semestralne-zadanie-73909-73984/blob/master/docs/obr6.png)

Obrázok 6 Graf zmeny bandwidthu v èase [6]

Budeme sledova zmeny hodnoty bitratu v plynúcom èase.

Bude vykonanıch aspoò 10 testov s nasledujúcimi parametrami:
* dåka testu - 120 sekúnd
* zmena bandwidthu - kadıch 30 sekúnd
* hodnoty bandwidthu - 1024 kb/s, 2048 kb/s, 3072 kb/s, 1024 kb/s
* video s codecom H.264 

Všetky testy budú následne vyhodnotené a porovnané s vısledkami z èlánku. Prípadné zhody alebo rozdiely budú zdokumentované.

# 3.	Literatúra
[1] Mininet Overview, 2017, http://mininet.org/overview/

[2] Software-Defined Networks and OpenFlow - The Internet Protocol Journal, Volume 16, No. 1, 2013, https://www.cisco.com/c/en/us/about/press/internet-protocol-journal/back-issues/table-contents-59/161-sdn.html

[3] Mendoca M., Astuto B., Obraczka K., Turletti T.: Survey of Software-Defined Networking: Past, Present, and Future of Programmable Networks,2013

[4] Kei Ohamura, 2013, NTT, https://osrg.github.io/ryu/slides/LinuxConJapan2013.pdf

[5] SDNCentral LLC 2017, https://www.sdxcentral.com/sdn/definitions/sdn-controllers/openflow-controller/

[6] Emulation of Dynamic Adaptive Streaming over HTTP with Mininet, 2015,Anatoliy Zabrovskiy, Evgeny Kuzmin, Evgeny Petrov, Mikhail Fomichev, Petrozavodsk State University, Petrozavodsk, Russia

[7] Software Defined Networking: Design and Deployment, Patricia A. Morreale, James M. Anderson, 2014

[8] Encoding Intelligence™ 2016, https://www.encoding.com/mpeg-dash/

[9] Christopher Mueller 21.4.2015, https://bitmovin.com/dynamic-adaptive-streaming-http-mpeg-dash/

[10] Ed Tittel, https://www.cisco.com/c/en/us/solutions/software-defined-networking/sdn-vs-nfv.html

	

