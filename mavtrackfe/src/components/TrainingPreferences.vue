<template>
  <div>
    <!--Page Title-->
    <div class="container-fluid mt-3 title">
      <div class="row">
        <div class="col">
          <h2 style="color: rgba(230, 43, 70, 1);">Customize Your Training Plan</h2>
        </div>
      </div>
    </div>

    <!--Name Training Plan-->
    <div class="container py-5">
      <div class="row">
        <div class="col-md-7 mb-5 mx-auto text-center">
          <h3 class="mb-4">Name Your Training Plan</h3>
          <input type="text" v-model="name" placeholder="Name Your Training Plan"
                 style="border-color: rgb(230, 43, 70)">
        </div>

        <!--List to select categories-->
        <div class="col-md-6 mx-auto text-center">
          <h4 class="mb-4">Choose Your Fitness Training Category</h4>
          <ul class="list-group">
            <li v-for="category in categories" :key="category.id" :value="category.id" class="list-group-item"
                style=" border: none;">
              <button class="btn btn-outline-danger btn-block" @click="selectCategory(category)">
                {{ category.name }}
              </button>
            </li>
          </ul>
        </div>

        <!--List to select goals-->
        <div class="col-md-6" v-if="selectedCategory">
          <h4 class="mb-4">Choose Your Fitness Training Goal</h4>
          <ul class="list-group">
            <li v-for="goal in goals.filter(g => g.train_cat.some(c => c.name === this.selectedCategory.name))"
                :key="goal.id"
                :value="goal.id"
                class="list-group-item"
                style=" border: none;">
              <button class="btn btn-outline-danger btn-block" @click="selectGoal(goal)">
                {{ goal.short_descr }}
              </button>
            </li>
          </ul>
        </div>

        <!--List to select levels-->
        <div class="col-md-6" v-if="selectedGoal">
          <h4 class="mb-4">Choose Your Training Level</h4>
          <ul class="list-group">
            <li v-for="level in levels" :key="level.id" :value="level.id" class="list-group-item"
                style=" border: none;">
              <button class="btn btn-outline-danger btn-block" @click="selectLevel(level)">
                {{ level.name }}
              </button>
            </li>
          </ul>
        </div>

        <!--List to select days-->
        <div class="col-md-6" v-if="selectedLevel">
          <h4 class="mb-4">Choose Your Fitness Training Days</h4>
          <div class="row">
            <div class="col-6 col-md-4 mt-2">
              <label class="btn btn-outline-danger btn-block">
                <input type="checkbox" v-model="days.sunday" class="d-none"/> Sunday
              </label>
            </div>
            <div class="col-6 col-md-4 mt-2">
              <label class="btn btn-outline-danger btn-block">
                <input type="checkbox" v-model="days.monday" class="d-none"/> Monday
              </label>
            </div>
            <div class="col-6 col-md-4 mt-2">
              <label class="btn btn-outline-danger btn-block">
                <input type="checkbox" v-model="days.tuesday" class="d-none"/> Tuesday
              </label>
            </div>
            <div class="col-6 col-md-4 mt-2">
              <label class="btn btn-outline-danger btn-block">
                <input type="checkbox" v-model="days.wednesday" class="d-none"/> Wednesday
              </label>
            </div>
            <div class="col-6 col-md-4 mt-2">
              <label class="btn btn-outline-danger btn-block">
                <input type="checkbox" v-model="days.thursday" class="d-none"/> Thursday
              </label>
            </div>
            <div class="col-6 col-md-4 mt-2">
              <label class="btn btn-outline-danger btn-block">
                <input type="checkbox" v-model="days.friday" class="d-none"/> Friday
              </label>
            </div>
            <div class="col-6 col-md-4 mt-2">
              <label class="btn btn-outline-danger btn-block">
                <input type="checkbox" v-model="days.saturday" class="d-none"/> Saturday
              </label>
            </div>
          </div>
        </div>
      </div>

      <!--User Error Message-->
      <div class="container mt-3">
        <div class="card">
          <div class="card-body">
            <h3 v-if="errorMessage" class="text-danger">{{ errorMessage }}</h3>
          </div>
        </div>
      </div>

      <!--User Selected Preferences-->
      <div v-if="selectedLevel" class="container mt-3">
        <h2 class="text-danger">You have selected:</h2>
        <div class="card">
          <div class="card-body">
            <p class="card-text">Category: <strong>{{ selectedCategory.name }}</strong></p>
            <p class="card-text">Goal: <strong>{{ selectedGoal.short_descr }}</strong></p>
            <p class="card-text">Level: <strong>{{ selectedLevel.name }}</strong></p>
            <p class="card-text">Your training days are: <strong>{{ selectedDays.join(', ') }}</strong></p>
          </div>
        </div>
      </div>
    </div>

    <!--Cancel and Create schedule buttons-->
    <div class="d-flex justify-content-center mt-3">
      <!--Cancel Button-->
      <button class="btn btn-secondary mr-3" @click="cancelPreference">Cancel</button>
      <!--Create Schedule Button-->
      <button class="btn btn-danger" @click="savePreference">View Schedule</button>
    </div>
  </div>
</template>
<script>
import {APIService} from '@/http/APIService';
import router from '@/router';

const apiService = new APIService();

