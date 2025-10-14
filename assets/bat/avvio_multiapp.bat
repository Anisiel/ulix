@echo off
setlocal
REM =========================================================
REM AVVIO MULTI-APP
REM ---------------------------------------------------------
REM Questo script apre più applicazioni in sequenza usando
REM il comando START. Ogni app si apre in una finestra separata.
REM ---------------------------------------------------------
REM MODIFICA QUI I PERCORSI SE NECESSARIO:
REM - Controlla i percorsi degli eseguibili delle app
REM - Aggiungi o rimuovi app secondo le tue esigenze
REM - Qui ci sono Outlook, Edge, Excel, Word, Zucchetti
REM - ESECUZIONE AUTOMATICA
REM - Si può inserire nella cartella Esecuzione automatica, per avvio automatico all'accesso.
REM - Clicca Win+R, digita shell:startup e premi Invio per aprire la cartella Esecuzione automatica
REM - Quindi copia questo file .bat lì dentro.
REM =========================================================

REM --- Avvia Microsoft Outlook ---
start "" "C:\Program Files\Microsoft Office\root\Office16\OUTLOOK.EXE"

REM --- Attendi 3 secondi prima di aprire la prossima app ---
timeout /t 3 /nobreak >nul

REM --- Avvia Microsoft Edge ---
start "" "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

REM --- Attendi 2 secondi ---
timeout /t 2 /nobreak >nul

REM --- Avvia Microsoft Excel ---
start "" "C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE"

REM --- Attendi 2 secondi ---
timeout /t 2 /nobreak >nul

REM --- Avvia Microsoft Word ---
start "" "C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE"

REM --- Attendi 2 secondi ---
timeout /t 2 /nobreak >nul

REM --- Avvia Zucchetti ---
start "" "https://pcm.hrzucchetti.it/hrppcm/jsp/login.jsp"

REM --- Messaggio finale ---
echo.
echo ✅ Tutte le applicazioni sono state avviate.
echo.
pause

endlocal