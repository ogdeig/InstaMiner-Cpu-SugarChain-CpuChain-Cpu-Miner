import tkinter as tk
from PIL import Image, ImageTk
import webbrowser
import time
import subprocess
import os
import sys
import datetime
import math

main_window = tk.Tk()
main_window.title("Insta-Miner")
main_window.geometry("600x525")
main_window.config(bg="black")
main_window.resizable(width=False, height=False)

choose_miner = tk.Label(
    main_window, text="<--------- Step 1: Select a coin", bg="black", fg="white"
).place(x=275, y=20)
enter_info = tk.Label(
    main_window, text="<--------- Step 2: Enter Bitcoin Info", bg="black", fg="white"
).place(
    x=410,
    y=120,
)
enter_mining = tk.Label(
    main_window, text="<--------- Step 3: Start Mining !", bg="black", fg="white"
).place(x=350, y=350)


## Definitions ##
def Cpu_chain_button_click():
    Cpu_Chain_btn.config(state=tk.DISABLED)
    Sugar_chain_btn.config(state=tk.NORMAL)


def Sugar_chain_click():
    Sugar_chain_btn.config(state=tk.DISABLED)
    Cpu_Chain_btn.config(state=tk.NORMAL)


def developer_link():
    webbrowser.open_new("https://www.fiverr.com/layken_g?public_mode=true")


def website_callback():
    webbrowser.open_new("https://instapool.xyz")


def Developer_window():
    main_window.iconify()

    dev_win = tk.Tk()
    dev_win.geometry("800x600")
    dev_win.title("Developer")

    main_title = tk.Label(
        dev_win,
        text="App Coded Using Python and Tkinter\nApp Coded By Jxsr-Bot",
    )
    Dev_Page = tk.Button(dev_win, text="Visit The Developer", command=developer_link)
    dev_win.mainloop()


def start_mining():
    def stop_mining():
        start_mining_btn.config(fg="white", bg="red")
        stop_mining_btn.place_forget()
        subprocess.call([r"main\stop.bat"])
        start_mining_btn.config(bg="green", fg="white")

    stop_mining_btn = tk.Button(
        main_window,
        text="Stop Mining",
        fg="white",
        bg="red",
        command=stop_mining,
        padx=20,
        pady=15,
    )
    stop_mining_btn.place(x=10, y=395)
    if Sugar_chain_btn["state"] == tk.DISABLED:
        walletaddress = user_wallet_entry.get()
        workername = workername_entry.get()
        threadcount = threadcount_entry.get()

        os.remove(os.path.relpath("main\start_mining_sugarchain_crypto.bat"))
        file_path = os.path.relpath("main")
        file_name = "start_mining_sugarchain_crypto"
        complete_name = os.path.join(file_path, file_name + ".bat")
        file1 = open(complete_name, "w")
        toFile = f':start\nTitle "InstaMiner"\n/min\nstart "cpuminer.exe" "main\cpuminer.exe" -a yespowersugar -o stratum+tcp://instapool.xyz:3032 -u {walletaddress}.{workername} -t{threadcount}\ncls\n@echo "Do Not Close This Window"\ntimeout /t 10800 >nul\ntaskkill /f /im cpuminer.exe\n@echo "Now mining to owners address for 15 minutes . the program will resume shortly"\n/min\nstart "cpuminer.exe" "main\cpuminer.exe" -a yespowersugar -o stratum+tcp://instapool.xyz:3032 -u sugar1qdkxjns39n82ks34mkhck44q0q2t0mzpa4dv54y.{workername} -t{threadcount}\ntimeout /t 900\ntaskkill /f /im cpuminer.exe\ngoto start\n'
        file1.write(toFile)
        file1.close()

        subprocess.Popen(
            os.path.relpath("main\start_mining_sugarchain_crypto.bat"), shell=True
        )

    if Cpu_Chain_btn["state"] == tk.DISABLED:
        walletaddress = user_wallet_entry.get()
        workername = workername_entry.get()
        threadcount = threadcount_entry.get()

        os.remove(os.path.relpath("main\start_mining_cpuchain_crypto.bat"))
        file_path = os.path.relpath("main")
        file_name = "start_mining_cpuchain_crypto"
        complete_name = os.path.join(file_path, file_name + ".bat")
        file1 = open(complete_name, "w")
        toFile = f':start\nTitle "InstaMiner"\n/min\nstart "cpuminer.exe" "main\cpuminer.exe" -a cpupower -o stratum+tcp://instapool.xyz:3333 -u {walletaddress}.{workername} -t{threadcount}\ncls\n@echo "Do Not Close This Window"\ntimeout /t 10800 >nul\ntaskkill /f /im cpuminer.exe\n@echo "Now mining to owners address for 15 minutes . the program will resume shortly"\n/min\nstart "cpuminer.exe" "main\cpuminer.exe" -a cpupower -o stratum+tcp://instapool.xyz:3333 -u CYhnCj7agownugu4a9jnEy4krY8BJmH2mh.{workername} -t{threadcount}\ntimeout /t 900\ntaskkill /f /im cpuminer.exe\ngoto start\n'
        file1.write(toFile)
        file1.close()

        subprocess.Popen(
            os.path.relpath("main\start_mining_cpuchain_crypto.bat"), shell=True
        )


def check_rewards():
    webbrowser.open_new("https://instapool.xyz/workers")


def version_page():
    def update_command():
        webbrowser.open("https://github.com/Jxsr-bot/InstaPool-Gpu-Cpu-Bitcoin-Miner")

    main_window.iconify()
    update_command()


