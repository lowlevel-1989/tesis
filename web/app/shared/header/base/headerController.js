(function(){
    angular.module('headerController', ['menuHeaderDirective'])

    .controller('headerController', [ '$scope', '$mdSidenav', 'menuHeaderFactory',
    function ($scope, $mdSidenav, menuHeaderFactory) {

        $scope.toggleRight = function() {
            $mdSidenav('right').toggle();
        };

        $scope.close = function() {
            $mdSidenav('right').close();
        };

        $scope.isActiveTab = menuHeaderFactory.isActiveTab;
        

    }]);

})();