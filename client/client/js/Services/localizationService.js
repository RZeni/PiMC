(function () {
  'use strict';
  angular

    .module('App.services')
    /**
     * @class App.services.localization
     */
    .factory('localization', localization);

  localization.$inject = [];

  function localization() {
    var dictionary = {
      'en': {
        BUTTONS: {
          BROADCASTS: "Broadcasts",
          FORGOT_PASSWORD:"Forgot Password?",
          FRIENDS: "Friends",
          HELP: "Help",
          SCHEDULE: "Schedule",
          SETTINGS: "Settings",
          SIGN_IN: "Sign In",
          SIGN_OUT: "Sign Out"
        },
        PERSON: {
          DOB: "Birth Date",
          EMAIL: "Email",
          FIRST_NAME: "First Name",
          LAST_NAME: "Last Name",
          SEX: "Sex",
        }
      }
    };

    return {
      getDictionary: function (lang) {
        return dictionary[lang];
      }
    }
  }
})();
