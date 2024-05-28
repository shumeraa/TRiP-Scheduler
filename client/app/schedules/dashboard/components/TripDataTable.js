import React, { useState } from 'react';
import { DataTable } from 'primereact/datatable';
import { Column } from 'primereact/column';
import { InputText } from 'primereact/inputtext';
import { FilterMatchMode } from 'primereact/api';

const TripDataTable = ({ tripData}) => {

const tripheader = <h1 className="mb-5 text-3xl text-center font-bold">Trip Data</h1>;
const tripfooter = <p className='ml-1'>Total Trips: {tripData ? tripData.length : 0}</p>;

const [filters, setFilters] = useState({
    global: { value: null, matchMode: FilterMatchMode.CONTAINS },
});

const header = (
    <div style={{ display: 'flex', flexDirection: 'column' }}>
        <div style={{ borderBottom: '2px solid black', marginBottom: '10px' }}>
            {tripheader}
        </div>
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
          value={tripData} 
          sortMode="multiple" 
          filters={filters}
          paginator
          rows={10}
          rowsPerPageOptions={[10, 20, 30]}
          className="table table-sm"
          header={header}
          footer={tripfooter}
          style={{ width: '80%' }} 
        >
          <Column field="trip_id" header="Trip ID" sortable></Column>
          <Column field="name" header="Name" sortable></Column>
          <Column field="category" header="Category" sortable></Column>
          <Column field="start_date" header="Start Date"></Column>
          <Column field="end_date" header="End Date"></Column>
          <Column field="lead_guides_needed" header="Lead Guides Needed" sortable></Column>
          <Column field="total_guides_needed" header="Total Guides Needed" sortable></Column>
        </DataTable>
      </div>
    </div>
  );
};

export default TripDataTable;
