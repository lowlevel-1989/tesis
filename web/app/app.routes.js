(function(){
    
    angular.module('routes', ['ngRoute'])
  
    .config(['$routeProvider', '$locationProvider', function ($routeProvider, $locationProvider) {
        
        $routeProvider.when('/working', {
            template: ' Trabajando '
        })
        .otherwise({
            redirectTo: '/working'
        });
        
        $locationProvider.hashPrefix('!');

    }]);

})();