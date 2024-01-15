<template>
  <div>
    <div class="container-fluid">
      <div class="row justify-content-center">
        <div class="col-md-8">
          <div class="col col-12 align-items-center justify-content-center text-danger">
            <blockquote>
              <h2>
                {{ validUserName }}'s Training Schedules
              </h2>
            </blockquote>
          </div>
          <!--Display Training Schedule if Any-->
          <div v-if="trainingSchedules.length > 0">
            <!--Encouragement Message-->
            <div class="container-fluid my-4">
              <div class="row justify-content-center">
                <div class="col-md-6">
                  <div class="card-body">
                    <div class="card p-1 shadow">
                      <p class="card-text text-danger">
                        {{ promptEncouragement[Math.floor(Math.random() * promptEncouragement.length)].prompt }}
                      </p>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!--Training Schedule Table-->
            <div class="table-responsive">
              <table class="table table-hover table-striped table-bordered">
                <thead>
                <tr class="table-danger">
                  <th scope="col" class="text-center">Name</th>
                  <th scope="col" class="text-center">Day Tasks</th>
                  <th scope="col" class="text-center"> Level {{ "&plusmn;" }}</th>
                </tr>
                </thead>
                <tbody>
                <!--Display List of Training Schedules-->
                <!--Display List of Training Schedules with not complete or complete task button-->
                <tr v-for="schedule in trainingSchedules" :key="schedule.id">
                  <td class="align-middle text-center">{{ schedule.name }}</td>
                  <td class="align-middle text-center">
                    <ul>
                      <li v-if="schedule.sunday">
                        <h5 class="text-danger">Sunday Workout</h5>
                        <span>
                          Warm up: Stretch for 5:00 minutes.
                          <br>
                          {{ schedule.sunday_workout }} {{ schedule.sunday_pace }} minutes.
                          <br>
                          <span v-if="schedule.sunday_distance > 0">Strive for {{
                              schedule.sunday_distance
                            }} miles.</span>
                          <br>
                          Cool down: Stretch for 3:00 minutes.
                        </span>
                        <br>
                        <button v-if="schedule.is_complete_sunday" class="btn btn-outline-success btn-xs ml-3 my-2"
                                @click="isCompleteSunday(schedule)">
                          {{ 'Complete' }}
                        </button>
                        <button v-else class="btn btn-outline-danger btn-xs ml-3 my-2"
                                @click="isCompleteSunday(schedule)">
                          {{ 'Not Complete' }}
                        </button>
                      </li>
                      <li v-if="schedule.monday">
                        <h5 class="text-danger">Monday Workout</h5>
                        <span>
                          Warm up: Stretch for 5:00 minutes.
                          <br>
                          {{ schedule.monday_workout }} {{ schedule.monday_pace }} minutes.
                          <br>
                          <span v-if="schedule.monday_distance > 0">Strive for {{
                              schedule.monday_distance
                            }} miles.</span>
                          <br>
                          Cool down: Stretch for 3:00 minutes.
                        </span>
                        <br>
                        <button v-if="schedule.is_complete_monday" class="btn btn-outline-success btn-xs ml-3 my-2"
                                @click="isCompleteMonday(schedule)">
                          {{ 'Complete' }}
                        </button>
                        <button v-else class="btn btn-outline-danger btn-xs ml-3 my-2"
                                @click="isCompleteMonday(schedule)">
                          {{ 'Not Complete' }}
                        </button>
                      </li>
                      <li v-if="schedule.tuesday">
                        <h5 class="text-danger">Tuesday Workout</h5>
                        <span>
                          Warm up: Stretch for 5:00 minutes.
                          <br>
                          {{ schedule.tuesday_workout }} {{ schedule.tuesday_pace }} minutes.
                          <br>
                          <span v-if="schedule.tuesday_distance > 0">Strive for {{
                              schedule.tuesday_distance
                            }} miles.</span>
                          <br>
                          Cool down: Stretch for 3:00 minutes.
                        </span>
                        <br>
                        <button v-if="schedule.is_complete_tuesday" class="btn btn-outline-success btn-xs ml-3 my-2"
                                @click="isCompleteTuesday(schedule)">
                          {{ 'Complete' }}
                        </button>
                        <button v-else class="btn btn-outline-danger btn-xs ml-3 my-2"
                                @click="isCompleteTuesday(schedule)">
                          {{ 'Not Complete' }}
                        </button>
                      </li>
                      <li v-if="schedule.wednesday">
                        <h5 class="text-danger">Wednesday Workout</h5>
                        <span>
                          Warm up: Stretch for 5:00 minutes.
                          <br>
                          {{ schedule.wednesday_workout }} {{ schedule.wednesday_pace }} minutes.
                          <br>
                          <span v-if="schedule.wednesday_distance > 0">Strive for {{ schedule.wednesday_distance }} miles.</span>
                          <br>
                          Cool down: Stretch for 3:00 minutes.
                        </span>
                        <br>
                        <button v-if="schedule.is_complete_wednesday" class="btn btn-outline-success btn-xs ml-3 my-2"
                                @click="isCompleteWednesday(schedule)">
                          {{ 'Complete' }}
                        </button>
                        <button v-else class="btn btn-outline-danger btn-xs ml-3 my-2"
                                @click="isCompleteWednesday(schedule)">
                          {{ 'Not Complete' }}
                        </button>
                      </li>
                      <li v-if="schedule.thursday">
                        <h5 class="text-danger">Thursday Workout</h5>
                        <span>
                          Warm up: Stretch for 5:00 minutes.
                          <br>
                          {{ schedule.thursday_workout }} {{ schedule.thursday_pace }} minutes.
                          <br>
                          <span v-if="schedule.thursday_distance > 0">Strive for {{
                              schedule.thursday_distance
                            }} miles.</span>
                          <br>
                          Cool down: Stretch for 3:00 minutes.
                        </span>
                        <br>
                        <button v-if="schedule.is_complete_thursday" class="btn btn-outline-success btn-xs ml-3 my-2"
                                @click="isCompleteThursday(schedule)">
                          {{ 'Complete' }}
                        </button>
                        <button v-else class="btn btn-outline-danger btn-xs ml-3 my-2"
                                @click="isCompleteThursday(schedule)">
                          {{ 'Not Complete' }}
                        </button>
                      </li>
                      <li v-if="schedule.friday">
                        <h5 class="text-danger">Friday Workout</h5>
                        <span>
                          Warm up: Stretch for 5:00 minutes.
                          <br>
                          {{ schedule.friday_workout }} {{ schedule.friday_pace }} minutes.
                          <br>
                          <span v-if="schedule.friday_distance > 0">Strive for {{
                              schedule.friday_distance
                            }} miles.</span>
                          <br>
                          Cool down: Stretch for 3:00 minutes.
                        </span>
                        <br>
                        <button v-if="schedule.is_complete_friday" class="btn btn-outline-success btn-xs ml-3 my-2"
                                @click="isCompleteFriday(schedule)">
                          {{ 'Complete' }}
                        </button>
                        <button v-else class="btn btn-outline-danger btn-xs ml-3 my-2"
                                @click="isCompleteFriday(schedule)">
                          {{ 'Not Complete' }}
                        </button>
                      </li>
                      <li v-if="schedule.saturday">
                        <h5 class="text-danger">Saturday Workout</h5>
                        <span>
                          Warm up: Stretch for 5:00 minutes.
                          <br>
                          {{ schedule.saturday_workout }} {{ schedule.saturday_pace }} minutes.
                          <br>
                          <span v-if="schedule.saturday_distance > 0">Strive for {{
                              schedule.saturday_distance
                            }} miles.</span>
                          <br>
                          Cool down: Stretch for 3:00 minutes.
                        </span>
                        <br>
                        <button v-if="schedule.is_complete_saturday" class="btn btn-outline-success btn-xs ml-3 my-2"
                                @click="isCompleteSaturday(schedule)">
                          {{ 'Complete' }}
                        </button>
                        <button v-else class="btn btn-outline-danger btn-xs ml-3 my-2"
                                @click="isCompleteSaturday(schedule)">
                          {{ 'Not Complete' }}
                        </button>
                      </li>
                    </ul>
                  </td>
                  <!--Level up and level down buttons-->
                  <td class="align-middle text-center">
                    <span style="font-size: 18px; font-weight: bold;">Current Level: {{ schedule.skd_level }}</span>
                    <br>
                    <br>
                    <button class="btn btn-outline-success btn-xs ml-3 my-2" @click="levelUp(schedule)">
                      Level Up
                    </button>
                    <br>
                    <button class="btn btn-outline-secondary btn-xs ml-3 my-2" @click="levelDown(schedule)">
                      Level Down
                    </button>
                  </td>
                </tr>
                </tbody>
              </table>
            </div>
          </div>
          <div v-else>
            <!--Encouragement Message-->
            <div class="container-fluid mt-4">
              <div class="row justify-content-center">
                <div class="col-md-6">
                  <div class="card-body">
                    <div class="card p-1 shadow">
                      <p class="card-text text-danger">
                        {{ promptEncouragement[Math.floor(Math.random() * promptEncouragement.length)].prompt }}
                      </p>
                    </div>
                  </div>
                  <p class="text-muted text-center mt-4">No Running Schedule Found</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!--Back To Training Preferences-->
    <div class="container mt-3">
      <div class="card-body">
        <button class="btn btn-danger" @click="goToTrainingPlans">Training Plans</button>
      </div>
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
      trainingPreferences: [],
      trainingSchedules: [],
      promptEncouragement: [],
      validUserName: "Guest",
    }
  },
  mounted() {
    this.getCustomers();
  },
  methods: {
    // Get user
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
    // Load training preferences
    loadTrainingPreferences() {
      apiService.getTrainingPreferenceList()
          .then((response) => {
            this.trainingPreferences = response.data;
            console.log('Preferences', this.trainingPreferences);
          })
          .catch((error) => {
            console.log('Error Load Preferences', error);
          });
    },
    // Load only logged in user training schedule
    loadTrainingSchedules() {
      if (localStorage.getItem("isAuthenticates")
          && JSON.parse(localStorage.getItem("isAuthenticates")) === true) {
        this.validUserName = JSON.parse(localStorage.getItem("log_user"));
        console.log('name', this.validUserName)
      }
      apiService.getTrainingScheduleUser(this.validUserName)
          .then((response) => {
                this.trainingSchedules = response.data.data.filter((schedule) => {
                  return schedule.user.username === this.validUserName;
                });

                console.log('Schedules', this.trainingSchedules);
              }
          )
          .catch((error) => {
            console.log('Error Load Schedules', error);
          });
    },
    // Load User encouragement message
    loadPromptEncouragement() {
      apiService.getPromptsEncouragementList()
          .then((response) => {
            this.promptEncouragement = response.data;
            console.log('Prompts', this.promptEncouragement);
          })
          .catch((error) => {
            console.log('Error Load Prompt', error);
          });
    },
    // Go to training plan page
    goToTrainingPlans() {
      router.push("/training-plans/");
    },
    // Check or uncheck is complete option
    isCompleteSunday(schedule) {
      if (this.trainingSchedules.find(s => s.id === schedule.id)) {
        schedule.is_complete_sunday = !schedule.is_complete_sunday;
      }
      apiService.updateTrainingSchedule(schedule.id, schedule)
          .then((response) => {
            console.log('Update Schedule', response.data);
          })
          .catch((error) => {
            console.log('Error Update Schedule', error);
          });
    },
    isCompleteMonday(schedule) {
      if (this.trainingSchedules.find(s => s.id === schedule.id)) {
        schedule.is_complete_monday = !schedule.is_complete_monday;
      }
      apiService.updateTrainingSchedule(schedule.id, schedule)
          .then((response) => {
            console.log('Update Schedule', response.data);
          })
          .catch((error) => {
            console.log('Error Update Schedule', error);
          });
    },
    isCompleteTuesday(schedule) {
      if (this.trainingSchedules.find(s => s.id === schedule.id)) {
        schedule.is_complete_tuesday = !schedule.is_complete_tuesday;
      }
      apiService.updateTrainingSchedule(schedule.id, schedule)
          .then((response) => {
            console.log('Update Schedule', response.data);
          })
          .catch((error) => {
            console.log('Error Update Schedule', error);
          });
    },
    isCompleteWednesday(schedule) {
      if (this.trainingSchedules.find(s => s.id === schedule.id)) {
        schedule.is_complete_wednesday = !schedule.is_complete_wednesday;
      }
      apiService.updateTrainingSchedule(schedule.id, schedule)
          .then((response) => {
            console.log('Update Schedule', response.data);
          })
          .catch((error) => {
            console.log('Error Update Schedule', error);
          });
    },
    isCompleteThursday(schedule) {
      if (this.trainingSchedules.find(s => s.id === schedule.id)) {
        schedule.is_complete_thursday = !schedule.is_complete_thursday;
      }
      apiService.updateTrainingSchedule(schedule.id, schedule)
          .then((response) => {
            console.log('Update Schedule', response.data);
          })
          .catch((error) => {
            console.log('Error Update Schedule', error);
          });
    },
    isCompleteFriday(schedule) {
      if (this.trainingSchedules.find(s => s.id === schedule.id)) {
        schedule.is_complete_friday = !schedule.is_complete_friday;
      }
      apiService.updateTrainingSchedule(schedule.id, schedule)
          .then((response) => {
            console.log('Update Schedule', response.data);
          })
          .catch((error) => {
            console.log('Error Update Schedule', error);
          });
    },
    isCompleteSaturday(schedule) {
      if (this.trainingSchedules.find(s => s.id === schedule.id)) {
        schedule.is_complete_saturday = !schedule.is_complete_saturday;
      }
      apiService.updateTrainingSchedule(schedule.id, schedule)
          .then((response) => {
            console.log('Update Schedule', response.data);
          })
          .catch((error) => {
            console.log('Error Update Schedule', error);
          });
    },
    // Level up
    levelUp(schedule) {
      console.log('Schedule id', schedule.id)
      if (this.trainingSchedules.find(s => s.id === schedule.id)) {
        schedule.skd_level++
      }
      if (this.trainingSchedules.find(s => s.id === schedule.id)) {
        schedule.sunday_distance *= 1.05;
        schedule.sunday_distance = schedule.sunday_distance.toFixed(2);
        try {
          const timeParts = schedule.sunday_pace.split(':');
          const hours = parseInt(timeParts[0]);
          const minutes = parseInt(timeParts[1]);
          const seconds = parseInt(timeParts[2]);
          if (isNaN(hours) || isNaN(minutes) || isNaN(seconds)) {
            throw new Error('Invalid time value');
          }
          let totalSeconds = (hours * 3600) + (minutes * 60) + seconds;
          totalSeconds += 30;
          const newTime = new Date(totalSeconds * 1000).toISOString().substr(11, 8);
          schedule.sunday_pace = newTime;
        } catch (error) {
          console.error(error);
        }
        apiService.updateTrainingSchedule(schedule.id, schedule)
            .then((response) => {
              console.log('Update Schedule', response.data);
            })
            .catch((error) => {
              console.log('Error Update Schedule', error);
            });
      }
      if (this.trainingSchedules.find(s => s.id === schedule.id)) {
        schedule.monday_distance *= 1.05;
        schedule.monday_distance = schedule.monday_distance.toFixed(2);
        try {
          const timeParts = schedule.monday_pace.split(':');
          const hours = parseInt(timeParts[0]);
          const minutes = parseInt(timeParts[1]);
          const seconds = parseInt(timeParts[2]);
          if (isNaN(hours) || isNaN(minutes) || isNaN(seconds)) {
            throw new Error('Invalid time value');
          }
          let totalSeconds = (hours * 3600) + (minutes * 60) + seconds;
          totalSeconds += 30;
          const newTime = new Date(totalSeconds * 1000).toISOString().substr(11, 8);
          schedule.monday_pace = newTime;
        } catch (error) {
          console.error(error);
        }
        apiService.updateTrainingSchedule(schedule.id, schedule)
            .then((response) => {
              console.log('Update Schedule', response.data);
            })
            .catch((error) => {
              console.log('Error Update Schedule', error);
            });
      }
      if (this.trainingSchedules.find(s => s.id === schedule.id)) {
        schedule.tuesday_distance *= 1.05;
        schedule.tuesday_distance = schedule.tuesday_distance.toFixed(2);
        try {
          const timeParts = schedule.tuesday_pace.split(':');
          const hours = parseInt(timeParts[0]);
          const minutes = parseInt(timeParts[1]);
          const seconds = parseInt(timeParts[2]);
          if (isNaN(hours) || isNaN(minutes) || isNaN(seconds)) {
            throw new Error('Invalid time value');
          }
          let totalSeconds = (hours * 3600) + (minutes * 60) + seconds;
          totalSeconds += 30;
          const newTime = new Date(totalSeconds * 1000).toISOString().substr(11, 8);
          schedule.tuesday_pace = newTime;
        } catch (error) {
          console.error(error);
        }
        apiService.updateTrainingSchedule(schedule.id, schedule)
            .then((response) => {
              console.log('Update Schedule', response.data);
            })
            .catch((error) => {
              console.log('Error Update Schedule', error);
            });
      }
      if (this.trainingSchedules.find(s => s.id === schedule.id)) {
        schedule.wednesday_distance *= 1.05;
        schedule.wednesday_distance = schedule.wednesday_distance.toFixed(2);
        try {
          const timeParts = schedule.wednesday_pace.split(':');
          const hours = parseInt(timeParts[0]);
          const minutes = parseInt(timeParts[1]);
          const seconds = parseInt(timeParts[2]);
          if (isNaN(hours) || isNaN(minutes) || isNaN(seconds)) {
            throw new Error('Invalid time value');
          }
          let totalSeconds = (hours * 3600) + (minutes * 60) + seconds;
          totalSeconds += 30;
          const newTime = new Date(totalSeconds * 1000).toISOString().substr(11, 8);
          schedule.wednesday_pace = newTime;
        } catch (error) {
          console.error(error);
        }
        apiService.updateTrainingSchedule(schedule.id, schedule)
            .then((response) => {
              console.log('Update Schedule', response.data);
            })
            .catch((error) => {
              console.log('Error Update Schedule', error);
            });
      }
      if (this.trainingSchedules.find(s => s.id === schedule.id)) {
        schedule.thursday_distance *= 1.05;
        schedule.thursday_distance = schedule.thursday_distance.toFixed(2);
        try {
          const timeParts = schedule.thursday_pace.split(':');
          const hours = parseInt(timeParts[0]);
          const minutes = parseInt(timeParts[1]);
          const seconds = parseInt(timeParts[2]);
          if (isNaN(hours) || isNaN(minutes) || isNaN(seconds)) {
            throw new Error('Invalid time value');
          }
          let totalSeconds = (hours * 3600) + (minutes * 60) + seconds;
          totalSeconds += 30;
          const newTime = new Date(totalSeconds * 1000).toISOString().substr(11, 8);
          schedule.thursday_pace = newTime;
        } catch (error) {
          console.error(error);
        }
        apiService.updateTrainingSchedule(schedule.id, schedule)
            .then((response) => {
              console.log('Update Schedule', response.data);
            })
            .catch((error) => {
              console.log('Error Update Schedule', error);
            });
      }
      if (this.trainingSchedules.find(s => s.id === schedule.id)) {
        schedule.friday_distance *= 1.05;
        schedule.friday_distance = schedule.friday_distance.toFixed(2);
        try {
          const timeParts = schedule.friday_pace.split(':');
          const hours = parseInt(timeParts[0]);
          const minutes = parseInt(timeParts[1]);
          const seconds = parseInt(timeParts[2]);
          if (isNaN(hours) || isNaN(minutes) || isNaN(seconds)) {
            throw new Error('Invalid time value');
          }
          let totalSeconds = (hours * 3600) + (minutes * 60) + seconds;
          totalSeconds += 30;
          const newTime = new Date(totalSeconds * 1000).toISOString().substr(11, 8);
          schedule.friday_pace = newTime;
        } catch (error) {
          console.error(error);
        }
        apiService.updateTrainingSchedule(schedule.id, schedule)
            .then((response) => {
              console.log('Update Schedule', response.data);
            })
            .catch((error) => {
              console.log('Error Update Schedule', error);
            });
      }
      if (this.trainingSchedules.find(s => s.id === schedule.id)) {
        schedule.saturday_distance *= 1.05;
        schedule.saturday_distance = schedule.saturday_distance.toFixed(2);
        try {
          const timeParts = schedule.saturday_pace.split(':');
          const hours = parseInt(timeParts[0]);
          const minutes = parseInt(timeParts[1]);
          const seconds = parseInt(timeParts[2]);
          if (isNaN(hours) || isNaN(minutes) || isNaN(seconds)) {
            throw new Error('Invalid time value');
          }
          let totalSeconds = (hours * 3600) + (minutes * 60) + seconds;
          totalSeconds += 30;
          const newTime = new Date(totalSeconds * 1000).toISOString().substr(11, 8);
          schedule.saturday_pace = newTime;
        } catch (error) {
          console.error(error);
        }
        apiService.updateTrainingSchedule(schedule.id, schedule)
            .then((response) => {
              console.log('Update Schedule', response.data);
            })
            .catch((error) => {
              console.log('Error Update Schedule', error);
            });
      }
    },
    // Level Down
    levelDown(schedule) {
      console.log('Schedule id', schedule.id)
      if (this.trainingSchedules.find(s => s.id === schedule.id) && schedule.skd_level > 0) {
        schedule.skd_level--
      }
      if (this.trainingSchedules.find(s => s.id === schedule.id)) {
        schedule.sunday_distance /= 1.05;
        schedule.sunday_distance = schedule.sunday_distance.toFixed(2);
        try {
          const timeParts = schedule.sunday_pace.split(':');
          const hours = parseInt(timeParts[0]);
          const minutes = parseInt(timeParts[1]);
          const seconds = parseInt(timeParts[2]);
          if (isNaN(hours) || isNaN(minutes) || isNaN(seconds)) {
            throw new Error('Invalid time value');
          }
          let totalSeconds = (hours * 3600) + (minutes * 60) + seconds;
          totalSeconds -= 30;
          const newTime = new Date(totalSeconds * 1000).toISOString().substr(11, 8);
          schedule.sunday_pace = newTime;
        } catch (error) {
          console.error(error);
        }
        apiService.updateTrainingSchedule(schedule.id, schedule)
            .then((response) => {
              console.log('Update Schedule', response.data);
            })
            .catch((error) => {
              console.log('Error Update Schedule', error);
            });
      }
      if (this.trainingSchedules.find(s => s.id === schedule.id)) {
        schedule.monday_distance /= 1.05;
        schedule.monday_distance = schedule.monday_distance.toFixed(2);
        try {
          const timeParts = schedule.monday_pace.split(':');
          const hours = parseInt(timeParts[0]);
          const minutes = parseInt(timeParts[1]);
          const seconds = parseInt(timeParts[2]);
          if (isNaN(hours) || isNaN(minutes) || isNaN(seconds)) {
            throw new Error('Invalid time value');
          }
          let totalSeconds = (hours * 3600) + (minutes * 60) + seconds;
          totalSeconds -= 30;
          const newTime = new Date(totalSeconds * 1000).toISOString().substr(11, 8);
          schedule.monday_pace = newTime;
        } catch (error) {
          console.error(error);
        }
        apiService.updateTrainingSchedule(schedule.id, schedule)
            .then((response) => {
              console.log('Update Schedule', response.data);
            })
            .catch((error) => {
              console.log('Error Update Schedule', error);
            });
      }
      if (this.trainingSchedules.find(s => s.id === schedule.id)) {
        schedule.tuesday_distance /= 1.05;
        schedule.tuesday_distance = schedule.tuesday_distance.toFixed(2);
        try {
          const timeParts = schedule.tuesday_pace.split(':');
          const hours = parseInt(timeParts[0]);
          const minutes = parseInt(timeParts[1]);
          const seconds = parseInt(timeParts[2]);
          if (isNaN(hours) || isNaN(minutes) || isNaN(seconds)) {
            throw new Error('Invalid time value');
          }
          let totalSeconds = (hours * 3600) + (minutes * 60) + seconds;
          totalSeconds -= 30;
          const newTime = new Date(totalSeconds * 1000).toISOString().substr(11, 8);
          schedule.tuesday_pace = newTime;
        } catch (error) {
          console.error(error);
        }
        apiService.updateTrainingSchedule(schedule.id, schedule)
            .then((response) => {
              console.log('Update Schedule', response.data);
            })
            .catch((error) => {
              console.log('Error Update Schedule', error);
            });
      }
      if (this.trainingSchedules.find(s => s.id === schedule.id)) {
        schedule.wednesday_distance /= 1.05;
        schedule.wednesday_distance = schedule.wednesday_distance.toFixed(2);
        try {
          const timeParts = schedule.wednesday_pace.split(':');
          const hours = parseInt(timeParts[0]);
          const minutes = parseInt(timeParts[1]);
          const seconds = parseInt(timeParts[2]);
          if (isNaN(hours) || isNaN(minutes) || isNaN(seconds)) {
            throw new Error('Invalid time value');
          }
          let totalSeconds = (hours * 3600) + (minutes * 60) + seconds;
          totalSeconds -= 30;
          const newTime = new Date(totalSeconds * 1000).toISOString().substr(11, 8);
          schedule.wednesday_pace = newTime;
        } catch (error) {
          console.error(error);
        }
        apiService.updateTrainingSchedule(schedule.id, schedule)
            .then((response) => {
              console.log('Update Schedule', response.data);
            })
            .catch((error) => {
              console.log('Error Update Schedule', error);
            });
      }
      if (this.trainingSchedules.find(s => s.id === schedule.id)) {
        schedule.thursday_distance /= 1.05;
        schedule.thursday_distance = schedule.thursday_distance.toFixed(2);
        try {
          const timeParts = schedule.thursday_pace.split(':');
          const hours = parseInt(timeParts[0]);
          const minutes = parseInt(timeParts[1]);
          const seconds = parseInt(timeParts[2]);
          if (isNaN(hours) || isNaN(minutes) || isNaN(seconds)) {
            throw new Error('Invalid time value');
          }
          let totalSeconds = (hours * 3600) + (minutes * 60) + seconds;
          totalSeconds -= 30;
          const newTime = new Date(totalSeconds * 1000).toISOString().substr(11, 8);
          schedule.thursday_pace = newTime;
        } catch (error) {
          console.error(error);
        }
        apiService.updateTrainingSchedule(schedule.id, schedule)
            .then((response) => {
              console.log('Update Schedule', response.data);
            })
            .catch((error) => {
              console.log('Error Update Schedule', error);
            });
      }
      if (this.trainingSchedules.find(s => s.id === schedule.id)) {
        schedule.friday_distance /= 1.05;
        schedule.friday_distance = schedule.friday_distance.toFixed(2);
        try {
          const timeParts = schedule.friday_pace.split(':');
          const hours = parseInt(timeParts[0]);
          const minutes = parseInt(timeParts[1]);
          const seconds = parseInt(timeParts[2]);
          if (isNaN(hours) || isNaN(minutes) || isNaN(seconds)) {
            throw new Error('Invalid time value');
          }
          let totalSeconds = (hours * 3600) + (minutes * 60) + seconds;
          totalSeconds -= 30;
          const newTime = new Date(totalSeconds * 1000).toISOString().substr(11, 8);
          schedule.friday_pace = newTime;
        } catch (error) {
          console.error(error);
        }
        apiService.updateTrainingSchedule(schedule.id, schedule)
            .then((response) => {
              console.log('Update Schedule', response.data);
            })
            .catch((error) => {
              console.log('Error Update Schedule', error);
            });
      }
      if (this.trainingSchedules.find(s => s.id === schedule.id)) {
        schedule.saturday_distance /= 1.05;
        schedule.saturday_distance = schedule.saturday_distance.toFixed(2);
        try {
          const timeParts = schedule.saturday_pace.split(':');
          const hours = parseInt(timeParts[0]);
          const minutes = parseInt(timeParts[1]);
          const seconds = parseInt(timeParts[2]);
          if (isNaN(hours) || isNaN(minutes) || isNaN(seconds)) {
            throw new Error('Invalid time value');
          }
          let totalSeconds = (hours * 3600) + (minutes * 60) + seconds;
          totalSeconds -= 30;
          const newTime = new Date(totalSeconds * 1000).toISOString().substr(11, 8);
          schedule.saturday_pace = newTime;
        } catch (error) {
          console.error(error);
        }
        apiService.updateTrainingSchedule(schedule.id, schedule)
            .then((response) => {
              console.log('Update Schedule', response.data);
            })
            .catch((error) => {
              console.log('Error Update Schedule', error);
            });
      }
    },
  },
  created() {
    this.loadTrainingPreferences()
    this.loadTrainingSchedules()
    this.loadPromptEncouragement()
  },
}
</script>
<style scoped>
.table th {
  font-size: 22px;
}

.table td {
  padding: 8px;
}

.table td:first-child {
  font-weight: bold;
  font-size: 18px;
}

.table li {
  list-style: none;
  margin-bottom: 4px;
}

.table-responsive {
  overflow-x: auto;
}

.table {
  font-size: 16px;
}

@media screen and (max-width: 768px) {
  .table-responsive {
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
  }

  ul {
    padding-inline-start: 0px !important;
  }
}

@media screen and (max-width: 576px) {
  .table-responsive {
    display: block;
    width: 100%;
    padding-left: 0;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
  }

  ul {
    padding-inline-start: 0px !important;
  }
}

</style>
