@echo off 
start 
/min
taskkill /f /im cpuminer.exe
taskkill /f /im cmd.exe
taskkill /f /im conhost.exe
exit