export default {
  data() {
    return {
      name: '',
      days: {
        monday: false,
        tuesday: false,
        wednesday: false,
        thursday: false,
        friday: false,
        saturday: false,
        sunday: false,
      },
      sundayWorkout: '',
      mondayWorkout: '',
      tuesdayWorkout: '',
      wednesdayWorkout: '',
      thursdayWorkout: '',
      fridayWorkout: '',
      saturdayWorkout: '',
      sundayPace: '',
      mondayPace: '',
      tuesdayPace: '',
      wednesdayPace: '',
      thursdayPace: '',
      fridayPace: '',
      saturdayPace: '',
      sundayDistance: '',
      mondayDistance: '',
      tuesdayDistance: '',
      wednesdayDistance: '',
      thursdayDistance: '',
      fridayDistance: '',
      saturdayDistance: '',
      categories: [],
      goals: [],
      levels: [],
      trainingPreferences: [],
      selectedCategory: null,
      selectedGoal: null,
      selectedLevel: null,
      selectedPreference: [],
      errorMessage: '',
    };
  },
  mounted() {
    this.getCustomers();
  },
  methods: {
    // Get User
    getCustomers() {
      apiService.getCustomerList().then(response => {
        if (localStorage.getItem("isAuthenticates")
            && JSON.parse(localStorage.getItem("isAuthenticates")) === true) {
          this.validUserName = JSON.parse(localStorage.getItem("log_user"));
        }
      }).catch(error => {
        if (error.response.status === 401) {
          localStorage.removeItem('isAuthenticates');
          localStorage.removeItem('log_user');
          localStorage.removeItem('token');
          router.push("/auth");
        }
      });
    },
    // Load Training Categories
    loadCategories() {
      apiService.getTrainingCategoryList()
          .then((response) => {
            this.categories = response.data;
            console.log('Categories', this.categories);
          })
          .catch((error) => {
            console.log('Error Load Categories', error);
          });
    },
    // Load Training Goals
    loadGoals() {
      apiService.getTrainingGoalList()
          .then((response) => {
            this.goals = response.data;
            console.log('Goals', this.goals);
          })
          .catch((error) => {
            console.log('Error Load Goals', error);
          });
    },
    // Load Training Levels
    loadLevels() {
      apiService.getTrainingLevelList()
          .then((response) => {
            this.levels = response.data;
            console.log('Levels', this.levels);
          })
          .catch((error) => {
            console.log('Error Load Levels', error);
          });
    },
    // Load Training Preferences
    loadTrainingPreferences() {
      apiService.getTrainingPreferenceList()
          .then((response) => {
            this.trainingPreferences.push(response.data);
            console.log('Load Preferences', this.trainingPreferences);
          })
          .catch((error) => {
            console.log('Error Load Preferences', error);
          });
    },
    // User Selected Training Category
    selectCategory(category) {
      this.selectedCategory = category;
      this.selectedGoal = '';
    },
    // User Selected Training Goal
    selectGoal(goal) {
      this.selectedGoal = goal;
      this.selectedLevel = '';
    },
    // User Selected Training Level
    selectLevel(level) {
      this.selectedLevel = level;
    },

    // Validate Training Preference Form
    validateForm() {
      let message = '';

      // Form Error Messages
      if (!this.name) {
        message = 'Please enter a name';
      } else if (!this.selectedCategory) {
        message = 'Please select a category';
      } else if (!this.selectedGoal) {
        message = 'Please select a goal';
      } else if (!this.selectedLevel) {
        message = 'Please select a level';
      } else if (this.selectedDays.length === 0) {
        message = 'Please select a least one day';
      }

      // Display the message to the user
      if (message) {
        this.errorMessage = message;
        return false;
      }
      return true;
    },

    // Save Preferences To Database
    savePreference() {
      // Validate that all preferences are valid
      if (this.validateForm()) {
        const preferenceData = {
          name: this.name,
          train_cat: this.selectedCategory.id,
          train_goal: this.selectedGoal.id,
          monday: this.days.monday,
          tuesday: this.days.tuesday,
          wednesday: this.days.wednesday,
          thursday: this.days.thursday,
          friday: this.days.friday,
          saturday: this.days.saturday,
          sunday: this.days.sunday,
          current_train_level: this.selectedLevel.id,
        };
        apiService.createTrainingPreference(preferenceData)
            .then((response) => {
              console.log('Create Preferences', response.data);
              // Update Training Preference
              this.trainingPreferences.push(response.data);
              // Save The Training Preference ID
              this.selectedPreference.push(this.trainingPreferences[this.trainingPreferences.length - 1].id)
              console.log('Selected Pref', this.selectedPreference)

              this.createDailyTask()
            })
            .catch((error) => {
              console.log('Error Create Pref', error);
            });
      }
    },
    // Create Training Schedule Logic
    createDailyTask() {
      // Running - 10K - Beginner
      if (this.selectedCategory.name === 'Running' && this.selectedGoal.short_descr === '10K' &&
          this.selectedLevel.name === 'Beginner') {
        this.selectedDays.forEach(day => {
          switch (day) {
            case 'Sunday':
              this.sundayWorkout = "Workout: Brisk walk and jog for"
              this.sundayPace = "00:25:00"
              this.sundayDistance = 1.5
              break
            case 'Monday':
              this.mondayWorkout = "Workout: Brisk walk and jog for"
              this.mondayPace = "00:25:00"
              this.mondayDistance = 1.5
              break
            case 'Tuesday':
              this.tuesdayWorkout = "Workout: Brisk walk and jog for"
              this.tuesdayPace = "00:25:30"
              this.tuesdayDistance = 1.75
              break
            case 'Wednesday':
              this.wednesdayWorkout = "Workout: Brisk walk and jog for"
              this.wednesdayPace = "00:25:30"
              this.wednesdayDistance = 1.75
              break
            case 'Thursday':
              this.thursdayWorkout = "Workout: Brisk walk and jog for"
              this.thursdayPace = "00:26:00"
              this.thursdayDistance = 2
              break
            case 'Friday':
              this.fridayWorkout = "Workout: Brisk walk and jog for"
              this.fridayPace = "00:26:00"
              this.fridayDistance = 2
              break
            case 'Saturday':
              this.saturdayWorkout = "Workout: Brisk walk and jog for"
              this.saturdayPace = "00:26:00"
              this.saturdayDistance = 2
              break
          }
        })
      } else if (this.selectedCategory.name === 'Running' && this.selectedGoal.short_descr === 'Half Marathon' &&
          this.selectedLevel.name === 'Beginner') {
        this.selectedDays.forEach(day => {
          switch (day) {
            case 'Sunday':
              this.sundayWorkout = "Workout: Brisk walk and jog for"
              this.sundayPace = "00:26:00"
              this.sundayDistance = 2
              break
            case 'Monday':
              this.mondayWorkout = "Workout: Brisk walk and jog for"
              this.mondayPace = "00:26:00"
              this.mondayDistance = 2
              break
            case 'Tuesday':
              this.tuesdayWorkout = "Workout: Brisk walk and jog for"
              this.tuesdayPace = "00:26:30"
              this.tuesdayDistance = 2.25
              break
            case 'Wednesday':
              this.wednesdayWorkout = "Workout: Brisk walk and jog for"
              this.wednesdayPace = "00:26:30"
              this.wednesdayDistance = 2.25
              break
            case 'Thursday':
              this.thursdayWorkout = "Workout: Brisk walk and jog for"
              this.thursdayPace = "00:27:00"
              this.thursdayDistance = 2.5
              break
            case 'Friday':
              this.fridayWorkout = "Workout: Brisk walk and jog for"
              this.fridayPace = "00:27:00"
              this.fridayDistance = 2.5
              break
            case 'Saturday':
              this.saturdayWorkout = "Workout: Brisk walk and jog for"
              this.saturdayPace = "00:27:00"
              this.saturdayDistance = 2.5
              break
          }
        })
      } else if (this.selectedCategory.name === 'Running' && this.selectedGoal.short_descr === 'Marathon' &&
          this.selectedLevel.name === 'Beginner') {
        this.selectedDays.forEach(day => {
          switch (day) {
            case 'Sunday':
              this.sundayWorkout = "Workout: Brisk walk and jog for"
              this.sundayPace = "00:27:00"
              this.sundayDistance = 2
              break
            case 'Monday':
              this.mondayWorkout = "Workout: Brisk walk and jog for"
              this.mondayPace = "00:27:00"
              this.mondayDistance = 2
              break
            case 'Tuesday':
              this.tuesdayWorkout = "Workout: Brisk walk and jog for"
              this.tuesdayPace = "00:27:30"
              this.tuesdayDistance = 2.5
              break
            case 'Wednesday':
              this.wednesdayWorkout = "Workout: Brisk walk and jog for"
              this.wednesdayPace = "00:27:30"
              this.wednesdayDistance = 2.5
              break
            case 'Thursday':
              this.thursdayWorkout = "Workout: Brisk walk and jog for"
              this.thursdayPace = "00:28:00"
              this.thursdayDistance = 2.75
              break
            case 'Friday':
              this.fridayWorkout = "Workout: Brisk walk and jog for"
              this.fridayPace = "00:28:00"
              this.fridayDistance = 2.75
              break
            case 'Saturday':
              this.saturdayWorkout = "Workout: Brisk walk and jog for"
              this.saturdayPace = "00:28:00"
              this.saturdayDistance = 2.75
              break
          }
        })
      }
      // Running - 10K - Intermediate
      else if (this.selectedCategory.name === 'Running' && this.selectedGoal.short_descr === '10K' &&
          this.selectedLevel.name === 'Intermediate') {
        this.selectedDays.forEach(day => {
          switch (day) {
            case 'Sunday':
              this.sundayWorkout = "Workout: Brisk walk and run for"
              this.sundayPace = "00:28:00"
              this.sundayDistance = 2.5
              break
            case 'Monday':
              this.mondayWorkout = "Workout: Brisk walk and run for"
              this.mondayPace = "00:28:00"
              this.mondayDistance = 2.5
              break
            case 'Tuesday':
              this.tuesdayWorkout = "Workout: Brisk walk and run for"
              this.tuesdayPace = "00:28:30"
              this.tuesdayDistance = 3
              break
            case 'Wednesday':
              this.wednesdayWorkout = "Workout: Brisk walk and run for"
              this.wednesdayPace = "00:28:30"
              this.wednesdayDistance = 3
              break
            case 'Thursday':
              this.thursdayWorkout = "Workout: Brisk walk and run for"
              this.thursdayPace = "00:29:00"
              this.thursdayDistance = 3.25
              break
            case 'Friday':
              this.fridayWorkout = "Workout: Brisk walk and run for"
              this.fridayPace = "00:29:00"
              this.fridayDistance = 3.25
              break
            case 'Saturday':
              this.saturdayWorkout = "Workout: Brisk walk and run for"
              this.saturdayPace = "00:29:00"
              this.saturdayDistance = 3.25
              break
          }
        })
      } else if (this.selectedCategory.name === 'Running' && this.selectedGoal.short_descr === 'Half Marathon' &&
          this.selectedLevel.name === 'Intermediate') {
        this.selectedDays.forEach(day => {
          switch (day) {
            case 'Sunday':
              this.sundayWorkout = "Workout: Brisk walk and run for"
              this.sundayPace = "00:29:00"
              this.sundayDistance = 3
              break
            case 'Monday':
              this.mondayWorkout = "Workout: Brisk walk and run for"
              this.mondayPace = "00:29:00"
              this.mondayDistance = 3
              break
            case 'Tuesday':
              this.tuesdayWorkout = "Workout: Brisk walk and run for"
              this.tuesdayPace = "00:29:30"
              this.tuesdayDistance = 3.25
              break
            case 'Wednesday':
              this.wednesdayWorkout = "Workout: Brisk walk and run for"
              this.wednesdayPace = "00:29:30"
              this.wednesdayDistance = 3.25
              break
            case 'Thursday':
              this.thursdayWorkout = "Workout: Brisk walk and run for"
              this.thursdayPace = "00:30:00"
              this.thursdayDistance = 3.5
              break
            case 'Friday':
              this.fridayWorkout = "Workout: Brisk walk and run for"
              this.fridayPace = "00:30:00"
              this.fridayDistance = 3.5
              break
            case 'Saturday':
              this.saturdayWorkout = "Workout: Brisk walk and run for"
              this.saturdayPace = "00:30:00"
              this.saturdayDistance = 3.5
              break
          }
        })
      } else if (this.selectedCategory.name === 'Running' && this.selectedGoal.short_descr === 'Marathon' &&
          this.selectedLevel.name === 'Intermediate') {
        this.selectedDays.forEach(day => {
          switch (day) {
            case 'Sunday':
              this.sundayWorkout = "Workout: Brisk walk and run for"
              this.sundayPace = "00:30:00"
              this.sundayDistance = 3.25
              break
            case 'Monday':
              this.mondayWorkout = "Workout: Brisk walk and run for"
              this.mondayPace = "00:30:00"
              this.mondayDistance = 3.25
              break
            case 'Tuesday':
              this.tuesdayWorkout = "Workout: Brisk walk and run for"
              this.tuesdayPace = "00:30:30"
              this.tuesdayDistance = 3.5
              break
            case 'Wednesday':
              this.wednesdayWorkout = "Workout: Brisk walk and run for"
              this.wednesdayPace = "00:30:30"
              this.wednesdayDistance = 3.5
              break
            case 'Thursday':
              this.thursdayWorkout = "Workout: Brisk walk and run for"
              this.thursdayPace = "00:31:00"
              this.thursdayDistance = 4
              break
            case 'Friday':
              this.fridayWorkout = "Workout: Brisk walk and run for"
              this.fridayPace = "00:31:00"
              this.fridayDistance = 4
              break
            case 'Saturday':
              this.saturdayWorkout = "Workout: Brisk walk and run for"
              this.saturdayPace = "00:31:00"
              this.saturdayDistance = 4
              break
          }
        })
      }
      // Running - 10K - Advanced
      else if (this.selectedCategory.name === 'Running' && this.selectedGoal.short_descr === '10K' &&
          this.selectedLevel.name === 'Advance') {
        this.selectedDays.forEach(day => {
          switch (day) {
            case 'Sunday':
              this.sundayWorkout = "Workout: Jog and run for"
              this.sundayPace = "00:31:00"
              this.sundayDistance = 3.5
              break
            case 'Monday':
              this.mondayWorkout = "Workout: Jog and run for"
              this.mondayPace = "00:31:00"
              this.mondayDistance = 3.5
              break
            case 'Tuesday':
              this.tuesdayWorkout = "Workout: Jog and run for"
              this.tuesdayPace = "00:31:30"
              this.tuesdayDistance = 3.75
              break
            case 'Wednesday':
              this.wednesdayWorkout = "Workout: Jog and run for"
              this.wednesdayPace = "00:31:30"
              this.wednesdayDistance = 3.75
              break
            case 'Thursday':
              this.thursdayWorkout = "Workout: Jog and run for"
              this.thursdayPace = "00:32:00"
              this.thursdayDistance = 4
              break
            case 'Friday':
              this.fridayWorkout = "Workout: Jog and run for"
              this.fridayPace = "00:32:00"
              this.fridayDistance = 4
              break
            case 'Saturday':
              this.saturdayWorkout = "Workout: Jog and run for"
              this.saturdayPace = "00:32:00"
              this.saturdayDistance = 4
              break
          }
        })
      } else if (this.selectedCategory.name === 'Running' && this.selectedGoal.short_descr === 'Half Marathon' &&
          this.selectedLevel.name === 'Advance') {
        this.selectedDays.forEach(day => {
          switch (day) {
            case 'Sunday':
              this.sundayWorkout = "Workout: Jog and run for"
              this.sundayPace = "00:32:00"
              this.sundayDistance = 4
              break
            case 'Monday':
              this.mondayWorkout = "Workout: Jog and run for"
              this.mondayPace = "00:32:00"
              this.mondayDistance = 4
              break
            case 'Tuesday':
              this.tuesdayWorkout = "Workout: Jog and run for"
              this.tuesdayPace = "00:32:30"
              this.tuesdayDistance = 4.25
              break
            case 'Wednesday':
              this.wednesdayWorkout = "Workout: Jog and run for"
              this.wednesdayPace = "00:32:30"
              this.wednesdayDistance = 4.25
              break
            case 'Thursday':
              this.thursdayWorkout = "Workout: Jog and run for"
              this.thursdayPace = "00:33:00"
              this.thursdayDistance = 4.5
              break
            case 'Friday':
              this.fridayWorkout = "Workout: Jog and run for"
              this.fridayPace = "00:33:00"
              this.fridayDistance = 4.5
              break
            case 'Saturday':
              this.saturdayWorkout = "Workout: Jog and run for"
              this.saturdayPace = "00:33:00"
              this.saturdayDistance = 4.5
              break
          }
        })
      } else if (this.selectedCategory.name === 'Running' && this.selectedGoal.short_descr === 'Marathon' &&
          this.selectedLevel.name === 'Advance') {
        this.selectedDays.forEach(day => {
          switch (day) {
            case 'Sunday':
              this.sundayWorkout = "Workout: Jog and run for"
              this.sundayPace = "00:32:00"
              this.sundayDistance = 4.5
              break
            case 'Monday':
              this.mondayWorkout = "Workout: Jog and run for"
              this.mondayPace = "00:32:00"
              this.mondayDistance = 4.5
              break
            case 'Tuesday':
              this.tuesdayWorkout = "Workout: Jog and run for"
              this.tuesdayPace = "00:32:30"
              this.tuesdayDistance = 4.75
              break
            case 'Wednesday':
              this.wednesdayWorkout = "Workout: Jog and run for"
              this.wednesdayPace = "00:32:30"
              this.wednesdayDistance = 4.75
              break
            case 'Thursday':
              this.thursdayWorkout = "Workout: Jog and run for"
              this.thursdayPace = "00:33:00"
              this.thursdayDistance = 5
              break
            case 'Friday':
              this.fridayWorkout = "Workout: Jog and run for"
              this.fridayPace = "00:33:00"
              this.fridayDistance = 5
              break
            case 'Saturday':
              this.saturdayWorkout = "Workout: Jog and run for"
              this.saturdayPace = "00:33:00"
              this.saturdayDistance = 5
              break
          }
        })
      }
      // Cycling - 18.6 Miles - Beginner
      else if (this.selectedCategory.name === 'Cycling' && this.selectedGoal.short_descr === '18.6 Miles' &&
          this.selectedLevel.name === 'Beginner') {
        this.selectedDays.forEach(day => {
          switch (day) {
            case 'Sunday':
              this.sundayWorkout = "Workout: Brisk cycle"
              this.sundayPace = "00:25:00"
              this.sundayDistance = 4.5
              break
            case 'Monday':
              this.mondayWorkout = "Workout: Brisk cycle"
              this.mondayPace = "00:25:00"
              this.mondayDistance = 4.5
              break
            case 'Tuesday':
              this.tuesdayWorkout = "Workout: Brisk cycle"
              this.tuesdayPace = "00:25:30"
              this.tuesdayDistance = 5.25
              break
            case 'Wednesday':
              this.wednesdayWorkout = "Workout: Brisk cycle"
              this.wednesdayPace = "00:25:30"
              this.wednesdayDistance = 5.25
              break
            case 'Thursday':
              this.thursdayWorkout = "Workout: Brisk cycle"
              this.thursdayPace = "00:26:00"
              this.thursdayDistance = 6
              break
            case 'Friday':
              this.fridayWorkout = "Workout: Brisk cycle"
              this.fridayPace = "00:26:00"
              this.fridayDistance = 6
              break
            case 'Saturday':
              this.saturdayWorkout = "Workout: Brisk cycle"
              this.saturdayPace = "00:26:00"
              this.saturdayDistance = 6
              break
          }
        })
      } else if (this.selectedCategory.name === 'Cycling' && this.selectedGoal.short_descr === '39.3 Miles' &&
          this.selectedLevel.name === 'Beginner') {
        this.selectedDays.forEach(day => {
          switch (day) {
            case 'Sunday':
              this.sundayWorkout = "Workout: Brisk cycle"
              this.sundayPace = "00:26:00"
              this.sundayDistance = 6
              break
            case 'Monday':
              this.mondayWorkout = "Workout: Brisk cycle"
              this.mondayPace = "00:26:00"
              this.mondayDistance = 6
              break
            case 'Tuesday':
              this.tuesdayWorkout = "Workout: Brisk cycle"
              this.tuesdayPace = "00:26:30"
              this.tuesdayDistance = 6.75
              break
            case 'Wednesday':
              this.wednesdayWorkout = "Workout: Brisk cycle"
              this.wednesdayPace = "00:26:30"
              this.wednesdayDistance = 6.75
              break
            case 'Thursday':
              this.thursdayWorkout = "Workout: Brisk cycle"
              this.thursdayPace = "00:27:00"
              this.thursdayDistance = 7.5
              break
            case 'Friday':
              this.fridayWorkout = "Workout: Brisk cycle"
              this.fridayPace = "00:27:00"
              this.fridayDistance = 7.5
              break
            case 'Saturday':
              this.saturdayWorkout = "Workout: Brisk cycle"
              this.saturdayPace = "00:27:00"
              this.saturdayDistance = 7.5
              break
          }
        })
      } else if (this.selectedCategory.name === 'Cycling' && this.selectedGoal.short_descr === '78.6 Miles' &&
          this.selectedLevel.name === 'Beginner') {
        this.selectedDays.forEach(day => {
          switch (day) {
            case 'Sunday':
              this.sundayWorkout = "Workout: Brisk cycle"
              this.sundayPace = "00:27:00"
              this.sundayDistance = 7.5
              break
            case 'Monday':
              this.mondayWorkout = "Workout: Brisk cycle"
              this.mondayPace = "00:27:00"
              this.mondayDistance = 7.5
              break
            case 'Tuesday':
              this.tuesdayWorkout = "Workout: Brisk cycle"
              this.tuesdayPace = "00:27:30"
              this.tuesdayDistance = 8.25
              break
            case 'Wednesday':
              this.wednesdayWorkout = "Workout: Brisk cycle"
              this.wednesdayPace = "00:27:30"
              this.wednesdayDistance = 8.25
              break
            case 'Thursday':
              this.thursdayWorkout = "Workout: Brisk cycle"
              this.thursdayPace = "00:28:00"
              this.thursdayDistance = 9
              break
            case 'Friday':
              this.fridayWorkout = "Workout: Brisk cycle"
              this.fridayPace = "00:28:00"
              this.fridayDistance = 9
              break
            case 'Saturday':
              this.saturdayWorkout = "Workout: Brisk cycle"
              this.saturdayPace = "00:28:00"
              this.saturdayDistance = 9
              break
          }
        })
      }
      // Cycling - 18.6 Miles - Intermediate
      else if (this.selectedCategory.name === 'Cycling' && this.selectedGoal.short_descr === '18.6 Miles' &&
          this.selectedLevel.name === 'Intermediate') {
        this.selectedDays.forEach(day => {
          switch (day) {
            case 'Sunday':
              this.sundayWorkout = "Workout: Brisk and moderate cycling"
              this.sundayPace = "00:28:00"
              this.sundayDistance = 9
              break
            case 'Monday':
              this.mondayWorkout = "Workout: Brisk and moderate cycling"
              this.mondayPace = "00:28:00"
              this.mondayDistance = 9
              break
            case 'Tuesday':
              this.tuesdayWorkout = "Workout: Brisk and moderate cycling"
              this.tuesdayPace = "00:28:30"
              this.tuesdayDistance = 10
              break
            case 'Wednesday':
              this.wednesdayWorkout = "Workout: Brisk and moderate cycling"
              this.wednesdayPace = "00:28:30"
              this.wednesdayDistance = 10
              break
            case 'Thursday':
              this.thursdayWorkout = "Workout: Brisk and moderate cycling"
              this.thursdayPace = "00:29:00"
              this.thursdayDistance = 11
              break
            case 'Friday':
              this.fridayWorkout = "Workout: Brisk and moderate cycling"
              this.fridayPace = "00:29:00"
              this.fridayDistance = 11
              break
            case 'Saturday':
              this.saturdayWorkout = "Workout: Brisk and moderate cycling"
              this.saturdayPace = "00:29:00"
              this.saturdayDistance = 11
              break
          }
        })
      } else if (this.selectedCategory.name === 'Cycling' && this.selectedGoal.short_descr === '39.3 Miles' &&
          this.selectedLevel.name === 'Intermediate') {
        this.selectedDays.forEach(day => {
          switch (day) {
            case 'Sunday':
              this.sundayWorkout = "Workout: Brisk and moderate cycling"
              this.sundayPace = "00:29:00"
              this.sundayDistance = 11
              break
            case 'Monday':
              this.mondayWorkout = "Workout: Brisk and moderate cycling"
              this.mondayPace = "00:29:00"
              this.mondayDistance = 11
              break
            case 'Tuesday':
              this.tuesdayWorkout = "Workout: Brisk and moderate cycling"
              this.tuesdayPace = "00:29:30"
              this.tuesdayDistance = 12
              break
            case 'Wednesday':
              this.wednesdayWorkout = "Workout: Brisk and moderate cycling"
              this.wednesdayPace = "00:29:30"
              this.wednesdayDistance = 12
              break
            case 'Thursday':
              this.thursdayWorkout = "Workout: Brisk and moderate cycling"
              this.thursdayPace = "00:30:00"
              this.thursdayDistance = 13
              break
            case 'Friday':
              this.fridayWorkout = "Workout: Brisk and moderate cycling"
              this.fridayPace = "00:30:00"
              this.fridayDistance = 13
              break
            case 'Saturday':
              this.saturdayWorkout = "Workout: Brisk and moderate cycling"
              this.saturdayPace = "00:30:00"
              this.saturdayDistance = 13
              break
          }
        })
      } else if (this.selectedCategory.name === 'Cycling' && this.selectedGoal.short_descr === '78.6 Miles' &&
          this.selectedLevel.name === 'Intermediate') {
        this.selectedDays.forEach(day => {
          switch (day) {
            case 'Sunday':
              this.sundayWorkout = "Workout: Brisk and moderate cycling"
              this.sundayPace = "00:30:00"
              this.sundayDistance = 13
              break
            case 'Monday':
              this.mondayWorkout = "Workout: Brisk and moderate cycling"
              this.mondayPace = "00:30:00"
              this.mondayDistance = 13
              break
            case 'Tuesday':
              this.tuesdayWorkout = "Workout: Brisk and moderate cycling"
              this.tuesdayPace = "00:30:30"
              this.tuesdayDistance = 13.75
              break
            case 'Wednesday':
              this.wednesdayWorkout = "Workout: Brisk and moderate cycling"
              this.wednesdayPace = "00:30:30"
              this.wednesdayDistance = 13.75
              break
            case 'Thursday':
              this.thursdayWorkout = "Workout: Brisk and moderate cycling"
              this.thursdayPace = "00:31:00"
              this.thursdayDistance = 14.5
              break
            case 'Friday':
              this.fridayWorkout = "Workout: Brisk and moderate cycling"
              this.fridayPace = "00:31:00"
              this.fridayDistance = 14.5
              break
            case 'Saturday':
              this.saturdayWorkout = "Workout: Brisk and moderate cycling"
              this.saturdayPace = "00:31:00"
              this.saturdayDistance = 14.5
              break
          }
        })
      }
      // Cycling - 18.6 Miles - Advanced
      else if (this.selectedCategory.name === 'Cycling' && this.selectedGoal.short_descr === '18.6 Miles' &&
          this.selectedLevel.name === 'Advance') {
        this.selectedDays.forEach(day => {
          switch (day) {
            case 'Sunday':
              this.sundayWorkout = "Workout: Brisk, moderate, & fast cycling"
              this.sundayPace = "00:31:00"
              this.sundayDistance = 14.5
              break
            case 'Monday':
              this.mondayWorkout = "Workout: Brisk, moderate, & fast cycling"
              this.mondayPace = "00:31:00"
              this.mondayDistance = 14.5
              break
            case 'Tuesday':
              this.tuesdayWorkout = "Workout: Brisk, moderate, & fast cycling"
              this.tuesdayPace = "00:31:30"
              this.tuesdayDistance = 15.25
              break
            case 'Wednesday':
              this.wednesdayWorkout = "Workout: Brisk, moderate, & fast cycling"
              this.wednesdayPace = "00:31:30"
              this.wednesdayDistance = 15.25
              break
            case 'Thursday':
              this.thursdayWorkout = "Workout: Brisk, moderate, & fast cycling"
              this.thursdayPace = "00:32:00"
              this.thursdayDistance = 16
              break
            case 'Friday':
              this.fridayWorkout = "Workout: Brisk, moderate, & fast cycling"
              this.fridayPace = "00:32:00"
              this.fridayDistance = 16
              break
            case 'Saturday':
              this.saturdayWorkout = "Workout: Brisk, moderate, & fast cycling"
              this.saturdayPace = "00:32:00"
              this.saturdayDistance = 16
              break
          }
        })
      } else if (this.selectedCategory.name === 'Cycling' && this.selectedGoal.short_descr === '39.3 Miles' &&
          this.selectedLevel.name === 'Advance') {
        this.selectedDays.forEach(day => {
          switch (day) {
            case 'Sunday':
              this.sundayWorkout = "Workout: Brisk, moderate, & fast cycling"
              this.sundayPace = "00:32:00"
              this.sundayDistance = 16
              break
            case 'Monday':
              this.mondayWorkout = "Workout: Brisk, moderate, & fast cycling"
              this.mondayPace = "00:32:00"
              this.mondayDistance = 16
              break
            case 'Tuesday':
              this.tuesdayWorkout = "Workout: Brisk, moderate, & fast cycling"
              this.tuesdayPace = "00:32:30"
              this.tuesdayDistance = 16.75
              break
            case 'Wednesday':
              this.wednesdayWorkout = "Workout: Brisk, moderate, & fast cycling"
              this.wednesdayPace = "00:32:30"
              this.wednesdayDistance = 16.75
              break
            case 'Thursday':
              this.thursdayWorkout = "Workout: Brisk, moderate, & fast cycling"
              this.thursdayPace = "00:33:00"
              this.thursdayDistance = 17.5
              break
            case 'Friday':
              this.fridayWorkout = "Workout: Brisk, moderate, & fast cycling"
              this.fridayPace = "00:33:00"
              this.fridayDistance = 17.5
              break
            case 'Saturday':
              this.saturdayWorkout = "Workout: Brisk, moderate, & fast cycling"
              this.saturdayPace = "00:33:00"
              this.saturdayDistance = 17.5
              break
          }
        })
      } else if (this.selectedCategory.name === 'Cycling' && this.selectedGoal.short_descr === '78.6 Miles' &&
          this.selectedLevel.name === 'Advance') {
        this.selectedDays.forEach(day => {
          switch (day) {
            case 'Sunday':
              this.sundayWorkout = "Workout: Brisk, moderate, & fast cycling"
              this.sundayPace = "00:32:00"
              this.sundayDistance = 17.5
              break
            case 'Monday':
              this.mondayWorkout = "Workout: Brisk, moderate, & fast cycling"
              this.mondayPace = "00:32:00"
              this.mondayDistance = 17.5
              break
            case 'Tuesday':
              this.tuesdayWorkout = "Workout: Brisk, moderate, & fast cycling"
              this.tuesdayPace = "00:32:30"
              this.tuesdayDistance = 18.5
              break
            case 'Wednesday':
              this.wednesdayWorkout = "Workout: Brisk, moderate, & fast cycling"
              this.wednesdayPace = "00:32:30"
              this.wednesdayDistance = 18.5
              break
            case 'Thursday':
              this.thursdayWorkout = "Workout: Brisk, moderate, & fast cycling"
              this.thursdayPace = "00:33:00"
              this.thursdayDistance = 19.5
              break
            case 'Friday':
              this.fridayWorkout = "Workout: Brisk, moderate, & fast cycling"
              this.fridayPace = "00:33:00"
              this.fridayDistance = 19.5
              break
            case 'Saturday':
              this.saturdayWorkout = "Workout: Brisk, moderate, & fast cycling"
              this.saturdayPace = "00:33:00"
              this.saturdayDistance = 20
              break
          }
        })
      }
      // Swimming - 100 Meters - Beginner
      else if (this.selectedCategory.name === 'Swimming' && this.selectedGoal.short_descr === '100 Meters' &&
          this.selectedLevel.name === 'Beginner') {
        this.selectedDays.forEach(day => {
          switch (day) {
            case 'Sunday':
              this.sundayWorkout = "Workout: Brisk swim"
              this.sundayPace = "00:10:00"
              this.sundayDistance = null
              break
            case 'Monday':
              this.mondayWorkout = "Workout: Brisk swim"
              this.mondayPace = "00:10:00"
              this.mondayDistance = null
              break
            case 'Tuesday':
              this.tuesdayWorkout = "Workout: Brisk swim"
              this.tuesdayPace = "00:10:30"
              this.tuesdayDistance = null
              break
            case 'Wednesday':
              this.wednesdayWorkout = "Workout: Brisk swim"
              this.wednesdayPace = "00:10:30"
              this.wednesdayDistance = null
              break
            case 'Thursday':
              this.thursdayWorkout = "Workout: Brisk swim"
              this.thursdayPace = "00:11:00"
              this.thursdayDistance = null
              break
            case 'Friday':
              this.fridayWorkout = "Workout: Brisk swim"
              this.fridayPace = "00:11:00"
              this.fridayDistance = null
              break
            case 'Saturday':
              this.saturdayWorkout = "Workout: Brisk swim"
              this.saturdayPace = "00:11:00"
              this.saturdayDistance = null
              break
          }
        })
      } else if (this.selectedCategory.name === 'Swimming' && this.selectedGoal.short_descr === '200 Meters' &&
          this.selectedLevel.name === 'Beginner') {
        this.selectedDays.forEach(day => {
          switch (day) {
            case 'Sunday':
              this.sundayWorkout = "Workout: Brisk swim"
              this.sundayPace = "00:11:00"
              this.sundayDistance = null
              break
            case 'Monday':
              this.mondayWorkout = "Workout: Brisk swim"
              this.mondayPace = "00:11:00"
              this.mondayDistance = null
              break
            case 'Tuesday':
              this.tuesdayWorkout = "Workout: Brisk swim"
              this.tuesdayPace = "00:11:30"
              this.tuesdayDistance = null
              break
            case 'Wednesday':
              this.wednesdayWorkout = "Workout: Brisk swim"
              this.wednesdayPace = "00:11:30"
              this.wednesdayDistance = null
              break
            case 'Thursday':
              this.thursdayWorkout = "Workout: Brisk swim"
              this.thursdayPace = "00:12:00"
              this.thursdayDistance = null
              break
            case 'Friday':
              this.fridayWorkout = "Workout: Brisk swim"
              this.fridayPace = "00:12:00"
              this.fridayDistance = null
              break
            case 'Saturday':
              this.saturdayWorkout = "Workout: Brisk swim"
              this.saturdayPace = "00:12:00"
              this.saturdayDistance = null
              break
          }
        })
      } else if (this.selectedCategory.name === 'Cycling' && this.selectedGoal.short_descr === '400 Meters' &&
          this.selectedLevel.name === 'Beginner') {
        this.selectedDays.forEach(day => {
          switch (day) {
            case 'Sunday':
              this.sundayWorkout = "Workout: Brisk swim"
              this.sundayPace = "00:12:00"
              this.sundayDistance = null
              break
            case 'Monday':
              this.mondayWorkout = "Workout: Brisk swim"
              this.mondayPace = "00:12:00"
              this.mondayDistance = null
              break
            case 'Tuesday':
              this.tuesdayWorkout = "Workout: Brisk swim"
              this.tuesdayPace = "00:12:30"
              this.tuesdayDistance = null
              break
            case 'Wednesday':
              this.wednesdayWorkout = "Workout: Brisk swim"
              this.wednesdayPace = "00:12:30"
              this.wednesdayDistance = null
              break
            case 'Thursday':
              this.thursdayWorkout = "Workout: Brisk swim"
              this.thursdayPace = "00:13:00"
              this.thursdayDistance = null
              break
            case 'Friday':
              this.fridayWorkout = "Workout: Brisk swim"
              this.fridayPace = "00:13:00"
              this.fridayDistance = null
              break
            case 'Saturday':
              this.saturdayWorkout = "Workout: Brisk swim"
              this.saturdayPace = "00:13:00"
              this.saturdayDistance = null
              break
          }
        })
      }
      // Swimming - 100 Meters - Intermediate
      else if (this.selectedCategory.name === 'Swimming' && this.selectedGoal.short_descr === '100 Meters' &&
          this.selectedLevel.name === 'Intermediate') {
        this.selectedDays.forEach(day => {
          switch (day) {
            case 'Sunday':
              this.sundayWorkout = "Workout: Brisk and moderate swimming"
              this.sundayPace = "00:13:00"
              this.sundayDistance = null
              break
            case 'Monday':
              this.mondayWorkout = "Workout: Brisk and moderate swimming"
              this.mondayPace = "00:13:00"
              this.mondayDistance = null
              break
            case 'Tuesday':
              this.tuesdayWorkout = "Workout: Brisk and moderate swimming"
              this.tuesdayPace = "00:14:30"
              this.tuesdayDistance = null
              break
            case 'Wednesday':
              this.wednesdayWorkout = "Workout: Brisk and moderate swimming"
              this.wednesdayPace = "00:14:30"
              this.wednesdayDistance = null
              break
            case 'Thursday':
              this.thursdayWorkout = "Workout: Brisk and moderate swimming"
              this.thursdayPace = "00:14:00"
              this.thursdayDistance = null
              break
            case 'Friday':
              this.fridayWorkout = "Workout: Brisk and moderate swimming"
              this.fridayPace = "00:14:00"
              this.fridayDistance = null
              break
            case 'Saturday':
              this.saturdayWorkout = "Workout: Brisk and moderate swimming"
              this.saturdayPace = "00:14:00"
              this.saturdayDistance = null
              break
          }
        })
      } else if (this.selectedCategory.name === 'Swimming' && this.selectedGoal.short_descr === '200 Meters' &&
          this.selectedLevel.name === 'Intermediate') {
        this.selectedDays.forEach(day => {
          switch (day) {
            case 'Sunday':
              this.sundayWorkout = "Workout: Brisk and moderate swimming"
              this.sundayPace = "00:14:00"
              this.sundayDistance = null
              break
            case 'Monday':
              this.mondayWorkout = "Workout: Brisk and moderate swimming"
              this.mondayPace = "00:14:00"
              this.mondayDistance = null
              break
            case 'Tuesday':
              this.tuesdayWorkout = "Workout: Brisk and moderate swimming"
              this.tuesdayPace = "00:14:30"
              this.tuesdayDistance = null
              break
            case 'Wednesday':
              this.wednesdayWorkout = "Workout: Brisk and moderate swimming"
              this.wednesdayPace = "00:14:30"
              this.wednesdayDistance = null
              break
            case 'Thursday':
              this.thursdayWorkout = "Workout: Brisk and moderate swimming"
              this.thursdayPace = "00:15:00"
              this.thursdayDistance = null
              break
            case 'Friday':
              this.fridayWorkout = "Workout: Brisk and moderate swimming"
              this.fridayPace = "00:15:00"
              this.fridayDistance = null
              break
            case 'Saturday':
              this.saturdayWorkout = "Workout: Brisk and moderate swimming"
              this.saturdayPace = "00:15:00"
              this.saturdayDistance = null
              break
          }
        })
      } else if (this.selectedCategory.name === 'Swimming' && this.selectedGoal.short_descr === '400 Meters' &&
          this.selectedLevel.name === 'Intermediate') {
        this.selectedDays.forEach(day => {
          switch (day) {
            case 'Sunday':
              this.sundayWorkout = "Workout: Brisk and moderate swimming"
              this.sundayPace = "00:15:00"
              this.sundayDistance = null
              break
            case 'Monday':
              this.mondayWorkout = "Workout: Brisk and moderate cycling"
              this.mondayPace = "00:15:00"
              this.mondayDistance = null
              break
            case 'Tuesday':
              this.tuesdayWorkout = "Workout: Brisk and moderate swimming"
              this.tuesdayPace = "00:15:30"
              this.tuesdayDistance = null
              break
            case 'Wednesday':
              this.wednesdayWorkout = "Workout: Brisk and moderate swimming"
              this.wednesdayPace = "00:15:30"
              this.wednesdayDistance = null
              break
            case 'Thursday':
              this.thursdayWorkout = "Workout: Brisk and moderate swimming"
              this.thursdayPace = "00:16:00"
              this.thursdayDistance = null
              break
            case 'Friday':
              this.fridayWorkout = "Workout: Brisk and moderate swimming"
              this.fridayPace = "00:16:00"
              this.fridayDistance = null
              break
            case 'Saturday':
              this.saturdayWorkout = "Workout: Brisk and moderate swimming"
              this.saturdayPace = "00:16:00"
              this.saturdayDistance = null
              break
          }
        })
      }
      // Swimming - 100 Meters - Advanced
      else if (this.selectedCategory.name === 'Swimming' && this.selectedGoal.short_descr === '100 Meters' &&
          this.selectedLevel.name === 'Advance') {
        this.selectedDays.forEach(day => {
          switch (day) {
            case 'Sunday':
              this.sundayWorkout = "Workout: Brisk, moderate, & fast swimming"
              this.sundayPace = "00:16:00"
              this.sundayDistance = null
              break
            case 'Monday':
              this.mondayWorkout = "Workout: Brisk, moderate, & fast swimming"
              this.mondayPace = "00:16:00"
              this.mondayDistance = null
              break
            case 'Tuesday':
              this.tuesdayWorkout = "Workout: Brisk, moderate, & fast swimming"
              this.tuesdayPace = "00:16:30"
              this.tuesdayDistance = null
              break
            case 'Wednesday':
              this.wednesdayWorkout = "Workout: Brisk, moderate, & fast swimming"
              this.wednesdayPace = "00:16:30"
              this.wednesdayDistance = null
              break
            case 'Thursday':
              this.thursdayWorkout = "Workout: Brisk, moderate, & fast swimming"
              this.thursdayPace = "00:17:00"
              this.thursdayDistance = null
              break
            case 'Friday':
              this.fridayWorkout = "Workout: Brisk, moderate, & fast swimming"
              this.fridayPace = "00:17:00"
              this.fridayDistance = null
              break
            case 'Saturday':
              this.saturdayWorkout = "Workout: Brisk, moderate, & fast swimming"
              this.saturdayPace = "00:17:00"
              this.saturdayDistance = null
              break
          }
        })
      } else if (this.selectedCategory.name === 'Swimming' && this.selectedGoal.short_descr === '200 Meters' &&
          this.selectedLevel.name === 'Advance') {
        this.selectedDays.forEach(day => {
          switch (day) {
            case 'Sunday':
              this.sundayWorkout = "Workout: Brisk, moderate, & fast swimming"
              this.sundayPace = "00:17:00"
              this.sundayDistance = null
              break
            case 'Monday':
              this.mondayWorkout = "Workout: Brisk, moderate, & fast swimming"
              this.mondayPace = "00:17:00"
              this.mondayDistance = null
              break
            case 'Tuesday':
              this.tuesdayWorkout = "Workout: Brisk, moderate, & fast swimming"
              this.tuesdayPace = "00:17:30"
              this.tuesdayDistance = null
              break
            case 'Wednesday':
              this.wednesdayWorkout = "Workout: Brisk, moderate, & fast swimming"
              this.wednesdayPace = "00:17:30"
              this.wednesdayDistance = null
              break
            case 'Thursday':
              this.thursdayWorkout = "Workout: Brisk, moderate, & fast swimming"
              this.thursdayPace = "00:18:00"
              this.thursdayDistance = null
              break
            case 'Friday':
              this.fridayWorkout = "Workout: Brisk, moderate, & fast swimming"
              this.fridayPace = "00:18:00"
              this.fridayDistance = null
              break
            case 'Saturday':
              this.saturdayWorkout = "Workout: Brisk, moderate, & fast swimming"
              this.saturdayPace = "00:18:00"
              this.saturdayDistance = null
              break
          }
        })
      } else if (this.selectedCategory.name === 'Swimming' && this.selectedGoal.short_descr === '400 Meters' &&
          this.selectedLevel.name === 'Advance') {
        this.selectedDays.forEach(day => {
          switch (day) {
            case 'Sunday':
              this.sundayWorkout = "Workout: Brisk, moderate, & fast swimming"
              this.sundayPace = "00:18:00"
              this.sundayDistance = null
              break
            case 'Monday':
              this.mondayWorkout = "Workout: Brisk, moderate, & fast swimming"
              this.mondayPace = "00:18:00"
              this.mondayDistance = null
              break
            case 'Tuesday':
              this.tuesdayWorkout = "Workout: Brisk, moderate, & fast swimming"
              this.tuesdayPace = "00:18:30"
              this.tuesdayDistance = null
              break
            case 'Wednesday':
              this.wednesdayWorkout = "Workout: Brisk, moderate, & fast swimming"
              this.wednesdayPace = "00:18:30"
              this.wednesdayDistance = null
              break
            case 'Thursday':
              this.thursdayWorkout = "Workout: Brisk, moderate, & fast swimming"
              this.thursdayPace = "00:19:00"
              this.thursdayDistance = null
              break
            case 'Friday':
              this.fridayWorkout = "Workout: Brisk, moderate, & fast swimming"
              this.fridayPace = "00:19:30"
              this.fridayDistance = null
              break
            case 'Saturday':
              this.saturdayWorkout = "Workout: Brisk, moderate, & fast swimming"
              this.saturdayPace = "00:20:00"
              this.saturdayDistance = null
              break
          }
        })
      }
      this.createSchedule()
    },

    // User Selected Training Task
    createSchedule() {
      // Schedule Data
      const scheduleData = {
        name: this.name,
        sunday_workout: this.sundayWorkout,
        monday_workout: this.mondayWorkout,
        tuesday_workout: this.tuesdayWorkout,
        wednesday_workout: this.wednesdayWorkout,
        thursday_workout: this.thursdayWorkout,
        friday_workout: this.fridayWorkout,
        saturday_workout: this.saturdayWorkout,
        sunday_pace: this.sundayPace,
        monday_pace: this.mondayPace,
        tuesday_pace: this.tuesdayPace,
        wednesday_pace: this.wednesdayPace,
        thursday_pace: this.thursdayPace,
        friday_pace: this.fridayPace,
        saturday_pace: this.saturdayPace,
        sunday_distance: this.sundayDistance,
        monday_distance: this.mondayDistance,
        tuesday_distance: this.tuesdayDistance,
        wednesday_distance: this.wednesdayDistance,
        thursday_distance: this.thursdayDistance,
        friday_distance: this.fridayDistance,
        saturday_distance: this.saturdayDistance,
        train_pref: this.selectedPreference,
        monday: this.days.monday,
        tuesday: this.days.tuesday,
        wednesday: this.days.wednesday,
        thursday: this.days.thursday,
        friday: this.days.friday,
        saturday: this.days.saturday,
        sunday: this.days.sunday,
      };
      apiService.createTrainingSchedule(scheduleData)
          .then((response) => {
            console.log('Create Schedule', response.data);
            router.push("/training-schedules/");
          })
          .catch((error) => {
            console.log('Error Create Schedule', error);
          });
    }
    ,
    cancelPreference() {
      router.push("/training-plans");
    }
  },
  computed: {
    // User Selected Training Days
    selectedDays() {
      const day = [];
      if (this.days.monday) day.push('Monday');
      if (this.days.tuesday) day.push('Tuesday');
      if (this.days.wednesday) day.push('Wednesday');
      if (this.days.thursday) day.push('Thursday');
      if (this.days.friday) day.push('Friday');
      if (this.days.saturday) day.push('Saturday');
      if (this.days.sunday) day.push('Sunday');
      return day;
    },
  },
  created() {
    this.loadCategories();
    this.loadGoals();
    this.loadLevels();
    this.loadTrainingPreferences()
  },
};
</script>

<style scoped>


</style>