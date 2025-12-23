from transformers import AutoModelForCausalLM

def load_model(model_name):
    return AutoModelForCausalLM.from_pretrained(model_name)
