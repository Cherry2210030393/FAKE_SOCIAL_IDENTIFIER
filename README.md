
# 🕵️‍♂️ Fake Social Media Account Identifier

This project is designed to detect fake or impersonated social media accounts (especially on Instagram) using real-time public data. It analyzes profile bios, usernames, post counts, image content, and other metadata to identify suspicious or fake activity.

---

## 🎯 Goal

To build a tool that flags potentially fake or impersonated accounts using a combination of:
- Web automation
- Natural Language Processing (NLP)
- Image analysis

---

## 🛠 Tech Stack

| Component      | Technology Used                     |
|----------------|-------------------------------------|
| Language       | Python                              |
| Automation     | Selenium (for scraping Instagram)   |
| NLP            | spaCy / NLTK (for bio analysis)     |
| Image Analysis | OpenCV / ImageHash                  |
| UI (Optional)  | Streamlit or Flask (for interface)  |
| Deployment     | GitHub / PythonAnywhere / Streamlit Cloud |

---

## 📌 Features

- 🔍 Extracts bio, username, followers, posts, and profile picture.
- 🧠 Uses NLP to detect suspicious keywords in bios.
- 🖼 Detects stock or repeated profile pictures using image hashing.
- 📆 Flags newly created or low-activity accounts.
- 🎭 Detects impersonation of celebrities/public figures.
- ✅ Real-time analysis using live Instagram data.

---

## 📸 Sample Detection Parameters

| Parameter            | Suspicious If...                                |
|----------------------|--------------------------------------------------|
| Username             | Contains random numbers, "official", "fan", etc.|
| Bio                  | Empty or full of emojis / weird symbols         |
| Profile Picture      | Matches common/famous photos                    |
| Followers vs Posts   | Very high followers but no posts                |
| Recent Activity      | No recent activity                              |

---

## 🚀 How to Run Locally

```bash
git clone https:https://github.com/Cherry2210030393/FAKE_SOCIAL_IDENTIFIER.git
cd FAKE_SOCIAL_IDENTIFIER
pip install -r requirements.txt
python app.py
```

---

## 🧪 How to Test

You can use test cases like:
- Simulated fake profiles with stock profile pictures
- Empty bios
- Scraped celebrity account names with random usernames

---

## 🧠 Example Use Cases

- Detecting impersonation of public figures
- Filtering fake followers
- Safety check before following or interacting with accounts

---

## 📂 Folder Structure

```
FAKE_SOCIAL_IDENTIFIER/
├── app.py
├── bio_analysis.py
├── image_compare.py
├── instagram_scraper.py
├── requirements.txt
└── README.md
```

---

## ⚠️ Disclaimer

This tool is for educational and research purposes only. It does not access private data or violate any platform's terms of use. All data is collected from public profiles.

---

