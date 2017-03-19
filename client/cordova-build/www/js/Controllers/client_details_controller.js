(function(){
  angular
    .module('App.controllers')

    /**
     * @class App.controllers.patientQueryController
     */
    .controller('patientQueryController', patientQueryController);

    patientQueryController.$inject = ['$scope','$stateParams', 'patientQueryService'];

    function patientQueryController($scope, $stateParams, patientQueryService) {
      $scope.selectedPatientIndex = $stateParams.clientID;
      $scope.client = {
        id: 1,
        firstName: "First",
        LastName: "Last",
        dob: new Date(),
        sex: "Male"
      };
      patientQueryService.getPatient($stateParams.clientID, function (client) {
        $scope.client = client;
      });
    }
})();
