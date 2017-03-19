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
          PATIENT: "Patient",
          PRACTITIONER: "Practitioner"
        },
        LAB:{
          ATTENDING_PRACTITIONER: "Attending Practitioner",
          ADMITTING_PRACTITIONER: "Admitting Practitioner",
          CODE: "Code",
          DATE: "Date",
          PRACTITIONER: "Practitioner",
          REQUESTING_PRACTITIONER: "Requesting Practitioner",
          REQUESTING_ORGANIZATION: "Requesting Organization",
          ORGANIZATION: "Organization",
          TEST_PERFORMED:"Test Performed",
          TYPE:"Test Request",
          UNIT_OF_MEASURE: "Unit Of Measure",
          PATIENT: "Patient",
          RESULT: "Result",
          ACCEPTABLE_RANGE: "Acceptable Range"
        },
        LANDING:{
          PATIENT_DESC: "Query laboratory information for patients.",
          PRACTITIONER_DESC: "Query laboratory information for practitioners."
        },
        PATIENT: {
          DOB: "Birth Date",
          END: "Query End Date",
          FIRST_NAME: "First Name",
          LAST_NAME: "Last Name",
          SEX: "Sex",
          START: "Query Start Date"
        },
        PATIENT_LIST:{

        },
        PROVIDER:{
          FIRST_NAME: "First Name",
          LAST_NAME: "Last Name",
          REQUESTING_HIC: "Requesting HIC"
        },
        PROVIDER_QUERY:{

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
