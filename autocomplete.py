from datasets import load_dataset, DatasetDict
from transformers import AutoConfig, AutoTokenizer, AutoModel,TrainingArguments, Trainer
from peft import LoraConfig, get_peft_model



model_name = "HooshvareLab/bert-fa-zwnj-base"
config = AutoConfig.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

# لود دیتاستی که خودمون آماده کردیم
train_dataset=load_dataset('csv', data_files='MainDataSet.csv')
test_dataset = load_dataset('csv', data_files='TestDataSet.csv')


lora_config=LoraConfig(
    r=14,
    bias="none",
    lora_alpha=32,
    lora_dropout=0.5,
    target_modules=["query", "value"],
)

lora_model=get_peft_model(model, lora_config)

training_arg=TrainingArguments(
    output_dir="./result",
    evaluation_strategy="epoch",
    weight_decay=0.01,
    num_train_epochs=10,
    per_device_train_batch_size=5000,
    per_device_eval_batch_size=8000
)

trainer= Trainer(
    model=lora_model,
    args=training_arg,
    train_dataset=train_dataset['train'],
    eval_dataset=test_dataset['train'],
)

trainer.train()