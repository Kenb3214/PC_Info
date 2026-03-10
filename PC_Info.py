import tkinter as tk
from tkinter import messagebox
import sys,os
import configparser
import psutil
import platform
import cpuinfo
import wmi
import pynvml
import subprocess
import threading #not use now
from setuptools import setup, Extension
import ctypes #not use now
import time
import datetime
import random

def check_already_running():
    current = psutil.Process().pid
    for p in psutil.process_iter(['pid','name']):
        if p.info['name'] == "PC_Info.exe" and p.info['pid'] != current:
            return True
    return False
if check_already_running():
    sys.exit("Already running")

try:
    try:
        config = configparser.ConfigParser()
        config.read('PC_Info_setting.ini', encoding='utf-8')
    except:
        file = open('error_log.txt', 'a')
        file.write(f"\n{datetime.datetime.now()}PC_Info_setting.ini not found")
        file.close()
        tk.messagebox.showerror('Error', 'PC_Info_setting.ini not found')
        sys.exit()

    try:
        Version = config['main']['Version']
    except:
        tk.messagebox.showerror('Error', 'PC_Info_setting.ini load Version error')
    try:
        lang = config['main']['language']
    except:
        tk.messagebox.showerror('Error', 'PC_Info_setting.ini load Language error')
    try:
        upd = config['main']['update_time']
    except:
        tk.messagebox.showerror('Error', 'PC_Info_setting.ini load main Update time error')
    try:
        upd2 = config['small_windows']['update_time']
    except:
        tk.messagebox.showerror('Error', 'PC_Info_setting.ini load small windows error')
    try:
        runin = config['main']['pc_using']
    except:
        tk.messagebox.showerror('Error', 'PC_Info_settng.ini load pc useing error')
    try:
        dickch = config['main']['main_disk_info']
    except:
        tk.messagebox.showerror('Error', 'PC_Info_setting.ini load disk info error')
    try:
        pyd = config['main']['pyd']
    except:
        tk.messagebox.showerror('Error', 'PC_Info_setting.ini load pyd error')
    try:
        diskcheck = config['main']['disk_check']
    except:
        tk.messagebox.showerror('Error', 'PC_Info_setting.ini load disk check error')

    try:
        (psutil.disk_usage(f'{dickch}:'))
    except:
        tk.messagebox.showerror('Error', 'ERROR PC_Info_setting.ini disk valid error')
        file = open('error_log.txt', 'a')
        file.write(f"\n{datetime.datetime.now()} disk valid error")
        file.close()
        sys.exit()

    if lang == "CN":
        bname = "主板是"
        makeby = "生產商是"
        OSis = "操作系統"
    elif lang == "ENG":
        bname = "Board is"
        makeby = "make by"
        OSis = "OS system"
    else:
        tk.messagebox.showerror("Error", "PC_Info_setting.ini Language error")
        file = open('error_log.txt', 'a')
        file.write(f"\n{datetime.datetime.now()} Language error")
        file.close()
        sys.exit()

    if pyd == True:
        try:
            setup(
                name="PC_Info",
                ext_modules=[Extension("PC_Info", ["PC_Info.c"])],
            )
        except:
            tk.messagebox.showerror("Error", "PC_Info.pyd setup error")
            file = open('error_log.txt', 'a')
            file.write(f"\n{datetime.datetime.now()} PC_Info setup error error")
            file.close()

    if diskcheck == True:
        try:
            diskname = ["ABCDEFGHIGKLMNOPQRST"]
            for x in diskname:
                psutil.disk_usage(f'{x}:')
            else:
                tk.messagebox.showerror("Error", "NULL")
        except:
            tk.messagebox.showerror("Error", "disk check error error")
    try:
        psutil.disk_usage('D:')
        diskD = True
    except:
        diskD = False
    try:
        psutil.disk_usage('E:')
        diskE = True
    except:
        diskE = False
    try:
        psutil.disk_usage('F:')
        diskF = True
    except:
        diskF = False
    try:
        psutil.disk_usage('G:')
        diskG = True
    except:
        diskG = False
    try:
        psutil.disk_usage('H:')
        diskH = True
    except:
        diskH = False
    try:
        psutil.disk_usage('I:')
    except:
        diskI = False
    try:
        psutil.disk_usage('J:')
        diskJ = True
    except:
        diskJ = False
    try:
        psutil.disk_usage('K:')
        diskK = True
    except:
        diskK = False
    try:
        psutil.disk_usage('L:')
        diskL = True
    except:
        diskL = False
    try:
        psutil.disk_usage('M:')
        diskM = True
    except:
        diskM = False
    try:
        psutil.disk_usage('N:')
        diskN = True
    except:
        diskN = False
