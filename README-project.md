📊 Digital Habits & Social Media Usage - Survey Project

This project is a Flask-based survey form designed to collect data from college students on their digital habits and social media usage. 
The collected responses are stored in MySQL database and can be later used for analysis and visualization in tools like Power BI. 
The goal is to analyze digital habits and social media usage patterns among college students through a survey form.

-------------------------------------------

🚀 Project Overview

- A web-based survey form was created using Flask and HTML and CSS.
- Responses are stored in a MySQL database.
- Data is later visualized in Power BI dashboards to extract meaningful insights.
- The form is deployed and tested using PythonAnywhere.

-------------------------------------------

🛠 Tech Stack

| Layer        | Tools Used                    |
|--------------|-------------------------------|
| Frontend     | HTML, CSS                     |
| Backend      | Python (Flask)                |
| Database     | MySQL                         |
| Visualization| Power BI                      |
| Deployment   | PythonAnywhere                |

------------------------------------------

📁 Project Structure

| survey_project/
  
     ├──FlaskApp/  
     |       ├── app.py              # Flask backend logic 
     |       ├── requirements.txt       # Python dependencies 
     |       ├── responses.sql            # MySQL table creation script
     |       ├── static/   
     |           ├── style.css          # CSS styling   
     |           ├── qr_image.png         # QR code image  
     |           ├── clipboard_bg.jpg         # Form Background image  
     |       ├── templates/  
     |            ├── form.html         # HTML form template 
     ├──PowerBI_dashboard
          ├──snapshots            # Store the dashboard(.pbix) file and all the snapshots here 
-----------------------------------------

🔐 Note

🚨 **For security reasons, all database credentials in app.py have been replaced with placeholders.**  
Update them locally before running the app.

-----------------------------------------

💻 How to Run This Project Locally

1. Clone this repository:

   ```bash
   git clone https://github.com/AnupamaChougule/Digital_habits_survey_project.git
   cd Digital_habits_survey_project

2. Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate        # or venv\Scripts\activate on Windows


3. Install dependencies:

pip install -r requirements.txt


4. Set up MySQL database using responses.sql.


5. Update your MySQL credentials in app.py.


6. Run the Flask app:

python app.py

-----------------------------------------

📊 Power BI Dashboard

After responses are collected in the MySQL database, they are exported and visualized in Power BI. Insights include patterns of daily usage, app preferences, screen time, etc.
Dashboards are stored separately and updated manually.

-----------------------------------------

📷 Snapshots

You can find:

 📊 Dashboard snapshots in the PowerBI_dashboard/ folder.

-----------------------------------------

📌 Author

Anupama Chougule
Computer Application Graduate | Aspiring Data Analyst

-----------------------------------------

### 🔗 Connect with me:
- [LinkedIn]---> www.linkedin.com/in/anupama-chougule271
- [GitHub]---> https://github.com/AnupamaChougule

-----------------------------------------

📃 License

This project is for academic and learning purposes only.

-----------------------------------------
