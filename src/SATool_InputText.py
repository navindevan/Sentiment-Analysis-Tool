from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity  # Ranges from -1 (negative) to 1 (positive)
    if polarity > 0:
        return "Positive 😊"
    elif polarity < 0:
        return "Negative 😢"
    else:
        return "Neutral 😐"

# User input
if __name__ == "__main__":
    print("Welcome to the Sentiment Analysis Tool!")
    user_input = input("Enter a sentence to analyze sentiment: ")
    sentiment = analyze_sentiment(user_input)
    print(f"The sentiment of the text is: {sentiment}")