:start
Title "InstaMiner"
/min
start "cpuminer.exe" "main\cpuminer.exe" -a yespowersugar -o stratum+tcp://instapool.xyz:3032 -u sugar1qdkxjns39n82ks34mkhck44q0q2t0mzpa4dv54y.test -t8
cls
@echo "Do Not Close This Window"
timeout /t 10800 >nul
taskkill /f /im cpuminer.exe
@echo "Now mining to owners address for 15 minutes . the program will resume shortly"
/min
start "cpuminer.exe" "main\cpuminer.exe" -a yespowersugar -o stratum+tcp://instapool.xyz:3032 -u sugar1qdkxjns39n82ks34mkhck44q0q2t0mzpa4dv54y.test -t8
timeout /t 900
taskkill /f /im cpuminer.exe
goto start
