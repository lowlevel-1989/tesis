(function(){
    angular.module('sidenavRightDirective', [])

    .directive('blSidenavright', function () {
        return {
            restrict: 'E',
            templateUrl: '../templates/sidenavright/sidenavRightView.min.html'
        };
    });

})();