# University of Malaya Natural Language Processing Group Assignment

This is a personal group assignment archive.

## Getting Started

* Gooddocument is a basic NLP engine basic prototype which is able to process real-world Social Media (Socmed) data in order to further study Z generation who are always on social media:
1. Normalization (BM -> Eng)
2. Syntax Classifier (Parsing)

### Prerequisites

* Install Miniconda and choose Python 3
* Install required libraries

```
NLTK, Textblob, python-docx and etc.
```



## Folder Structure
 * Documents (Contains Unprocessed and Processed Documents)
 1. nlpabbreviation.py (Codes for taking care of abbreviation using n-gram)
 2. nlp data cleaning.py (Codes for cleaning data)
 3. gui.py (Main file to start the GUI)

 ## Steps to run the code
 1. Open Command Prompt (For Anaconda or other environment, you need to open Anaconda Prompt and Activate the required environment.)
 2. Change directory to the folder containing the files.
 ```
 cd C:\Users\<User>\Documents\Devs\NLP-final-project
 ```
 3. Run the following code and a Gooddocument window will be displayed.
 
 ```
 python gui.py
 ```
 4. Click "Start" and wait for few minutes.
 5. The main interface will be shown and ready to rock 'n roll.

## Functions in the application
* Insert file - This allow user to choose the document to be processed. Only Docx format will be supported. The folder containing desired files is documents.
* Metaprofilling - List out sentences by same user.
* Clean - Clean the unnecessary text like reply, emoticon.
* Fix - Look for abbreviation's root word.
* Translate - Normalize document into English language.
* Tree - Parse Tree for document.

