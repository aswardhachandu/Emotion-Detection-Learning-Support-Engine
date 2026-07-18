from transformers import AutoTokenizer, AutoModelForSequenceClassification

MODEL_PATH = "models/bert_emotion_model_final"

tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)

print("✅ Model loaded successfully!")