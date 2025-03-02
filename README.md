# Sentiment Analysis Tool

## 💡 Overview

The **Sentiment Analysis Tool (SATool)** is a Python-based project designed to analyze the sentiment of text data. It determines whether the sentiment is positive, negative, or neutral and provides a simple and intuitive interface to process text inputs, text files, and CSV files with feedback data. This project is ideal for individuals or organizations looking to automate the sentiment analysis process for customer feedback, reviews, or any textual data.

---

## 🔥 Features

- Analyze text input directly.
- Analyze sentiment from text files.
- Upload and analyze sentiment for a CSV file containing feedback.
- Generate output files with sentiment analysis results.
- Easy-to-use interface and detailed results for every input line or record.

---

## 📂 Dependencies

The following Python libraries are required:

- pandas - For handling CSV files.
- textblob - For performing sentiment analysis.
- tk - For file dialogs (part of the standard Python library).

To install the dependencies, use:

```bash
pip install -r requirements.txt
```
---
## 🚀 How It Works

1. The tool uses TextBlob to analyze the sentiment of the input text.
2. Sentiment polarity ranges:
  - Positive: Polarity > 0
  - Neutral: Polarity = 0
  - Negative: Polarity < 0
3. Outputs are displayed in the console and/or saved to new files based on the script used.
---
## 📘 Usage

Run one of the following scripts depending on your requirement:

- SATool_InputText.py - For single-line text sentiment analysis.
- SATool_InputFilePath.py - To analyze a text file line by line.
- ATool_UploadTextFile.py - Upload a text file for analysis.
- SATool_UploadCSVFile.py - Upload a CSV file for analysis.
---
## 📂 Input Files

Ensure that the required input files are available for the tools:

1. **Sample_Input.txt**  
   This text file can be uploaded into the tool **SATool_UploadTextFile.py**. It contains sample data in a text format for processing.

2. **SA_Input.csv**  
   This CSV file can be uploaded into the tool **SATool_UploadCSVFile.py**. It contains structured data in CSV format to be processed by the script.
---
## 📝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/SAToolNewFeature`)
3. Commit your changes (`git commit -m 'Add some SAToolNewFeature'`)
4. Push to the branch (`git push origin feature/SAToolNewFeature`)
5. Open a Pull Request
---
## 📜 License

This project is licensed undet the MIT License. See the [LICENSE.md](LICENSE) file for details.

---
## 📞 Connect

For feedback, questions, or more SQL tips, connect with me:

🔗 [LinkedIn](https://www.linkedin.com/in/naveenkumarm): Let's connect and discuss database strategies!

▶️ [YouTube Channel](https://www.youtube.com/@ttwithnaveen): Subscribe for more database insights and tutorials.
