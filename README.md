💬 Gemini Chatbot (Console-Based)  
A simple console-based chatbot built using Google's Generative AI (gemini-2.0-flash) API and Python. This chatbot lets you have real-time conversations with Google's Gemini model via the terminal.

🚀 Features
- Connects to Gemini 2.0 Flash using google-generativeai

- Real-time chat interaction via terminal

- Stops on typing "stop"

- Uses .env file for safe API key management

🧠 Requirements
- Python 3.8+

- Google Generative AI API Key

Packages:

```google-generativeai```

```python-dotenv```

📦 Installation
Clone the repository  
```git clone https://github.com/your-username/gemini-chatbot.git```
```cd gemini-chatbot```

Install dependencies
- ```pip install -r requirements.txt```

- Set up your .env file
- Create a .env file in the root of the project and add this line:
- GOOGLE_API_KEY=your_gemini_api_key_here

🧑‍💻 Usage
Run the chatbot:  
- ```python chat.py```

Start chatting with Gemini! Type "stop" to end the session.

📁 File Structure
gemini-chatbot/  
├── chat.py → Main chatbot script  
├── .env → API key (not uploaded to GitHub)  
├── requirements.txt → Python dependencies  
└── README.md → This file  

📜 Example  

You: Hello!  
Gemini: Hello! How can I assist you today?  
You: Tell me a joke  
Gemini: Why don't skeletons fight each other? Because they don't have the guts!

🛑 Disclaimer  
This is a basic implementation meant for learning and experimentation. Please follow Google's API usage guidelines and avoid exposing your API keys publicly.