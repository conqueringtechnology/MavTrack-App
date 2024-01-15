/* eslint-disable */
import axios from 'axios';

const API_URL = 'https://mavtrack.pythonanywhere.com';
// const API_URL = 'http://127.0.0.1:8000';

export class APIService {
    constructor() {
    }

    // Login User
    authenticateLogin(credentials) {
        const url = `${API_URL}/auth/`;
        return axios.post(url, credentials);
    }

    // Register User
    registerUser(credentials) {
        const url = `${API_URL}/register/`;
        credentials.customusername = credentials.username
        return axios.post(url, credentials);
    }

    // Get Fun facts
    getFunFactList() {
        return axios.get(`${API_URL}/fun-facts/`);
    }

    // Get Daily Hints
    getDailyHintList() {
        return axios.get(`${API_URL}/daily-hints/`);
    }

    // Get Daily Hints
    getPromptsEncouragementList() {
        return axios.get(`${API_URL}/prompts-encouragement/`);
    }

    // Get Recommended Exercises
    getRecommendedExerciseList() {
        return axios.get(`${API_URL}/recommended-exercises/`);
    }

    // Get Categories
    getTrainingCategoryList() {
        const url = `${API_URL}/training-categories/`;
        const token = localStorage.getItem('token');
        const config = {
            headers: {
                Authorization: `JWT ${token}`,
            },
        };
        return axios.get(url, config);
    }

    // Get Goals
    getTrainingGoalList() {
        const url = `${API_URL}/training-goals/`;
        const token = localStorage.getItem('token');
        const config = {
            headers: {
                Authorization: `JWT ${token}`,
            },
        };
        return axios.get(url, config);
    }

    // Get level
    getTrainingLevelList() {
        const url = `${API_URL}/training-levels/`;
        const token = localStorage.getItem('token');
        const config = {
            headers: {
                Authorization: `JWT ${token}`,
            },
        };
        return axios.get(url, config);
    }

    // Create Training Preferences
    createTrainingPreference(preferences) {
        const url = `${API_URL}/training-preferences-create/`;
        const token = localStorage.getItem('token');
        const config = {
            headers: {
                Authorization: `JWT ${token}`,
            },
        };
        console.log("Output Preference", preferences)
        return axios.post(url, preferences, config)
    }

    // Get Training Preferences List with user
    getTrainingPreferenceList(userId) {
        const url = `${API_URL}/training-preferences/?user=${userId}`;
        let jwtToken = localStorage.getItem('token');
        const headers = {Authorization: `jwt ${jwtToken}`};
        return axios.get(url, {headers: headers});
    }

    // Delete Training Preferences
    deletePlan(preference_Pk) {
        const url = `${API_URL}/training-preferences/${preference_Pk}`;
        let jwtToken = localStorage.getItem('token');
        const headers = {Authorization: `jwt ${jwtToken}`};
        return axios.delete(url, {headers: headers});
    }

    // Create Training Schedule
    createTrainingSchedule(schedules) {
        const url = `${API_URL}/training-schedules/`;
        const token = localStorage.getItem('token');
        const config = {
            headers: {
                Authorization: `JWT ${token}`,
            },
        };
        console.log("Output Schedule", schedules)
        return axios.post(url, schedules, config);
    }

    // Get Training Schedule with User
    getTrainingScheduleUser(userId) {
        const url = `${API_URL}/training-schedules/?user=${userId}`;
        let jwtToken = localStorage.getItem('token');
        const headers = {Authorization: `jwt ${jwtToken}`};
        return axios.get(url, {headers: headers});
    }

    // Update training Schedule
    updateTrainingSchedule(scheduleId, updatedSchedule) {
        const url = `${API_URL}/training-schedules/${scheduleId}/update/`;
        const token = localStorage.getItem('token');
        const config = {
            headers: {
                Authorization: `JWT ${token}`,
            },
        };
        console.log('Updated Schedule', updatedSchedule);
        return axios.put(url, updatedSchedule, config);
    }

    // Forgot Password
    forgotPassword(email) {
        const url = `${API_URL}/forgot-password/`;
        const data = {email};
        return axios.post(url, data).then((response) => response.data);
    }


    // Reset Password
    resetPassword(uidb64, token, newPassword) {
        const url = `${API_URL}/reset-password/${uidb64}/${token}/`;
        const data = {
            uid: uidb64,
            token: token,
            new_password: newPassword,
        };
        return axios.post(url, data);
    }

    // Customers
    getCustomer(param_pk) {
        const url = `${API_URL}/api/customers/${param_pk}`;
        let jwtToken = localStorage.getItem('token');
        console.log(":::jwtToken:::::" + jwtToken);
        const headers = {Authorization: `jwt ${jwtToken}`};
        return axios.get(url, {headers: {Authorization: `jwt ${jwtToken}`}});
    }

    getCustomerList() {
        const url = `${API_URL}/api/customers/`;
        let jwtToken = localStorage.getItem('token');
        console.log(":::jwtToken:::::" + jwtToken);
        const headers = {Authorization: `jwt ${jwtToken}`};
        return axios.get(url, {headers: headers});
    }

    deleteCustomer(customer_Pk) {
        const url = `${API_URL}/api/customers/${customer_Pk}`;
        let jwtToken = localStorage.getItem('token');
        const headers = {Authorization: `jwt ${jwtToken}`};
        return axios.delete(url, {headers: headers});
    }
}

