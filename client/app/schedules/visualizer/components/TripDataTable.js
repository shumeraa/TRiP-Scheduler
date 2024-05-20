import React from 'react';
import { DataTable } from 'primereact/datatable';
import { Column } from 'primereact/column';

const TripDataTable = ({ tripData, filters, tripheader, tripfooter }) => {
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
          header={tripheader}
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
