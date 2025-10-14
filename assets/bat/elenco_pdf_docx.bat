REM =========================================================
REM Qui la documentazione: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands
REM risorse1: https://en.wikibooks.org/wiki/Windows_Batch_Scripting
REM risorse2: https://www.robvanderwoude.com/batexamples.php
REM risorse3: https://learn.openwaterfoundation.org/owf-learn-windows-shell/useful-batch-files/useful-batch-files/
REM =========================================================

@echo off
setlocal enableextensions
REM =========================================================
REM ELENCO PDF & DOCX (RICORSIVO) + ESCLUSIONI (~$)
REM =========================================================
set "root=C:\Users\ufabiani\Downloads\mio\PCM CV\articoli"
set "out=C:\Users\ufabiani\Downloads\mio\PCM CV\articoli\elenco_pdf_docx.txt"

if not exist "%root%\" (echo Errore: "%root%" non trovata & goto :end)
for %%D in ("%out%") do if not exist "%%~dpD" mkdir "%%~dpD" >nul 2>&1

(
  dir "%root%" /b /s *.pdf
  dir "%root%" /b /s *.docx
) | findstr /vi /c:"~$" > "%out%"

echo. & echo ✅ Elenco salvato: "%out%" & echo.
pause
:end
endlocal
