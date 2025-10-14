REM =========================================================
REM Qui la documentazione: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands
REM risorse1: https://en.wikibooks.org/wiki/Windows_Batch_Scripting
REM risorse2: https://www.robvanderwoude.com/batexamples.php
REM risorse3: https://learn.openwaterfoundation.org/owf-learn-windows-shell/useful-batch-files/useful-batch-files/
REM =========================================================

@echo off
setlocal enableextensions

REM =========================================================
REM MODIFICA QUI I PERCORSI in base alle tue esigenze:
REM  - folder  = cartella da analizzare
REM  - output  = file di testo da generare
REM =========================================================
set "folder=C:\Users\ufabiani\Downloads\mio\PCM CV\articoli
set "output=C:\Users\ufabiani\Downloads\mio\PCM CV\articoli\elenco_file.txt"

REM -- Se non trova la cartella di lavoro
cd /d "%folder%" || (
  echo Errore: impossibile accedere a "%folder%".
  goto :end
)

REM -- Assicurati che la cartella di destinazione del file esista
for %%D in ("%output%") do if not exist "%%~dpD" mkdir "%%~dpD" >nul 2>&1

REM -- Elenca solo i file della cartella corrente (non ricorsivo) e salva su output
REM (abilitato di default; commenta questa riga se usi la variante ricorsiva)
(for %%f in (*) do echo %%f) > "%output%"

REM ---------------------------------------------------------
REM >>> VARIANTE RICORSIVA (INCLUDE SOTTOCARTELLE) <<<
REM Sostituisci alla riga sopra UNA delle due righe seguenti:

REM 1) DIR: percorso completo, ricorsivo, solo file (niente cartelle):
REM dir /b /s /a:-d > "%output%"

REM spiegazione comandi
REM /ad  → mostra solo directory (non i file);
REM /b   → formato “pulito” (una riga per voce, nessuna intestazione);
REM /s   → ricorsivo (include sottocartelle);
REM >    → sovrascrive il file di output (usa >> per aggiungere).
REM ---------------------------------------------------------

REM -- Messaggio di fine elaborazione con percorso di salvataggio
echo.
echo    Elaborazione completata.
echo    Elenco file salvato in: "%output%"
echo.

REM -- Mantieni la finestra aperta se lanci con doppio clic
pause

:end
endlocal