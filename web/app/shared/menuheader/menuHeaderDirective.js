(function(){
    angular.module('menuHeaderDirective', [])

    .directive('blMenuheader', function () {
        return {
            restrict: 'E',
            templateUrl: '../templates/menuheader/menuHeaderView.min.html'
        };
    });

})();