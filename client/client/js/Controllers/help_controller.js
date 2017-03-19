(function(){
  'use strict';
  angular
    .module('App.controllers')

    /**
     * @class App.controllers.helpController
     */
    .controller('helpController', helpController);

    helpController.$inject = ['$scope','$stateParams'];

    function helpController($scope, $stateParams) {

    }
})();
