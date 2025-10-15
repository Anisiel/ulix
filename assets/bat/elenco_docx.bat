REM =========================================================
REM Qui la documentazione: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands
REM risorse1: https://en.wikibooks.org/wiki/Windows_Batch_Scripting
REM risorse2: https://www.robvanderwoude.com/batexamples.php
REM risorse3: https://learn.openwaterfoundation.org/owf-learn-windows-shell/useful-batch-files/useful-batch-files/
REM =========================================================



@echo off
setlocal

REM =========================================================
REM ELENCO SOLO FILE DOCX (RICORSIVO) ? SALVA SU FILE
REM MODIFICA QUI I PERCORSI:
REM  - root  = cartella da analizzare
REM  - out   = file di testo da generare
REM =========================================================
set "root=C:\Users\ufabiani\Downloads\mio\PCM CV\articoli"
set "out=C:\Users\ufabiani\Downloads\mio\PCM CV\articoli\elenco_docx.txt"

REM -- Controlla che la cartella esista
if not exist "%root%\" (
    echo Errore: cartella non trovata: "%root%"
    goto :end
)

REM -- Crea la cartella di destinazione se manca
for %%D in ("%out%") do if not exist "%%~dpD" mkdir "%%~dpD" >nul 2>&1

REM -- Elenca tutti i file DOCX (ricorsivo) e salva su file
dir "%root%\*.docx" /b /s > "%out%"

echo.
echo ? Completato. Elenco DOCX salvato in: "%out%"
echo.
pause

:end
endlocal