(function(){
    
    angular.module('routes', ['ngRoute'])
  
    .config(['$routeProvider', '$locationProvider', function ($routeProvider, $locationProvider) {
        
        $routeProvider.when('/books', {
            templateUrl: '../templates/book/bookView.min.html',
            controller: 'bookController'
        })
        .when('/', {
            templateUrl: '../templates/home/homeView.min.html'
        })
        .otherwise({
            redirectTo: '/'
        });
        
        $locationProvider.hashPrefix('!');

    }]);

})();