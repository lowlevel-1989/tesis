(function(){
    angular.module('headerDirective', [])

    .directive('blHeader', function () {
        return {
            restrict: 'E',
            templateUrl: '../templates/header/headerView.min.html'
        };
    });

})();