<template>
  <div class="container mt-5">
    <div class="card mx-auto" style="max-width: 500px;">
      <div class="card-header bg-danger text-white">
        <h1 class="mb-0">Reset Password</h1>
      </div>
      <div class="card-body">
        <div v-if="success" class="alert alert-success">
          Your password has been reset successfully.
        </div>
        <div v-else>
          <form @submit.prevent="resetPassword">
            <div class="form-group">
              <label for="new_password">New Password</label>
              <input type="password" class="form-control" id="new_password" v-model="newPassword" required>
            </div>
            <div class="form-group">
              <label for="confirm_password">Confirm Password</label>
              <input type="password" class="form-control" id="confirm_password" v-model="confirmPassword" required>
            </div>
            <button type="submit" class="btn btn-danger">Reset Password</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {APIService} from '@/http/APIService';

const apiService = new APIService();

export default {
  data() {
    return {
      newPassword: '',
      confirmPassword: '',
      success: false,
      error: '',
    }
  },
  methods: {
    resetPassword() {
      const uidb64 = this.$route.params.uidb64;
      const token = this.$route.params.token;
      const newPassword = this.newPassword;
      const confirmPassword = this.confirmPassword;
      if (newPassword !== confirmPassword) {
        alert('Passwords do not match.');
        return;
      }
      try {
        const response = apiService.resetPassword(uidb64, token, newPassword);
        // Handle successful response
        console.log(response);
        this.success = true;
      } catch (error) {
        // Handle error
        console.error(error);
      }
    }
  }
}
</script>