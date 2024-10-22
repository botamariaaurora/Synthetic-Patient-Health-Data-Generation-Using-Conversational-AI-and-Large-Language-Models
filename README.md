# Synthetic-Patient-Health-Data-Generation-Using-Conversational-AI-and-Large-Language-Models

This GitHub repository holds the research work focusing on generating synthetic tabular data using DPC_GANs combined Large Language Model Lamma 2(shraded version).

Advanced generative models like Generative Adversarial Networks (GANs) have demonstrated their capability in creating realistic synthetic patient records, including Electronic Health Records (EHR), CT scans, EEG, and ECG data. These models utilize real-world patient data to simulate and produce synthetic data that closely mirrors the statistical and structural properties of the original data. However, these models are heavily dependent on the quality and quantity of the input data and face limitations in generating synthetic data that significantly diverges from the input. Additionally, there are technical barriers that make it challenging for domain experts, such as health researchers, doctors, or clinicians, to effectively use these models in their practice. These models typically do not accommodate direct human input for generating or modifying synthetic data.

In response to these challenges, this project aims to develop a conversational AI tool capable of
incorporating human input to generate synthetic patient health data. Our approach for this research project will begin with the selection of The MIMIC-III (Medical Information Mart for Intensive Care III) which is a large database consisting of 26 publicly available tables, made up of classified medical information from more than 40,000 patients in critical care. A vast variety of data is included in the collection, containing patient demographics, vital signs, laboratory test results, prescription drugs, diagnoses and notes from medical procedures. The suggested approach combines LLM model LlaMA-2 Chat-7B-HF with DPC_GANsfor patient EHR data. This tool will create an interface that enables healthcare professionals to make specific requests, such as “generate 2000 Type 2 diabetes patients EHR data with 20 important diabetes observations based on the US population” or inquire about the sources of real-world data and guidelines used for synthesizing data. This approach seeks to make generative models more accessible and practical for healthcare professionals, bridging the gap between complex AI technologies and everyday clinical applications.


**Code Reproducibility:**

To facilitate the reproducibility of our results, we have organized the code under the 'Notebooks' section. Each notebook runs on Google Colaboratory and within this section corresponds to a singular experiment, allowing for an in-depth review of our findings. Navigating into 'Notebook' section you will find the code on how we trained DP_GANs, the preprocess of our final dataset, the fine tuning of our LLM model, the evaluation of generated synthetic data and the evaluation of the final results. The 'Final_datasets' folder, located under 'Notebooks,' includes two different chapter files. After splitting the whole dataset into different chapters we chose 4, 5 and 6 csv files for training and generating synthetic data. Finally you can also have a look at 'Supervisor Notes' that we took as a group during different phases with out supervisor.

# **Phase 1:**
* **🤔 State of the art papers:** https://docs.google.com/document/d/14fAp4seVLp1mbdW4lItT5j0s4gk4LaIIgoO71ObmHDw/edit?usp=sharing

* **📋 Agenda suggestion for next meeting 15.03.2024:** https://docs.google.com/document/d/1smT2DTMNG_CbiJQ45Tx2MuxzRu3T8JyJvMcVOG7NxQQ/edit?usp=sharing

* **📋 Agenda suggestion for meeting 6.03.2024:** [https://docs.google.com/document/d/1SpEhd3o1PvfAQpnfE7HJ4aV_ceH8jufSevIjU9dPxrA/edit](https://docs.google.com/document/d/1SpEhd3o1PvfAQpnfE7HJ4aV_ceH8jufSevIjU9dPxrA/edit?usp=sharing)https://docs.google.com/document/d/1SpEhd3o1PvfAQpnfE7HJ4aV_ceH8jufSevIjU9dPxrA/edit?usp=sharing

* **Research Questions:** https://docs.google.com/document/d/14fAp4seVLp1mbdW4lItT5j0s4gk4LaIIgoO71ObmHDw/edit?usp=sharing

* **Initial Pipeline:** https://drive.google.com/file/d/1XMnE-PdrOR-j6rpSO7FXYdPPj5sErXq3/view?usp=sharing

* **📅 Next Scheduled Meetings:** 6.03.2024 10:00-10:45, 15.03.2024 13:15-14:00

* **Gannt Chart Draft:** https://drive.google.com/file/d/1ED0JKXPVFLZJsBbJJVSB00ql_BM9DXMM/view?usp=sharing

* **Report:** https://www.overleaf.com/2996128184nyxkhtnzxvsv#6efd5f

# **Phase 2:**
* **Task division:** https://docs.google.com/document/d/1d6dnG-uJXu1UF4h7IHu0oszDZylle-ubn2bHmILzZhI/edit?usp=sharing
* **Agenda 07.05.2024:** https://docs.google.com/document/d/1k7B-N7keAZUcvgVRXHzchoxkHoJlotUT94LocM_BQfc/edit?usp=sharing
* **Drive Link:** https://drive.google.com/drive/folders/1RIBgXQPFIJhbWA4kMKijyY5QPRc9K4gn?usp=sharing
* **Layman's Blog Post:** https://drive.google.com/file/d/1sv6Im0dQi9PFF6GMNrOiutpH5TRHC7w0/view?usp=share_link

* # **Phase 3:**
* **Agenda 17.06.2024:** https://drive.google.com/file/d/1W9zvD328VkMqAaygsCHjM8CRJOgWNmDq/view?usp=sharing
* **General Description of MIMIC-III Dataset:** https://drive.google.com/file/d/1QXnZpV1gbLHdvsBngTy_aI-lX7x7HBZu/view?usp=sharing
* **Final Report:** https://www.overleaf.com/read/mpxmqzktdzbj#99613e
  

# :computer: Installation

To set up the environment for this project, follow these steps:

1. **Install required packages:**

   Run the following commands to install the necessary Python packages with their specific versions for DPC_GANs:

   ```bash
   !pip install sdv==1.6.0 
   !pip install rdt==1.9.0  
   !pip install dp_cgans==0.0.6


1. **Install required packages:**

   Run the following commands to install the necessary Python packages for LLM:

   ```bash
   !pip install -q -U trl transformers accelerate git+[https://github.com/huggingface/peft.git (https://github.com/huggingface/peft.git)
   !pip install -q datasets bitsandbytes einops wandb

# 🐍 Use with Python

If your input is tabular data, for DPC_GANs run the following code:

```python
from dp_cgans import DP_CGAN
import pandas as pd

def closest_tenth(n):
  return n - n%10
num_epochs = 100
batch_size = closest_tenth(int(num_of_rows/10))

model = DP_CGAN(
   epochs=num_epochs, # number of training epochs
   batch_size=batch_size, # the size of each batch
   cuda = True,
   log_frequency=True,
   verbose=True,
   generator_dim=(128, 128, 128),
   discriminator_dim=(128, 128, 128),
   generator_lr=2e-4,
   discriminator_lr=2e-4,
   discriminator_steps=1,
   private=False,
)


print("Start training model")
model.fit(training_data)
model.save(f"/content/gdrive/MyDrive/Notebooks/test data/generated data/generator_chapter_{dataset_number}.pkl")
# modify this to run on your accounts
# model.save(f"PATH TO YOUR DRIVE/generator_chapter_{dataset_number}.pkl")

# Generate new synthetic rows
syn_data = model.sample(num_of_rows)

syn_data.to_csv(f"/content/gdrive/MyDrive/Notebooks/test data/generated data/syn_data_chapter_{dataset_number}.csv")
# modify this to run on your accounts
# syn_data.to_csv(f"PATH TO YOUR DRIVE/syn_data_chapter_{dataset_number}.csv")
