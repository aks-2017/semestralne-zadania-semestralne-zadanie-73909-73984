# 1.	Softv�rovo definovan� siete
Inicializova�, kontrolova�, meni� a mana�ova� spr�vanie siete dynamicky cez rozhranie.

![alt text](https://github.com/aks-2017/semestralne-zadania-semestralne-zadanie-73909-73984/blob/master/docs/obr1.png)

Obr�zok 1 Tradi�n� sie�(v�avo) a SDN(vpravo) [6]

Tradi�n� hardv�rov� siete nezodpovedaj� neust�le sa meniacim potreb�m v oblasti v�po�tovej techniky a �lo�iska v prostrediach d�tov�ch centier a poskytovate�ov slu�ieb. SDN (Software-Defined Networking) poskytuje lep�ie mo�nosti v tak�ch situ�ci�ch, kde mnoh� vlastnosti vy�aduj� flexibilnej�� a dynamickej�� pr�stup. Vlastnosti SDN s� [10]:
* Priamo programovate�n� � sie�ov� kontrola je priamo programovate�n� preto�e je oddelen� od smerovac�ch funkci�
* Agiln� � oddelenie kontroly od smerovania umo��uje administr�torom dynamicky prisp�sobova� sie�ov� prem�vku aby sp��ala meniace sa potreby
* Centr�lne mana�ovate�n� � sie�ov� inteligencia je centralizovan� v SDN kontrol�roch, ktor� udr�uj� celkov� poh�ad na sie�. 
* Programovate�n� � umo��uje r�chlo meni� konfigur�ciu, mana�ova�, zabezpe�i� alebo optimalizova� sie� r�chlo cez automatick� SDN programy, ktor� si m��u �udia p�sa� sami, preto�e nie s� propriet�rne

Oproti tradi�nej sieti je SDN sie� riaden� kontrol�rom, ktor� m� nieko�ko rov�n. Medzi z�kladn� roviny patria [10]:
* Riadiaca rovina ovl�da to kam sa bud� posiela� spr�vy
* D�tov� rovina u� len posiela pod�a toho, �o mu riadiaca rovina povie

## 1.1.	Prostredie Mininet

Mininet je sie�ov� emul�tor, ktor� umo��uje vytv�ra� koncov� zariadenia, prep�na�e, smerova�e, a linky medzi nim. Mininet host sa spr�va rovnako ako re�lna ma�ina a je mo�n� sa na� pripoji� pomocou SSH. �o sa t�ka OpenFlow kontrol�rov, Mininet je ve�mi flexibiln� a umo��uje prida� do simul�cie mno�stvo typov kontrol�rov. Siete Mininetu pracuj� so skuto�n�m k�dom vr�tane �tandardn�ch sie�ov�ch aplik�ci� Unix / Linux, ako aj na skuto�nom jadre Linuxu a sie�ovom z�sobn�ku. Hlavn� funkcie n�stroja Mininet s� [1]: 
* poskytuje jednoduch� a lacn� sie�ov� testovacie m�dium pre v�voj aplik�ci� nad protokolom OpenFlow
* umo��uje viacer�m s�be�n�m v�voj�rom pracova� nez�visle na tej istej topol�gii
* podporuje regresn� testy na �rovni syst�mu, ktor� s� opakovate�n� a �ahko zabalen�
* umo��uje zlo�it� testovanie topol�gie bez nutnosti prepojenia fyzickej siete
* podporuje �ubovo�n� vlastn� topol�gie a obsahuje z�kladn� sadu parametrizovan�ch topol�gi�
* je pou�ite�n� mimo krabice bez programovania a tie� poskytuje priamu a roz��rite�n� Python API pre vytv�ranie a experimentovanie so sie�ami
* slu�ba Mininet poskytuje jednoduch� sp�sob, ako dosiahnu� spr�vne spr�vanie syst�mu (a v rozsahu podporovanom va��m hardv�rom, v�konom) a experimentova� s topol�giami.

Mininet kombinuje mnoh� z najlep��ch funkci� emul�torov a �pecializovan�ch simul�torov. V porovnan� s pr�stupmi zalo�en�mi na �plnej virtualiz�cii syst�mu, spolo�nos� Mininet vynik� v [1]:
* r�chlej�om bootovan�
* umo��uje spravova� stovky hostite�ov a prep�na�ov
* poskytuje v��iu ��rku p�sma
* Jednoducho sa in�taluje

V porovnan� s hardv�rov�mi testovac�mi doskami, Mininet vynik� v [1]:
* je r�chlo rekonfigurovate�n� a re�tartovate�n�

V porovnan� so simul�tormi, Mininet vynik� v [1]:
* be�� na re�lnom, nemodifikovanom k�de vr�tane aplika�n�ho k�du
* �ahko sa prip�ja k re�lnym sie�am

## 1.2.	Kontrol�r

OpenFlow kontrol�r je typ SDN kontrol�ra, ktor� pou��va OpenFlow protokol. OpenFlow kontrol�r pou��va OpenFlow protokol aby spojil a konfiguroval sie�ov� zariadenia, ako smerova�e a prep�na�e, na n�jdenie najlep�ej cesty v prem�vke. SDN kontrol�ry teda u�ah�uj� riadenie siete a dok�u riadi� cel� komunik�ciu medzi aplik�ciami a zariadeniami, tak aby sa �o najefekt�vnej�ie upravil tok prem�vky, tak ako je v danom momente potrebn�. Ke� nie je riadiaca rovina implementovan� vo firmv�ri, ale je implementovan� v softv�ri, administr�tori dok�u mana�ova� sie� ove�a jednoduch�ie, viac dynamicky a s lep�ou granularitou. OpenFlow kontrol�r teda tvor� centr�lnu kontroln� jednotku v sieti, ktor� riadi v�etku prem�vku, v�etky zariadenia v sieti vykon�vaj� akcie tak ako od nich po�aduje kontrol�r a podporuje OpenFlow. [5]

### 1.2.1.	Kontrol�r Ryu

Ryu poskytuje ve�mi siln� pomer medzi jeho v�hodami a nev�hodami, v prospech v�hod. Ryu si stavia medzi jej hlavne piliere v�hod tri charakteristiky: kvalita k�du, funkcionalita a pou�ite�nos�. Podporuje nieko�ko protokolov, pre spr�vu sie�ov�ch zariaden�, t�mi s� napr. Netconf, OF-config, no prim�rne OpenFlow vo verzi�ch a� po aktu�lnu 1.5. Je nap�san� v jazyku Python. [4]

## 1.3.	Protokol Openflow

Je protokol medzi kontrol�rom a sie�ov�mi zariadeniami, ako aj n�stroj pre �pecifik�ciu logickej �trukt�ry siete. Pracuje v r�mci TCP (Transmission Control Protocol), kde by mal po��va� na porte 6653. M��e vykona� r�zne akcie [2]: 
* prid�vanie, zmena alebo vyra�ovanie paketov, pod�a vopred definovan�ch pravidiel a akci�
* smerovanie akceptovan�ch paketov prep�na�om
* neakceptovan� pakety s� smerovan� do kontrol�ra, ktor� m��e:
  * zmeni� pravidl� smerovacej tabu�ky na jednom alebo viacer�ch prep�na�och
  * nastavi� nov� pravidl�, aby tak predi�iel ve�kej komunik�ci� medzi prep�na�om a kontrol�rom

![alt text](https://github.com/aks-2017/semestralne-zadania-semestralne-zadanie-73909-73984/blob/master/docs/obr2.png)

Obr�zok 2 Openflow prep�na� [2]

Obr�zok popisuje pribli�n� komunik�ciu v r�mci OpenFlow protokolu [2]: 
* SDN kontrol�r komunikuje s prep�na�mi, ktor� s� kompatibiln� s OpenFlow, pomocou OpenFlow protokolu be�iaceho cez SSL (Secure Sockets Layer)
* ka�d� prep�na� sa pripoj� k zariadeniam cie�ov�ho pou��vate�a, ktor� s� zdrojmi a cie�mi paketov�ch tokov
* ka�d� prep�na� m� nieko�ko tabuliek (spomenut�ch vy��ie), implementovan�ch hardv�rom alebo firmv�rom, ktor� sa pou��vaj� na riadenie toku cez prep�na�e

## 1.4.	Prep�na�

Preposielacie zariadenie v SDN sa naz�va forwarder a pozost�va z dvoch �ast� [3]:
* prietokovej tabu�ky (flow table) obsahuj�cej z�znam a akciu na prij�manie akt�vnych tokov
* abstrak�nej vrstvy, ktor� bezpe�ne komunikuje s riadiacou jednotkou (kontrol�rom) o nov�ch vstupoch, ktor� sa v danom momente nenach�dzaj� v tokovej tabu�ke. 

OpenFlow prep�na� pozost�va z jednej alebo viacer�ch tabuliek tokov, ktor� ukladaj� z�znamy pre vyh�adanie alebo presmerovanie paketov. [3]

Po pr�chode paketov na OpenFlow prep�na� sa hlavi�ka paketu extrahuje a porovn� s pol��kom zhody (match field) z tabu�ky tokov. Ak sa zhoduje hlavi�ka paketu s pol��kom v tabu�ke, tak prep�na� pou�ije pr�slu�n� sadu in�trukci� spojen� s dan�m tokom. V pr�pade, �e sa nen�jde �iadna zhoda s tabu�kou tokov, tak nasleduj�ca akcia prep�na�a bude z�visie� od in�trukci� definovan�ch v tabu�ke ch�baj�cich tokov (table-miss flow entry), napr. zahodenie paketu. [3]
 
## 1.5.	Dynamick� adapt�vne streamovanie

Hlavn� my�lienka Dynamic adaptive streaming (MPEG-DASH) je rozdeli� s�bor s medi�lnym obsahom na segmenty, ktor� m��u by� enk�dovan� na r�znych bitratoch. Segmenty s� poskytnut� na webovom servery a m��u by� stiahnut� cez HTTP (GET request). Segmenty s� referencovan� pomocou URL (definovan� v RFC3986). Segmenty sa �alej m��u deli� aj na men�ie subsegmenty. Mo�n� obsahy segmentov [8] [9]: 
* SegmentBase - najz�kladnej�ia reprezent�cia
* SegmentList � obsahuje zoznam SegmentURL
* SegmentTemplate � vysklad�va zoznam segmentov

Na vysvetlenie vz�ahov medzi segmentami, MPEG-DASH zadefinovalo Media Presentation Description (MPD). MPD je XML s�bor, ktor� reprezentuje r�zne vlastnosti medi�lneho obsahu a jednotliv� segmenty pre ka�d� vlastnos�. T�to �trukt�ra prezentuje spojenie medzi segmentami a bitratom. [8] [9]

Na obr�zku je mo�n� vidie� princ�p MPEG-DASH. Server rozdel� medi�lny obsah na segmenty podla kvality na Low, Medium a Best. Klient pod�a aktu�lneho bandwidthu a CPU kapacity vyber� medzi kvalitou medi�lneho obsahu. [8] [9] 

![alt text](https://github.com/aks-2017/semestralne-zadania-semestralne-zadanie-73909-73984/blob/master/docs/obr3.png)

Obr�zok 3 Princ�p fungovania MPEG-DASH [8]


# 2.	N�vrh

## 2.1.	Topol�gia
V na�om preveden� budeme pou��va� rovnak� topol�giu, ak� bola uveden� v �l�nku. Bude obsahova� server, switch, virut�lny switch, klientsk� PC a VM v ktorej bude be�a� Mininet. Pre zl��ite�nos� rie�enia bud� pou��t� rovnak� rozsahy IP adries ako v �l�nku:
* adresy v rozsahu-192.168.1.0/24
* adresy v rozsahu-192.168.2.0/24

![alt text](https://github.com/aks-2017/semestralne-zadania-semestralne-zadanie-73909-73984/blob/master/docs/obr4.png)

Obr�zok 4 N�vrh topol�gie [6]
 
## 2.2.	Technol�gie

Porovnanie pou�it�ch technol�gi� v �l�nku a n�vrhu na�ich technol�gi�:

|Pou��t� technol�gia v �l�nku|Na�a navrhnut� technol�gia|
|-------------|:-------------:|
|Server Apache HTTP| Server Nginx |
|Klientsk� PC (Win 8, I7, 8GB RAM)|Klientsk� PC (Win 10, I5, 8GB RAM)|
|Prehr�va� - Bitmovin|Prehr�va� � VLC|
|Kontr�l�r - nespomenut�|Kontrol�r - Ryu|
|Codec - nespomenut�|Codec - H.264|
|Virtu�lny switch - OpenVSwitch|Virtu�lny switch - OpenVSwitch|
|Mininet verzie 2.2.1|Mininet verzie 2.2.2|
|Datab�za - MySQL|Datab�za - PostgreSQL|	

Rozhodli sme sa od �l�nku odl�i� inou vo�bou HTTP servera, prehr�va�a, klientsk�ho PC, vo�bou vlastn�ho kontrol�ra, codecom, verziou Mininetu a inou datab�zou. V pr�pade zistenia vz�jomnej nekompatibility alebo nekompatibility s technikou MPEG-DASH sk�sime pou�i� in� kompatibiln� zariadenia alebo technol�gie. T�m by sme chceli dok�za� univerz�lnos� prostredia Mininet aj v nov�ej verzi� s pou�it�m in�ch technol�gi�.

## 2.3.	Princ�p testovania

Testova� budeme podobn�m princ�pom, ako je pou�it� v �l�nku. Video v codecu H.264 bude streamovan� pomocou VLC media player s vyu��t�m techniky MPEG-DASH. Bandwidth bude menen� cez framework Mininetu minievents, ktor� umo��uje meni� bandwidth a in� vlastnosti dynamicky. 

Na nasleduj�com obr�zku m��me vidie� uk�ku JSONu, ktor� bude meni� bandwidth na linke medzi rozhran�m root-eth0 a virtu�lnym switchom (Link1).

![alt text](https://github.com/aks-2017/semestralne-zadania-semestralne-zadanie-73909-73984/blob/master/docs/obr5.png)

Obr�zok 5 Uk�ka JSONu [6]

Ka�d� test bude trva� 120 sek�nd a ka�d�ch 30 sek�nd budeme na linke Link1 meni� bandwidth napr�klad na hodnoty 1024 kb/s, 2048 kb/s a 3072 kb/s, pod�a nasleduj�ceho grafu. 

![alt text](https://github.com/aks-2017/semestralne-zadania-semestralne-zadanie-73909-73984/blob/master/docs/obr6.png)

Obr�zok 6 Graf zmeny bandwidthu v �ase [6]

Budeme sledova� zmeny hodnoty bitratu v plyn�com �ase.

Bude vykonan�ch aspo� 10 testov s nasleduj�cimi parametrami:
* d�ka testu - 120 sek�nd
* zmena bandwidthu - ka�d�ch 30 sek�nd
* hodnoty bandwidthu - 1024 kb/s, 2048 kb/s, 3072 kb/s, 1024 kb/s
* video s codecom H.264 

V�etky testy bud� n�sledne vyhodnoten� a porovnan� s v�sledkami z �l�nku. Pr�padn� zhody alebo rozdiely bud� zdokumentovan�.

# 3.	Literat�ra
[1] Mininet Overview, 2017, http://mininet.org/overview/

[2] Software-Defined Networks and OpenFlow - The Internet Protocol Journal, Volume 16, No. 1, 2013, https://www.cisco.com/c/en/us/about/press/internet-protocol-journal/back-issues/table-contents-59/161-sdn.html

[3] Mendoca M., Astuto B., Obraczka K., Turletti T.: Survey of Software-Defined Networking: Past, Present, and Future of Programmable Networks,2013

[4] Kei Ohamura, 2013, NTT, https://osrg.github.io/ryu/slides/LinuxConJapan2013.pdf

[5] SDNCentral LLC 2017, https://www.sdxcentral.com/sdn/definitions/sdn-controllers/openflow-controller/

[6] Emulation of Dynamic Adaptive Streaming over HTTP with Mininet, 2015,Anatoliy Zabrovskiy, Evgeny Kuzmin, Evgeny Petrov, Mikhail Fomichev, Petrozavodsk State University, Petrozavodsk, Russia

[7] Software Defined Networking: Design and Deployment, Patricia A. Morreale, James M. Anderson, 2014

[8] Encoding Intelligence� 2016, https://www.encoding.com/mpeg-dash/

[9] Christopher Mueller 21.4.2015, https://bitmovin.com/dynamic-adaptive-streaming-http-mpeg-dash/

[10] Ed Tittel, https://www.cisco.com/c/en/us/solutions/software-defined-networking/sdn-vs-nfv.html

	

