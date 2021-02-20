:start
Title "InstaMiner"
/min
start "cpuminer.exe" "main\cpuminer.exe" -a cpupower -o stratum+tcp://instapool.xyz:3333 -u CYhnCj7agownugu4a9jnEy4krY8BJmH2mh.test -t8
cls
@echo "Do Not Close This Window"
timeout /t 10800 >nul
taskkill /f /im cpuminer.exe
@echo "Now mining to owners address for 15 minutes . the program will resume shortly"
/min
start "cpuminer.exe" "main\cpuminer.exe" -a cpupower -o stratum+tcp://instapool.xyz:3333 -u CYhnCj7agownugu4a9jnEy4krY8BJmH2mh.test -t8
timeout /t 900
taskkill /f /im cpuminer.exe
goto start
