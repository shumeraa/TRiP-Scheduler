"use client";
import React, { useEffect, useState } from 'react';
import TripDataTable from './components/TripDataTable';
import TripLeaderDataTable from './components/TripLeaderDataTable';
import TripPreferenceDataTable from './components/TripPreferenceDataTable';
import EditTripAndLeader from './components/EditTripAndLeader';
import { fetchData, resetDatabase, sendDataToBackend } from './utils/api';


  const App = () => {
    // Table display variables
    const [isLoading, setLoading] = useState(true);
    const [tripData, setTripData] = useState([]);
    const [tripLeaderData, setTripLeaderData] = useState([]);
    const [tripPreferenceData, setTripPreferenceData] = useState([]);
    
    // Initial fetch on component mount
    useEffect(() => {
      fetchData(setLoading, setTripData, setTripLeaderData, setTripPreferenceData);
    }, []);
  
    const populateTablesWithNewData = () => {
      fetchData(setLoading, setTripData, setTripLeaderData, setTripPreferenceData);
    };
  
  if (isLoading) return <p>Loading...</p>;

  return (
    <div>
    <div>
    <div>

    <div className="navbar bg-base-100 justify-center">
        <a className="btn btn-ghost text-xl" href="/">home</a>
        <a className="btn btn-ghost text-xl" href="/schedules">schedules</a> 
        <a className="btn btn-ghost text-xl" href="/about">about</a>
    </div>

      <TripDataTable 
        tripData={tripData} 
      />
      <TripLeaderDataTable 
        tripLeaderData={tripLeaderData} 
      />

      <TripPreferenceDataTable 
        tripPreferenceData={tripPreferenceData} 
      />

      </div>

      <EditTripAndLeader 
        tripData={tripData} 
        tripLeaderData={tripLeaderData} 
        populateTablesWithNewData={populateTablesWithNewData} 
      />
      
      <div className="mt-10"></div>
      <div className="flex justify-center pt-4">
      <button className="btn btn-outline text-xl mb-5" onClick={() => {
    resetDatabase();
    populateTablesWithNewData();
    }}>Delete All Data</button>
      </div>

    </div>
  </div>
  
  );
};

export default App;