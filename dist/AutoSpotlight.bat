@echo off
set SCRIPT="%USERPROFILE%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\MySpotlight.lnk"
set PWS=%windir%\System32\WindowsPowerShell\v1.0\powershell.exe
%PWS% -Command "$ws = New-Object -ComObject WScript.Shell; $s = $ws.CreateShortcut('%SCRIPT%'.Trim('\"')); $S.TargetPath = 'E:\GetSpotlight.exe'; $S.Save()"

schtasks /create /tn "MySpotlight" /tr "E:\GetSpotlight.exe" /sc daily /st 10:00