except:
    tk.messagebox.showerror("ERROR","Start up ERROR")

def main():

 root = tk.Tk()
 root.title("PC Info v1.7")
 root.geometry("540x525")

 if dickch == "C": #Disk
     alldick = (psutil.disk_usage('/'))  # disk
     dC = (psutil.disk_usage('C:'))  # disk
     dickthing = f"{round(dC.used / (1024 ** 3), 4)}GB / {round(dC.total / (1024 ** 3), 4)}GB free = {round(dC.free / (1024 ** 3), 4)}GB used = {dC.percent} %"
     if dC.percent > 85:
         if lang == "ENG":
             CDlang = "Disk C"
             poC = "disk C is full,more then 85%"
         elif lang == "CN":
             CDlang = "本機磁碟C"
             poC = "本機磁碟C 滿了，佔用大於85%"
     elif dC.percent < 10:
         if lang == "ENG":
             CDlang = "Disk C"
             poC = "disk C is now,less then 10%"
         elif lang == "CN":
             CDlang = "本機磁碟C"
             poC = "CDlang = 本機磁碟C 很新，佔用小於10%"
     else:
         if lang == "ENG":
             CDlang = "Disk C"
             poC = "disk C is good"
         else:
             CDlang = "本機磁碟C"
             poC = "本機磁碟C 很好"

 else:
     othdick = (psutil.disk_usage(f'{dickch}:'))
     dickthing = f"{round(othdick.used / (1024 ** 3), 4)}GB / {round(othdick.total / (1024 ** 3), 4)}GB free = {round(othdick.free / (1024 ** 3), 4)}GB used = {othdick.percent} %"
     if othdick.percent > 85:
         if lang == "ENG":
             CDlang = f"Disk {dickch}"
             poC = f"disk {dickch} is full,more then 85%"
         elif lang == "CN":
             poC = f"新增磁碟{dickch} 滿了，佔用大於85%"
     elif othdick.percent < 10:
         if lang == "ENG":
             CDlang = f"Disk {dickch}"
             poC = f"dick {dickch} is now,less then 10%"
         elif lang == "CN":
             poC = f"新增磁碟{dickch} 很新，佔用小於10%"
     else:
         if lang == "ENG":
             CDlang = f"Disk {dickch}"
             poC = f"disk {dickch} is good"
         else:
             CDlang = f"新增磁碟{dickch}"
             poC = f"新增磁碟{dickch} 很好"
 cpu_info = cpuinfo.get_cpu_info()
 v_core = psutil.cpu_count()
 real_core = psutil.cpu_count(logical=False)
 try: #WMI
     pc = wmi.WMI()
     gpu_info = pc.Win32_VideoController()[0].name
     board_info = pc.Win32_BaseBoard()[0].product
     board_make_by = pc.Win32_BaseBoard()[0].manufacturer
     bios_info = pc.Win32_BIOS()[0].name
     bios_make_by = pc.Win32_BIOS()[0].manufacturer
 except :
     gpu_info = "GPU not available"
     board_info = "unknown"
     board_make_by = "unknown"
     bios_info = "unknown"
     bios_make_by = "unknown"

 tk.Label(root, text="PC Info").grid(row=0, column=0)
 tk.Label(root, text=f"{bname} {board_info} make by {board_make_by} \nBIOS version is {bios_info} {makeby} {bios_make_by}").grid(row=1, column=0)
 tk.Label(root, text=f"{OSis} : {platform.platform()}").grid(row=2, column=0)
 tk.Label(root, text=f"CPU is {cpu_info['brand_raw']} virtual core :{v_core} real core :{real_core} arch : {cpu_info['arch']}").grid(row=3, column=0)
 tk.Label(root, text=f"GPU is {gpu_info}").grid(row=4, column=0)
 tk.Label(root, text=f"{CDlang}  : {dickthing} , {poC}").grid(row=5, column=0)

 cpu_label = tk.Label(root, text="CPU use (%): ...")
 cpu_label.grid(row=6, column=0, columnspan=2)
 ram_label = tk.Label(root, text="RAM use (%): ...")
 ram_label.grid(row=7, column=0, columnspan=2)
 ram_gb_label = tk.Label(root, text="RAM use (GB): ...")
 ram_gb_label.grid(row=8, column=0, columnspan=2)
 gpu_label = tk.Label(root, text="GPU RAM use (%): ...")
 gpu_label.grid(row=9, column=0, columnspan=2)
 gpu_gb_label = tk.Label(root, text="GPU RAM use (GB): ...")
 gpu_gb_label.grid(row=10, column=0, columnspan=2)

 try:
     pynvml.nvmlInit()
     gpu_available = True
 except pynvml.NVMLError:
     gpu_available = False

 def update_stats():
     try:
         cpu = psutil.cpu_percent(interval=0,percpu=True)
         cpu_label.config(text=f"CPU use (%): {cpu}")
     except:
         tk.messagebox.showerror("Error", "Error CPU update ERROR")
         file = open('error_log.txt', 'a')
         file.write(f"\n{datetime.datetime.now()} CPU update ERROR")
         file.close()
     try:
         ram = psutil.virtual_memory()
         outlookram = f"{ram.total / 1024 / 1024 / 1024:.2f}"
         ram_label.config(text=f"RAM use (%): {ram.percent}")
         ram_gb_label.config(text=f"RAM use : {round(ram.used / 1e9, 2)} / {outlookram} GB ( GB)")
     except:
         tk.messagebox.showerror("Error", "Error RAM update ERROR")
     if gpu_available:
         try:
             handle = pynvml.nvmlDeviceGetHandleByIndex(0)
             mem = pynvml.nvmlDeviceGetMemoryInfo(handle)
             util = pynvml.nvmlDeviceGetUtilizationRates(handle)
             temperature = pynvml.nvmlDeviceGetTemperature(handle, pynvml.NVML_TEMPERATURE_GPU)
             gpu_label.config(text=f"GPU useing (%): {util.gpu}%")
             gpu_gb_label.config(text=f"GPU RAM use (MB): {mem.used / 1024 ** 2:.0f} / {mem.total / 1024 ** 2:.0f} MB\nGPU RAM use (GB): {mem.used / 1024 ** 3:.0f} / {mem.total / 1024 ** 3:.0f} GB\nGPU temperature : {temperature}'C")
             config['test'] = {'GPU_test': 'late update'}
             with open('PC_Info_setting.ini', 'w') as configfile:
                 config.write(configfile)
         except pynvml.NVMLError:
             gpu_label.config(text="GPU RAM (%): not available")
             gpu_gb_label.config(text="GPU RAM (GB): not available")
             config['test'] = {'GPU_test': 'False'}
             with open('PC_Info_setting.ini', 'w') as configfile:
                config.write(configfile)
     else:
         gpu_label.config(text="GPU RAM (%): not available")
         gpu_gb_label.config(text="GPU RAM (GB): not available\nGPU RAM use (MB): not available\nGPU temperature : not available")

     if upd == "1":
         root.after(1000, update_stats)
     elif upd == "2":
      root.after(2000, update_stats)
     elif upd == "3":
         root.after(3000, update_stats)
     elif upd == "4":
         root.after(4000, update_stats)
     elif upd == "5":
         root.after(5000, update_stats)
     else:
         tk.messagebox.showerror("Error", "PC_Info_setting.ini Update time error")


 # 啟動第一次更新
 update_stats()

 def test_again():
     PC_test()
 def PC_test(): #CPU GPU test
     def PC_test_again():
         test_again()
         PC_test.destroy()
     PC_test = tk.Toplevel()
     PC_test.title("cpu/gpu test")
     PC_test.geometry("200x200")
     tk.Label(PC_test, text="cpu/gpu test ").grid(row=0, column=0)
     cpusttime = time.time()
     count = 0
     while True:
         n1 = random.randint(1111111111111111111111111111111111111111, 9999999999999999999999999999999999999999)
         n2 = random.randint(1111111111111111111111111111111111111111, 9999999999999999999999999999999999999999)
         n3 = random.randint(1111111111111111111111111111111111111111, 9999999999999999999999999999999999999999)
         n4 = random.randint(1111111111111111111111111111111111111111, 9999999999999999999999999999999999999999)
         n5 = random.randint(1111111111111111111111111111111111111111, 9999999999999999999999999999999999999999)
         n6 = random.randint(1111111111111111111111111111111111111111, 9999999999999999999999999999999999999999)
         n7 = random.randint(1111111111111111111111111111111111111111, 9999999999999999999999999999999999999999)
         n8 = random.randint(1111111111111111111111111111111111111111, 9999999999999999999999999999999999999999)
         n9 = random.randint(1111111111111111111111111111111111111111, 9999999999999999999999999999999999999999)
         n10 = random.randint(1111111111111111111111111111111111111111, 9999999999999999999999999999999999999999)
         cputest1 = n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8 * n9 * n10
         cputest2 = n1 // n2 // n3 // n4 // n5 // n6 // n7 // n8 // n9 // n10
         count += 1
         if count >= 999:
             break
     cpuextime = time.time()
     tk.Label(PC_test, text=f"CPU test(random math): {cpuextime - cpusttime:.6f}").grid(row=1, column=0)
     tk.Label(PC_test, text=f"GPU test(random math): late update").grid(row=2, column=0) #update late
     tk.Button(PC_test, text="test again", command=PC_test_again).grid(row=3, column=0)

 def Disk_Info():
     alldiskInfo = tk.Toplevel()
     alldiskInfo.title("Disk usering")
     alldiskInfo.geometry("400x200")
     tk.Label(alldiskInfo, text="Disk usering").grid(row=0, column=0)
     tk.Label(alldiskInfo, text=f"Disk C :{round(dC.used / (1024 ** 3), 4)}GB / {round(dC.total / (1024 ** 3), 4)}GB free = {round(dC.free / (1024 ** 3), 4)}GB used = {dC.percent} %").grid(row=1, column=0)
     if diskD == True:
         dD = psutil.disk_usage('D:')
         tk.Label(alldiskInfo,text=f"Disk D :{round(dD.used / (1024 ** 3), 4)}GB / {round(dD.total / (1024 ** 3), 4)}GB free = {round(dD.free / (1024 ** 3), 4)}GB used = {dD.percent} %").grid(row=2, column=0)
     if diskE == True:
         dE = psutil.disk_usage('E:')
         tk.Label(alldiskInfo,text=f"Disk E :{round(dE.used / (1024 ** 3), 4)}GB / {round(dE.total / (1024 ** 3), 4)}GB free = {round(dE.free / (1024 ** 3), 4)}GB used = {dE.percent} %").grid(row=3, column=0)
     if diskF == True:
         dF = psutil.disk_usage('F:')
         tk.Label(alldiskInfo,text=f"Disk F :{round(dF.used / (1024 ** 3), 4)}GB / {round(dF.total / (1024 ** 3), 4)}GB free = {round(dF.free / (1024 ** 3), 4)}GB used = {dF.percent} %").grid(row=4, column=0)
     if diskG == True:
         dG = psutil.disk_usage('G:')
         tk.Label(alldiskInfo,text=f"Disk G :{round(dG.used / (1024 ** 3), 4)}GB / {round(dG.total / (1024 ** 3), 4)}GB free = {round(dG.free / (1024 ** 3), 4)}GB used = {dG.percent} %").grid(row=5, column=0)
     if diskH == True:
         dH = psutil.disk_usage('H:')
         tk.Label(alldiskInfo,text=f"Disk H :{round(dH.used / (1024 ** 3), 4)}GB / {round(dH.total / (1024 ** 3), 4)}GB free = {round(dH.free / (1024 ** 3), 4)}GB used = {dH.percent} %").grid(row=6, column=0)
     if diskI == True:
         dI = psutil.disk_usage('I:')
         tk.Label(alldiskInfo,text=f"Disk I :{round(dI.used / (1024 ** 3), 4)}GB / {round(dI.total / (1024 ** 3), 4)}GB free = {round(dI.free / (1024 ** 3), 4)}GB used = {dI.percent} %").grid(row=7, column=0)
     if diskJ == True:
         dJ = psutil.disk_usage('J:')
         tk.Label(alldiskInfo,text=f"Disk J :{round(dJ.used / (1024 ** 3), 4)}GB / {round(dJ.total / (1024 ** 3), 4)}GB free = {round(dJ.free / (1024 ** 3), 4)}GB used = {dJ.percent} %").grid(row=8, column=0)
     if diskK == True:
         dK = psutil.disk_usage('K:')
         tk.Label(alldiskInfo,text=f"Disk K :{round(dK.used / (1024 ** 3), 4)}GB / {round(dK.total / (1024 ** 3), 4)}GB free = {round(dK.free / (1024 ** 3), 4)}GB used = {dK.percent} %").grid(row=9, column=0)
     if diskL == True:
         dL = psutil.disk_usage('L:')
         tk.Label(alldiskInfo,text=f"Disk L :{round(dL.used / (1024 ** 3), 4)}GB / {round(dL.total / (1024 ** 3), 4)}GB free = {round(dL.free / (1024 ** 3), 4)}GB used = {dL.percent} %").grid(row=10, column=0)
     if diskM == True:
         dM = psutil.disk_usage('M:')
         tk.Label(alldiskInfo,text=f"Disk M :{round(dM.used / (1024 ** 3), 4)}GB / {round(dM.total / (1024 ** 3), 4)}GB free = {round(dM.free / (1024 ** 3), 4)}GB used = {dM.percent} %").grid(row=11, column=0)
     if diskN == True:
         dN = psutil.disk_usage('N:')
         tk.Label(alldiskInfo,text=f"Disk N :{round(dN.used / (1024 ** 3), 4)}GB / {round(dN.total / (1024 ** 3), 4)}GB free = {round(dN.free / (1024 ** 3), 4)}GB used = {dN.percent} %").grid(row=12, column=0)

 def txtfile():
     try:
         pcram = psutil.virtual_memory()
         try:
             dCtxt = f"Disk C :{round(dC.used / (1024 ** 3), 4)}GB / {round(dC.total / (1024 ** 3), 4)}GB free = {round(dC.free / (1024 ** 3), 4)}GB used = {dC.percent} %"
             if diskD == True:
                 dD = psutil.disk_usage('D:')
                 dDtxt = f"Disk D :{round(dD.used / (1024 ** 3), 4)}GB / {round(dD.total / (1024 ** 3), 4)}GB free = {round(dD.free / (1024 ** 3), 4)}GB used = {dD.percent} %"
             else:
                 dDtxt = " "
             if diskE == True:
                 dE = psutil.disk_usage('E:')
                 dEtxt = f"Disk E :{round(dE.used / (1024 ** 3), 4)}GB / {round(dE.total / (1024 ** 3), 4)}GB free = {round(dE.free / (1024 ** 3), 4)}GB used = {dE.percent} %"
             else:
                 dEtxt = " "
             if diskF == True:
                 dF = psutil.disk_usage('F:')
                 dFtxt = f"Disk F :{round(dF.used / (1024 ** 3), 4)}GB / {round(dF.total / (1024 ** 3), 4)}GB free = {round(dF.free / (1024 ** 3), 4)}GB used = {dF.percent} %"
             else:
                 dFtxt = " "
             if diskG == True:
                 dG = psutil.disk_usage('G:')
                 dGtxt = f"Disk G :{round(dG.used / (1024 ** 3), 4)}GB / {round(dG.total / (1024 ** 3), 4)}GB free = {round(dG.free / (1024 ** 3), 4)}GB used = {dG.percent} %"
             else:
                 dGtxt = " "
             if diskH == True:
                 dH = psutil.disk_usage('H:')
                 dHtxt = f"Disk H :{round(dH.used / (1024 ** 3), 4)}GB / {round(dH.total / (1024 ** 3), 4)}GB free = {round(dH.free / (1024 ** 3), 4)}GB used = {dH.percent} %"
             else:
                 dHtxt = " "
             if diskI == True:
                 dI = psutil.disk_usage('I:')
                 dItxt = f"Disk I :{round(dI.used / (1024 ** 3), 4)}GB / {round(dI.total / (1024 ** 3), 4)}GB free = {round(dI.free / (1024 ** 3), 4)}GB used = {dI.percent} %"
             else:
                 dItxt = " "
             if diskJ == True:
                 dJ = psutil.disk_usage('J:')
                 dJtxt = f"Disk J :{round(dJ.used / (1024 ** 3), 4)}GB / {round(dJ.total / (1024 ** 3), 4)}GB free = {round(dJ.free / (1024 ** 3), 4)}GB used = {dJ.percent} %"
             else:
                 dJtxt = " "
             if diskK == True:
                 dK = psutil.disk_usage('K:')
                 dKtxt = f"Disk K :{round(dK.used / (1024 ** 3), 4)}GB / {round(dK.total / (1024 ** 3), 4)}GB free = {round(dK.free / (1024 ** 3), 4)}GB used = {dK.percent} %"
             else:
                 dKtxt = " "
             if diskL == True:
                 dL = psutil.disk_usage('L:')
                 dLtxt = f"Disk L :{round(dL.used / (1024 ** 3), 4)}GB / {round(dL.total / (1024 ** 3), 4)}GB free = {round(dL.free / (1024 ** 3), 4)}GB used = {dL.percent} %"
             else:
                 dLtxt = " "
             if diskM == True:
                 dM = psutil.disk_usage('M:')
                 dMtxt = f"Disk M :{round(dM.used / (1024 ** 3), 4)}GB / {round(dM.total / (1024 ** 3), 4)}GB free = {round(dM.free / (1024 ** 3), 4)}GB used = {dM.percent} %"
             else:
                 dMtxt = " "
             if diskN == True:
                 dN = psutil.disk_usage('N:')
                 dNtxt = f"Disk N :{round(dN.used / (1024 ** 3), 4)}GB / {round(dN.total / (1024 ** 3), 4)}GB free = {round(dN.free / (1024 ** 3), 4)}GB used = {dN.percent} %"
             else:
                 dNtxt = " "
             Disktext = f"{dCtxt}\n{dDtxt}\n{dEtxt}\n{dFtxt}\n{dGtxt}\n{dHtxt}\n{dItxt}\n{dJtxt}\n{dKtxt}\n{dLtxt}\n{dMtxt}\n{dNtxt} "
         except:
             tk.messagebox.showerror("Error", "save disk file error")
             file = open('error_log.txt', 'a')
             file.write(f"\n{datetime.datetime.now()} save disk file error")
             file.close()
             sys.exit()
         try:
             handle = pynvml.nvmlDeviceGetHandleByIndex(0)
             mem = pynvml.nvmlDeviceGetMemoryInfo(handle)
             gpuram = f"{mem.total / 1024 ** 3:.0f}"
         except:
             gpuram = "None"
         file = open("about PC.txt", "w")
         file.write(f"about you PC by PC_Info v{Version} \n{bname} {board_info} make by {board_make_by} BIOS version is {bios_info} {makeby} {bios_make_by} \n{OSis} : {platform.platform()} \nCPU is {cpu_info['brand_raw']} virtual core :{v_core} real core :{real_core} arch : {cpu_info['arch']}\nRAM is {pcram.total / 1024 / 1024 / 1024:.2f} GB \nGPU is {gpu_info}({gpuram} GB) \n{Disktext}")
         file.close()
         tk.messagebox.showinfo("PC Info", "about PC.txt saved in you PC")
     except:
         tk.messagebox.showerror("Error", "error to save ")
         file = open('error_log.txt', 'a')
         file.write(f"\n{datetime.datetime.now()} save error")
         file.close()

 def app():
    messagebox.showinfo("about this app",f"about this app\napp name: PC_Info\napp version: {Version}\nMake by: Kenb3214\nThis app in {(os.getcwd()) } \nlink:https://github.com/Kenb3214/PC_Info")
 def update_log():
    messagebox.showinfo("update log", f"Update.txt")
 def Useing():
     if runin == "app":
         try:
             subprocess.run(["PC_Info.bat"])
         except:
             tk.messagebox.showerror("Error", "error to start PC_useing.exe")
     elif runin == "local":
         samllmain()

 tk.Button(root, text="samll windows(PC useing)", command=Useing).grid(pady=5)
 tk.Button(root, text="All Disk useing", command=Disk_Info).grid(pady=5)
 tk.Button(root, text="cpu test", command=PC_test).grid(pady=5)
 tk.Button(root, text="about this app", command=app).grid(pady=5)
 tk.Button(root, text="update log", command=update_log).grid(pady=5)
 tk.Button(root, text="get txt file", command=txtfile).grid(pady=5)
 tk.Button(root, text="exit", command=root.destroy).grid(pady=5)

 root.mainloop()

