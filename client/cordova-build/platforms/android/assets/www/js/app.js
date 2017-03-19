(function(){
  /**
   * @namespace App
   */
  angular.module('App', [
    'ionic','ion-datetime-picker',
    'App.controllers',
    'App.services',
    'App.filters',
    'App.directives',
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

        .state('landing', {
          url: '/landing',
          templateUrl: 'templates/landing.html',
          controller: 'landingController'
        })

        .state('clientList', {
          url: '/clientList',
          templateUrl: 'templates/client_list.html',
          controller: 'clientListController'
        })

        .state('clientDetails', {
          url: '/clientList/:clientID',
          templateUrl: 'templates/client_details.html',
          controller: 'clientDetailsController'
        });

      // if none of the above states are matched, use this as the fallback
      $urlRouterProvider.otherwise('/landing');

    })
    .constant("BASE", {
      "URL": "http://127.0.0.1",
      "PORT": "8080"
    })
})();
