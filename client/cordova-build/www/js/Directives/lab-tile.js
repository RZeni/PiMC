(function () {
  'use strict';
  angular

    .module('App.directives')
    /**
     * @class App.directives.patientTile
     */
    .directive('labTile', function () {
      return {
        restrict: 'E',
        templateUrl: 'templates/lab_tile.html',
        replace: true
      };
    });
})();
