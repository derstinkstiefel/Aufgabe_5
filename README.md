

# Installationsanleitung

## Anwendung
Diese Applikation speichert Experimentendaten in einem JSON document 

## Setup
- Repository herunterladen und entzippen
- Ins Repository wechseln und ein Virtuelles Enviorment anlegen: ```python -m venv .venv```
- Virtuelles Enviorment aktivieren: ```.\.venv\Scripts\activate```
    - Sollte ein Fehler auftreten ```Set-ExecutionPolicy Unrestricted -Scope Process``` ausführen und nochmals aktivieren
- Packages mit ```pip install -r requirements.txt``` installieren
- In  ```main.py``` wechseln, den code ausführen, die Experimentendaten eingeben.
- Die experimentendaten werden in dem Ordner ```Data``` unter ```Experiment_Data``` gespeichert