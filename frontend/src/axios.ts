// src/axios.ts
import axios from 'axios';

const axiosInstance = axios.create({
  baseURL: '/api/', // Use the relative base URL since the proxy is set up
  headers: {
    'Content-Type': 'application/json',
  },
});

export default axiosInstance;
