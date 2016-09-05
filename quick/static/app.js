// Create main Angular module
var app = angular.module('YourApp', ['ngRoute'])

// Configure to use interpolation punctuation that differs from Django's
// and add the CSRF token when communicating via XHR with Django
angular.module('YourApp').config(
[
    '$interpolateProvider',
    '$httpProvider',
    '$routeProvider',
    function($interpolateProvider, $httpProvider, $routeProvider) {

      $interpolateProvider.startSymbol('((');
      $interpolateProvider.endSymbol('))');

      $httpProvider.defaults.xsrfCookieName = 'csrftoken';
      $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

      $routeProvider
        .when('/auth', {
          controller: 'MainController',
          templateUrl: '/static/auth.html'
        })
        .when('/hello', {
          controller: 'HelloController',
          templateUrl: '/static/hello.html'
        });
  }
]);
