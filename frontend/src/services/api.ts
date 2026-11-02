import axios from 'axios';

const rawBaseUrl = import.meta.env.VITE_API_BASE_URL || '';
const baseURL = rawBaseUrl.endsWith('/api/v1')
  ? rawBaseUrl
  : rawBaseUrl
  ? `${rawBaseUrl.replace(/\/+$/, '')}/api/v1`
  : '/api/v1';

const api = axios.create({
  baseURL,
});

api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response && error.response.status === 401) {
      localStorage.removeItem('token');
      localStorage.removeItem('user');
    }
    return Promise.reject(error);
  }
);

export default api;
