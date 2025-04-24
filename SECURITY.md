# 🔐 Security Policy – Octahedron AI by Octahedron Tech

We take security seriously at **Octahedron Tech** and strive to protect user data, APIs, and the platform itself from vulnerabilities or misuse.

---

## 📥 Reporting a Vulnerability

If you discover a security vulnerability, please report it responsibly.

- 📧 Contact: [tanush.chugh@hotmail.com](mailto:tanush.chugh@hotmail.com)
- Please include:
  - A clear description of the issue
  - Steps to reproduce (if applicable)
  - Potential impact or exploitability

We appreciate responsible disclosure and will aim to resolve issues promptly.

---

## 🛡️ Best Practices for Users

To help keep your setup secure:

- **Never expose your `.env` file.** It contains sensitive information like API keys and tokens.  
- Add `.env` to `.gitignore` to prevent it from being committed to version control.
- Use **GitHub Secrets** or a similar service to store keys in CI/CD pipelines.
- Keep your dependencies updated. Use `pip list --outdated` regularly.
- Avoid hardcoding secrets or tokens directly in your source code.

---

## 🔄 Dependency Management

We rely on trusted libraries, including:

- `discord.py`
- `torch`
- `requests`
- `python-dotenv`

We recommend using tools like:
- [`pip-audit`](https://pypi.org/project/pip-audit/)
- [GitHub Dependabot](https://github.com/dependabot)

To scan for known vulnerabilities and outdated packages.

---

## 🧪 Security Enhancements

We integrated:  
- ✅ Automated dependency vulnerability scans
- 🔍 Security-focused linting tools
- 🚫 PR blockers for insecure or deprecated code patterns

---

Thank you for helping us keep **Octahedron AI** safe and secure! 🛡️✨
