(function(){

    var _APP = 'BibliotecaVirtual';

    var _API = 'http://formatcomtesis.com.ve/api/';

    var _DESCRIPTION = 'Esta es la Biblioteca UJGH';

    var _SERVICES = [   
            
    ];

    var _CONTROLLERS = [
            'headerController', 
            'bookController' 
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

    .factory('PageTitle', function() {
        var title = 'Biblioteca Virtual';
        return {
            title: function() { return title; },
            setTitle: function(newTitle) { title = newTitle; }
        };
    })

    .factory('MetaInformation', function() {
        var metaDescription = _DESCRIPTION;
        return {
            metaDescription: function() { return metaDescription; },
            reset: function() {
                metaDescription = '';
            },
            setMetaDescription: function(newMetaDescription) {
                metaDescription = newMetaDescription;
            }
        };
    })

    .controller('Controller', ['$scope', 'PageTitle', 'MetaInformation', 
    function ($scope, PageTitle, MetaInformation) {
        $scope.PageTitle       = PageTitle;
        $scope.MetaInformation = MetaInformation;
    }]);

})();
