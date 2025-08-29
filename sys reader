import platform
import psutil

def system_info():
    print("💻 System Information")
    print("OS:", platform.system(), platform.release())
    print("Processor:", platform.processor())
    print("CPU Cores:", psutil.cpu_count(logical=True))
    print("Memory:", round(psutil.virtual_memory().total / (1024**3), 2), "GB")

system_info()
