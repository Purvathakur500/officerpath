# 🛡️ OfficerPath

A comprehensive Defence Exam Preparation Platform built using **Python**, **Streamlit**, and **PostgreSQL**. OfficerPath helps defence aspirants organize their preparation by tracking study sessions, practicing mock tests and previous year questions, monitoring fitness, and planning study schedules.

🌐 **Live Demo:** (https://officerpath-3q2pibbs529zjbgzycvhek.streamlit.app/)

💻 **GitHub Repository:** https://github.com/Purvathakur500/officerpath

---

## 📖 About the Project

OfficerPath is a one-stop platform designed for students preparing for defence examinations such as NDA, CDS, AFCAT, and CAPF. It combines study management, performance tracking, and fitness planning into a simple and interactive dashboard.

The application stores user data securely in a PostgreSQL database hosted on Neon and is deployed using Streamlit Community Cloud.

---

## ✨ Features

### 👤 User Management
- Register new users
- Existing user login
- User-specific dashboard

### 📚 Study Tracker
- Log daily study sessions
- Record study duration
- View study history
- Track consistency

### 📝 Mock Tests
- Multiple defence exam subjects
- Instant score calculation
- Performance analysis

### 📖 Previous Year Questions (PYQ)
- Practice exam-wise PYQs
- Automatic scoring
- Attempt history

### 💪 Fitness Tracker
- Daily workout tracking
- Defence fitness preparation
- Progress monitoring

### 🤖 AI Study Planner
- Personalized study planning
- Structured preparation guidance

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend Logic |
| Streamlit | Web Application |
| PostgreSQL (Neon) | Cloud Database |
| Psycopg2 | Database Connectivity |
| Git & GitHub | Version Control |
| Streamlit Community Cloud | Deployment |

---

## 📂 Project Structure

```
OfficerPath/
│
├── app.py
├── database/
│   ├── db.py
│   └── queries.py
│
├── pages/
│   ├── registration.py
│   ├── dashboard.py
│   ├── fitness.py
│   ├── practice_pyq.py
│   └── ai_planner.py
│
├── mock_tests/
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Purvathakur500/officerpath.git
```

Go to the project directory

```bash
cd officerpath
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.streamlit/secrets.toml` file with your PostgreSQL credentials:

```toml
DB_HOST = "your_host"
DB_NAME = "your_database"
DB_USER = "your_username"
DB_PASSWORD = "your_password"
DB_PORT = "5432"
```

Run the application

```bash
streamlit run app.py
```

---

## 📊 Database

The application uses PostgreSQL hosted on **Neon**.

Main tables include:

- Users
- StudySessions
- PYQResults

---

## 🚀 Future Improvements

- Leaderboard
- Daily study reminders
- AI-powered performance analysis
- Subject-wise analytics
- Mobile responsive UI
- Dark mode

---

## 👨‍💻 Developer

**Purva Thakur**

GitHub: https://github.com/Purvathakur500

---

## 📜 License

This project was developed for academic and learning purposes as part of a software development bootcamp.
