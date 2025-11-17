import React from "react";

function MovieList({ recommendations }) {
  return (
    <div style={{ width: "60%", margin: "auto", textAlign: "left" }}>
      {recommendations ? (
        <pre style={{ whiteSpace: "pre-wrap" }}>{recommendations}</pre>
      ) : (
        <p>No recommendations yet.</p>
      )}
    </div>
  );
}

export default MovieList;
