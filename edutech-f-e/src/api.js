import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/'; // replace with your Django backend URL

export const fetchAdmins = async () => {
    const response = await axios.get(`${API_URL}admins`);
    return response.data;
};

export const adminLogin = async (data) => {
    try {
        const response =  await axios.post(`${API_URL}admins/login`, data);
        return response.data;
    }
    catch(err) {
        return err.message;
    }
    
}

// Add other API calls (getLearners, getCourses, etc.) here
