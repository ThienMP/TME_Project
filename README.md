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

License
-------
This project is licensed under the MIT License. See the LICENSE file for details.
