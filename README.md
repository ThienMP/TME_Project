Model Performance & Efficiency Measurement
==========================================

A Python simple program to measure performance and efficiency of various public pre-trained language models. 
The project provides tools for hardware profiling, energy consumption tracking, and optional Nsight GPU measurement.

Objective
---------
The goal of this project is to evaluate performance and efficiency of existing public pre-trained models across multiple metrics, including:

- Hardware utilization (GPU usage, memory, etc.)
- Energy consumption (CodeCarbon, PyJoules)
- Nsight GPU metrics (optional, for advanced profiling)

Setup & Installation
--------------------
1. Clone the repository:
```bash
git clone https://github.com/username/model-performance.git
```
2. Create venv enviroment:
```powershell 
cd path\to\your\project
python -m venv env
```
3. Activate your virtual enviroment:
```powershell 
.\env\Scripts\activate
```

4. Install dependencies:
```powershell 
pip install -r requirements.txt
```

5. Add your Hugging Face token:
   Replace `PLEASE PUT YOUR HUGGING FACE TOKEN HERE` in `main.py` with your Hugging Face access token.

> Note: Some model also require extra installation please read the error and installing accordingly to each model you are using.


Supported Models
----------------
BERT
- google-bert/bert-base-uncased (110M)
- google-bert/bert-large-uncased (340M)

LLaMA (Meta)
- meta-llama/Llama-2-7b-hf (7B)
- meta-llama/Llama-2-13b-hf (13B)

Mamba
- state-spaces/mamba-130m (130M)
- state-spaces/mamba-370m (370M)
- state-spaces/mamba-790m (790M)
- state-spaces/mamba-1.4b (1.4B)
- state-spaces/mamba-2.8b (2.8B)

Falcon
- tiiuae/falcon-7b (7B)

Mistral
- mistralai/Mistral-7B-v0.1 (7B)

Gemma (Google)
- google/gemma-2b (2B)
- google/gemma-2-9b (9B)

Phi (Microsoft)
- microsoft/phi-2 (2.7B)
- microsoft/phi-3-small-8k-instruct (7B)
- microsoft/phi-3-medium-128k (14B)

> Note: Some very large models are commented out due to hardware limitations.

Features
--------
- Supports multiple public pre-trained models
- Measure hardware performance with Nvidia SMI/NVML
- Track energy consumption with CodeCarbon and PyJoules
- Optional Nsight profiling for GPU-intensive tasks
- Threaded execution for simultaneous model run and performance report

License
-------
This project is licensed under the MIT License. See the LICENSE file for details.
