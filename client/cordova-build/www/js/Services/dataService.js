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
      getPatients: getPatients
    };

    function getPatients(token){
      return $http({
        method: 'GET',
        url: BASE.URL+":"+BASE.PORT+'/getClients',
        params: {
          token: token
        }
      })
        .then(getPatientsComplete)
        .catch(getPatientsFailed);

      function getPatientsComplete(response) {
        return $q.resolve(response.data);
      }

      function getPatientsFailed(error) {
        console.log('XHR Failed for getPatients.' + error.data);
        return $q.reject(error);
      }
    }
  }
})();
