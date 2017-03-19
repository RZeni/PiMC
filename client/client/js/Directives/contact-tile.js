(function () {
  'use strict';
  angular

    .module('App.directives')
    /**
     * @class App.directives.contactTile
     */
    .directive('contactTile', function () {
      return {
        restrict: 'E',
        templateUrl: 'templates/app/partials/contact-tile.html',
        replace: true
      };
    });
})();
