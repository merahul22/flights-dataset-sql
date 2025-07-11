﻿

# ✈️ Flight Data Visualization Dashboard

```markdown


This project is a **flight data analysis dashboard** built using **Streamlit** for the frontend and **MySQL** for backend data storage. It helps analyze airline frequencies, popular routes, and flight trends with interactive visualizations.

---

## 📌 Features

- 🔍 View flights between selected **Source** and **Destination**
- 📈 Visualize **Airline Frequency**
- 🛫 Identify the **Busiest Airports**
- 📅 Track **Daily Flight Frequencies**
- 🎨 Dark mode theme support

---

## 🗂️ Project Structure

```

flights-dataset-sql/
│
├── app.py                  # Main Streamlit app
├── dbhelper.py            # Database class to handle MySQL queries
├── requirements.txt       # All required Python packages
├── flights.csv            # Raw dataset (CSV format)
└── README.md              # Project documentation

````

---

## 💾 Database Setup

1. **Create a MySQL database** called `mydatabase`
2. **Create a table** `flights` with columns matching the dataset:

```sql
CREATE TABLE flights (
  Airline VARCHAR(50),
  Date_of_Journey DATE,
  Source VARCHAR(50),
  Destination VARCHAR(50),
  Route VARCHAR(100),
  Dep_Time TIME,
  Duration INT,
  Total_Stops VARCHAR(20),
  Price INT
);
````

3. **Insert data** using Python (done automatically using `pandas` + `mysql.connector`) or via PHPMyAdmin.

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/flights-dataset-sql.git
cd flights-dataset-sql
```

### 2. Create and activate a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install required packages

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit app

```bash
streamlit run app.py
```

---

## 🎨 Dark Theme in Streamlit

You can enable dark mode via:

1. Streamlit menu → **Settings** → **Theme** → Select **Dark**
2. Or, modify `~/.streamlit/config.toml`:

```toml
[theme]
base="dark"
primaryColor="#00bfff"
backgroundColor="#0e1117"
secondaryBackgroundColor="#262730"
textColor="#ffffff"
```

---

## 📊 Dependencies

```
streamlit
mysql-connector-python
pandas
plotly
```

---

## 👨‍💻 Author

**Rahul Choursiya**

---





