import React from 'react';
import { DataTable } from 'primereact/datatable';
import { Column } from 'primereact/column';

const TripLeaderDataTable = ({ tripLeaderData, filters, leadheader, leadfooter }) => {
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
          header={leadheader}
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
