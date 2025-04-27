# 🚀 Octahedron AI – Your AI Memory Keeper! 🧠✨  

Octahedron AI (by Octahedron Tech) remembers, so you don’t have to! With **smart recall**, **deep insights**, and **effortless conversation**, it keeps knowledge at your fingertips. Whether you're brainstorming, researching, or solving problems — Octahedron AI is your ultimate AI companion! 🤖💡  

## 💵 Donate/Support me  
- [![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/O5O71E53A8)

## 😎 Octahedron AI is primarily open-source but includes certain parts that may remain closed-source due to security, financial, or proprietary reasons. Here’s a breakdown ⛓️‍💥  
### Open-Source Components  
- The core AI functions, commands, and integration with models like LLaMA 3.2, BLIP-2, and OpenJourney. (Other models coming soon, for now LLaMA 3.2 is the only one)  
- Most of the interaction logic for Discord commands.  
- Front-end components like the web interface and public utilities. (Coming soon)  

### Closed-Source Components (coming soon)  
- Payment Algorithms: The financial logic behind user subscriptions and payments will remain closed-source for security and business reasons. (Implementing soon)  
- Key Generation: The algorithm and related functions for generating activation keys will be closed-source to maintain the security of the system. (Implementing soon)  
- Database Handling: Parts of the database management system, especially those related to sensitive data, may be closed-source as they evolve. (Implementing soon)  

### License  
- This project is open-source under the MPL-2.0 license, except for the closed-source components which are proprietary and not open to modification or distribution.  

### Contributing  
- Contributions to open-source portions of the project are welcome! Please fork the repository, make your changes, and submit a pull request.  
- If you're interested in working on or integrating with the closed-source components, please [contact](mailto:tanush.chugh@hotmail.com) us for collaboration opportunities.  

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
```
1️⃣ Clone the Repository  
git clone https://github.com/TanushChugh19/Octahedron-AI.git
cd Octahedron-AI

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Set Up Environment Variables
Create a .env file to store API keys and tokens (keep the file in the same directory as app.py file):
TOKEN=your_discord_bot_token_here
API_KEY=your_timezonedb_api_key_here
- link for api: (https://timezonedb.com/)

4️⃣ Replace ALLOWED_USER = 0 in app.py with your discord user id.

5️⃣ Run the Bot
python bot.py

6️⃣ Alternatively, use setup.sh or setup.bat and perform step 3 and 4
- For Linux/macOS:  
  bash setup.sh  
- For Windows:  
  setup.bat
```
🗒️ **Note:**  
- You may need to adjust the PyTorch version inside the `requirements.txt` file based on your CUDA version (default is CUDA 12.8).
- Octahedron AI is mostly open-source but some parts like payment algorithms, key generation and database related files may become closed-source as time passes.

⚙️ **Usage Once running, Octahedron AI responds to Discord commands:**  
- *hello – Greet the AI.
- *oct <message> – Chat with Octahedron AI.

**👥 Contributing
We welcome contributions! Follow these steps:**
- Fork this repository and clone it to your machine.
- Create a new branch for your feature (git checkout -b feature-branch).
- Make changes, test them, and commit updates.
- Submit a pull request explaining your improvements.

**🐛 Known Bugs/Flaws (Status — Patched: ✅ | Pending Fix: ❌ | Patched changes are in latest release: `v0.1-alpha.2`)**  
- ❌ `describe` command is functional but provides inaccurate image descriptions.  
- ❌ `imagegen` and `rag` commands are not implemented yet.
- ❌ No database backend implemented — currently using in-memory or file-based storage.  
- ✅ In `v0.0-alpha.1 Python's` `random` module for key generation — not cryptographically secure.
- ✅ In `v0.0-alpha.1` `zones` command caused the bot to hang on slow/unresponsive APIs.
- ✅ In `v0.0-alpha.1` `describe` command triggers `KeyError` sometimes.
- ✅ In `v0.0-alpha.1` `zones` command API call link had double quotation for `API_KEY` in f string with double quotes.  

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
