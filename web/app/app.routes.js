(function(){
    
    angular.module('routes', ['ngRoute'])
  
    .config(['$routeProvider', '$locationProvider', function ($routeProvider, $locationProvider) {
        
        $routeProvider.when('/books', {
            templateUrl: '../templates/book/bookView.min.html',
            controller: 'bookController'
        })
        .when('/working', {
            template: ' Trabajando '
        })
        .otherwise({
            redirectTo: '/working'
        });
        
        $locationProvider.hashPrefix('!');

    }]);

})();