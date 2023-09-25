import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/'; // replace with your Django backend URL
const token = localStorage.getItem("token") ? localStorage.getItem("token") : null;

export const fetchAdmins = async (filters) => {
    const response = await axios.get(`${API_URL}admins`, {
        headers: {
          'Authorization': `Token ${token}`
        },
        params: filters
      });
    return response.data;
};

export const fetchLearners = async (filters) => {
    const response = await axios.get(`${API_URL}learners`, {
        headers: {
          'Authorization': `Token ${token}`
        },
        params: filters
      });
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

export const learnerLogin = async (data) => {
    try {
        const response =  await axios.post(`${API_URL}learners/login`, data);
        return response.data;
    }
    catch(err) {
        return err.message;
    }   
}

// Add other API calls (getLearners, getCourses, etc.) here
