(function(){

    var _APP = 'BibliotecaVirtual';

    var _API = 'http://formatcomtesis.com.ve/api/';

    var _SERVICES = [   
            
    ];

    var _CONTROLLERS = [
            'bookController',
            'homeController'
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
