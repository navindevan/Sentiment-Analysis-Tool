import pandas as pd
from textblob import TextBlob
from tkinter import Tk, filedialog
import os


def analyze_sentiment(text):
    """Analyze the sentiment of a given text."""
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity  # Ranges from -1 (negative) to 1 (positive)
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"


def process_csv(file_path):
    """Read a CSV file, analyze the Feedback column, and add a Feedback Type column."""
    try:
        # Load the CSV file into a DataFrame
        df = pd.read_csv(file_path)

        # Ensure the Feedback column exists
        if 'Feedback' not in df.columns:
            return None, "Error: 'Feedback' column not found in the file."

        # Analyze sentiment for each row in the Feedback column
        df['Feedback Type'] = df['Feedback'].apply(lambda text: analyze_sentiment(str(text)))

        # Return the modified DataFrame
        return df, None
    except Exception as e:
        return None, f"Error processing CSV file: {e}"


def save_csv(df, file_path):
    """Save the DataFrame to a new CSV file."""
    try:
        output_path = os.path.splitext(file_path)[0] + "_with_sentiment.csv"
        df.to_csv(output_path, index=False)
        print(f"Results saved to {output_path}")
    except Exception as e:
        print(f"Error saving CSV file: {e}")


if __name__ == "__main__":
    print("Welcome to the Sentiment Analysis Tool for CSV files!")
    print("Please select a CSV file to analyze.")

    # Use Tkinter to open a file dialog
    root = Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(
        title="Select a CSV File",
        filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*"))
    )

    if not file_path:
        print("No file selected. Exiting.")
    else:
        print(f"Analyzing file: {file_path}")
        df, error = process_csv(file_path)

        if error:
            # If there's an error, print it
            print(error)
        else:
            # Save the updated DataFrame to a new CSV file
            save_csv(df, file_path)
