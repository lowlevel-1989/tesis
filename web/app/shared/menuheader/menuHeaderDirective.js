(function(){
    angular.module('menuHeaderDirective', ['menuHeaderController'])

    .directive('blMenuheader', function () {
        return {
            restrict: 'E',
            templateUrl: '../templates/menuheader/menuHeaderView.min.html',
            controller: 'menuHeaderController'
        };
    });

})();