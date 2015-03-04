(function(){
    
    angular.module('routes', ['ngRoute'])
  
    .config(['$routeProvider', '$locationProvider', function ($routeProvider, $locationProvider) {
        
        $routeProvider.when('/books', {
            templateUrl: '../templates/books/booksView.min.html',
            controller: ''
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