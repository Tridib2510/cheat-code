# Cheat Code — Your DSA Helper

**Cheat Code** is a Python-based **GenAI-powered DSA assistant** that helps you analyze and understand Data Structures & Algorithms problems using automation and AI.

> ⚠️ Disclaimer  
> This project is built strictly for **learning and experimentation**.  
> It is **not intended for cheating in interviews, exams, or competitive programming platforms**.

---

## Features

- AI-assisted DSA problem solving  
- Screenshot / image-based problem input  
- Cloudinary image upload integration  
- Groq LLM integration for fast responses  
- Modular Python utilities  

---

## Project Structure

cheat-code/
│
├── main.py # Main entry point
├── utils/ # Helper utilities
├── requirements.txt # Python dependencies
├── pyproject.toml # Project configuration
├── README.md
└── .gitignore

yaml
Copy code

---

## Step-by-Step Setup Guide

### Step 1: Clone the Repository

```bash
git clone https://github.com/Tridib2510/cheat-code.git
cd cheat-code
Step 2: Create and Activate a Virtual Environment (Recommended)
bash
Copy code
python -m venv venv
Windows

bash
Copy code
venv\Scripts\activate
macOS / Linux

bash
Copy code
source venv/bin/activate
Step 3: Install Dependencies
bash
Copy code
pip install -r requirements.txt
Step 4: Set Up Environment Variables
Create a .env file in the root directory:

bash
Copy code
touch .env
Add the following to the .env file:

env
Copy code
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_cloudinary_api_key
CLOUDINARY_API_SECRET=your_cloudinary_api_secret

GROQ_API_KEY=your_groq_api_key
Where to get API keys:

Cloudinary: https://cloudinary.com/console

Groq: https://console.groq.com

Step 5: Run the Application
bash
Copy code
python main.py
After this, the application will start and you can follow the on-screen instructions to analyze DSA problems.

Project Purpose
Learn how GenAI integrates with real-world developer tools

Experiment with vision + LLM workflows

Build an AI-powered coding assistant

Create a strong portfolio project

Future Improvements
Better problem detection

Improved reasoning and explanations

GUI / Desktop version

Safety and misuse prevention

Contributing
Contributions are welcome.

Fork the repository

Create a new branch

Commit your changes

Open a Pull Request
