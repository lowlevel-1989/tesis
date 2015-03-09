(function(){
    angular.module('headerController', ['menuHeaderDirective'])

    .controller('headerController', [ '$scope', '$mdSidenav', 
    function ($scope, $mdSidenav) {

        $scope.toggleRight = function() {
            $mdSidenav('right').toggle();
        };

        $scope.close = function() {
            $mdSidenav('right').close();
        };

    }]);

})();