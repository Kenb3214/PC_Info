# PC_Info(version = 1.9)
一個查看電腦硬件的程式.

# PC_useing
小窗口看使用率.
# PC_Info_setting.ini
-main
 - language = ENG/CN(自定義要與文件名一樣，例language = XXX要XXX.json XXX要一樣)
 - encoding = auto(auto只適用於ENG/CN,自定義要改變格式)
 - update_time = 1(1-5s)
 - pc_using = app/local(app=PC_Info.bat to open PC_using.exe,local is call samllmain() in PC_Info.py)

-small_windows
 - update_time = 2(1-5s)
 - at_top = True(at top/是否一直置頂)
# Note
 - 目前只可在Windows上使用(wmi)
# Update Log
 - 2025/9/20 1.0 Start
 - 2025/10/12 1.5 add PC Info can get txt file
 - 2025/11/27 1.8 add NVML GPU Temperature and PC using
 - 2026/3/10 1.81 上線/Upload to Github
 - 2026/3/13 1.9 將語言模塊從主程式寫死改成json文件
# 主要依賴
 - python==3.14
 - nvidia-ml-py==13.590.48
 - psutil==7.2.2
 - py-cpuinfo==9.0.0
 - pynvml==13.0.1
 - WMI==1.5.1