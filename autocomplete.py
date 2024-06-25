from datasets import load_dataset
from transformers import AutoConfig, AutoTokenizer, AutoModel
from peft import LoraConfig, get_peft_model, prepare_model_for_int8_training

model_name = "HooshvareLab/bert-fa-zwnj-base"
config = AutoConfig.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

dataset=load_dataset('csv', data_files='MainDataSet.csv')