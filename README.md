# Cheat Code — Your DSA Helper

**Cheat Code** is a Python-based **GenAI-powered DSA assistant** that helps you analyze and understand Data Structures & Algorithms problems using automation and AI.

⚠️ **Disclaimer**
This project is built strictly for **learning and experimentation purposes**.
It is **NOT intended for cheating** in interviews, exams, or competitive programming platforms.

---

## 🚀 Features

* 🧠 AI-assisted DSA problem solving
* 📸 Screenshot / image-based problem input
* ☁️ Cloudinary image upload integration
* ⚡ Groq LLM integration for fast responses
* 🛠️ Modular and extendable Python utilities

---

## 📂 Project Structure

```
cheat-code/
├── main.py                # Main entry point
├── utils/                 # Helper utilities
├── requirements.txt       # Python dependencies
├── pyproject.toml         # Project configuration
├── README.md
└── .gitignore
```

---

## 🎬 Demo Video

You can watch the demo video directly below:
https://res.cloudinary.com/dsloz7tfz/video/upload/v1767334920/Screen_Recording_2026-01-02_104618_1_uufsti.mp4

---

## 🛠️ Step-by-Step Setup Guide (UV Package Manager)

### Step 1: Clone the Repository

```bash
git clone https://github.com/Tridib2510/cheat-code.git
cd cheat-code
```

---

### Step 2: Install Dependencies Using UV

```bash
uv install
```

This will automatically create an isolated environment and install all required dependencies.

---

### Step 3: Set Up Environment Variables

Create a `.env` file in the **root directory** of the project:

```bash
touch .env
```

Add the following variables to the `.env` file:

```env
CLOUDINARY_CLOUD_NAME=your_cloudinary_cloud_name
CLOUDINARY_API_KEY=your_cloudinary_api_key
CLOUDINARY_API_SECRET=your_cloudinary_api_secret

GROQ_API_KEY=your_groq_api_key
```

🔑 **Get API Keys From**

* Cloudinary Console → [https://cloudinary.com/console](https://cloudinary.com/console)
* Groq Console → [https://console.groq.com](https://console.groq.com)

---

### Step 4: Run the Application with UV

```bash
uv run main.py
```

This ensures your project runs inside the UV-managed environment with all dependencies loaded.

---

## 🎯 Project Purpose

* Learn how **GenAI integrates with real-world developer tools**
* Experiment with **vision + LLM pipelines**
* Build an **AI-powered coding assistant**
* Create a strong **portfolio project**

---

## 🧩 Future Improvements

* 🔍 Improved problem detection
* 🧠 Better reasoning and explanations
* 🖥️ GUI / Desktop application
* 🔐 Safety & misuse prevention

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Open a Pull Request

---

## 📜 License

This project is licensed under the **MIT License**.

---

⭐ If you find this project useful, consider giving it a star!
Happy coding 🚀
