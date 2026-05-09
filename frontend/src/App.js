import React from 'react';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Mini Splunk</h1>
        <p>Log Intelligence System</p>
      </header>

      <main className="App-main">
        <section className="dashboard">
          <h2>Dashboard</h2>
          <p>TODO: Implement dashboard components</p>

          <div className="stats">
            <div className="stat-card">
              <h3>Total Logs</h3>
              <p>0</p>
            </div>
            <div className="stat-card">
              <h3>Active Incidents</h3>
              <p>0</p>
            </div>
            <div className="stat-card">
              <h3>AI Analysis</h3>
              <p>0</p>
            </div>
          </div>
        </section>
      </main>
    </div>
  );
}

export default App;
