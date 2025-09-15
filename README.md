👩‍💻 Women in Tech in Ghana – Interactive Dashboard

An interactive data dashboard built with Streamlit, Pandas, and Plotly to explore insights, trends, and opportunities for women in Ghana’s tech ecosystem.

🌍 Live Demo on Streamlit Cloud
 (https://women-in-tech-ghana-g99wbow4j6zp8ptbyxi7wq.streamlit.app/)

📊 Features

Trends Over Time – Line charts showing women in tech leadership and workforce growth.

STEM Graduates – Bar chart comparing male vs female graduates by region.

Roles in Tech – Interactive pie chart showing women’s representation in various tech roles.

Leadership by Region – Compare representation across Accra, Kumasi, etc.

Communities Map – Explore women-in-tech hubs (e.g., Soronko Academy, Women in Tech Africa).

Filters & Interactivity – Choose year, region, and category dynamically.

🛠 Tech Stack

Streamlit
 – web app framework

Plotly Express
 – interactive charts

Pandas
 – data manipulation

Data: Mock dataset + Ghana communities (CSV)

📂 Project Structure
women-in-tech-ghana/
│── data/
│    ├── education.csv
│    ├── roles.csv
│    ├── leadership.csv
│    └── communities.csv
│── app.py
│── requirements.txt
│── README.md

🚀 Run Locally

Clone the repo:

git clone https://github.com/Priscillagit/women-in-tech-ghana.git
cd women-in-tech-ghana


Create & activate a virtual environment (Windows example):

python -m venv venv
venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt


Run the dashboard:

streamlit run app.py


Open your browser → http://localhost:8501

🌐 Deployment

You can deploy for free on Streamlit Cloud:

Push this repo to GitHub.

Go to share.streamlit.io
.

Connect your GitHub repo.

Deploy 🚀.

📌 Future Improvements

Add real data from Ghana Statistical Service & Women in Tech Africa reports.

Include salary gap analysis.

Add survey insights (barriers, opportunities, mentorship impact).

Build a React/Next.js version for public web hosting.

👤 Author

Developed by Priscilla Dankwa

💼 Fiverr: https://www.fiverr.com/s/yv4v7Q5


✨ This dashboard highlights the importance of women in Ghana’s growing tech ecosystem and provides data-driven storytelling to inspire change.
