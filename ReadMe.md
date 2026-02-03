# 📊 Chemical Equipment Parameter Visualizer

### Hybrid Web + Desktop Application

**Developed by: Pankhudi Gupta**

---

## 🧾 Project Overview

The **Chemical Equipment Parameter Visualizer** is a hybrid application that runs both as:

* 🌐 Web Application (React.js)
* 🖥 Desktop Application (PyQt5)

The system allows users to upload a CSV file containing chemical equipment data. The Django backend processes the data using Pandas and returns analytical summaries and visualizations.

Both frontend applications consume the same REST API.

---

## 🏗 Architecture Overview

```
React (Web)        PyQt5 (Desktop)
        │
        │ REST API
        ▼
Django + DRF Backend
        │
        ▼
SQLite Database
```

---

## 🛠 Tech Stack

| Layer            | Technology                      |
| ---------------- | ------------------------------- |
| Backend          | Django + Django REST Framework  |
| Data Processing  | Pandas                          |
| Database         | SQLite                          |
| Web Frontend     | React.js + Chart.js + Bootstrap |
| Desktop Frontend | PyQt5 + Matplotlib              |
| Version Control  | Git & GitHub                    |

---

## 📂 Project Structure

```
chemical-equipment-visualizer/
│
├── backend/              # Django backend
│   ├── manage.py
│   ├── backend/
│   ├── equipment/
│
├── web/                  # React frontend
│
├── desktop/              # Desktop application
│   └── desktop_app.py
│
├── venv/                 # Python virtual environment
├── sample_equipment_data.csv
└── README.md
```

---

# ⚙️ Installation & Setup Guide

Follow these steps exactly to run the project.

---

# 🐍 1️⃣ Backend Setup (Django)

### Step 1: Clone Repository

```
git clone https://github.com/pankhudi24bai10877-star/Chemical-Equipment-Parameter-Visualizer
cd chemical-equipment-visualizer
```

---

### Step 2: Create Virtual Environment

```
python -m venv venv
```

Activate:

**Windows**

```
venv\Scripts\activate
```

**Mac/Linux**

```
source venv/bin/activate
```

---

### Step 3: Install Backend Dependencies

```
pip install django
pip install djangorestframework
pip install pandas
pip install reportlab
pip install django-cors-headers
pip install pyqt5 matplotlib requests
```

---

### Step 4: Apply Database Migrations

```
cd backend
python manage.py makemigrations
python manage.py migrate
```

---

### Step 5: Run Backend Server

```
python manage.py runserver
```

Server will start at:

```
http://127.0.0.1:8000/
```

Keep this terminal running.

---

# 🌐 2️⃣ Web Application Setup (React)

Open a new terminal.

```
cd web
```

### Install Node Modules

```
npm install
```

If required:

```
npm install axios chart.js react-chartjs-2 bootstrap
```

---

### Run Web Application

```
npm start
```

Web app runs at:

```
http://localhost:3000
```

---

# 🖥 3️⃣ Desktop Application Setup

Make sure Django backend is running first.

Open a new terminal:

```
cd desktop
```

Run:

```
python desktop_app.py
```

The desktop dashboard will open.

---

# 📄 Sample CSV Format

The CSV file must contain the following columns:

```
Equipment Name, Type, Flowrate, Pressure, Temperature
```

Example:

```
Pump1, Pump, 120, 10, 45
Valve1, Valve, 90, 8, 50
Reactor1, Reactor, 150, 12, 60
```

---

# 📊 Features Implemented

✔ CSV Upload (Web & Desktop)
✔ Data Processing using Pandas
✔ Summary Statistics (Total & Averages)
✔ Equipment Type Distribution
✔ Pie & Bar Charts (Web)
✔ Embedded Chart (Desktop)
✔ Database Storage (Last 5 Datasets)
✔ REST API Architecture
✔ Hybrid Application Design

---

# 🔐 Authentication

Basic authentication enabled in Django REST Framework configuration.

Admin panel accessible at:

```
http://127.0.0.1:8000/admin/
```

Create superuser if required:

```
python manage.py createsuperuser
```

---

# 🧪 Testing Instructions for Examiner

1. Start Django backend.
2. Start React frontend.
3. Upload sample CSV in web app.
4. Observe:

   * Summary cards
   * Pie chart
   * Bar chart
5. Run desktop application.
6. Upload same CSV.
7. Verify:


---
# 👩‍💻 Developer

**Pankhudi Gupta**
Hybrid Web + Desktop Application
Intern Screening Project