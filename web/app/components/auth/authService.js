(function(){

    var auth = angular.module('authService', [])

    .factory('userService', ['$http', 'bibliotecaApi', function ($http, bibliotecaApi) {
        return {
            logIn: function(username, password) {
                return $http({
                    method: 'post',
                    url: bibliotecaApi.host+'auth/', 
                    data: {username: username, password: password}
                });
            }
        };
    }])
    
    .factory('authService', function() {
        var auth = {
            isAuthenticated: false
        };
        return auth;
    })


    .factory('tokenInterceptor', ['$q', '$window', '$location', 'authService',
    function ($q, $window, $location, authService) {
        return {
            request: function (config) {
                config.headers = config.headers || {};
                if ($window.sessionStorage.token) {
                    config.headers.Authorization = 'token ' + $window.sessionStorage.token;
                }
                return config;
            },
     
            requestError: function(rejection) {
                return $q.reject(rejection);
            },
     
            response: function (response) {
                if (response !== null && response.status == 200 && $window.sessionStorage.token && !authService.isAuthenticated)
                    authService.isAuthenticated = true;
                return response || $q.when(response);
            },
     
             // Revoke client authentication if 401 is received 
            responseError: function(rejection) {
                if (rejection !== null && rejection.status === 401 && ($window.sessionStorage.token || authService.isAuthenticated)) {
                    delete $window.sessionStorage.token;
                    delete $window.sessionStorage.isAuthenticated;
                    authService.isAuthenticated = false;
                    $location.path('/');
                }
     
                return $q.reject(rejection);
            }
        };
    }]);
    
})();