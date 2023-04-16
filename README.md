# FastAPI Sentiment Analysis

This repository contains a simple FastAPI app that uses the Transformers library to perform sentiment analysis on a given text input.

## Getting Started

Follow these steps to set up the project on your local machine.

### Prerequisites

- Python 3.6 or higher
- [pip](https://pip.pypa.io/en/stable/installation/)
- [venv](https://docs.python.org/3/library/venv.html) (optional, but recommended)

### Installation

1. Clone the repository:

git clone https://github.com/your_username/fastapi-sentiment-analysis.git


2. (Optional, but recommended) Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate # On Windows, use venv\Scripts\activate


3. Install the required packages:

pip install fastapi uvicorn pydantic transformers tensorflow

Replace tensorflow with pytorch if you prefer to use PyTorch, or install both if needed.

4. Run the FastAPI app:

uvicorn main:app --reload

Replace "main" with the name of your Python file if different.

5. Access the app in your browser:
Visit the root endpoint at http://localhost:8000/
Access the interactive documentation at http://localhost:8000/docs

### MIT License

This project is licensed under the terms of the MIT license. See the LICENSE file for details.
