import cv2
from deepface import DeepFace
# 1. Move the import to the TOP of the file
from database_manager import add_emotion_record 

cap = cv2.VideoCapture(0)
# Use a counter to avoid spamming the database every single frame
frame_counter = 0

print("Starting Emotion Detection... Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    frame_counter += 1
    
    # 2. Only process every 30th frame (approx once per second)
    # This keeps your performance high!
    if frame_counter % 30 == 0:
        try:
            results = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False, detector_backend='ssd')
            
            for result in results:
                emotion = result['dominant_emotion']
                
                # 3. Add your logging logic here
                if emotion == "sad":
                    print("Sadness detected, logging to database...")
                    add_emotion_record("chandu@example.com", "Detected via webcam", emotion)
                
                # ... (rest of your drawing code)
        except Exception as e:
            print(f"Error: {e}")

    cv2.imshow('Emotion Detection Engine', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()