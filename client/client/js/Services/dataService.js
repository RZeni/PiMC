(function () {
  'use strict';
  angular

    .module('App.services')
    /**
     * @class App.services.localization
     */
    .factory('dataService', dataService);

  dataService.$inject = ['$http', '$q', 'BASE'];

  function dataService($http, $q, BASE) {
    var options = {
      srEngines : [
        "Sphynx Offline Recognition",
        "Google Speech Recognition",
        "Google Cloud Services",
        "Microsoft Bing Speech Recognition"
      ],
      musicServices : [
        "Spotify",
        "Last FM",
        "SoundCloud",
        "Amazon Prime Music"
      ],
      weatherServices : [
        "Open Weather Map",
        "Yahoo",
        "Weather.com",
        "NOAA"
      ],
      radioServices : [
        "Last FM"
      ]
    };

    return {
      getPreferences: getPreferences,
      setPreferences: setPreferences,
      getOptions: getOptions
    };

    function getPreferences(){
      return $http({
        method: 'GET',
        url: BASE.URL+":"+BASE.PORT+'/getPreferences',
      })
      .then(getPreferencesSuccessful)
      .catch(getPreferencesFailed);

      function getPreferencesSuccessful(response) {
        return $q.resolve(response.data);
      }

      function getPreferencesFailed(error) {
        console.error('XHR Failed for get. ' + JSON.stringify(error));
        return $q.reject({
          selectedSREngine : "Google Speech Recognition",
          selectedMusicService : "Spotify",
          selectedWeatherService : "NOAA",
          keyword : ""
        });
      }
    }

    function setPreferences(preferences){
      var temp = options.srEngines.indexOf(preferences.srService);
      if(temp != -1)
        preferences.srService = temp;

      temp = options.musicServices.indexOf(preferences.musicService);
      if(temp != -1)
        preferences.musicService = temp;

      temp = options.weatherServices.indexOf(preferences.weatherService);
      if(temp != -1)
        preferences.weatherService = temp;

      console.log(preferences);
      return $http({
        method: 'POST',
        url: BASE.URL+":"+BASE.PORT+'/setPreferences',
        params: {
          preferences: preferences
        }
      })
      .then(setPreferencesSuccessful)
      .catch(setPreferencesFailed);

      function setPreferencesSuccessful(response) {
        return $q.resolve(response.data);
      }

      function setPreferencesFailed(error) {
        console.error('XHR Failed for set Pref.' + error.data);
        return $q.reject(error);
      }
    }

    function getOptions() {
      return options;
    }
  }
})();
