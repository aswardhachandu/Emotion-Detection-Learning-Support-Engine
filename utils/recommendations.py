recommendations = {

"joy":"😊 Keep learning! Solve more coding problems.",

"sadness":"😔 Take a short break and return refreshed.",

"fear":"📚 Start with easier concepts first.",

"anger":"🧘 Relax for five minutes.",

"neutral":"📖 Continue your learning.",

"love":"❤️ Keep your motivation high.",

"curiosity":"🔍 Explore more resources.",

"confusion":"🤔 Revise the topic again."

}

def get_recommendation(emotion):

    return recommendations.get(
        emotion,
        "Keep practicing every day."
    )