import React, { useState } from 'react';
import { DataTable } from 'primereact/datatable';
import { Column } from 'primereact/column';
import { InputText } from 'primereact/inputtext';
import { FilterMatchMode } from 'primereact/api';

const TripPreferenceDataTable = ({ tripPreferenceData}) => {

  const prefheader = <h1 className="mb-5 text-3xl text-center font-bold">Trip Preference Data</h1>;
  const preffooter = <p className='ml-1'>Total Preferences: {tripPreferenceData ? tripPreferenceData.length : 0}</p>;

  const [filters, setFilters] = useState({
    global: { value: null, matchMode: FilterMatchMode.CONTAINS },
  });

  const header = (
    <div style={{ display: 'flex', flexDirection: 'column' }}>
        <div style={{ borderBottom: '2px solid black', marginBottom: '10px' }}>
            {prefheader}
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
    <div className='mt-5 App pb-12'>
      <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
        <DataTable 
          value={tripPreferenceData} 
          sortMode="multiple" 
          filters={filters}
          paginator
          rows={10}
          rowsPerPageOptions={[10, 20, 30]}
          className="table table-sm"
          header={header}
          footer={preffooter}
          style={{ width: '80%' }} 
        >
          <Column field="trip_leader_id" header="Trip Leader ID" sortable></Column>
          <Column field="trip_leader_name" header="Name" sortable></Column>
          <Column field="trip_id" header="Trip ID" sortable></Column>
          <Column field="trip_name" header="Name" sortable></Column>
          <Column field="preference" header="Preference" sortable></Column>
        </DataTable>
      </div>
    </div>
  );
};

export default TripPreferenceDataTable;
