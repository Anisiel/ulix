@echo off
setlocal

REM =========================================================
REM ELENCO SOLO FILE PDF (RICORSIVO) → SALVA SU FILE
REM MODIFICA QUI I PERCORSI:
REM  - root  = cartella da analizzare
REM  - out   = file di testo da generare
REM =========================================================
set "root=C:\Users\ufabiani\Downloads\mio\PCM CV\articoli"
set "out=C:\Users\ufabiani\Downloads\mio\PCM CV\articoli\elenco_pdf.txt"

if not exist "%root%\" (
    echo Errore: cartella non trovata: "%root%"
    goto :end
)

REM Elenca tutti i file PDF (ricorsivo) e salva su file
dir "%root%\*.pdf" /b /s > "%out%"

echo.
echo ✅ Completato. Elenco PDF salvato in: "%out%"
echo.
pause

:end
endlocal