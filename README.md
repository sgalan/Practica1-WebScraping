# Pràctica 1. Web scraping

<!-- TOC depthFrom:1 depthTo:8 withLinks:1 updateOnSave:1 orderedList:0 -->

- [Estudi de la presència de conceptes relatius a la sostenibilitat en l’àmbit de les contractacions públiques europees](#Estudi-de-la-presència-de-conceptes-relatius-a-la-sostenibilitat-en-l’àmbit-de-les-contractacions-públiques-europees)
    - [Descripció](#descripció)
    - [Membres del grup](#membres-del-grup)   
    - [Descripció dels fitxers](#descripció-dels-fitxers)
    - [Recursos](#recursos)
    


<!-- /TOC -->
# Estudi de la presència de conceptes relatius a la transformació digital en l’àmbit de les contractacions públiques europees

## Descripció

Aquesta pràctica s'ha realitzat per l'assignatura de Tipologia i cicle de vida de les dades del Màster de Data science de la Universitat Oberta de Catalunya (UOC). En aquest treball hem aplicat tècniques de web scraping mitjançant el llenguatge de programació Python per tal d'obtenir informació sobre la geo-localització de les contractacions públiques relacionades amb la transformació digital dins de l'àmbit europeu, en concret a Espanya.

## Membres del grup

Aquesta activitat ha estat realitzada per David Roche Valles i Silvia Galan Martínez.

## Descripció dels fitxers

En el repositori podem trobar diferents documents:

* **src/get_nuts.py**: Programa per tal d'aplicar tècniques de web scraping per la compleció del dataset amb informació geo-espacial.
* **src/nuts_dictionary.pickle**: Diccionari el qual conté la relació entre sobre les províncies a Espanya i el seu codi [NUTS](https://ec.europa.eu/eurostat/web/nuts/background).
* **pdf/respostes.pdf**: Document en format PDF el qual conté les respostes a les diferents preguntes de la pràctica.
* **Images/**: Dins d'aquesta carpeta es troben les imatges obtingudes o usades pel desenvolupament del projecte.
* **csv/**: Dins d'aquesta carpeta es troben el dataset d'entrada (Input) i el de sortida (Output) pel codi `get_nuts.py`, els quals contenen informació rellevant per cada projecte. Aquesta informació ha estat obtinguda a través de [Tenders Electronic Daily](https://data.europa.eu/euodp/en/data/dataset/ted-csv)

## Recursos

1. European Union comission. (2020). TED Tenders Electronic Daily. Recuperat de: https:// ted.europa.eu/TED/main/HomePage.do
2. Subirats, L. Calvo, M. (2018). Web Scraping. Editorial UOC.
3. Muñoz-Garcia, C., Vila, J. (2019). Value creation in the international public procurement market: In search of springbok firms. Journal of Business Research, (101), 516-521. Recuperat de: https://doi.org/10.1016/j.jbusres.2018.12.041.
4. Sanchez-Graells, A. (2019). Data-Driven and Digital Procurement Governance: Revisiting Two Well-Known Elephant Tales. SSRN, 1-18. Recuperat de: http://dx.doi.org/10.2139/ ssrn.3440552
5. Halsbenning, S., Niemann, M. (2019). The European Procurement Dilemma-First Steps to Introduce Data-Driven Policy-Making in Public Procurement. IEEE 21st Conference on Business Informatics (CBI). 303-311. Recuperat de: https://ieeexplore.ieee.org/document/ 8808005
