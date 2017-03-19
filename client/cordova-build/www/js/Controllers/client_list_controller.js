(function(){
  angular
    .module('App.controllers')

    /**
     * @class App.controllers.patientListController
     */
    .controller('clientListController', clientListController);

    clientListController.$inject = ['$scope', 'clientDetailsService'];

    function clientListController($scope, clientDetailsService) {
      $scope.clients = [{
        id: 1,
        firstName: "First",
        LastName: "Last",
        dob: new Date(),
        sex: "Male"
      }];

      clientDetailsService.getPatients("atoken" ,function(clients){
        $scope.clients = clients;
      });
    }
})();
