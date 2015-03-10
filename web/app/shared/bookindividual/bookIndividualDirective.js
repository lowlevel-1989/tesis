(function(){
    angular.module('bookIndividualDirective', [])

    .directive('blBookindividual', function () {
        return {
            restrict: 'E',
            templateUrl: '../templates/bookindividual/bookIndividualView.min.html',
            scope: {
                bookcontent: '=?'
            }
        };
    });

})();