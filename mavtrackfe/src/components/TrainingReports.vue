<template>
  <div>
    <head>
      <link href="//maxcdn.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css" rel="stylesheet">
    </head>
  </div>
  <div class="container-fluid">
    <!--Welcome Title -->
    <div class="row align-items-center justify-content-center">
      <div class="col col-12 align-items-center justify-content-center text-danger">
        <blockquote>
          <h2>
            {{ validUserName }}'s Training Reports
          </h2>
        </blockquote>
      </div>

      <!-- Training Overview Report table Small Screen-->
      <div class="row align-items-center justify-content-center">
        <div class="d-md-none" id="collapsable-card" style="width: 80%">
          <div>
            <h4>Training Overview</h4>
          </div>
          <div class="card mb-3">
            <h6 @click="sortList('name')" style="color: rgb(255, 0, 0); float: left"><b>Name</b> <br><i
                class="fa fa-fw fa-sort"></i></h6>
          </div>
          <div class="card" v-for="report in reports" :key="report.id">
            <div class="card-header" style="color: rgb(109,129,133);" :id="'heading' + report.id">
              <button class="btn btn-link collapsed"
                      data-toggle="collapse"
                      :data-target="'#collapse' + report.id"
                      aria-expanded="true"
                      :aria-controls="'collapse' + report.id"
              >

                <h6 style="color: rgb(255, 0, 0); float: left">{{ report.name }}</h6>
              </button>
            </div>
            <div :id="'collapse' + report.id"
                 class="collapse"
                 :aria-labelledby="'heading' + report.id"
                 data-bs-parent="#collapsable-card"
            >
              <div class="card-body bg-light">
                <p><b>Name:</b> {{ report.name }}</p>
                <p><b>Category:</b> {{ report.train_cat.name }}</p>
                <p><b>Goal:</b> {{ report.train_goal.short_descr }}</p>
                <p><b>Level:</b> {{ report.current_train_level.name }}</p>
                <p><b>Start Date:</b> {{ new Date(report.created_date).toLocaleDateString('en-US') }}</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Training Summary Report table Small Screen-->
        <div class="row align-items-center justify-content-center mt-5">
          <div class="d-md-none">
            <h4>Training Summary</h4>
            <div class="card mt-3">
              <div class="card-header">
                <h6 scope="col" class="text-danger"><b>Workout Days</b></h6>
                <div class="card-body text-center bg-light">
                  <p style="white-space: pre-wrap">{{ workoutDays(this.schedules) }}</p>
                </div>
              </div>
            </div>

            <div class="card mt-3">
              <div class="card-header">
                <h6 scope="col" class="text-danger"><b>Rest Days</b></h6>
                <div class="card-body text-center bg-light">
                  <p style="white-space: pre-wrap">{{ restDays(this.schedules) }}</p>
                </div>
              </div>
            </div>

            <div class="card mt-3">
              <div class="card-header">
                <h6 scope="col" class="text-danger"><b>Complete</b></h6>
                <div class="card-body text-center bg-light">
                  <p style="white-space: pre-wrap">{{ completeTask(this.schedules) }}</p>
                </div>
              </div>
            </div>

            <div class="card mt-3">
              <div class="card-header">
                <h6 scope="col" class="text-danger"><b>Not Complete</b></h6>
                <div class="card-body text-center bg-light">
                  <p style="white-space: pre-wrap">{{ notCompleteTask(this.schedules) }}</p>
                </div>
              </div>
            </div>

            <div class="card mt-3">
              <div class="card-header">
                <h6 scope="col" class="text-danger"><b>Total Time</b></h6>
                <div class="card-body text-center bg-light">
                  <p>{{ totalTime(this.schedules) }}</p>
                </div>
              </div>
            </div>

            <div class="card mt-3">
              <div class="card-header">
                <h6 scope="col" class="text-danger"><b>Total Distance</b></h6>
                <div class="card-body text-center bg-light">
                  <p>{{ totalDistance(this.schedules) }}</p>
                </div>
              </div>
            </div>
          </div>
        </div>


        <!-- training Overview Report table Large Screen-->
        <div class="col col-12 col-md-10 d-none d-xl-block d-lg-block d-md-block">
          <h4 class="text-left mt-2">Training Overview</h4>
          <table class="table table-hover table-striped table-bordered" style="overflow-y: auto" :headers="headers">
            <thead>
            <tr class="table-danger">
              <th @click="sortList('name')" scope="col"><b>Name</b> <br><i class="fa fa-fw fa-sort"></i></th>
              <th @click="sortList('train_cat.name')" scope="col"><b>Category</b> <br><i
                  class="fa fa-fw fa-sort"></i>
              </th>
              <th @click="sortList('train_goal.short_descr')" scope="col"><b>Goal</b> <br><i
                  class="fa fa-fw fa-sort"></i></th>
              <th @click="sortList('current_train_level.name')" scope="col"><b>Level</b> <br><i
                  class="fa fa-fw fa-sort"></i></th>
              <th @click="sortList('created_date')" scope="col"><b>Start Date</b> <br><i
                  class="fa fa-fw fa-sort"></i>
              </th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="report in reports" v-bind:key="report">
              <th scope="row">
                <router-link :to="{ name: 'TrainingSchedules' }" style="color: rgb(255, 0, 0);">{{
                    report.name
                  }}
                </router-link>
              </th>
              <td>{{ report.train_cat.name }}</td>
              <td>{{ report.train_goal.short_descr }}</td>
              <td>{{ report.current_train_level.name }}</td>
              <td>{{ new Date(report.created_date).toLocaleDateString('en-US') }}</td>
            </tr>
            </tbody>
          </table>
        </div>

        <!-- training Report table Large Screen-->
        <div class="col col-12 col-md-10 d-none d-xl-block d-lg-block d-md-block mt-5">
          <h4 class="text-left mb-2">Training Summary</h4>
          <table class="table table-hover table-striped table-bordered" style="overflow-y: auto" :headers="headers">
            <thead>
            <tr class="table-danger">
              <th scope="col"><b>Workout Days</b></th>
              <th scope="col"><b>Rest Days</b></th>
              <th scope="col"><b>Complete</b></th>
              <th scope="col"><b>Not Complete</b></th>
              <th scope="col"><b>Total Time</b></th>
              <th scope="col"><b>Total Distance</b></th>
            </tr>
            </thead>
            <tbody>
            <tr>
              <td style="white-space: pre-wrap">{{ workoutDays(this.schedules) }}</td>
              <td v-if="restDays(this.schedules)" style="white-space: pre-wrap">
                {{ restDays(this.schedules) }}
              </td>
              <td v-else style="white-space: pre-wrap">
                <p>None</p>
              </td>
              <td style="white-space: pre-wrap">{{ completeTask(this.schedules) }}</td>
              <td style="white-space: pre-wrap">{{ notCompleteTask(this.schedules) }}</td>
              <td>{{ totalTime(this.schedules) }}</td>
              <td>{{ totalDistance(this.schedules) }}</td>
            </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import router from '../router';
