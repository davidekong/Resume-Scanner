from transformers import MarianMTModel, MarianTokenizer

# Load the Chinese-to-English model
model_name = "Helsinki-NLP/opus-mt-zh-en"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

def translate_text(text):
    # Skip if it’s not a string or already English-like (e.g., dates, numbers)
    if not isinstance(text, str) or text.replace(".", "").isdigit():
        return text
    # Tokenize and translate
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
    translated = model.generate(**inputs)
    return tokenizer.decode(translated[0], skip_special_tokens=True)


translate_text("")