(function(){
    var auth = angular.module('authController', [])

    .controller('authController', [ 
    '$scope', '$http', '$location', '$window', 'userService', 'authService',
    function ($scope, $http, $location, $window, userService, authService) {
        $scope.logIn = function (username, password) {
            if (username !== undefined && password !== undefined) {
                userService.logIn(username, password).success(function(data) {
                    authService.isAuthenticated  = true;
                    $window.sessionStorage.isAuthenticated = true;
                    $window.sessionStorage.token           = data.token;
                    $location.path('/home');
                    console.log(data);
                }).error(function(status, data) {
                    $scope.error = true;
                    console.log('error');
                    console.log(data);
                });
            }
        };

       $scope.logOut = function (){
            if (authService.isAuthenticated) {
                authService.isAuthenticated = false;
                delete $window.sessionStorage.isAuthenticated;
                delete $window.sessionStorage.token;
                $location.path('/');
            }
        };
    }]);

})();