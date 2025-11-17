import React, { useState } from "react";
import axios from "axios";

function MovieForm({ setRecommendations }) {
  const [preference, setPreference] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    const res = await axios.post("http://127.0.0.1:8000/recommend", { preference });
    setRecommendations(res.data.recommendations);
  };

  return (
    <form onSubmit={handleSubmit} style={{ marginBottom: "30px" }}>
      <input
        type="text"
        placeholder="Enter your movie preferences (e.g., sci-fi, romance)"
        value={preference}
        onChange={(e) => setPreference(e.target.value)}
        style={{ padding: "10px", width: "60%" }}
      />
      <button
        type="submit"
        style={{ padding: "10px 20px", marginLeft: "10px", cursor: "pointer" }}
      >
        Get Recommendations
      </button>
    </form>
  );
}

export default MovieForm;
