(function(){
    angular.module('menuHeaderController', ['menuHeaderService'])

    .controller('menuHeaderController', ['$scope', '$mdSidenav', 'menuHeaderFactory', 
    function ($scope, $mdSidenav, menuHeaderFactory) {

        $scope.toggleRight = function() {
            $mdSidenav('right').toggle();
        };

        $scope.tabs = menuHeaderFactory.tabs;

    }]);

})();