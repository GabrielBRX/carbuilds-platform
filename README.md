
# CarBuilds Platform

REST API built with Python and FastAPI for managing car builds, users, and image uploads.

## 🚀 Technologies Used

- Python
- FastAPI
- SQLAlchemy
- Pydantic
- JWT Authentication
- SQLite
- Swagger/OpenAPI
- Git & GitHub

---

## 📌 Features

- User registration
- JWT authentication login
- Full CRUD for car builds
- Image upload and management
- Modular project architecture
- Automatic Swagger documentation
- Data validation and error handling

---

## 📂 Project Structure

```bash
backend/
│
├── app/
│   ├── models/
│   ├── routers/
│   ├── schemas/
│   ├── services/
│   ├── database/
│   └── core/
│
├── uploads/
├── requirements.txt
└── main.py

⚙️ Running the Project

1. Clone the repository
git clone https://github.com/GabrielBRX/carbuilds-platform.git

2. Enter the folder
cd carbuilds-platform/backend

3. Create a virtual environment
python -m venv venv

4. Activate the virtual environment
Windows

venv\\Scripts\\activate
Linux/macOS
source venv/bin/activate
5. Install dependencies
pip install -r requirements.txt

6. Run the project
uvicorn app.main:app --reload

📖 API Documentation

Swagger:

http://127.0.0.1:8000/docs

Redoc:

http://127.0.0.1:8000/redoc
🎯 Project Goal

This project was created to practice Back-end development using FastAPI, REST API architecture, JWT authentication, and database integration.

