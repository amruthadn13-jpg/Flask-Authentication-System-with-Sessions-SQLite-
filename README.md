# 🔐 Flask Authentication System with Sessions (SQLite)

## 📌 Overview

This project is a **complete Authentication System** built using **Flask (Python)**, **SQLite**, and **HTML/CSS**, with **session-based login management**.

It allows users to:

* Register an account
* Login securely
* Access a protected dashboard
* Logout safely

This project demonstrates **real-world backend concepts**, including session handling and route protection.

---

## ⚙️ Features

✔️ User Registration system
✔️ User Login system
✔️ SQLite database integration
✔️ Session-based authentication
✔️ Protected dashboard route
✔️ Logout functionality
✔️ Clean UI (Login + Register page)
✔️ Dynamic success/error messages

---

## 🛠️ Tech Stack

* **Backend:** Python (Flask)
* **Frontend:** HTML, CSS
* **Database:** SQLite3
* **Authentication:** Flask Sessions

---

## 📂 Project Structure

```id="proj2"
flask-authentication-system-with-session/
│
├── app.py                 # Main Flask application
├── users.db              # SQLite database (auto-created)
│
├── templates/
│   ├── index.html        # Login + Register page
│   └── dashboard.html    # Protected dashboard page
│
└── README.md             # Documentation
```

---

## 🔄 How It Works

### 🔹 Registration Flow

1. User enters username & password
2. Backend checks if username exists
3. If not → stores user in database
4. Displays success/error message

---

### 🔹 Login Flow

1. User submits login form
2. Backend verifies credentials
3. If valid:

   * Stores username in session
   * Redirects to dashboard

---

### 🔹 Dashboard Access

* Only accessible if user is logged in
* Checks:

```python id="code1"
if "user" in session:
```

---

### 🔹 Logout Flow

* Clears session:

```python id="code2"
session.pop("user", None)
```

* Redirects to home page

---

## 🧠 Backend Concepts Used

### ✅ Session Handling

```python id="code3"
session["user"] = username
```

* Stores logged-in user in session

---

### ✅ Route Protection

```python id="code4"
if "user" in session:
```

* Prevents unauthorized access

---

### ✅ Redirects

```python id="code5"
redirect("/dashboard")
```

* Navigates user after login

---

### ✅ Database Operations

* Create table
* Insert user
* Fetch user
* Validate credentials

---

## 🌐 Frontend (UI)

### ✨ Pages

#### 🏠 index.html

* Login form
* Register form
* Displays messages

#### 📊 dashboard.html

* Shows logged-in username
* Logout button

---

## ▶️ How to Run

### 1️⃣ Install Flask

```bash id="run1"
pip install flask
```

### 2️⃣ Run the application

```bash id="run2"
python app.py
```

### 3️⃣ Open browser

```id="run3"
http://127.0.0.1:5000/
```

---

## 📸 Sample Output

* ✅ `Registered Successfully`
* ❌ `Username already exists`
* ❌ `Invalid Login`
* 🎉 `Welcome Amrutha` (Dashboard)

---

## 🔐 Security Note

⚠️ This project uses **plain text passwords** (not secure for production)

### Recommended Improvements:

* Use **bcrypt** for password hashing
* Store hashed passwords instead of plain text
* Use environment variables for secret key
* Add CSRF protection

---

## 🚀 Future Enhancements

* 🔑 Password hashing (bcrypt)
* 🍪 Secure session configuration
* 🔒 JWT-based authentication
* 🎨 UI improvement with Bootstrap
* 📧 Email verification system
* 🔄 Password reset feature

---

## 🧠 Learning Outcomes

* Flask routing and request handling
* SQLite database integration
* Session management
* Authentication flow implementation
* Route protection
* Frontend-backend integration

---

## 👩‍💻 Author

**Amrutha D N**

---

⭐ If you like this project, consider giving it a star!
