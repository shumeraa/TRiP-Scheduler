import React, { useState } from 'react';
import { DataTable } from 'primereact/datatable';
import { Column } from 'primereact/column';
import { InputText } from 'primereact/inputtext';
import { FilterMatchMode } from 'primereact/api';

const TripLeaderDataTable = ({ tripLeaderData}) => {

const leadheader = <h1 className="mb-5 text-3xl text-center font-bold">Trip Leader Data</h1>;
const leadfooter = <p className='ml-1'>Total Leaders: {tripLeaderData ? tripLeaderData.length : 0}</p>;

const [filters, setFilters] = useState({
    global: { value: null, matchMode: FilterMatchMode.CONTAINS },
  });

const header = (
    <div style={{ display: 'flex', flexDirection: 'column' }}>
        {leadheader}
        <div style={{ display: 'flex', alignItems: 'center', marginTop: '10px' }}>
        <h1 className='text-xs font-bold mb-1 mr-2'>Filter: </h1>
        <InputText 
            className="ml-1 input input-bordered input-secondary input-sm max-w-xs"
            onInput={(e) => 
            setFilters({
                global: { value: e.target.value, matchMode: FilterMatchMode.CONTAINS },
            })
            }
        />
        </div>
    </div>
    );

  return (
    <div className='mt-5 App'>
      <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
        <DataTable 
          value={tripLeaderData} 
          sortMode="multiple" 
          filters={filters}
          paginator
          rows={10}
          rowsPerPageOptions={[10, 20, 30]}
          className="table table-sm"
          header={header}
          footer={leadfooter}
          style={{ width: '80%' }} 
        >
          <Column field="id" header="ID" sortable></Column>
          <Column field="name" header="Name" sortable></Column>
          <Column field="class_year" header="Class Year" sortable></Column>
          <Column field="semesters_left" header="Semesters Left" sortable></Column>
          <Column field="num_trips_assigned" header="Num Trips Assigned" sortable></Column>
          <Column field="preferred_co_leaders" header="Preferred Co-Leaders" sortable></Column>
          <Column field="reliability_score" header="Reliability Score" sortable></Column>
          <Column field="mountain_biking_role" header="Mountain Biking Roll" sortable></Column>
          <Column field="overnight_role" header="Overnight Role" sortable></Column>
          <Column field="sea_kayaking_role" header="Sea Kayaking Role" sortable></Column>
          <Column field="spelunking_Role" header="Spelunking Role" sortable></Column>
          <Column field="surfing_role" header="Surfing Role" sortable></Column>
          <Column field="watersports_role" header="Watersports Role" sortable></Column>
        </DataTable>
      </div>
    </div>
  );
};

export default TripLeaderDataTable;
