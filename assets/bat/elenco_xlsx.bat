@echo off
setlocal

REM =========================================================
REM ELENCO SOLO FILE EXCEL (.XLSX) (RICORSIVO) → SALVA SU FILE
REM MODIFICA QUI I PERCORSI:
REM  - root  = cartella da analizzare
REM  - out   = file di testo da generare
REM =========================================================
set "root=C:\Users\ufabiani\Downloads\mio\PCM CV\articoli"
set "out=C:\Users\ufabiani\Downloads\mio\PCM CV\articoli\elenco_excel.txt"

if not exist "%root%\" (
    echo Errore: cartella non trovata: "%root%"
    goto :end
)

REM Elenca tutti i file XLSX (ricorsivo) e salva su file
dir "%root%\*.xlsx" /b /s > "%out%"

echo.
echo ✅ Completato. Elenco EXCEL salvato in: "%out%"
echo.
pause

:end
