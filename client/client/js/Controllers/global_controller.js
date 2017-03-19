(function(){
  'use strict';
  angular
    .module('App.controllers')

    /**
     * @class App.controllers.globalController
     */
    .controller('globalController', globalController);

  globalController.$inject = ['$scope', '$state', '$ionicSideMenuDelegate', 'localization'];

  function globalController($scope, $state, $ionicSideMenuDelegate, localization) {
    $scope.mode = "web";
    $scope.sideMenuOpen = false;
    $scope.DICTIONARY = localization.getDictionary('en');

    init();

    function init() {
      if(window && window.process && window.process.type)
        $scope.mode = "desktop";

      if(navigator.userAgent.match(/Cordova/i))
        $scope.mode = "mobile";

      $scope.$watch(function () {
        return $ionicSideMenuDelegate.isOpenLeft();
      }, function (isOpen) {
        if ($scope.sideMenuOpen && !isOpen)
          $scope.sideMenuOpen = !$scope.sideMenuOpen;
        else if (!$scope.sideMenuOpen && isOpen)
          $scope.sideMenuOpen = !$scope.sideMenuOpen;
      });
    }
  }
})();
