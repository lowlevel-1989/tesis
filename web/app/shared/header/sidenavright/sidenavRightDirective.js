(function(){
    angular.module('sidenavRightDirective', [])

    .directive('blSidenavright', function () {
        return {
            restrict: 'E',
            templateUrl: '../templates/header/sidenavright/sidenavRightView.min.html'
        };
    });

})();