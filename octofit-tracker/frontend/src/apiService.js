import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000'; // Update this if the backend runs on a different URL or port

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const getUserProfile = async () => {
  const response = await apiClient.get('/profile/');
  return response.data;
};

export const getActivityLogs = async () => {
  const response = await apiClient.get('/activities/');
  return response.data;
};

export const createActivityLog = async (activityData) => {
  const response = await apiClient.post('/activities/', activityData);
  return response.data;
};

export default apiClient;
