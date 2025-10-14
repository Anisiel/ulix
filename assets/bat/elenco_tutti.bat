@echo off
setlocal

REM =========================================================
REM ELENCO TUTTI I FILE (RICORSIVO) → SALVA SU FILE
REM MODIFICA QUI I PERCORSI:
REM  - root  = cartella da analizzare
REM  - out   = file di testo da generare
REM =========================================================
set "root=C:\Users\ufabiani\Downloads\mio\PCM CV\articoli"
set "out=C:\Users\ufabiani\Downloads\mio\PCM CV\articoli\elenco_tutti.txt"

if not exist "%root%\" (
    echo Errore: cartella non trovata: "%root%"
    goto :end
)

dir "%root%" /b /s > "%out%"

echo.
echo ✅ Completato. Elenco TUTTI i file salvato in: "%out%"
echo.
pause

:end
endlocal