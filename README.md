# Wave_Plus – Instrukcja uruchomienia miernika radonu (MIDAS)

Interfejs Python do integracji miernika radonu z systemem MIDAS DAQ.

---

Struktura katalogu na komputerze w Cezamacie
$HOME/workspace/
 ├── online/
 ├── online-radon/
 └── packages/
      └── wave-plus/
           └── src/
                ├── midas_radon.py
                ├── radon_ble.py
                └── __pycache__/

## 2.Konfiguracja środowiska
Dla komputera w Cezamacie nie jest wymagana

### 1. Ustawienie sciezki /online-radon w /online/exptab
\dots
radon /home/astrocent/workspace/online-radon radon
\dots


## 3. Uruchomienie serwera MIDAS
### Serwer o nazwie radon
$cd ~/workspace/online/ 
$mserver -e radon -D
$mhttpd -e radon

## 4.Uruchomienie programu midas_radon

$python midas_radon.py

Available experiments on local computer
\dots
Wybrac: radon
\dots

