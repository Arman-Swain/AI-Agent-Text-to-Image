# 🖼️ AI Agent – Text to Image Generator

## 📌 Project Overview

This project is a terminal-based AI agent that converts natural language text prompts into images using a free AI image generation service (Pollinations AI).

The system is designed to be simple, modular, and stable, focusing on backend logic rather than UI complexity. All generated images are automatically stored in a centralized folder for easy access and future use.

---

## ✨ Features

- Convert any text prompt into an image
- Uses a free text-to-image AI service (no API key required)
- Terminal-based interaction (simple and reliable)
- Automatically saves images in a dedicated `images/` folder
- Fully dynamic (no hardcoded prompts)
- Modular and extensible Python architecture
- Compatible with modern Python versions (tested on Python 3.14)

---

## 🛠️ Tech Stack

### Programming Language
- Python 3.10+ (tested on Python 3.14)

### Libraries Used
- requests – for making HTTP requests to the AI image API
- Pillow (PIL) – for handling and opening image files
- uuid – for generating unique image filenames
- os – for directory and file management

### AI Service
- Pollinations AI (free text-to-image generation)

---

## 📁 Project Structure

AI-Agent-Text-to-Image/
│
├── app/
│   ├── main.py              # Terminal entry point
│   ├── agent.py             # Agent decision logic
│   └── tools/
│       ├── __init__.py
│       └── image.py         # Image generation logic
│
├── images/                  # All generated images are stored here
│
├── requirements.txt
└── README.md

---

## ⚙️ Prerequisites

### System Requirements
- Windows / macOS / Linux
- Stable internet connection

### Software Requirements
- Python 3.10 or higher
- pip (Python package manager)

### Install Required Libraries

pip install requests pillow

---

## ▶️ How to Run the Project

1. Clone the repository

   git clone https://github.com/Arman-Swain/AI-Agent-Text-to-Image.git

2. Navigate to the project directory

   cd AI-Agent-Text-to-Image

3. Run the application

   python app/main.py

4. Enter a text prompt

   You: a futuristic robot drinking chai

5. The generated image will be saved automatically inside the `images/` folder.

---

## 🔄 How It Works

1. User enters a text prompt in the terminal
2. The agent processes the input
3. The prompt is sent to the AI image generation service
4. The generated image is downloaded
5. The image is saved with a unique name in the `images/` directory
6. The image path is displayed to the user

---

## 🤖 AI Agent Used

This project uses a task-oriented, rule-based AI agent.

- Receives user input
- Decides the action
- Invokes an external tool (image generation API)
- Produces the final output (generated image)

This follows the Simple Reflex Agent model in AI theory.

---

## 📌 Importance of the Project

- Demonstrates real-world Generative AI integration
- Shows practical use of AI agents with tool invocation
- Useful for learning API integration, modular Python design, and file handling
- Applicable to content creation, design prototyping, and creative AI applications

---

## 🔑 Key Technical Highlights

- Clean and modular architecture
- Centralized image storage
- Defensive programming practices
- No heavy ML frameworks required
- Easy to extend with UI or additional AI capabilities

---

## 🚀 Future Enhancements

- Web-based UI (Gradio / Streamlit)
- Prompt enhancement using LLMs
- Image style presets
- Image gallery viewer
- Batch image generation
- Cloud deployment

---

## 🧾 License

This project is intended for educational and learning purposes.

---

## 👨‍💻 Author

Arman Swain  
GitHub: https://github.com/Arman-Swain
