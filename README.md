## 🤖 AI SQL Automation using LangChain and OpenAI

This project allows you to interact with your SQL Server database using natural language.
Instead of writing SQL queries manually, you can ask questions in plain English, and the AI will generate and execute SQL queries automatically.

---

# 📌 Features

* Connect to SQL Server using Windows Authentication
* Ask questions in natural language
* Automatically generates SQL queries
* Executes queries and returns results
* Uses OpenAI GPT model for intelligent responses
* Beginner-friendly project structure

---

# 🛠️ Technologies Used

* Python
* LangChain
* OpenAI GPT-4o-mini
* SQLAlchemy
* PyODBC
* Microsoft SQL Server
* dotenv

---

# 📁 Project Structure

```
AI_SQL_AUTOMATION/
│
├── main.py
├── .env
├── requirements.txt
└── README.md


# 💬 Example Questions

You can ask questions like:

```
List all tables
```

```
Show top 5 customers by sales
```

```
Count total orders
```

```
Show total revenue
```

---

# 🧠 How it works

1. User enters a question
2. LangChain SQL Agent converts it into SQL query
3. SQL query is executed on SQL Server
4. Results are returned in natural language

---

# 🔒 Requirements

* Python 
* SQL Server installed
* ODBC Driver 17 for SQL Server
* OpenAI API Key

---

# 📸 Example Output

```
Please ask your question: list all tables

Answer:
Customers, Orders, Products
```

# 👨‍💻 Author

Jayachandra

---

# ⭐ If you like this project, please star the repository!
