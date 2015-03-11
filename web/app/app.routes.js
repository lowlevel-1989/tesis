(function(){
    
    angular.module('routes', ['ngRoute'])
  
    .config(['$routeProvider', '$locationProvider', function ($routeProvider, $locationProvider) {
        
        $routeProvider.when('/books', {
            templateUrl: '../templates/book/bookView.min.html',
            controller: 'bookController'
        })
        .when('/tesis', {
            templateUrl: '../templates/tesis/tesisView.min.html',
            controller: 'tesisController'
        })
        .when('/leyes', {
            templateUrl: '../templates/leyes/leyesView.min.html',
            controller: 'leyesController'
        })
        .when('/revistas', {
            templateUrl: '../templates/revistas/revistasView.min.html',
            controller: 'revistasController'
        })
        .when('/home', {
            templateUrl: '../templates/home/homeView.min.html'
        })
        .otherwise({
            redirectTo: '/home'
        });
        
        $locationProvider.hashPrefix('!');

    }]);

})();