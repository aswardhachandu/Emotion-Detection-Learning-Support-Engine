# main.py
from database_manager import add_emotion_record
from analyzer import predict_emotion

def run_engine(email, user_input):
    # 1. Analyze the input
    emotion = predict_emotion(user_input)
    
    # 2. Store the result
    add_emotion_record(email, user_input, emotion)
    
    print(f"Detected: {emotion} | Saved to database.")

if __name__ == "__main__":
    # Test it out!
    run_engine("chandu@example.com", "I am feeling very happy today!")
# main.py addition
def sanitize_input(text):
    # Remove extra spaces and limit length to prevent database bloat
    return text.strip()[:500]