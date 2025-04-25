# 🚀 Octahedron AI – Your AI Memory Keeper! 🧠✨  

Octahedron AI (by Octahedron Tech) remembers, so you don’t have to! With **smart recall**, **deep insights**, and **effortless conversation**, it keeps knowledge at your fingertips. Whether you're brainstorming, researching, or solving problems — Octahedron AI is your ultimate AI companion! 🤖💡  

## 🔥 Features  
✅ **Smart Recall** – Context-aware responses with memory for past interactions.  
✅ **Deep Insights** – AI-driven knowledge, research support, and brainstorming assistance.  
✅ **Effortless Conversations** – Fluid discussions without losing track of important information.  
✅ **Coding** – Advanced coding in Java, C#, C, C++, Python and JavaScript. (1983 character limit, increasing soon)  
✅ **Time Keeping** – Tells the local time and time from vairous time-zones.  
✅ **Secure & Customizable** – Keep private data safe and tailor responses to fit your needs.  
❌ **Image Descriptions** – Seamless descriptions of uploaded images. (Inaccurate and under development)  
❌ **Image Generation** – Generate AI images and art with great precission. (Under development)  
❌ **Web Search** – Why stop at December 2023 training data when you can search the web for latest responses. (Under development)  

## 🛠 Installation & Setup  
```bash
1️⃣ Clone the Repository  
git clone https://github.com/TanushChugh19/Octahedron-AI.git
cd Octahedron-AI

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Set Up Environment Variables
Create a .env file to store API keys and tokens:
TOKEN=your_discord_bot_token_here
API_KEY=your_ai_model_api_key_here

4️⃣ Run the Bot
python bot.py

5️⃣ Alternatively, use setup.sh or setup.bat
- For Linux/macOS:  
  bash setup.sh  
- For Windows:  
  setup.bat
```
🗒️ **Note:**  
- You may need to adjust the PyTorch version inside the `requirements.txt` file based on your CUDA version (default is CUDA 12.8).  

⚙️ **Usage Once running, Octahedron AI responds to Discord commands:**  
- *hello – Greet the AI.
- *oct <message> – Chat with Octahedron AI.

**👥 Contributing
We welcome contributions! Follow these steps:**
- Fork this repository and clone it to your machine.
- Create a new branch for your feature (git checkout -b feature-branch).
- Make changes, test them, and commit updates.
- Submit a pull request explaining your improvements.

**🐛 Known Bugs/Flaws (Status — Patched: ✅ | Pending Fix: ❌)**  
- ❌ describe command is functional but provides inaccurate image descriptions  
- ❌ generate and web commands are not implemented yet  
- ❌ Uses Python's random module for key generation — not cryptographically secure  
- ❌ No database backend implemented — currently using in-memory or file-based storage  
- ✅ In v0.0-alpha.1, zones command caused the bot to hang on slow/unresponsive APIs (Patched) | Fix: Added timeout to API requests — please download the latest app.py from source, not from releases.  

**📜By contributing, you agree to follow the MPL-2.0 License, ensuring all modified files remain open-source. This project is licensed under MPL-2.0, meaning:**  
- You must credit the original author.
- You can modify and share the code, but all modified files must stay under MPL-2.0.
- You can’t relicense the project as proprietary.
- Certain features (such as payment handling) may be closed-source under separate terms.

**🔒 Security & Environment Files
To keep sensitive data private:**
- Add .env to .gitignore to prevent secrets from being pushed to GitHub.
- Use GitHub Secrets for storing API keys in workflows.

**📬 Contact & Support**  
Have questions or suggestions?  
Reach out via:  
📧 Email: [tanush.chugh@hotmail.com](mailto:tanush.chugh@hotmail.com)  
🌍 Website: Coming Soon!  
📡 Discord Community: Coming Soon!  
**Octahedron** is just a prompt away! 🔥✨  
