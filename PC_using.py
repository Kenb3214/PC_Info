import tkinter as tk
from tkinter import messagebox
import sys,os
import configparser
import psutil
import pynvml
import threading
import time
import datetime

try:
    config = configparser.ConfigParser()
    config.read('PC_Info_setting.ini', encoding='utf-8')
    upd2 = config['small_windows']['update_time']
    top = config['small_windows']['at_top']
except:
    tk.messagebox.showerror("Error","Error to read PC_Info.ini")

try:
    def main():
        samllroot = tk.Tk()
        samllroot.title("PC useing")
        samllroot.geometry("200x100")
        if top == True:
            samllroot.attributes("-topmost", True)
        elif top == False:
            samllroot.attributes("-topmost", False)
        else:
            samllroot.attributes("-topmost", True)
        cpu_label = tk.Label(samllroot, text="CPU use (%): ...")
        cpu_label.grid(row=0, column=0, columnspan=2)
        ram_label = tk.Label(samllroot, text="RAM use (%): ...")
        ram_label.grid(row=1, column=0, columnspan=2)
        gpu_label = tk.Label(samllroot, text="GPU RAM use (%): ...")
        gpu_label.grid(row=3, column=0, columnspan=2)
        gpu_mb_label = tk.Label(text="GPU RAM use (MB): ...")
        gpu_mb_label.grid(row=4, column=0, columnspan=2)

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
                    gpu_mb_label.config(text=f"GPU RAM: {mem.used / 1024 ** 2:.0f} / {mem.total / 1024 ** 2:.0f} MB")
                except pynvml.NVMLError:
                    gpu_label.config(text="GPU RAM (%): not available")
                    gpu_mb_label.config(text="GPU RAM use (MB): not available")
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

        tk.Button(samllroot, text="exit", command=samllroot.destroy).grid(pady=4)

        samllroot.mainloop()
except:
    tk.messagebox.showerror("Error", "Error start PC_useing.exe")

if __name__ == "__main__":
    main()