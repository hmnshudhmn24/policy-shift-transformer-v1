def segment_policy(text):
    return [p for p in text.split("\n") if len(p.strip()) > 50]
