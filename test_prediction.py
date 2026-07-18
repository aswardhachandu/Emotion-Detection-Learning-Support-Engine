from utils.predictor import predict_emotion

text = "I am very happy today."

emotion, confidence = predict_emotion(text)

print("Emotion:", emotion)
print("Confidence:", confidence)