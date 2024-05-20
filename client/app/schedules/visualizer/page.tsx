"use client";
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Link from 'next/link';
import { PrimeReactProvider, PrimeReactContext } from 'primereact/api';
import { DataTable } from 'primereact/datatable';
import { Column } from 'primereact/column';
import { FilterMatchMode } from 'primereact/api';
import { InputText } from 'primereact/inputtext';
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
    const [filters, setFilters] = useState({
      global: { value: null, matchMode: FilterMatchMode.CONTAINS },
    });
  
    const tripheader = <h1 className="mb-5 text-3xl text-center font-bold">Trip Data</h1>;
    const tripfooter = <p className='ml-1'>Total Trips: {tripData ? tripData.length : 0}</p>;
  
    const leadheader = <h1 className="mb-5 text-3xl text-center font-bold">Trip Leader Data</h1>;
    const leadfooter = <p className='ml-1'>Total Leaders: {tripLeaderData ? tripLeaderData.length : 0}</p>;
  
    const prefheader = <h1 className="mb-5 text-3xl text-center font-bold">Trip Preference Data</h1>;
    const preffooter = <p className='ml-1'>Total Preferences: {tripPreferenceData ? tripPreferenceData.length : 0}</p>;
  
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
        filters={filters} 
        tripheader={tripheader} 
        tripfooter={tripfooter} 
      />
      <TripLeaderDataTable 
        tripLeaderData={tripLeaderData} 
        filters={filters} 
        leadheader={leadheader} 
        leadfooter={leadfooter} 
      />
      <TripPreferenceDataTable 
        tripPreferenceData={tripPreferenceData} 
        filters={filters} 
        setFilters={setFilters} 
        prefheader={prefheader} 
        preffooter={preffooter} 
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