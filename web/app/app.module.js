(function(){

    var _APP = 'BibliotecaVirtual';

    var _API = 'http://www.ujgh.edu.ve:8000/';

    var _SERVICES = [   
            
    ];

    var _CONTROLLERS = [
            'bookController',
            'homeController',
            'tesisController',
            'otrosController'
    ];

    var _DIRECTIVES = [
            'headerDirective',
            'sidenavRightDirective'
    ];

    var _THIRD_PARTY_APPS = [
            'ngMaterial',
            'infinite-scroll'
    ]; 


    var _DEPENDENCIES = _SERVICES.concat(_CONTROLLERS); 
        _DEPENDENCIES = _DEPENDENCIES.concat(_DIRECTIVES);
        _DEPENDENCIES = _DEPENDENCIES.concat(_THIRD_PARTY_APPS);
        _DEPENDENCIES = _DEPENDENCIES.concat(['routes']);


    angular.module(_APP, _DEPENDENCIES)
    
    .factory('api', function() {
        return {
            url: _API
        };
    })

    .controller('Controller', ['$scope', function ($scope) {
        $scope.loading = true;
    }]);

})();
