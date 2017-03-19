(function () {
  'use strict';
  angular

    .module('App.services')
    /**
     * @class App.services.localization
     */
    .factory('clientDetailsService', clientDetailsService);

  clientDetailsService.$inject = ['dataService'];

  function clientDetailsService(dataService) {
    var patients = [];
    init();

    return {
      getPatients: getPatients,
      getPatient: getPatient
    };

    function init(){
      patients = [
        {
          id: 1,
          firstName: "First",
          LastName: "Last",
          dob: new Date(),
          sex: "Male"
        }
      ]
    }

    function getPatients(token, callback){
      dataService.getPatients(
        token
      ).then(function (data) {
        patients = data;
        callback(data);
      });
    }

    function getPatient(index) {
      return patients[index];
    }
  }
})();
