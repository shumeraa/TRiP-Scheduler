"use client"; 

import React, { useState } from 'react';
import axios from 'axios';

const FileUpload = () => {
  const [fileContainer, setFileContainer] = useState([]);
  const [separateExcelFiles, setSeparateExcelFiles] = useState([]);

  const handleFileContainerChange = (e) => {
    console.log('File container selected:', e.target.files);
    setFileContainer(Array.from(e.target.files));
  };

  const handleSeparateExcelFilesChange = (e) => {
    console.log('Separate Excel files selected:', e.target.files);
    setSeparateExcelFiles(Array.from(e.target.files));
  };

  const handleUpload = async () => {
    if (fileContainer.length === 0 && separateExcelFiles.length === 0) {
      console.error('Files not selected');
      return;
    }

    const formData = new FormData();
    fileContainer.forEach((file, index) => {
      formData.append(`fileContainer_${index}`, file);
    });
    separateExcelFiles.forEach((file, index) => {
      formData.append(`separateExcelFile_${index}`, file);
    });

    // Debugging: Log the form data entries
    for (let pair of formData.entries()) {
      console.log(`${pair[0]}: ${pair[1].name}`);
    }

    try {
      const response = await axios.post('http://localhost:5000/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      console.log('Upload successful', response.data);
    } catch (error) {
      console.error('Error uploading files', error);
    }
  };

  return (
    <div>
        <h2 style={{ fontSize: '2rem', marginBottom: '40px' }}>Upload Files</h2>
      <input type="file" webkitdirectory="" directory="" accept=".xlsx" multiple onChange={handleFileContainerChange} style={{ marginRight: '20px' }}/>
      <input type="file" accept=".xlsx,.xls" multiple onChange={handleSeparateExcelFilesChange} />
      <div style={{ marginTop: '40px' }}>
        <button className="btn btn-wide btn-primary" onClick={handleUpload}>Upload</button>
      </div>
    </div>
  );
};

export default FileUpload;
