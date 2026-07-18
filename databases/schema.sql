-- Create the Users table
CREATE TABLE Users (
    email VARCHAR(255) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(50),
    login_count INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create the Emotion_Records table
CREATE TABLE Emotion_Records (
    record_id INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255),
    field VARCHAR(100),
    input_text TEXT,
    predicted_emotion VARCHAR(50),
    secondary_emotion VARCHAR(50),
    confidence_score DECIMAL(5, 4),
    model_used VARCHAR(100),
    ai_response TEXT,
    response_type VARCHAR(50),
    FOREIGN KEY (email) REFERENCES Users(email) ON DELETE CASCADE
);
