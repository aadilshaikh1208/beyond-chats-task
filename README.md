# Reddit User Persona Generator (BeyondChats Internship Task)

This project is a Python script that takes a **Reddit user profile URL**, scrapes their latest posts and comments using Reddit’s API, and uses an **open-source LLM via Ollama** to generate a **detailed user persona** in `.txt` format.

The generated persona includes:
- User details (age, occupation, location, etc.)
- Behavior and habits
- Frustrations and motivations
- Personality type (introvert/extrovert, intuitive, etc.)
- Goals and needs
- **Quoted evidence** from Reddit content for each point

---

## 📁 Folder Structure

reddit-persona-generator/
  - generate_persona.py # Main executable script
  - reddit_config.py # Reddit API credentials (user must fill)
  - requirements.txt # Python libraries required
  - personas/ # Output folder for persona files
      - kojied.txt
      - Hungry-Move-6603.txt



## ⚙️ Setup Instructions

### 1. Clone the Repository
  ```bash
  git clone https://github.com/your-username/reddit-persona-generator.git
  cd reddit-persona-generator
```


### 2. Install Required Python Packages
  ```bash
  pip install -r requirements.txt
```

-  Ollama is not a pip package — you must install it manually from:
https://ollama.com

 ### 3. Setup Reddit API
  -Go to https://www.reddit.com/prefs/apps
  -Click “create another app”
  -Choose app type: script
  -Give any name, and add http://localhost:8080 as the redirect URI
  -After creating, copy the client ID and secret

  ```bash
  REDDIT_CLIENT_ID = "your_client_id"
  REDDIT_CLIENT_SECRET = "your_client_secret"
  REDDIT_USER_AGENT = "persona-bot"
```

### 4.  Pull an Ollama Model (For example I have used gemma3:1b model if Ollama)
  -Make sure you have Ollama installed on your system.
  ```bash
  ollama pull gemma3:1b
```
### 5. Running the Script
```bash
python generate_persona.py
```

### 6.When prompted, paste a full Reddit user profile URL, for example:
  - https://www.reddit.com/user/kojied/
  - The script will:
  - Fetch latest 20 posts & comments
  - Generate a structured persona using Ollama
  - Save the result in the /personas/ folder as kojied.txt

### 7. Sample Output Included:
  - This repo already includes sample persona files as requested:
  - personas/kojied.txt
  - personas/Hungry-Move-6603.txt
  - Each file contains:
  - User details (age, role, location, tier)
  - Behavior, habits, frustrations
  - Motivations, personality type
  - Goals & needs
  - Quoted evidence for each insight

