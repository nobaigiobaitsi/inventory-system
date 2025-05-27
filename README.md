# Inventory Management System (Work in Progress)

A simple inventory management system built with **Python** and **MySQL**. This is a CLI-based tool designed for single-user use (for now), focused on CRUD operations for managing stock.

> This project is a work in progress, starting as a local app. The goal is to eventually turn it into a full-stack web-based solution.

---

## 🚀 Features (so far)

- Add a new product
- Connect securely to a MySQL database using environment variables
- Update stock quantities (coming next)
- View current inventory (coming soon)
- Remove a product (coming soon)

---

## 🏗️ Tech Stack

- Python
- MySQL (local database)
- `mysql-connector-python`
- `.env` file for secure credentials (excluded via `.gitignore`)

---

## 🔐 Security Notes

- Credentials (user, password, etc.) are stored in a `.env` file and loaded securely using `python-dotenv`.
- The `.env` file is excluded from Git using `.gitignore`.

---
