import axios from 'axios';

export const fetchData = async (setLoading, setTripData, setTripLeaderData, setTripPreferenceData) => {
  try {
    setLoading(true); // Set loading to true at the beginning of the fetch
    const response = await axios.get('http://localhost:5000/get-data');
    const data = response.data;

    // separate data into individual arrays
    const { trip, trip_leader, trip_preference } = data;
    setTripData(trip);
    setTripLeaderData(trip_leader);
    setTripPreferenceData(trip_preference);

    setLoading(false);
  } catch (error) {
    console.error('Error fetching data:', error);
    setLoading(false);
  }
};

export const resetDatabase = () => {
  fetch('http://localhost:5000/reset-database', { // Adjust the URL based on your Flask server address and port
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
  })
  .then(response => response.json())
  .then(data => {
    if (data.success) {
      alert('Database has been reset successfully!');
    } else {
      alert('Failed to reset the database.');
    }
  })
  .catch(error => {
    console.error('Error:', error);
  });
};

export const sendDataToBackend = () => {
  let dataToSend = {};
  const selects = document.querySelectorAll('select');
  selects.forEach(select => {
    // Assuming you want to use the ID as the key
    if (select.id) dataToSend[select.id] = select.value;
  });
  const textInputs = document.querySelectorAll('input[type="text"]');
  textInputs.forEach((input) => {
    // Using placeholder as key; ensure placeholders are unique or consider a different attribute
    if (input.placeholder) dataToSend[input.placeholder] = input.value;
  });
  fetch('http://localhost:5000/api/modifyLeader', { // Update port if your Flask app runs on a different one
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(dataToSend),
  })
  .then(response => response.json())
  .then(data => alert(JSON.stringify(data)))
  .catch(error => console.error('Error:', error));
};
