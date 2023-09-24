import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/'; // replace with your Django backend URL

export const fetchAdmins = async () => {
    console.log("Fetch admins called")
    const response = await axios.get(`${API_URL}admins`);
    return response.data;
};

// Add other API calls (getLearners, getCourses, etc.) here
