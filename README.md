# Wave_Plus – Instrukcja uruchomienia miernika radonu (MIDAS)

Interfejs Python do integracji miernika radonu z systemem MIDAS DAQ.

---

## 1. Wymagania

- System Linux (testowane na Fedora)
- Zainstalowany MIDAS
- Python 3.8+
- 3 terminale

Wymagana struktura katalogów:

```
$HOME/
 ├── midas
 ├── online/
 │    └── radon/
 └── exptab
```

---

## 2. Konfiguracja środowiska


W katalogu projektu znajduje się plik `setup_env.sh`, który konfiguruje
wszystkie wymagane zmienne środowiskowe MIDAS.

Nadaj mu prawa wykonywania (jednorazowo):

```bash
chmod +x setup_env.sh
```

W KAŻDYM nowym terminalu uruchom:

```bash
source setup_env.sh
```

⚠ Ważne:  
Nie używaj `./setup_env.sh`, ponieważ zmienne środowiskowe
nie zostaną ustawione w aktualnym shellu.
---

## 3. Uruchomienie serwera MIDAS

### Terminal 1 – Serwer MIDAS

```bash
cd ~/online/radon
mserver -e radon -D
mhttpd -e radon
```

W przypadku ponownego połączenia:

```bash
mhttpd -e radon
```

---

## 4. Uruchomienie skryptu WavePlus

### Terminal 2 – Integracja z MIDAS

Przejdź do katalogu projektu:

```bash
cd ~/waveplus
python midas_radon.py
```

---

## 5. Logi

Plik logów zapisywany jest w:

```
$HOME/online/radon/midas.log
```

---

## 6. Uwagi

- Wszystkie terminale muszą mieć ustawione zmienne środowiskowe.
- Katalog `~/online/radon` musi istnieć przed uruchomieniem systemu.
- MIDAS musi być poprawnie zainstalowany w `~/midas`.

---
