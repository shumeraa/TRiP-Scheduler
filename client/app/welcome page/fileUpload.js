// FileUpload.js
"use client";

import React, { useState } from "react";
import axios from "axios";
import Link from "next/link";

const FileUpload = () => {
  const [guideFile, setGuideFile] = useState(null);
  const [tripPrefFiles, setTripPrefFiles] = useState([]);
  const [uploaded, setUploaded] = useState(false);

  const handleFileChange = (event, fileType) => {
    const uploadedFiles = event.target.files;
    if (fileType === "guide") {
      setGuideFile(uploadedFiles[0]);
    } else if (fileType === "tripPref") {
      setTripPrefFiles(Array.from(uploadedFiles));
    }
  };

  const handleUpload = async () => {
    try {
      const formData = new FormData();
      formData.append("guide_file", guideFile);
      tripPrefFiles.forEach((file, index) => {
        formData.append(`trip_pref_file_[${index}]`, file);
      });
      const response = await axios.post("http://localhost:5000/upload", formData);
      console.log(response.data);
      setUploaded(true);
    } catch (error) {
      console.error("Error uploading files:", error);
    }
  };

  return (
    <div className="flex flex-col items-center mt-20">
      <h1 className="mb-10 text-4xl font-bold">Upload Files Here!</h1>
      <div className="mb-5">
        <label className="flex flex-col items-center">
          <span className="font-bold mb-2">Trip Preferences</span>
          <input
            type="file"
            className="file-input file-input-bordered"
            accept=".xlsx"
            onChange={(e) => handleFileChange(e, "tripPref")}
            multiple
          />
        </label>
        <button
          className="btn btn-outline btn-default mt-4"
          onClick={handleUpload}
        >
          Upload Files
        </button>
        {uploaded && <p className="text-green-500 mt-2">Files uploaded successfully!</p>}
      </div>
      <div className="mb-5">
        <label className="flex flex-col items-center">
          <span className="font-bold mb-2">Lead/Assistant Guide Status</span>
          <input
            type="file"
            className="file-input file-input-bordered"
            accept=".xlsx"
            onChange={(e) => handleFileChange(e, "guide")}
          />
        </label>
        <button
          className="btn btn-outline btn-default mt-4"
          onClick={handleUpload}
        >
          Upload File
        </button>
        {uploaded && <p className="text-green-500 mt-2">File uploaded successfully!</p>}
      </div>
    </div>
  );
};

export default FileUpload;
