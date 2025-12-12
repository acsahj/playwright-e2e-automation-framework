🚀 Playwright Python Automation Framework

A modern, scalable **Playwright + Python + Pytest** end-to-end (E2E) automation framework designed to demonstrate professional automation engineering practices using the **Page Object Model (POM)** pattern.

---

📚 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation & Setup](#installation--setup)
- [Running Tests](#running-tests)
- [Reports & Artifacts](#reports--artifacts)
- [Pages & Test Design](#pages--test-design)
- [CI/CD Pipeline](#cicd-pipeline)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

---

📖 Overview

This project automates key workflows of a sample application such as:

- Login  
- Product listing  
- Add-to-cart  
- Checkout  
- Negative flows  

It is structured to be clean, maintainable, scalable, and CI-friendly — perfect for learning and building your GitHub automation portfolio.

---

✨ Features

- 🚀 Fast & reliable browser automation with **Playwright**
- 🧩 Modular **Page Object Model** architecture
- 🧪 Testing powered by **Pytest**
- 📊 HTML reporting using **pytest-html**
- 📸 Automatic screenshots & videos on failure
- 🎯 Reusable fixtures for browser/context/page
- 📁 Config-based setup for URLs/test data
- 🤖 Optional GitHub Actions CI pipeline

---

## 🛠 Tech Stack

| Component | Tool |
|----------|------|
| Language | Python 3.x |
| Automation | Playwright |
| Test Runner | Pytest |
| Reporting | pytest-html |
| Code Quality | Black, isort, Flake8 |
| CI/CD | GitHub Actions |

---

## 📁 Project Structure
project/
├── scripts/
│    └── install_browsers.sh
├── src/
│    ├── pages/
│    │     ├── base_page.py
│    │     └── login_page.py
│    └── utils/
├── tests/
│    └── e2e/
├── configs/
├── reports/
├── requirements.txt
├── pytest.ini
├── .gitignore
└── README.md

---

## 📦 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>

2️⃣ Create Virtual Environment
python3 -m venv venv
source venv/bin/activate   # Mac/Linux

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Install Playwright Browsers
./scripts/install_browsers.sh

or
playwright install


▶️ Running Tests
Run all tests
pytest

Run tests in headed mode (browser visible)
pytest --headed

Run with HTML report
pytest --html=reports/report.html

Run a specific test file
pytest tests/e2e/test_login.py


🧩 Pages & Test Design

This framework uses the Page Object Model (POM) pattern:
	•	BasePage contains shared helper methods
	•	LoginPage contains login-specific elements & actions
	•	Additional pages (ProductPage, CartPage, CheckoutPage) can be added as the test suite grows

This keeps tests clean, readable, and scalable.

⸻

⚙️ CI/CD Pipeline

A GitHub Actions workflow (.github/workflows/ci.yml) can be configured to:
	•	Set up Python
	•	Install dependencies
	•	Install Playwright browsers
	•	Run tests
	•	Upload reports/screenshots as artifacts

(Add after CI setup is complete.)

⸻

🌱 Future Enhancements
	•	Cross-browser test matrix (Chromium, Firefox, WebKit)
	•	Parallel execution
	•	Visual regression testing
	•	Accessibility testing (axe-core)
	•	Retry logic for flaky tests
	•	Allure reporting

⸻

🤝 Contributing

Contributions are welcome!
Please create an issue or submit a pull request for any suggestions or improvements.

⸻

📄 License

This project is licensed under the MIT License.
Feel free to use it for learning or portfolio purposes.