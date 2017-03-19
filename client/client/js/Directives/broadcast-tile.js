(function () {
  'use strict';
  angular

    .module('App.directives')
    /**
     * @class App.directives.broadcastTile
     */
    .directive('broadcastTile', function () {
      return {
        restrict: 'E',
        templateUrl: 'templates/app/partials/broadcast-tile.html',
        replace: true
      };
    });
})();
