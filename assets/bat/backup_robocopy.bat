REM =========================================================
REM Qui la documentazione:https://learn.microsoft.com/it-it/windows-server/administration/windows-commands/robocopy
REM =========================================================

REM ==================ISTRUZIONI=================================
REM /L = “List only” → anteprima: Robocopy non copia nulla, non elimina nulla, non crea cartelle: stampa solamente l’elenco di ciò che farebbe.
REM /L = “List only” è pensato per controllare prima di lanciare l’operazione reale
REM Quindi: prima si fa un “controllo”, e poi se si toglie /L si fa la copia vera.
REM Nel batch c'è il messaggio “Se tutto ok, togli lo switch /L” per ricordare che è una prova a secco.
REM Rimosso /L, Robocopy esegue davvero la copia secondo le altre opzioni:
REM /E: include sottocartelle anche vuote
REM /COPY:DAT: copia Dati, Attributi, Timestamp file
REM /DCOPY:DA: copia Dati e Attributi delle cartelle
REM /R:1 /W:1: 1 tentativo di retry, attesa 1 s
REM /NFL /NDL: log “snello” (no elenco file/dir)
REM /TEE: scrive output sia a video sia nel log
REM /LOG+:"%log%": accoda al log esistente (usa /LOG: per sovrascrivere)
REM (Tutte opzioni documentate nella scheda ufficiale di Robocopy.) [holoviews.org]
REM ===================================================

@echo off
setlocal enableextensions
REM =========================================================
REM BACKUP/SYNC con ROBOCOPY (DRY-RUN con /L → togli /L per eseguire)
REM Doc: robocopy
REM Inserisci qui sotto sorgente, destinazione, log
REM =========================================================
set "src=C:\Users\ufabiani\Downloads\mio\PCM CV\articoli"
set "dst=C:\Users\ufabiani\Downloads\mio\PCM CV\BackupDati"
set "log=C:\Users\ufabiani\Downloads\mio\PCM CV\BackupDati\Logs\robocopy_backup.log"

if not exist "%src%\" (echo Sorgente non trovata: "%src%" & goto :end)
for %%D in ("%dst%") do if not exist "%%~fD" mkdir "%%~fD" >nul 2>&1
for %%D in ("%log%") do if not exist "%%~dpD" mkdir "%%~dpD" >nul 2>&1

REM ESEGUI IL COMANDO robocopy (ricorda la /L per controllare prima di eseguire)
robocopy "%src%" "%dst%" /E /COPY:DAT /DCOPY:DA /R:1 /W:1 /NFL /NDL /TEE /LOG+:"%log%" /L

echo. & echo   DRY-RUN completato. Controlla il log: "%log%"
echo    Se tutto ok, togli lo switch /L nella riga robocopy. & echo.
pause
:end
endlocal