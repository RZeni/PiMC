(function(){
  angular
    .module('App.controllers')

    /**
     * @class App.controllers.globalController
     */
    .controller('globalController', globalController);

  globalController.$inject = ['$scope', '$state', 'localization'];

  function globalController($scope, $state, localization) {
    $scope.mode = "web";
    $scope.DICTIONARY = localization.getDictionary('en');

    init();

    function init() {

      console.log(navigator.userAgent.match(/Cordova/i));

      if(window && window.process && window.process.type){
        console.log(process.versions['electron']);
        console.log(window.process.type);
        $scope.mode = "desktop"
      }

      if(navigator.userAgent.match(/Cordova/i)) {
        $scope.mode = "mobile"
      }
    }
  }
})();
