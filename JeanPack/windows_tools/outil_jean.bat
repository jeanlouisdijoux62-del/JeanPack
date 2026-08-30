@echo off
set "DEST=%USERPROFILE%\Desktop\liste_jean.txt"

echo =============================== > "%DEST%"
echo Liste des fichiers du dossier Documents >> "%DEST%"
echo =============================== >> "%DEST%"
dir "%USERPROFILE%\Documents" /b >> "%DEST%"

echo Fichier créé : %DEST%
pause
