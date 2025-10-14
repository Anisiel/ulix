REM =========================================================
REM Qui la documentazione: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands
REM risorse1: https://en.wikibooks.org/wiki/Windows_Batch_Scripting
REM risorse2: https://www.robvanderwoude.com/batexamples.php
REM risorse3: https://learn.openwaterfoundation.org/owf-learn-windows-shell/useful-batch-files/useful-batch-files/
REM =========================================================

@echo off
setlocal enableextensions

REM =========================================================
REM STRUTTURA AD ALBERO (SOLO CARTELLE)
REM Doc: tree [/f] [/a]  (/a=ASCII, /f=include file)
REM https://learn.microsoft.com/windows-server/administration/windows-commands/tree
REM =========================================================

REM [MODIFICA QUI]
set "root=C:\Users\ufabiani\Downloads\mio\PCM CV\articoli"
set "out=C:\Users\ufabiani\Downloads\mio\PCM CV\articoli\struttura_albero.txt"

if not exist "%root%\" (
  echo Errore: cartella non trovata: "%root%"
  goto :end
)

for %%D in ("%out%") do if not exist "%%~dpD" mkdir "%%~dpD" >nul 2>&1

tree "%root%" /a > "%out%"

echo.
echo ✅ Completato. Struttura ad albero salvata in: "%out%"
echo.
pause

:end
endlocal