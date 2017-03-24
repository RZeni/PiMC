(function(){
  /**
   * @namespace App
   */
  angular.module('App', [
    'ionic',
    'ion-datetime-picker',
    'App.controllers',
    'App.services',
    'App.filters',
    'App.directives',
    'ui.select',
    'ionMDRipple'])

    .run(function($ionicPlatform,$state,$rootScope) {
      $rootScope.$state = $state;
      $ionicPlatform.ready(function() {

      });
    })

    .config(function($stateProvider, $urlRouterProvider) {
      // Ionic uses AngularUI Router which uses the concept of states
      // Learn more here: https://github.com/angular-ui/ui-router
      // Set up the various states which the app can be in.
      $stateProvider
        .state('main', {
          abstract: true,
          templateUrl: 'templates/layout.html',
          controller: 'layoutController'
        })

        .state('main.defaults', {
          url: '/defaults',
          templateUrl: 'templates/app/defaults.html',
          controller: 'defaultsController'
        })

        .state('main.broadcasts', {
          url: '/broadcasts',
          templateUrl: 'templates/app/broadcasts.html',
          controller: 'broadcastsController'
        })

        .state('main.help', {
          url: '/schedule',
          templateUrl: 'templates/app/help.html',
          controller: 'helpController'
        })

      // if none of the above states are matched, use this as the fallback
      $urlRouterProvider.otherwise('/defaults');

    })
    .constant("BASE", {
      "URL": "http://127.0.0.1",
      "PORT": "5000"
    })
    .constant("API_KEY", 'AIzaSyB8nFUM0XpNSvvNj3krCkSoi1m80bbN7kA');
})();
