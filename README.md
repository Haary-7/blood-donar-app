# 🩸 Blood Donor Finder App  

A **Flask-based web application** that helps users **register as blood donors** and allows others to **search for donors by blood group & city**.  
The goal is to make blood availability faster and easier during emergencies.  


## 🚀 Features  
- 📝 **Register Donor** → Add donor details (Name, Age, Contact, Blood Group, City)  
- 🔍 **Search Donors** → Find donors by **blood group + city**  
- 📋 **Donor Directory** → View donor list with contact info  
- 🎨 **Simple UI** → Clean and responsive design with Bootstrap  

*(Future Enhancements planned)*  
- 🔑 Donor login & authentication  
- 📲 SMS/Email notifications for urgent requests  
- 📊 City-wise donor availability analytics  


## 🛠️ Tech Stack  

**Frontend:**  
- HTML5, CSS3, Bootstrap  

**Backend:**  
- Python (Flask)  

**Database:**  
- SQLite (initial) → scalable to MySQL/Postgres  

**Deployment Options:**  
- Heroku / Render / Railway (free hosting)  
- Docker (optional)  


## 📂 Project Structure  

blood-donor-app/
│── app.py # Flask entry point
│── requirements.txt # Dependencies
│── README.md # Project documentation
│── .gitignore # Ignore venv, pycache, etc.
│── donors.db # SQLite database (auto-created)
│── templates/ # HTML files
│ ├── base.html
│ ├── register.html
│ ├── search.html
│── static/ # CSS/JS files



## ⚙️ Setup & Installation  

1️⃣ Clone the repo  
git clone https://github.com/Haary-7/blood-donor-app.git
cd blood-donor-app

2️⃣ Create a Virtual Environment
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the App
python app.py

App will be available at → http://127.0.0.1:5000/



Contributions are welcome!

Fork the repo

Create a new branch (feature-xyz)

Commit changes & push

Open a Pull Request


📜 License
This project is licensed under the MIT License.

