# Movie Recommendation Web App

A modern movie recommendation system built with FastAPI backend and React frontend, powered by OpenAI API to provide personalized movie suggestions based on your preferences.

---

## 🚀 Features

· 🎬 AI-Powered Recommendations - Get personalized movie suggestions using OpenAI
· 🔍 Natural Language Queries - Describe what you want in plain English
· ⚡ Fast Response - Real-time recommendations with modern UI
· 🎨 Beautiful Interface - Clean, responsive React frontend
· 📱 Mobile Friendly - Works perfectly on all devices

---

## 🏗️ Tech Stack

Component Technology
Backend FastAPI, Python, OpenAI API
Frontend React, JavaScript, HTML/CSS
API RESTful API
Development Uvicorn, npm

---

## 📁 Project Structure

```
movie-recommendation-app/
├── backend/
│   ├── main.py              # FastAPI server
│   ├── requirements.txt     # Python dependencies
│   ├── .env                # Environment variables
│   └── venv/               # Virtual environment
└── frontend/
    ├── src/
    │   ├── App.js          # Main React component
    │   └── components/     # React components
    ├── package.json        # Node.js dependencies
    └── public/             # Static files
```

---

## 🛠️ Installation & Setup

Prerequisites

· Python 3.8+
· Node.js 14+
· OpenAI API account

## 1️⃣ Backend Setup

```bash
# Open terminal and navigate to backend
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt

# Set up environment variables
# Create a .env file and add your OpenAI API key
echo "OPENAI_API_KEY=your_actual_openai_api_key_here" > .env

# Run the FastAPI server
uvicorn main:app --reload
```

Backend runs at 👉 http://localhost:8000

## 2️⃣ Frontend Setup

```bash
# Open a NEW terminal window/tab
cd frontend

# Install Node.js dependencies
npm install

# Start the React development server
npm start
```

Frontend runs at 👉 http://localhost:3000

---

## 🎯 How to Use

1. Open your browser and go to http://localhost:3000
2. Enter your movie preferences in natural language, for example:
   · "Action movies with strong female leads"
   · "Funny romantic comedies from the 90s"
   · "Sci-fi movies with mind-bending plots"
   · "Award-winning dramas from 2020s"
3. Click "Get Recommendations"
4. View your personalized recommendations - The app will display 3-5 curated movie suggestions

---

## 🔧 API Endpoints

Get Movie Recommendations

```http
POST http://localhost:8000/recommend
Content-Type: application/json

{
  "preferences": "Action movies with strong female leads"
}
```

Response:

```json
{
  "recommendations": [
    {
      "title": "Mad Max: Fury Road",
      "year": 2015,
      "reason": "Features Charlize Theron as the formidable Imperator Furiosa"
    }
  ]
}
```

---

## 🐛 Troubleshooting

Common Issues & Solutions

Backend won't start:

· Ensure virtual environment is activated
· Check if .env file exists with valid OpenAI API key
· Verify all dependencies are installed: pip list

Frontend connection issues:

· Make sure backend is running on port 8000
· Check browser console for CORS errors
· Verify API endpoint in frontend code

No recommendations returned:

· Check OpenAI API key validity
· Ensure you have sufficient API credits
· Try simpler, more specific queries

---

## 🚀 Deployment

Backend Deployment Options:

· Railway: Easy FastAPI deployment
· Heroku: Traditional PaaS
· AWS EC2: Full control VPS

Frontend Deployment Options:

· Netlify: Simple drag-and-drop
· Vercel: Optimized for React
· GitHub Pages: Free static hosting

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (git checkout -b feature/AmazingFeature)
3. Commit your changes (git commit -m 'Add some AmazingFeature')
4. Push to the branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

---

Start discovering your next favorite movie! 🎥🍿
