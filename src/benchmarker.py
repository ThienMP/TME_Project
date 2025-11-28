'''
Objective: To measure performance & efficiency of the existing public pre-trained model

Provided functions:
Nsight Measuremnt Section
+ This section is meant for running Nsight system/compute only enable it when needed.

Efficency Measurement
+ This section is to run code carbon and py Joules only enable individual that needed.

Hardware performance
+ For Nvidia Smi and NVML check. 

'''
import threading
from model_System import model_Runner
from measurement import measurement_Tools


#---------- MODEL LIST ----------#
models = [
    # BERT (uncased)
    "google-bert/bert-base-uncased", #110M
    "google-bert/bert-large-uncased", #340M

    # LLaMA (Meta)
    "meta-llama/Llama-2-7b-hf", #7B
    "meta-llama/Llama-2-13b-hf", #13B
    #"meta-llama/Llama-2-70b-hf" #70B
    #"meta-llama/Llama-3.1-405B", #405B

    # Mamba
    "state-spaces/mamba-130m", #130M
    "state-spaces/mamba-370m", #370M
    "state-spaces/mamba-790m", #790M
    "state-spaces/mamba-1.4b", #1.4B
    "state-spaces/mamba-2.8b", #2.8B

    # Falcon
    "tiiuae/falcon-7b", #7b
    #"tiiuae/falcon-40b", #40B
    #"tiiuae/falcon-180b", #180B

    # Mistral
    "mistralai/Mistral-7B-v0.1", #7B
    #"mistralai/Mixtral-8x7B-v0.1", #45B
    #"mistralai/Mixtral-8x22B-v0.1", #140B
    #"mistralai/Mistral-Large-Instruct-2407", #123B

    # Qwen3
    #"Qwen/Qwen3-235B-A22B", 235B-22B

    # DeepSeek unable to load and run

    # Gemma (Google)
    "google/gemma-2b",#2B
    "google/gemma-2-9b", #9B
    #"google/gemma-3-27b-it", #27B

    # Phi (Microsoft)
    "microsoft/phi-2", #2.7B
    "microsoft/phi-3-small-8k-instruct", #7B
    "microsoft/phi-3-medium-128k" #14B
]

if __name__ == "__main__":
    
    
    key = PLEASE PUT YOUR HUGGING FACE TOKEN HERE


    get_measure = measurement_Tools()
    current_Model = model_Runner(key, models[9])
    
    #Nsight Measuremnt section
    #falcon7b.run_Model()
    
    #Efficiency Measurement Section
    #code_Carbon_Tracker = get_measure.code_Carbon(current_Model.run_Model)
    #py_Joules_Tracker = get_measure.py_Joules(current_Model.run_Model)
    

    #Hardware Performance Measurement Section
    '''
    thread = []
    report_Output = threading.Thread(target=get_measure.report_Hardware)
    model_Thread = threading.Thread(target=current_Model.run_Model)

    report_Output.start()
    model_Thread.start()

    report_Output.join()
    model_Thread.join()
    '''


    




