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

def analyze_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            results = []
            for line_number, line in enumerate(lines, start=1):
                line = line.strip()  # Remove any leading/trailing whitespace
                if line:  # Skip empty lines
                    sentiment = analyze_sentiment(line)
                    results.append((line_number, line, sentiment))
            return results
    except FileNotFoundError:
        return None, "File not found. Please check the file path and try again."
    except Exception as e:
        return None, f"An error occurred: {e}"

if __name__ == "__main__":
    print("Welcome to the Sentiment Analysis Tool!")
    file_path = input("Enter the path to your text file: ")
    results = analyze_file(file_path)
    if results:
        print("\n--- Sentiment Analysis Results ---")
        for line_number, line, sentiment in results:
            print(f"Line {line_number}: {line} -> Sentiment: {sentiment}")
    else:
        print(results[1])
