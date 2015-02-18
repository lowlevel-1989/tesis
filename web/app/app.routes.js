(function(){
    
    var routes = angular.module('biblioteca.routes', ['ngRoute'])
    
    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/working', {
            template: ' Trabajando ',
            access: { requiredLogin: false }
        })
        .when('/login', {
            templateUrl: 'app/components/auth/authView.html',
            controller: 'authController',
            access: { requiredLogin: false }
        })
        .when('/home', {
            template: 'ENTRE',
            access: { requiredLogin: true }
        })
        .otherwise({
            redirectTo: '/working'
        });
    }]);

})();