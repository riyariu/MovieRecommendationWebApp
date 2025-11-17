from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .database import Base, engine, SessionLocal
from .models import MoviePreference
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS (allow frontend requests)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class PreferenceInput(BaseModel):
    preference: str


@app.post("/recommend")
async def recommend_movies(input: PreferenceInput, db: Session = Depends(get_db)):
    prompt = f"Recommend 3–5 movies for someone who likes: {input.preference}. Provide a short explanation for each."

    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a movie recommendation engine."},
                {"role": "user", "content": prompt},
            ],
        )

        recommendations = response.choices[0].message.content.strip()

        # Save to DB
        movie_pref = MoviePreference(
            preference=input.preference, recommendations=recommendations
        )
        db.add(movie_pref)
        db.commit()

        return {"recommendations": recommendations}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
