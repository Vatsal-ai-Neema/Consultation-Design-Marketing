# Consultation Design Marketing – Full Stack Flask Project

🌐 Live Demo
🔗 Deployed URL
https://consultation-design-marketing-1.onrender.com

A full-stack **Flask-based web application** for a digital consultation & marketing agency.  
The project includes dynamic sections for **Projects**, **Clients**, and **Contact management**, along with an **Admin Panel** for managing content.

---

## 🚀 Features

- Responsive marketing website (HTML, CSS)
- Dynamic **Projects** & **Clients** sections
- Image upload support
- Admin panel using **Flask-Admin**
- Database integration using **Flask-SQLAlchemy**
- Deployed on **Render**
- Production-ready setup using **Gunicorn**

---

## 🛠️ Tech Stack

**Frontend**
- HTML5
- CSS3

**Backend**
- Python
- Flask
- Flask-SQLAlchemy
- Flask-Admin

**Database**
- SQLite (current)
- PostgreSQL (planned for production persistence)

**Deployment**
- Render
- Gunicorn

🗄️ Database Note

-Currently using SQLite for simplicity.
-Data persists locally but may reset on redeploy.
-PostgreSQL integration is planned for permanent data storage in production.

📌 Future Improvements

-PostgreSQL integration
-Admin authentication
-Image optimization
-Pagination for projects & clients
-Backup & restore support

👤Author
Vatsal Neema
GitHub: https://github.com/Vatsal-ai-Neema

##⚙️ Local Setup
```bash
1️⃣ Clone the repository
git clone https://github.com/Vatsal-ai-Neema/Consultation-Design-Marketing.git
cd Consultation-Design-Marketing

## 📂 Project Structure
.
├── app.py
├── models.py
├── requirements.txt
├── start.sh
├── static/
│ ├── style.css
│ └── uploads/
├── templates/
│ └── index.html
└── .gitignore

2️⃣ Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run the application
python app.py
