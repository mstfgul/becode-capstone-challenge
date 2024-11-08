# Theme Prediction and Article Recommendation App

This project is a Streamlit application that allows you to predict the theme of a headline and get related article recommendations.

## Requirements

- Python 3.7 or higher
- Streamlit
- Joblib
- SentenceTransformers
- JSON
- Random

## Installation

1. Clone this repository:
    ```sh
    git clone https://github.com/mstfgul/becode-capstone-challenge.git
    cd becode-capstone-challenge
    ```

2. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Place the model files and article information in the appropriate directories:
    - `/scraping/models/classifier_model.joblib`
    - `/scraping/models/label_encoder.joblib`
    - `/scraping/articles_info.json`

## Usage

1. Start the Streamlit application:
    ```sh
    python main.py
    ```

2. In the browser window that opens, enter a headline or theme to predict and get article recommendations.

## Project Structure

- `main.py`: Entry point for the application. It starts the Streamlit application.
- `streamlit_file.py`: Main Streamlit application file.
- `scraping/models/`: Directory containing the classifier model and label encoder.
- `scraping/articles_info.json`: JSON file containing article information.
- `scrapping_final.py`: Script for updating data.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

Mustafa GUL
Junior Data Engineer
