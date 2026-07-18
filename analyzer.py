# analyzer.py
from transformers import pipeline

# We set 'device=-1' to ensure it uses CPU (default). 
# If you eventually get a GPU, change this to 0 for a massive speed boost.
print("Loading AI model... please wait.")
classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", device=-1)

def predict_emotion(text):
    # This will now return the highest-scoring emotion
    result = classifier(text)[0]
    return result['label'].capitalize()