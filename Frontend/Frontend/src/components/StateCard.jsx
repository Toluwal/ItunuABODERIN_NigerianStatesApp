import { useEffect, useState } from "react";
function StateCard() {
  const [states, setStates] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  async function getStates() {
    try {
      const response = await fetch("http://127.0.0.1:8000/states");
      if (!response.ok) {
        throw new Error("Encountered an issue while fetching states");
      }
      const data = await response.json();
      setStates(data.states || []);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }
  useEffect(() => {
    getStates();
  }, []);
  if (loading) return <p>Loading States...</p>;
  if (error) return <p>Error: {error}</p>;
  return (
    <div className="container">
      <h1>Nigerian States Cards</h1>
      {states.length === 0 ? (
        <p>No states found.</p>
      ) : (
        <div className="states_list">
          {states.map(state => (
            <div key={state.id} className="states_card">
                <p>{state.name}</p>
                <p>{state.capital}</p>
                <p>{state.region}</p>
                <p>{state.slogan}</p>
                <p>{state.population}</p>
                <p>{state.landmarks}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
export default StateCard;