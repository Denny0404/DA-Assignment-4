
# Database Automation Assignment 4 – PROG8850

## 🧾 Overview

This project demonstrates the use of Ansible and Flyway to automate database schema deployment, testing, and version control. It manages a MySQL database for subscribers and supports a CI/CD-compatible migration strategy.

---

## 📁 Project Structure

```
DA-Assignment-4/
├── migrations/                 # Flyway SQL migration scripts (V1, V2, V3...)
├── up.yaml                     # Ansible playbook to initialize DB and run Flyway
├── down.yaml                   # Ansible playbook to dump seed data and stop DB
├── dbtests.py                  # Python script to validate DB schema
├── flyway.conf                 # Flyway configuration for MySQL connection
├── flyway/                     # Flyway CLI (unzipped)
└── README.md                   # This guide
```

---

## ⚙️ Setup Instructions

### 1️⃣ Install Requirements

```bash
sudo apt update
sudo apt install mysql-server -y
sudo service mysql start

pip install -r requirements.txt  # mysql-connector-python
```

---

### 2️⃣ Configure MySQL User

```bash
sudo mysql -e "ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY ''; FLUSH PRIVILEGES;"
```

---

### 3️⃣ Download Flyway

```bash
curl -L https://repo1.maven.org/maven2/org/flywaydb/flyway-commandline/9.22.3/flyway-commandline-9.22.3-linux-x64.tar.gz -o flyway.tar.gz
tar -xzf flyway.tar.gz
mv flyway-9.22.3 flyway
chmod +x flyway/flyway
```

---

## 🚀 How to Run the Project

### ✅ 1. Run `up.yaml`

```bash
ansible-playbook up.yaml
```

This playbook:
- Starts MySQL
- Creates the `subscribers` database
- Runs Flyway migrations (V1, V2, V3...)

---

### ✅ 2. Validate Schema

```bash
python dbtests.py
```

Expected Output:
```
✅ Schema validation passed.
```

---

### ✅ 3. Check Data (optional)

```bash
sudo mysql -u root
USE subscribers;
SELECT * FROM subscriber;
```

You should see the `email` and `subscription_date` columns.

---

### ✅ 4. Run `down.yaml`

```bash
ansible-playbook down.yaml
```

This:
- Seeds new subscriber data to V2 file
- Stops MySQL service

---

## 🧪 Testing Changes

### Add Migration

```bash
# Make migration file like V3__add_column.sql
# OR run:
./flyway/flyway -configFiles=flyway.conf repair
```

### Test

```bash
python dbtests.py
```

---

## 📝 Notes

- `up.yaml` is idempotent
- Always commit the migration files after `down.yaml`
- Use Git commits after each migration and test

---

## 🏁 Submission Checklist

- [x] `up.yaml` correctly sets up and runs Flyway
- [x] `dbtests.py` validates DB structure (tests for subscription_date)
- [x] `down.yaml` dumps data and stops DB
- [x] README provided with all instructions

---

## 👨‍💻 Author

Denish Akbari  
Course: PROG8850 – Database Automation  
Conestoga College, 2025
