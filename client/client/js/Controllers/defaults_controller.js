(function(){
  'use strict';
  angular
    .module('App.controllers')

    /**
     * @class App.controllers.defaultsController
     */
    .controller('defaultsController', defaultsController);

    defaultsController.$inject = ['$scope','$stateParams', 'dataService', '$timeout'];

    function defaultsController($scope, $stateParams, dataService, $timeout) {
      $scope.options = dataService.getOptions();
      $scope.loginQueue = [];

      $scope.$watchCollection(function () {
        return $scope.preferences;
      }, function(){
        console.log($scope.preferences);
        if($scope.preferences && $scope.preferences.keyword) {
          dataService.setPreferences(angular.copy($scope.preferences)).then(function (data) {
            for(var service in data.srService){
              console.log(service);
              loginQueue.push(service);
            }
          });
        }
      });

      dataService.getPreferences().then(function (data) {
        $scope.preferences = {};
        $scope.preferences.keyword = data.keyword;
        $scope.preferences.srService = $scope.options.srEngines[data.srService];
        $scope.preferences.musicService = $scope.options.musicServices[data.musicService];
        $scope.preferences.weatherService = $scope.options.weatherServices[data.weatherService];
        console.log($scope.preferences);
      });

      $scope.ddSelectSelected = {}; // Must be an object
    }
})();
