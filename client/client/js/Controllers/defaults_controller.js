(function(){
  'use strict';
  angular
    .module('App.controllers')

    /**
     * @class App.controllers.defaultsController
     */
    .controller('defaultsController', defaultsController);

    defaultsController.$inject = ['$scope','$stateParams'];

    function defaultsController($scope, $stateParams) {
      $scope.options = {
        srEngines : [
          "Sphynx Offline Recognition",
          "Google Speech Recognition",
          "Google Cloud Services",
          "Microsoft Bing Speech Recognition"
        ],
        musicServices : [
          "Amazon Prime Music",
          "Google Play Music",
          "SoundCloud",
          "Spotify"
        ]
      };

      $scope.prefrences = {
        selectedSREngine : "Google Speech Recognition",
        selectedMusicService : null
      };
      $scope.ddSelectSelected = {}; // Must be an object
    }
})();
