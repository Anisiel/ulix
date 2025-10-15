REM =========================================================
REM Qui la documentazione: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands
REM risorse1: https://en.wikibooks.org/wiki/Windows_Batch_Scripting
REM risorse2: https://www.robvanderwoude.com/batexamples.php
REM risorse3: https://learn.openwaterfoundation.org/owf-learn-windows-shell/useful-batch-files/useful-batch-files/
REM =========================================================


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