@echo off
setlocal enableextensions

REM =========================================================
REM PULIZIA FILE VECCHI CON ALERT + LOG
REM Cancella file più vecchi di N giorni (ricorsivo) e salva log.
REM MODIFICA QUI:
REM  - target = cartella da analizzare (ora è Downloads\cestino)
REM  - days   = soglia in giorni
REM  - log    = percorso file di log
REM =========================================================
set "target=C:\Users\ufabiani\Downloads\cestino"
set "days=30"
set "log=C:\Users\ufabiani\Downloads\temp\pulizia_log.txt"

REM -- Modalità simulazione (1 = non cancella, solo mostra/logga)
set "simulate=1"

if not exist "%target%\" (
    echo Errore: cartella non trovata: "%target%"
    goto :end
)

echo =========================================================
echo Pulizia cartella: %target%
echo File più vecchi di: %days% giorni
echo Modalità simulazione: %simulate%
echo =========================================================

REM -- Conta i file che verrebbero eliminati
for /f %%C in ('forfiles /p "%target%" /s /d -%days% /c "cmd /c if @isdir==FALSE echo 1" ^| find /c "1"') do set count=%%C

if %count%==0 (
    echo Nessun file da eliminare.
    goto :end
)

echo Trovati %count% file da eliminare.
echo.
set /p confirm="Procedere? (Y/N): "
if /i not "%confirm%"=="Y" (
    echo Operazione annullata.
    goto :end
)

REM -- Scrivi intestazione log
echo ==== Pulizia avviata: %DATE% %TIME% ==== >> "%log%"
echo Cartella: %target%  Giorni: %days% >> "%log%"
echo --------------------------------------------------------- >> "%log%"

REM -- Elimina o simula
forfiles /p "%target%" /s /d -%days% /c "cmd /c if @isdir==FALSE (
    if %simulate%==1 (
        echo [SIMULAZIONE] @path >> \"%log%\"
    ) else (
        echo Eliminato: @path >> \"%log%\"
        del /q @path
    )
)"

REM -- Rimuovi cartelle vuote (solo se non simulazione)
if %simulate%==0 (
    for /f "delims=" %%D in ('dir "%target%" /ad /b /s ^| sort /r') do rd "%%D" 2>nul
)

echo.
echo ✅ Operazione completata. Log: %log%
echo.
pause

:end
endlocal