# Ancient Language Processing (ALP)

The Ancient Language Processing (ALP) project aims to advance the study of ancient Egyptian hieratic texts by using modern machine learning techniques, including Handwritten Text Recognition (HTR), Transliteration, Translation, and Period Classification. This project focuses on training models that can recognize ancient signs, transliterate them into modern characters, translate the meaning, and classify texts by their historical periods using large language models (LLMs).


## 🏺 Project Overview

Hieratic, an ancient Egyptian script, is a complex writing system. This project helps scholars and researchers digitize and analyze historical documents by training state-of-the-art models for:

	•	Handwritten Text Recognition (HTR): Identifying signs in scanned hieratic manuscripts.
	•	Transliteration: Converting hieratic signs to modern transliterated text.
	•	Translation: Translating the transliterated text to modern language.
	•	Period Classification: Categorizing the text into different historical periods.

This toolset is valuable for archaeologists, historians, and anyone involved in the study of ancient texts.


## 📂 Project Structure

Here’s an overview of the updated project structure:

```plain text
Ancient-Language-Processing/
├── .git                    # Git metadata
├── .github                 # GitHub-specific configurations (Actions, templates)
├── .gitignore              # Git ignore settings
├── .readthedocs.yaml       # ReadTheDocs configuration
├── docs/                   # Sphinx documentation source files
│   ├── make.bat
│   ├── Makefile
│   └── source
│       ├── conf.py
│       └── index.rst
├── environment.yaml        # Conda environment specification
├── LICENSE                 # Project license
├── README.md               # Project description
├── requirements.txt        # Python dependencies
├── setup.py                # Setup file for packaging
├── src/                    # Source code
│   ├── __init__.py
│   ├── classification/     # Period classification logic
│   ├── htr/                # HTR logic
│   ├── preprocessing/      # Image preprocessing
│   └── translation/        # Transliteration and translation logic
├── frontend/               # React frontend application
│   ├── public/             # Public assets and HTML
│   ├── src/                # React source code (JSX, components, styles)
│   ├── package.json        # Frontend dependencies and scripts
│   └── ...
└── tests/                  # Unit and integration tests
```


## ⚙️ Installation

To get started, clone the repository and install the necessary dependencies.

Prerequisites:

	•	Python: Version 3.8 or above
	•	Conda: For creating a reproducible environment
	•	Tesseract OCR: Required for image-based text recognition

### Step 1: Clone the Repository

git clone https://github.com/MargotBelot/Ancient-Language-Processing.git

cd Ancient-Language-Processing

### Step 2: Set Up the Conda Environment

You can set up a virtual environment using the provided environment.yaml file:

conda env create -f environment.yaml

conda activate alp-env

### Step 3: Install Dependencies (Optional)

Alternatively, if you don’t use Conda, you can install dependencies via requirements.txt:

pip install -r requirements.txt


## 🌐 Frontend Setup (React)

The frontend/ directory contains the React app that serves as the user interface.

### Step 1: Install Frontend Dependencies

cd frontend

npm install

### Step 2: Start the React App

npm start

The app will run locally at http://localhost:3000.

Optionally, you can run both backend and frontend concurrently using tools like concurrently.


## 📚 Usage

Once everything is set up, you can begin using the project. Here’s a basic usage example for Handwritten Text Recognition (HTR):


For more usage examples, check the examples/ directory (coming soon).


## 🛠 Contributing

We welcome contributions! If you’d like to contribute to the project, please fork the repository, create a new branch, and submit a pull request. Ensure that you add tests for any new features or bug fixes.

### Steps to contribute:

	1.	Fork the repository
	2.	Create a new branch (git checkout -b feature-name)
	3.	Make your changes
	4.	Commit and push your changes (git push origin feature-name)
	5.	Create a pull request


## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.


## 📄 Documentation

For more details on how to use, contribute, or set up this project, check out the [documentation](https://ancient-langue-processing.readthedocs.io/en/latest/).