import {APIService} from '@/http/APIService';

const apiService = new APIService();

export default {
  name: "TrainingReport",
  data: () => ({
    reports: {},
    schedules: [],
    validUserName: "Guest",
    sortedByASC: true,
    reportSize: 0,
    isMobile: false,
    headers: [
      {text: 'Name', sortable: false, align: 'left',},
      {text: 'Category', sortable: false, align: 'left',},
      {text: 'Goal', sortable: false, align: 'left',},
      {text: 'Level', sortable: false, align: 'left',},
      {text: 'Start Date', sortable: false, align: 'left',},
    ],
  }),
  mounted() {
    this.getCustomers();
  },
  methods: {
    sortList(sortBy) {
      if (this.sortedByASC) {
        this.reports.sort((x, y) => (x[sortBy] > y[sortBy] ? -1 : 1));
        this.sortedByASC = false;
      } else {
        this.reports.sort((x, y) => (x[sortBy] < y[sortBy] ? -1 : 1));
        this.sortedByASC = true;
      }
      if (sortBy === 'train_cat.name') {
        if (this.sortedByASC) {
          this.reports.sort((x, y) => (x.train_cat.name > y.train_cat.name ? -1 : 1));
        } else {
          this.reports.sort((x, y) => (x.train_cat.name < y.train_cat.name ? -1 : 1));
        }
      }
      if (sortBy === 'train_goal.short_descr') {
        if (this.sortedByASC) {
          this.reports.sort((x, y) => (x.train_goal.short_descr > y.train_goal.short_descr ? -1 : 1));
        } else {
          this.reports.sort((x, y) => (x.train_goal.short_descr < y.train_goal.short_descr ? -1 : 1));
        }
      }
      if (sortBy === 'current_train_level.name') {
        if (this.sortedByASC) {
          this.reports.sort((x, y) => (x.current_train_level.name > y.current_train_level.name ? -1 : 1));
        } else {
          this.reports.sort((x, y) => (x.current_train_level.name < y.current_train_level.name ? -1 : 1));
        }
      }
      if (sortBy === 'created_date') {
        if (this.sortedByASC) {
          this.reports.sort((x, y) => (x.created_date > y.created_date ? -1 : 1));
        } else {
          this.reports.sort((x, y) => (x.created_date < y.created_date ? -1 : 1));
        }
      }
    },
    onResize() {
      if (window.innerWidth > 600)
        this.isMobile = false;
      else
        this.isMobile = true;
    },
    showMessages() {
      console.log(this.$route.params.msg)
      if (this.$route.params.msg) {
        this.showMsg = this.$route.params.msg;
      }
    },
    // Get User
    getCustomers() {
      apiService.getCustomerList().then(response => {
        this.customers = response.data.data;
        console.log('Customers', this.customers)
        this.customerSize = this.customers.length;
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
    // Load Reports
    loadReports() {
      if (localStorage.getItem("isAuthenticates")
          && JSON.parse(localStorage.getItem("isAuthenticates")) === true) {
        this.validUserName = JSON.parse(localStorage.getItem("log_user"));
        console.log('name', this.validUserName)
      }
      // Load Training Preferences Data
      apiService.getTrainingPreferenceList(this.validUserName)
          .then((response) => {
                this.reports = response.data.data.filter((report) => {
                  return report.user.username === this.validUserName;
                });
              }
          )
          .catch((error) => {
            console.log('Error Load Plans', error);
          });
      // Load Training Schedule data
      apiService.getTrainingScheduleUser(this.validUserName)
          .then((response) => {
                this.schedules = response.data.data.filter((schedule) => {
                  return schedule.user.username === this.validUserName;
                });
              }
          )
          .catch((error) => {
            console.log('Error Load Schedules', error);
          });
    },
    // Display workout days
    workoutDays(schedule) {
      const days = new Set();
      schedule.forEach(function (schedule) {
        if (schedule.sunday) days.add('Sunday');
        if (schedule.monday) days.add('Monday');
        if (schedule.tuesday) days.add('Tuesday');
        if (schedule.wednesday) days.add('Wednesday');
        if (schedule.thursday) days.add('Thursday');
        if (schedule.friday) days.add('Friday');
        if (schedule.saturday) days.add('Saturday');
      });
      const workoutDays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'].filter(day => days.has(day));
      return workoutDays.join('\n');
    },
    // Display rest days
    restDays(schedule) {
      const days = new Set();
      schedule.forEach(function (schedule) {
        if (schedule.sunday) days.add('Sunday');
        if (schedule.monday) days.add('Monday');
        if (schedule.tuesday) days.add('Tuesday');
        if (schedule.wednesday) days.add('Wednesday');
        if (schedule.thursday) days.add('Thursday');
        if (schedule.friday) days.add('Friday');
        if (schedule.saturday) days.add('Saturday');
      });
      const restDays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'].filter(day => !days.has(day));
      return restDays.join('\n');
    },
    // Display completed tasks
    completeTask(schedule) {
      const completes = new Set();
      schedule.forEach(function (schedule) {
        if (schedule.is_complete_sunday) completes.add(schedule.sunday_workout + " " + schedule.sunday_pace);
        if (schedule.is_complete_monday) completes.add(schedule.monday_workout + " " + schedule.monday_pace);
        if (schedule.is_complete_tuesday) completes.add(schedule.tuesday_workout + " " + schedule.tuesday_pace);
        if (schedule.is_complete_wednesday) completes.add(schedule.wednesday_workout + " " + schedule.wednesday_pace);
        if (schedule.is_complete_thursday) completes.add(schedule.thursday_workout + " " + schedule.thursday_pace);
        if (schedule.is_complete_friday) completes.add(schedule.friday_workout + " " + schedule.friday_pace);
        if (schedule.is_complete_saturday) completes.add(schedule.saturday_workout + " " + schedule.saturday_pace);
      });
      return Array.from(completes).join('\n');
    },
    // Display non completed tasks
    notCompleteTask(schedule) {
      const notCompletes = new Set();
      schedule.forEach(function (schedule) {
        if (!schedule.is_complete_sunday) notCompletes.add(schedule.sunday_workout + " " + schedule.sunday_pace);
        if (!schedule.is_complete_monday) notCompletes.add(schedule.monday_workout + " " + schedule.monday_pace);
        if (!schedule.is_complete_tuesday) notCompletes.add(schedule.tuesday_workout + " " + schedule.tuesday_pace);
        if (!schedule.is_complete_wednesday) notCompletes.add(schedule.wednesday_workout + " " + schedule.wednesday_pace);
        if (!schedule.is_complete_thursday) notCompletes.add(schedule.thursday_workout + " " + schedule.thursday_pace);
        if (!schedule.is_complete_friday) notCompletes.add(schedule.friday_workout + " " + schedule.friday_pace);
        if (!schedule.is_complete_saturday) notCompletes.add(schedule.saturday_workout + " " + schedule.saturday_pace);
      });
      return Array.from(notCompletes).join('\n');
    },
    // Display Total time
    totalTime(schedule) {
      let totalSeconds = 0;
      schedule.forEach(function (schedule) {
        if (schedule.sunday) totalSeconds += this.getSeconds(schedule.sunday_pace);
        if (schedule.monday) totalSeconds += this.getSeconds(schedule.monday_pace);
        if (schedule.tuesday) totalSeconds += this.getSeconds(schedule.tuesday_pace);
        if (schedule.wednesday) totalSeconds += this.getSeconds(schedule.wednesday_pace);
        if (schedule.thursday) totalSeconds += this.getSeconds(schedule.thursday_pace);
        if (schedule.friday) totalSeconds += this.getSeconds(schedule.friday_pace);
        if (schedule.saturday) totalSeconds += this.getSeconds(schedule.saturday_pace);
      }, this);
      const hours = Math.floor(totalSeconds / 3600);
      const minutes = Math.floor((totalSeconds % 3600) / 60);
      const seconds = totalSeconds % 60;
      return `${this.formatTime(hours)}:${this.formatTime(minutes)}:${this.formatTime(seconds)}`;
    },
    getSeconds(time) {
      const [hours, minutes, seconds] = time.split(':').map(Number);
      return hours * 3600 + minutes * 60 + seconds;
    },
    formatTime(value) {
      return value.toString().padStart(2, '0');
    },
    totalDistance(schedule) {
      let totalDistance = 0;
      schedule.forEach(function (daySchedule) {
        if (daySchedule.sunday && daySchedule.sunday_distance !== null) totalDistance += parseFloat(daySchedule.sunday_distance);
        if (daySchedule.monday && daySchedule.monday_distance !== null) totalDistance += parseFloat(daySchedule.monday_distance);
        if (daySchedule.tuesday && daySchedule.tuesday_distance !== null) totalDistance += parseFloat(daySchedule.tuesday_distance);
        if (daySchedule.wednesday && daySchedule.wednesday_distance !== null) totalDistance += parseFloat(daySchedule.wednesday_distance);
        if (daySchedule.thursday && daySchedule.thursday_distance !== null) totalDistance += parseFloat(daySchedule.thursday_distance);
        if (daySchedule.friday && daySchedule.friday_distance !== null) totalDistance += parseFloat(daySchedule.friday_distance);
        if (daySchedule.saturday && daySchedule.saturday_distance !== null) totalDistance += parseFloat(daySchedule.saturday_distance);
      });
      console.log('distance', totalDistance)
      return totalDistance.toFixed(2);
    },

  },
  created() {
    this.loadReports()
  },
};
</script>
<style>
button {
  padding: 1rem;
  border: 0;
  cursor: pointer;
}
</style>