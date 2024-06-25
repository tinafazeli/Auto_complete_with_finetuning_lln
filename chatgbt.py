from peft import LoraConfig, get_peft_model, prepare_model_for_int8_training
from transformers import Trainer, TrainingArguments

# پیکربندی LoRA
lora_config = LoraConfig(
    r=8,
    lora_alpha=32,
    target_modules=["query", "value"],
    lora_dropout=0.1,
    bias="none"
)

# آماده‌سازی مدل برای فاین‌تیون
# model = prepare_model_for_int8_training(model)
# model = get_peft_model(model, lora_config)

# تنظیمات آموزش
training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="epoch",
    learning_rate=5e-5,
    per_device_train_batch_size=4,
    per_device_eval_batch_size=4,
    num_train_epochs=3,
    weight_decay=0.01,
)

# ساخت Trainer
trainer = Trainer(
    model=model,
    # args=training_args,
    # train_dataset=tokenized_datasets['train'],
    # eval_dataset=tokenized_datasets['test'],
)

# شروع آموزش
trainer.train()
