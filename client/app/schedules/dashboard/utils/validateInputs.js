import { useState } from 'react';

export const useValidation = () => {
  const [showInvalidNumberAlert, setShowInvalidNumberInput] = useState(false);

  const validateNumInput = (setFieldValue) => (e) => {
    const value = e.target.value;
    const semesterValue = parseInt(value, 10);
    
    if (value === '' || (!Number.isNaN(semesterValue) && (semesterValue >= 0 && semesterValue < 20))) {
      setShowInvalidNumberInput(false); // Hide error message if input is valid
    } else {
      setShowInvalidNumberInput(true); // Show error message
      setFieldValue(''); // Resets the input if out of bounds
    }
  };

  const validateYear = (setFieldValue) => (e) => {
    const value = e.target.value;
    const monthValue = parseInt(value, 10);
    
    if (value === '' || (!Number.isNaN(monthValue) && (monthValue >= 2000 && monthValue < 2100))) {
      setShowInvalidNumberInput(false); // Hide error message if input is valid
    } else {
      setShowInvalidNumberInput(true); // Show error message
      setFieldValue(''); // Resets the input if out of bounds
    }
  };

  const validateMonth = (setFieldValue) => (e) => {
    const value = e.target.value;
    const monthValue = parseInt(value, 10);
    
    if (value === '' || (!Number.isNaN(monthValue) && (monthValue >= 0 && monthValue < 13))) {
      setShowInvalidNumberInput(false); // Hide error message if input is valid
    } else {
      setShowInvalidNumberInput(true); // Show error message
      setFieldValue(''); // Resets the input if out of bounds
    }
  };

  const validateDay = (setFieldValue) => (e) => {
    const value = e.target.value;
    const monthValue = parseInt(value, 10);
    
    if (value === '' || (!Number.isNaN(monthValue) && (monthValue >= 0 && monthValue < 32))) {
      setShowInvalidNumberInput(false); // Hide error message if input is valid
    } else {
      setShowInvalidNumberInput(true); // Show error message
      setFieldValue(''); // Resets the input if out of bounds
    }
  };

  const validateTripName = (setFieldValue) => (e) => {
    const value = e.target.value;    
    if (value === '' || value.length < 50 && /^[a-zA-Z ]+$/.test(value)) {
      // 1. The input is an empty string, OR
      // 2. The string is shorter than 50 characters and contains only letters.
      setShowInvalidNumberInput(false); // Hide error message if input is valid
    } else {
      setShowInvalidNumberInput(true); // Show error message
      setFieldValue(''); // Resets the input if out of bounds
    }
  };

  return {
    showInvalidNumberAlert,
    validateNumInput,
    validateYear,
    validateMonth,
    validateDay,
    validateTripName,
  };
};
