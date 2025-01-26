import os
from textblob import TextBlob
from tkinter import Tk, filedialog


def analyze_sentiment(text):
    """Analyze the sentiment of a given text."""
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity  # Ranges from -1 (negative) to 1 (positive)
    if polarity > 0:
        return "Positive 😊"
    elif polarity < 0:
        return "Negative 😢"
    else:
        return "Neutral 😐"


def analyze_file(file_path):
    """Analyze each line of a file and return the results."""
    results = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line_number, line in enumerate(lines, start=1):
                line = line.strip()  # Remove leading/trailing whitespace
                if line:  # Skip empty lines
                    sentiment = analyze_sentiment(line)
                    results.append((line_number, line, sentiment))
        return results
    except Exception as e:
        return f"Error: {e}"


def save_results(results, output_path):
    """Save the analysis results to a file."""
    try:
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write("Line Number\tText\tSentiment\n")
            file.write("-" * 50 + "\n")
            for line_number, text, sentiment in results:
                file.write(f"{line_number}\t{text}\t{sentiment}\n")
        print(f"Results saved to {output_path}")
    except Exception as e:
        print(f"Error saving results: {e}")


if __name__ == "__main__":
    print("Welcome to the Sentiment Analysis Tool!")
    print("Please select a text file to analyze.")

    # Use Tkinter to open a file dialog
    root = Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(
        title="Select a Text File",
        filetypes=(("Text Files", "*.txt"), ("All Files", "*.*"))
    )

    if not file_path:
        print("No file selected. Exiting.")
    else:
        print(f"Analyzing file: {file_path}")
        results = analyze_file(file_path)

        if isinstance(results, str):
            # If there's an error, results will be a string
            print(results)
        else:
            # Display results
            print("\n--- Sentiment Analysis Results ---")
            for line_number, line, sentiment in results:
                print(f"Line {line_number}: {line} -> Sentiment: {sentiment}")

            # Save results to a new file
            output_path = os.path.splitext(file_path)[0] + "_results.txt"
            save_results(results, output_path)
