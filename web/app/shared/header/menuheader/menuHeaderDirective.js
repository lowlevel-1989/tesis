(function(){
    angular.module('menuHeaderDirective', ['menuHeaderController'])

    .directive('blMenuheader', function () {
        return {
            restrict: 'E',
            templateUrl: '../templates/header/menuheader/menuHeaderView.min.html',
            controller: 'menuHeaderController'
        };
    });

})();