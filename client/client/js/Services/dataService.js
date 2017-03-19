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

    return {
      getPreferences: getPreferences
    };

    function getPreferences(token){
      return $http({
        method: 'GET',
        url: BASE.URL+":"+BASE.PORT+'/getPreferences',
        params: {
          token: token
        }
      })
      .then(authenticationSuccessful)
      .catch(authenticationFailed);

      function authenticationSuccessful(response) {
        return $q.resolve(response.data);
      }

      function authenticationFailed(error) {
        console.log('XHR Failed for getPatients.' + error.data);
        return $q.reject(error);
      }
    }
  }
})();
