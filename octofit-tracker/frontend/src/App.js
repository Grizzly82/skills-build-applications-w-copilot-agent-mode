import { useEffect, useState } from 'react';
import { getUserProfile, getActivityLogs } from './apiService';
import './App.css';

function App() {
  const [userProfile, setUserProfile] = useState(null);
  const [activityLogs, setActivityLogs] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const profile = await getUserProfile();
        setUserProfile(profile);

        const activities = await getActivityLogs();
        setActivityLogs(activities);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Welcome to OctoFit Tracker</h1>
        {userProfile && (
          <div>
            <h2>User Profile</h2>
            <p>Name: {userProfile.user}</p>
            <p>Age: {userProfile.age}</p>
            <p>Height: {userProfile.height} cm</p>
            <p>Weight: {userProfile.weight} kg</p>
          </div>
        )}
        <h2>Activity Logs</h2>
        <ul>
          {activityLogs.map((log) => (
            <li key={log.id}>
              {log.activity_type} - {log.duration} minutes
            </li>
          ))}
        </ul>
      </header>
    </div>
  );
}

export default App;
