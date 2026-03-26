# basic dummy training script (interview ke liye enough)

from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("gpt2")
tokenizer = AutoTokenizer.from_pretrained("gpt2")

print("Fine-tuning setup ready ✅")