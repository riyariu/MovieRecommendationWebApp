import React, { useState } from "react";
import MovieForm from "./components/MovieForm";
import MovieList from "./components/MovieList";
import "./App.css";

function App() {
  const [recommendations, setRecommendations] = useState("");

  return (
    <div className="App" style={{ textAlign: "center", marginTop: "50px" }}>
      <h1>🎬 Movie Recommender</h1>
      <MovieForm setRecommendations={setRecommendations} />
      <MovieList recommendations={recommendations} />
    </div>
  );
}

export default App;
