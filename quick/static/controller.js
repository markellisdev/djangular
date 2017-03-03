app.controller('MainController', function($scope, $http, $location) {

  $scope.user = {
    username: "guest12",
    password: "12345",
    email: "steve@steve.com",
    first_name: "Steve",
    last_name: "Brownlee"
  };

  $scope.register = function() {
      $http({
        url: "/register",
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded"
        },
        data: {
          "username": $scope.user.username,
          "password": $scope.user.password,
          "email": $scope.user.email,
          "first_name": $scope.user.first_name,
          "last_name": $scope.user.last_name
        }
      }).then(res => {
        if (res.data.success === true) {
            $location.path('/hello');
        } else {
            // Show dialog element telling user that registration failed
        }
      });
  };


  $scope.login = function() {
      $http({
        url: "/login",
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded"
        },
        data: {
          "username": $scope.user.username,
          "password": $scope.user.password
        }
      }).then(res => {
        if (res.data.success === true) {
            console.log(res)
            $location.path('/hello');
        } else {
            // Show dialog element telling user that registration failed
        }
      });
  };

});