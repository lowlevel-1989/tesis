(function(){
    angular.module('headerDirective', ['headerController'])

    .directive('blHeader', function () {
        return {
            restrict: 'E',
            templateUrl: '../templates/header/base/headerView.min.html',
            controller: 'headerController'
        };
    });

})();