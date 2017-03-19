(function(){
  'use strict';
  angular
    .module('App.controllers')

    /**
     * @class App.controllers.broadcastsController
     */
    .controller('broadcastsController', broadcastsController);

    broadcastsController.$inject = ['$scope','$stateParams'];

    function broadcastsController($scope, $stateParams) {
      $scope.broadcasts = [{
        img: "",
        city: "Oakville",
        creationTime: new Date('2017-01-27'),
        country: "Canada",
        endTime: new Date('2017-01-30'),
        lat: 54.4,
        long: -55.5,
        number: "12",
        province: "Ontario",
        startTime: new Date('2017-01-28'),
        street: "Main st.",
        venue: "Pizza Pizza"
      },{
        img: "",
        city: "Oakville",
        creationTime: new Date('2017-01-27'),
        country: "Canada",
        endTime: new Date('2017-01-30'),
        lat: 54.4,
        long: -55.5,
        number: "12",
        province: "Ontario",
        startTime: new Date('2017-01-28'),
        street: "Main st.",
        venue: "Pizza Pizza"
      }];
    }
})();
