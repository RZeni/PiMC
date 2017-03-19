(function(){
  'use strict';
  angular
    .module('App.controllers')

    /**
     * @class App.controllers.layoutController
     */
    .controller('layoutController', layoutController);

  layoutController.$inject = ['$scope'];

  function layoutController($scope) {

    init();

    function init() {

    }
  }
})();
