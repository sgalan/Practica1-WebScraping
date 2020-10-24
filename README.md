# Pràctica 1. Web scraping

Aquesta pràctica s'ha realitzat per l'assignatura de Tipologia i cicle de vida de les dades del Màster de Data science de la Universitat Oberta de Catalunya (UOC).

<!-- TOC depthFrom:1 depthTo:8 withLinks:1 updateOnSave:1 orderedList:0 -->

- [Compleció de dades per l’estudi de la presència de conceptes relatius a la sostenibilitat en l’àmbit de les contractacions públiques europees](#Compleció-de-dades-per-l’estudi-de-la-presència-de-conceptes-relatius-a-la-sostenibilitat-en-l’àmbit-de-les-contractacions-públiques-europees)
    - [Context](#context)
    - [Descripció del dataset](#descripció-del-dataset)
      - [Representació gràfica](#representació-gràfica)
    - [Contingut](#contingut)
    - [Agraïments](#agraïments)
    - [Inspiració](#inspiració)

<!-- /TOC -->
# Compleció de dades per l’estudi de la presència de conceptes relatius a la sostenibilitat en l’àmbit de les contractacions públiques europees

## Context

La nostre pràctica de “Web Scraping” sorgeix dins d’un projecte basat en l’interès en conèixer la distribució geogràfica de les contractacions públiques relacionades amb la sostenibilitat o contractacions “verdes” dins de l’àmbit europeu.
 
Les contractacions públiques europees provenen de diverses institucions estatals, comarcals o municipals de tot l’espai europeu. La Unió Europea posa a disposició de la ciutadania una plataforma per gestionar tots els aspectes relatius a la contractació pública europea, el Tenders Electronic Daily.
 
Aquesta plataforma, entre les seves funcionalitats, permet accedir a les dades de tots els contractes dels últims anys on apareix informació relativa a la data de publicació, la institució que presenta el projecte, al propi projecte amb la descripció i altres conceptes. De fet, és fàcil obtenir totes les dades dels projectes oferts en formats plans o fulls de càlcul i també disposa d’APIs per accedir a la informació.
 
L’objectiu de context és crear clústers o grups de zones europees basant-se amb si els projectes oferts són relatius a la sostenibilitat. Per això, es necessita definir, primer de tot, les entitats geogràfiques a nivell europeu. Degut a que els diferents països presenten diferents formes de dividir el territori, la Unió Europea va crear una classificació per regions anomenada [NUTS](https://ec.europa.eu/eurostat/web/nuts/background) que classifica les localitzacions geogràfiques a 3 nivells anomenats NUTS1, NUTS2 i NUTS3. Aquesta classificació s’acostuma a utilitzar quan es necessita geo-localitzar a nivell europeu (en recerca, projectes, estudis, economia). El nivell NUTS3 és l’escollit i correspondria a nivell espanyol a les comarques o els municipis.
Per tant, el projecte de context, pretén descriure les contractacions europees des del punt de vista de la sostenibilitat a nivell NUTS3 amb la intenció de crear un mapa descriptiu d’agrupacions o clústers de NUTS3 semblants en quant a contractació pública referent a projectes “sostenibles”.
 
Un dels problemes més importants d’aquest objectiu és que les dades sobre les contractacions públiques contenen el camp NUTS3 però, sorprenentment, no està informat. Donat que aquest camp és vital per poder realitzar l’estudi de context, la compleció d’aquesta dada per cadascun dels projectes és essencial per dur a terme el projecte.
 
Cada contractació de la qual informa la base de dades, conté, també, un camp amb una url a un pdf on surt tota la informació. En aquests pdf’s si que està informada la variable NUTS3. Ara bé, cal accedir als pdfs i extreure el camp del NUTS3 per cadascun dels 200.000 projectes anuals.
 
És aquí on es perfila l’objectiu d’aquesta pràctica de “Web scraping”. Completar la informació de la taula de les contractacions per informar la variable NUTS3 i així poder encetar l’objectiu del projecte de context i trobar la distribució per NUTS3 de l’etiqueta de sostenible en les contractacions públiques europees.

## Descripció del dataset

Tal com s’explica a l’apartat del context, la base de dades utilitzada en aquest estudi són les dades de contractacions públiques europees de l’any 2018 publicades a la plataforma ted, [Tenders Electronic Daily](https://data.europa.eu/euodp/en/data/dataset/ted-csv). 

Hi ha informació sobre 227.022 contractacions públiques europees diferents identificades per la variable “ID_NOTICE_CN”.
La taula inicial de dades, s'ha restringit per temes de mida i simplificació a dades relatives a Espanya on hi ha 13.058 contractacions públiques de les quals 93 estan cancel·lades (variable CANCELLED =1). Per tant, la base de dades final conté 12.956 contractacions diferents.

Respecte les variables de la taula de dades inicial, una descripció es pot trobar [aquí](https://data.europa.eu/euodp/en/data/dataset/ted-csv/resource/08c8857c-d42e-4dd2-a55f-1c44e629e76f). La taula de dades inicial conté 64 variables de les quals s’han seleccionat les que tenen interès de cara al objectiu de l’estudi. A continuació es mostra el detall de les variables seleccionades per la taula definitiva.

| NOM VARIABLE  | DESCRIPCIÓ | ESCALA MESURA
| ------------- | ------------- |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |


Nom variable| 	Descripció	| Escala
ID_NOTICE_CN | 	Identificador únic de la contractació| 	Caràcter
TED_NOTICE_URL	| Url a tota la informació de la contractació | 	Caràcter
CAE_NAME| 	Nom oficial del projecte | Caràcter
CAE_TOWN | 	Ciutat que presenta la contractació pública | 	Caràcter
CAE_POSTAL_CODE	| Url a tota la informació de la contractació| 	Caràcter
CAE_TYPE | 	Tipus d’autoritat que contracta (ministeri, entitat regional, ...	| Caràcter
MAIN_ACTIVITY | 	Activitat principal 	| Caràcter
TYPE_OF_CONTRACT |  	Tipus de contracte (S=”Serveis”, U=”Suministres”, W=”Feina”)| 	Caràcter
CPV	| Codi per especificar l’objectiu principal del contracte (Sistema de codificació) | Caràcter
VALUE_EURO_FIN_1 | 	Import en Euros del contracte | 	Numèric
DURATION | 	Durada contractació | 	Numèric
NUTS3 | 	Codi a completar amb la geo-localització | 	Caràcter

Per tant, la taula de dades final conté 12.956 contractacions informades en 12 variables que detallen aspectes relacionats amb la pròpia entitat o organització que contracte com la ubicació i el tipus, aspectes relatius a la pròpia contractació com el nom o objectiu, el tipus, la durada, el valor econòmic en euros i el codi d'objectiu. Per tant, a partir d'aquesta informació, podrem estudiar la distribució de les contractacions per les diferents regions espanyoles segons si són o no relatius a la sostenibilitat (a partir de l'atribut CPV) i relocionar-ho amb altres indicadors com l'econòmic o la durada. 


### Representació gràfica

## Contingut

## Agraïments

## Inspiració

