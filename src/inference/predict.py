from transformers import pipeline

def predict(text, model_path):
    pipe = pipeline("text-generation", model=model_path)
    return pipe(text, max_new_tokens=150)
