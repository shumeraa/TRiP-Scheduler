import React from 'react';
import { DataTable } from 'primereact/datatable';
import { Column } from 'primereact/column';
import { InputText } from 'primereact/inputtext';
import { FilterMatchMode } from 'primereact/api';

const TripPreferenceDataTable = ({ tripPreferenceData, filters, setFilters, prefheader, preffooter }) => {
  return (
    <div className='mt-5 App'>
      <h1 className='text-xs font-bold mb-1 ml-2'>Filter: </h1>
      <InputText 
        className="ml-1 input input-bordered input-secondary input-sm max-w-xs"
        onInput={(e) => 
          setFilters({
            global: { value: e.target.value, matchMode: FilterMatchMode.CONTAINS },
          })
        }
      />
      <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
        <DataTable 
          value={tripPreferenceData} 
          sortMode="multiple" 
          filters={filters}
          paginator
          rows={10}
          rowsPerPageOptions={[10, 20, 30]}
          className="table table-sm"
          header={prefheader}
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
