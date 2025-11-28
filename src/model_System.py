#Import
import os, torch
from huggingface_hub import login
from transformers import AutoTokenizer, pipeline, AutoModelForCausalLM


class model_Runner:
    def __init__(self, login_Key, given_Model, quantization = True):
        self.hf_Key = login_Key
        self.model = given_Model
        self.quantization = quantization

    def run_Model(self):
        
        #Model and Device variable
        current_Model = self.model
        print(f"Model Confirm: {current_Model}")

        #Hugging Face login
        login(token=self.hf_Key)

        #Ensure the system is load in GPU prevent load everything in CPU
        if torch.cuda.is_available():
            torch.cuda.init()
            torch.rand(1).cuda()
            
            #Confirm GPU exist
            print("GPU is available and recognized")
            print(f"Number of CUDA devices: {torch.cuda.device_count()}")
            print(f"CUDA device name: {torch.cuda.get_device_name(0)}")

            #Tokenizer
            get_Tokennizer = AutoTokenizer.from_pretrained(current_Model, use_fast = False)

            #Load model
            if self.quantization == False:
                get_Model = AutoModelForCausalLM.from_pretrained(current_Model, device_map = "auto")
            else:
                get_Model = AutoModelForCausalLM.from_pretrained(current_Model, device_map = "auto", load_in_8bit=True ) 

            #set the pad_token_id for the model
            get_Model.config.pad_token_id = get_Tokennizer.eos_token_id

            generator = pipeline(
                'text-generation', 
                model = get_Model, 
                tokenizer = get_Tokennizer,
                device_map="auto")

             
            # os.system('cls') #Comment this out if you wish to see the setup setting

            print("CUDA available:", torch.cuda.is_available())
            print("Current device:", torch.cuda.get_device_name(0))
            print("Memory allocated:", torch.cuda.memory_allocated()/1024**2, "MB")
            print("Memory reserved:", torch.cuda.memory_reserved()/1024**2, "MB")


            while True:
                prompt = input("Enter Text (q to exit): ")
                if prompt.strip().lower() == "q":
                    print("Exiting program...")
                    break

                output = generator(prompt, max_new_tokens=256)
                print("\nGenerated:")
                print(output[0]["generated_text"])
                print("\n----------------------------------\n")


        else:
            print("ERROR: UNABLE TO LOCATED GPU")


            

