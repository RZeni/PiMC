(function () {
  'use strict';
  angular

    .module('App.directives')
    /**
     * @class App.directives.patientTile
     */
    .directive('patientTile', function () {
      return {
        restrict: 'E',
        templateUrl: 'templates/client_tile.html',
        replace: true
      };
    });
})();
