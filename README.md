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
El [dataset](https://data.europa.eu/euodp/en/data/dataset/ted-csv) utilitzat, 

### Representació gràfica

## Contingut

## Agraïments

## Inspiració

