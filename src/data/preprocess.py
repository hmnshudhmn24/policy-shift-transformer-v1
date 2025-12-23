def preprocess(example):
    text = example["text"]
    target = example.get("target", "")
    example["input_text"] = f"Policy Context:\n{text}\n\nPredicted Shift:"
    example["labels"] = target
    return example