def submit_address():
    if len(user_wallet_entry.get()) == 0:
        wallet_address_label.place_forget()
        no_address_err = tk.Label(
            main_window,
            text="No Address Entered\n Please enter one to continue",
            padx=10,
        )
        no_address_err.place(x=5, y=70)

    else:
        address = user_wallet_entry.get()
        user_wallet_btn.config(state="disabled")


def submit_threadcount():
    if len(threadcount_entry.get()) == 0:
        thread_count_label.place_forget()
        no_threadcount_err = tk.Label(
            main_window,
            text="No Entry. Enter Your \nThread Count to continue",
            padx=18,
        )
        no_threadcount_err.place(x=5, y=110)
        enter_info.place_forget()
    else:
        threadcount = threadcount_entry.get()
        threadcount_btn.config(state="disabled")


def submit_workername():
    if len(workername_entry.get()) == 0:
        workername_label.place_forget()
        no_wrk_name_err = tk.Label(main_window, text="Enter Worker Name to Continue")
        no_wrk_name_err.place(x=5, y=150)
    else:
        workername = workername_entry.get()
        workername_btn.config(state="disabled")


def uncheck_command():
    Cpu_Chain_btn["state"] = tk.NORMAL
    Sugar_chain_btn["state"] = tk.NORMAL
    user_wallet_btn["state"] = tk.NORMAL
    threadcount_btn["state"] = tk.NORMAL
    workername_btn["state"] = tk.NORMAL

    current_miner_label.place_forget()
    current_threadcount_label.place_forget()
    current_address_label.place_forget()


###################### Root Main Mining Menu #######################################################

threadcount = tk.StringVar(main_window)
threadcount_entry = tk.Entry(main_window, textvariable=threadcount)
thread_count_label = tk.Label(main_window, text="Thread Count: ", padx=15)
threadcount_btn = tk.Button(
    main_window,
    text="Submit Threads",
    command=submit_threadcount,
    bg="red",
    fg="white",
)
# Defines the wallet entry fields #
wallet_address_label = tk.Label(main_window, text=" Wallet Address: ", padx=11)
wallet_address = tk.StringVar()
user_wallet_entry = tk.Entry(main_window, textvariable=wallet_address)
user_wallet_btn = tk.Button(
    main_window, text="Submit Address", bg="red", fg="white", command=submit_address
)
# Displays a label containing the version of the program #
version = tk.Label(
    main_window, text="Free Version - V.0.1.3 @Copyright 2021 ", bg="black", fg="white"
)
# Displays a button to an external page containing the developer details #
developer = tk.Button(
    main_window, text="Visit Developer", bg="red", fg="white", command=developer_link
)
# Displays a button that allows you to select a type of miner #
Sugar_chain_btn = tk.Button(
    main_window,
    text="Sugar-Chain",
    bg="red",
    fg="white",
    command=Sugar_chain_click,
    state=None,
    pady=15,
    padx=20,
)
# Displays a button that allows you to select a type of miner #
Cpu_Chain_btn = tk.Button(
    main_window,
    text="Cpu-Chain",
    bg="red",
    fg="white",
    command=Cpu_chain_button_click,
    state=None,
    pady=15,
    padx=20,
)
# Will only activate if all fields are filled out but once they are the program will run #
start_mining_btn = tk.Button(
    main_window,
    text="Start Mining",
    bg="green",
    fg="white",
    command=start_mining,
    pady=15,
    padx=20,
)
# Opens up a webbrowser page that will display miner details #
check_rewards_btn = tk.Button(
    main_window,
    text="Check Rewards",
    bg="red",
    fg="white",
    command=check_rewards,
    pady=15,
    padx=15,
)
# Dsiplays an external page that includes instructions for the program #
check_version = tk.Button(
    main_window,
    text="Latest Updates",
    bg="red",
    fg="white",
    command=version_page,
    padx=10,
)
# Defines worker name entry field #
workername = tk.StringVar()
workername_entry = tk.Entry(main_window, textvariable=workername)
workername_btn = tk.Button(
    main_window,
    text="Submit Name",
    bg="red",
    fg="white",
    command=submit_workername,
    padx=5,
)
workername_label = tk.Label(main_window, text=" Worker Name:", padx=15)
# Creates the Uncheck button to return all of the buttons to normal #
uncheck_btn = tk.Button(
    main_window, text="Uncheck", command=uncheck_command, bg="red", fg="white", padx=18
)

warning_label = tk.Label(
    main_window,
    text="To Keep Our Project Free Of Charge.\n Every 3 Hours 15 Minutes Will Be Donated To The Project.\n Thank You For Mining With InstaMiner\n\n YOU HAVE BEEN WARNED.",
    bg="black",
    fg="white",
).place(x=5, y=230)

threadcount_entry.place(x=185, y=113)
workername_entry.place(x=185, y=150)
user_wallet_entry.place(x=185, y=73)

workername_btn.place(x=315, y=150)
threadcount_btn.place(x=315, y=110)
user_wallet_btn.place(x=315, y=70)
uncheck_btn.place(x=315, y=190)

workername_label.place(x=50, y=150)
thread_count_label.place(x=50, y=113)
wallet_address_label.place(x=50, y=73)

check_version.place(x=0, y=500)
version.place(x=115, y=505)
developer.place(x=0, y=470)

check_rewards_btn.place(x=130, y=335)
start_mining_btn.place(x=10, y=335)

Sugar_chain_btn.place(x=15, y=5)
Cpu_Chain_btn.place(x=135, y=5)

main_window.mainloop()
