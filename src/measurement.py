'''
Objective of class: Measurement tools for ML efficiency

Function:
- Nvidia-smi
- Nvidia-nvml
- Codecarbon
- pyJoules
- Nsight System
- Nsight Compute
'''
#import
import os
import time
import pynvml
import subprocess
from codecarbon import EmissionsTracker
from pyJoules.energy_meter import EnergyContext
from pyJoules.handler.csv_handler import CSVHandler
from pyJoules.device.nvidia_device import NvidiaGPUDomain

class measurement_Tools:

    def __init__(self, output_dir="output"):
        # Ensure the output folder exists
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

#--------------------------------------------------------------------------------- Nvidia SMI
    def nvidia_Smi(self):
        #This is for if you want to run the SMI by itself.
        '''
        subprocess.Popen(
            'start cmd /k "nvidia-smi -l 3"',
            shell=True
        )
        '''
        result = subprocess.run(
            ["nvidia-smi"],
            capture_output=True,
            text=True
        )
        return result.stdout
    
#--------------------------------------------------------------------------------- Nvidia NVML   
    def nvidia_Nvml(self):
            pynvml.nvmlInit()
            device_Count = pynvml.nvmlDeviceGetCount()
            performance_Stat = [] #performance GPU list

            #for very GPU on the system. Perform a check
            for gpu_Index in range(device_Count):
                current_GPU = pynvml.nvmlDeviceGetHandleByIndex(gpu_Index)

                #GPU Util (%)
                get_Utilstat = pynvml.nvmlDeviceGetUtilizationRates(current_GPU)
                gpu_Util = get_Utilstat.gpu
                memory_Util = get_Utilstat.memory

                #memory usage (MB)
                get_Memoryinfo = pynvml.nvmlDeviceGetMemoryInfo(current_GPU)
                memory_Total = get_Memoryinfo.total / 1024**2
                memory_Used = get_Memoryinfo.used / 1024**2
                memory_Free = get_Memoryinfo.free / 1024**2

                #power comsumption (Watts)
                power_Consumption = pynvml.nvmlDeviceGetPowerUsage(current_GPU) / 1000

                #Temperature (C)
                temperature_Stat = pynvml.nvmlDeviceGetTemperature(current_GPU, pynvml.NVML_TEMPERATURE_GPU)

                #Add the perfromance stat
                performance_Stat.append({
                    "GPU Index" : gpu_Index,
                    "GPU Util (%)": gpu_Util,
                    "Memory Util (%)": memory_Util,
                    "Memory Used (MB)": memory_Used,
                    "Memory Free (MB)": memory_Free,
                    "Memory Total (MB)": memory_Total,
                    "Power (W)": power_Consumption,
                    "Temperature (C)": temperature_Stat,
                })
            pynvml.nvmlShutdown()
            return performance_Stat
    
#--------------------------------------------------------------------------------- code carbon
    def code_Carbon(self, func, *args, **kwargs):
        # Create tracker with output_dir
        tracker = EmissionsTracker(
            log_level='warning', #Change this label "info, warning, or critical to your needed"
            output_dir=self.output_dir  #save output to the output folder
        )

        tracker.start()
        result = func(*args, **kwargs)
        tracker.stop()  # kg CO2
        return result

#--------------------------------------------------------------------------------- py joules
    def py_Joules(self, func, *args, **kwargs):
        # CSV in output folder
        csv_path = os.path.join(self.output_dir, "pyJoules_log.csv")
        csv_handler = CSVHandler(csv_path)

        # Run the function inside EnergyContext
        with EnergyContext(handler=csv_handler,
                           domains=[ NvidiaGPUDomain(0)],
                           start_tag=func.__name__) as ctx:
            result = func(*args, **kwargs)  # Call the function normally
            ctx.record(tag=f'{func.__name__}_end')  # Optional extra record

        # Save CSV
        csv_handler.save_data()

        # Return function's result
        return result
    
#--------------------------------------------------------------------------------- report Hardware

    def report_Hardware (self):
        subprocess.Popen('start cmd /k python -c "from measurement import measurement_Tools; measurement_Tools().report()"', shell=True)

    def report(self):
        try:
            report_Index = 0
            while True:
                print (f"\n***************************************")
                print (f"--- REPOT START - REPORT {report_Index} ---")
                print (f"\n***************************************")
                #SMI REPORT
                print("-------------------- SMI REPORT --------------------\n")

                print(self.nvidia_Smi())

                print("-"*55 + "\n")

                #NVML REPORT
                print("-------------------- NVML REPORT --------------------\n")

                nvml_stats = self.nvidia_Nvml() # returns a list of dicts
                for stat in nvml_stats:
                    print(f"GPU: {stat['GPU Index']}")
                    print(f"GPU Utilization: {stat['GPU Util (%)']}% | Memory Usage: {stat['Memory Used (MB)']:.1f}/{stat['Memory Total (MB)']:.1f} MB | Power: {stat['Power (W)']:.1f} W")
                    print("-"*20)

                print("-"*55 + "\n")

                print (f"\n***************************************")
                print (f"--- REPOT END - REPORT {report_Index} ---")
                print (f"***************************************\n")
                report_Index = report_Index + 1

                time.sleep(3) #update every 3 second 
        except KeyboardInterrupt:
            print("Measurement End")