def samllmain():
    def mainlink():
        main()
        samllroot.destroy()
    samllroot = tk.Tk()
    samllroot.title("PC useing")
    samllroot.geometry("200x100")
    samllroot.attributes("-topmost", True)
    cpu_label = tk.Label(samllroot, text="CPU use (%): ...")
    cpu_label.grid(row=0, column=0, columnspan=2)
    ram_label = tk.Label(samllroot, text="RAM use (%): ...")
    ram_label.grid(row=1, column=0, columnspan=2)
    gpu_label = tk.Label(samllroot, text="GPU RAM use (%): ...")
    gpu_label.grid(row=3, column=0, columnspan=2)

    try:
        pynvml.nvmlInit()
        gpu_available = True
    except pynvml.NVMLError:
        gpu_available = False

    def update_stats():
        try:
            cpu = psutil.cpu_percent(interval=0.1)
            cpu_label.config(text=f"CPU: {cpu}%")
        except:
            tk.messagebox.showerror("Error", "Error CPU update ERROR")
            file = open('error_log.txt', 'a')
            file.write(f"\n{datetime.datetime.now()} CPU update ERROR")
            file.close()
        try:
            ram = psutil.virtual_memory()
            ram_label.config(text=f"RAM: {ram.percent}%")
        except:
            tk.messagebox.showerror("Error", "Error RAM update ERROR")
        if gpu_available:
            try:
                handle = pynvml.nvmlDeviceGetHandleByIndex(0)
                mem = pynvml.nvmlDeviceGetMemoryInfo(handle)
                util = pynvml.nvmlDeviceGetUtilizationRates(handle)
                temperature = pynvml.nvmlDeviceGetTemperature(handle, pynvml.NVML_TEMPERATURE_GPU)
                gpu_label.config(text=f"GPU: {util.gpu}% {temperature}'C")
                config['test'] = {'GPU_test': 'late update'}
                with open('PC_Info_setting.ini', 'w') as configfile:
                    config.write(configfile)
            except pynvml.NVMLError:
                gpu_label.config(text="GPU RAM (%): not available")
                config['test'] = {'GPU_test': 'False'}
                with open('PC_Info_setting.ini', 'w') as configfile:
                    config.write(configfile)
        else:
            gpu_label.config(text="GPU(%): not available")
        if upd2 == "1":
            samllroot.after(100, update_stats)
        elif upd2 == "2":
            samllroot.after(200, update_stats)
        elif upd2 == "3":
            samllroot.after(300, update_stats)
        elif upd2 == "4":
            samllroot.after(400, update_stats)
        elif upd2 == "5":
            samllroot.after(500, update_stats)
        else:
            tk.messagebox.showerror("Error", "PC_Info_setting.ini Update time error")

    update_stats()

    tk.Button(samllroot,text="full windows",command=mainlink).grid(pady=4)

if __name__ == "__main__":
    main()