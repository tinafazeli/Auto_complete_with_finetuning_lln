from datasets import load_dataset, DatasetDict
from transformers import AutoConfig, AutoTokenizer, AutoModel,TrainingArguments, Trainer
from peft import LoraConfig, get_peft_model



model_name = "HooshvareLab/bert-fa-zwnj-base"
config = AutoConfig.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)


train_dataset=load_dataset('csv', data_files='MainDataSet.csv')['train']
test_dataset = load_dataset('csv', data_files='TestDataSet.csv')['train']

dataset_dict = DatasetDict({
    'train': train_dataset,
    'test': test_dataset
})

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
    per_device_train_batch_size=5,
    per_device_eval_batch_size=16
)

trainer= Trainer(
    model=lora_model,
    args=training_arg,
    train_dataset=dataset_dict['train'],
    eval_dataset=dataset_dict['test']
)

trainer.train()