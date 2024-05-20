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
import { fetchData, resetDatabase, sendDataToBackend } from './utils/api';
import { useValidation } from './utils/validateInputs';

  const App = () => {
    // Table display variables
    const [isLoading, setLoading] = useState(true);
    const [tripData, setTripData] = useState([]);
    const [tripLeaderData, setTripLeaderData] = useState([]);
    const [tripPreferenceData, setTripPreferenceData] = useState([]);
    const [filters, setFilters] = useState({
      global: { value: null, matchMode: FilterMatchMode.CONTAINS },
    });

    const {
      showInvalidNumberAlert,
      validateNumInput,
      validateYear,
      validateMonth,
      validateDay,
      validateTripName,
    } = useValidation();
  
    const tripheader = <h1 className="mb-5 text-3xl text-center font-bold">Trip Data</h1>;
    const tripfooter = <p className='ml-1'>Total Trips: {tripData ? tripData.length : 0}</p>;
  
    const leadheader = <h1 className="mb-5 text-3xl text-center font-bold">Trip Leader Data</h1>;
    const leadfooter = <p className='ml-1'>Total Leaders: {tripLeaderData ? tripLeaderData.length : 0}</p>;
  
    const prefheader = <h1 className="mb-5 text-3xl text-center font-bold">Trip Preference Data</h1>;
    const preffooter = <p className='ml-1'>Total Preferences: {tripPreferenceData ? tripPreferenceData.length : 0}</p>;
  
    // Edit data variables
    const [classYear, setClassYear] = useState('');
    const [semestersLeft, setSemestersLeft] = useState('');
    const [numTripsAssigned, setNumTripsAssigned] = useState('');
    const [tripName, setTripName] = useState('');
    const [startDateYear, setStartDateYear] = useState('');
    const [startDateMonth, setStartDateMonth] = useState('');
    const [startDateDay, setStartDateDay] = useState('');
    const [endDateYear, setEndDateYear] = useState('');
    const [endDateMonth, setEndDateMonth] = useState('');
    const [endDateDay, setEndDateDay] = useState('');
  
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

      <details className="collapse bg-base-200">
          <summary className="collapse-title text-l font-medium">Click to Edit Rows</summary>
          <div className="collapse-content"> 
          <div className="flex justify-center">
        <div style={{ fontSize: '15px' }}> 
          Leave fields blank if you do not want to change their value :)
        </div>
      </div>
      <div className="join justify-start items-center space-x-2 p-6">
      <span className="font-semibold" style={{whiteSpace: 'nowrap'}}>Edit Trip Leader:</span>
      <select id="tripLeaderSelect" className="select select-bordered text-xs">
        <option disabled selected>Trip Leader Name</option>
        {tripLeaderData.map(trip_leader => (
          <option key={trip_leader.id} value={trip_leader.id} className="p-2 text-sm leading-6">
            {trip_leader.name}
          </option>
        ))}
      </select>
      <input type="text" placeholder="Class year" className="input input-bordered input-sm w-1/6 max-w-xs" value={classYear} onBlur={validateYear(setClassYear)}  onChange={(e) => setClassYear(e.target.value)}/>
      <input type="text" placeholder="Semesters Left" className="input input-bordered input-sm w-1/4 max-w-xs" value={semestersLeft} onBlur={validateNumInput(setSemestersLeft)}  onChange={(e) => setSemestersLeft(e.target.value)}/>
      <input type="text" placeholder="Number of Trips Assigned" className="input input-bordered input-sm w-2/5 max-w-xs" value={numTripsAssigned} onBlur={validateNumInput(setNumTripsAssigned)}  onChange={(e) => setNumTripsAssigned(e.target.value)}/>
      <select id="coLead1" className="select select-bordered text-xs">
      <option disabled selected>1st Preferred Co-Lead</option>
        {tripLeaderData.map(trip_leader => (
          <option key={trip_leader.id} value={trip_leader.id} className="p-2 text-sm leading-6">
            {trip_leader.name}
          </option>
        ))}
      </select>
      <select id="coLead2" className="select select-bordered text-xs">
      <option disabled selected>2nd Preferred Co-Lead</option>
        {tripLeaderData.map(trip_leader => (
          <option key={trip_leader.id} value={trip_leader.id} className="p-2 text-sm leading-6">
            {trip_leader.name}
          </option>
        ))}
      </select>
      <select id="coLead3" className="select select-bordered text-xs">
      <option disabled selected>3rd Preferred Co-Lead</option>
        {tripLeaderData.map(trip_leader => (
          <option key={trip_leader.id} value={trip_leader.id} className="p-2 text-sm leading-6">
            {trip_leader.name}
          </option>
        ))}
      </select>
      </div>

      <div className="join justify-start space-x-2 pl-40">
      <select id="bikingLeaderStatus" className="select select-bordered text-xs w-1/3">
        <option disabled selected>Biking Status</option>
        <option>Lead Guide</option>
        <option>Interested in Promotion</option>
        <option>Not Interested in Promotion</option>
      </select>
      <select id="overnightLeaderStatus" className="select select-bordered text-xs w-1/3">
        <option disabled selected>Overnight Status</option>
        <option>Lead Guide</option>
        <option>Interested in Promotion</option>
        <option>Not Interested in Promotion</option>
      </select>
      <select id="seaKayakingLeaderStatus" className="select select-bordered text-xs w-1/3">
        <option disabled selected>Sea Kayaking Status</option>
        <option>Lead Guide</option>
        <option>Interested in Promotion</option>
        <option>Not Interested in Promotion</option>
      </select>
      <select id="spelunkingLeaderStatus" className="select select-bordered text-xs w-1/3">
        <option disabled selected>Spelunking Status</option>
        <option>Lead Guide</option>
        <option>Interested in Promotion</option>
        <option>Not Interested in Promotion</option>
      </select>
      <select id="surfingLeaderStatus" className="select select-bordered text-xs w-1/3">
        <option disabled selected>Surfing Status</option>
        <option>Lead Guide</option>
        <option>Interested in Promotion</option>
        <option>Not Interested in Promotion</option>
      </select>
      <select id="watersportsLeaderStatus" className="select select-bordered text-xs w-1/3">
        <option disabled selected>Watersports Status</option>
        <option>Lead Guide</option>
        <option>Interested in Promotion</option>
        <option>Not Interested in Promotion</option>
      </select>
      </div>
      {/* End of the "Edit trip leader" join section */}
      
      {/* Start of the "Edit trip" join section */}
      <div className="join justify-start items-center space-x-2 p-20 py-10">
      <span className="font-semibold" style={{whiteSpace: 'nowrap'}}>Edit Trip:</span>
      <select id="tripSelect" className="select select-bordered text-xs">
        <option disabled selected>Trip ID</option>
        {tripData.map(trip => (
          <option key={trip.trip_id} value={trip.trip_id} className="p-2 text-sm leading-6">
            {trip.trip_id}
          </option>
        ))}
      </select>
      <input type="text" placeholder="Trip Name" className="input input-bordered input-sm w-1/2 max-w-xs" value={tripName} onBlur={validateTripName(setTripName)} onChange={(e) => setTripName(e.target.value)}/>
      <select id="categorySelect" className="select select-bordered text-xs">
        <option disabled selected>Trip Category</option>
        <option>Surfing</option>
        <option>Sea Kayaking</option>
        <option>Biking</option>
        <option>Watersports</option>
        <option>Spelunking</option>
        <option>Overnight</option>
      </select>
      <input type="text" placeholder="Start Date Year" className="input input-bordered input-sm w-1/4 max-w-xs" value={startDateYear} onBlur={validateYear(setStartDateYear)}  onChange={(e) => setStartDateYear(e.target.value)}/>
      <span className="font-semibold" style={{whiteSpace: 'nowrap'}}>/</span>
      <input type="text" placeholder="Start Month" className="input input-bordered input-sm w-1/5 max-w-xs" value={startDateMonth} onBlur={validateNumInput(setStartDateMonth)}  onChange={(e) => setStartDateMonth(e.target.value)}/>
      <span className="font-semibold" style={{whiteSpace: 'nowrap'}}>/</span>
      <input type="text" placeholder="Start Day" className="input input-bordered input-sm w-1/5 max-w-xs" value={startDateDay} onBlur={validateDay(setStartDateDay)}  onChange={(e) => setStartDateDay(e.target.value)}/>
      <span className="font-semibold" style={{whiteSpace: 'nowrap'}}>--></span>
      <input type="text" placeholder="End Date Year" className="input input-bordered input-sm w-1/4 max-w-xs" value={endDateYear} onBlur={validateYear(setEndDateYear)}  onChange={(e) => setEndDateYear(e.target.value)}/>
      <span className="font-semibold" style={{whiteSpace: 'nowrap'}}>/</span>
      <input type="text" placeholder="End Month" className="input input-bordered input-sm w-1/5 max-w-xs" value={endDateMonth} onBlur={validateNumInput(setEndDateMonth)}  onChange={(e) => setEndDateMonth(e.target.value)}/>
      <span className="font-semibold" style={{whiteSpace: 'nowrap'}}>/</span>
      <input type="text" placeholder="End Day" className="input input-bordered input-sm w-1/5 max-w-xs" value={endDateDay} onBlur={validateDay(setEndDateDay)}  onChange={(e) => setEndDateDay(e.target.value)}/>
      </div>
      <div className="join justify-start space-x-2 pl-40">
      <select id="leadGuidesNeeded" className="select select-bordered text-xs">
        <option disabled selected># of Lead Guides</option>
        <option>0</option>
        <option>1</option>
        <option>2</option>
        <option>3</option>
        <option>4</option>
      </select>
      <select id="totalGuidesNeeded" className="select select-bordered text-xs">
        <option disabled selected># of Total Guides</option>
        <option>0</option>
        <option>1</option>
        <option>2</option>
        <option>3</option>
        <option>4</option>
      </select>
      </div>
      <div className="flex justify-center pt-4">
      <button className="btn btn-primary  " onClick={() => {
    sendDataToBackend();
    populateTablesWithNewData();
  }}>Submit Trip Changes</button>
      </div>
      </div>
    </details>
      {/* End of the "Edit trip" join section, start displaying data */}

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
      <div className="mt-10"></div>
      <div className="flex justify-center pt-4">
      <button className="btn btn-outline text-xl mb-5" onClick={() => {
    resetDatabase();
    populateTablesWithNewData();
    }}>Delete All Data</button>
      </div>

    </div>
      
      
    
      <div className="min-h-screen flex flex-col justify-between">
    <footer style={{ position: 'fixed', bottom: 0, width: '100%', textAlign: 'center' }}>
    {showInvalidNumberAlert && (
      <div role="alert" className="alert alert-error mt-2">
        <svg xmlns="http://www.w3.org/2000/svg" className="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
        <span>Please enter a valid input</span>
      </div>
    )}
  </footer>
  </div>
  </div>
  
  );
};


export default App;