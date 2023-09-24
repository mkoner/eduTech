import axios from 'axios';

const API_URL = 'http://localhost:8000'; // replace with your Django backend URL

export const getAdmins = async () => {
    const response = await axios.get(`${API_URL}/admins`);
    return response.data;
};

// Add other API calls (getLearners, getCourses, etc.) here
