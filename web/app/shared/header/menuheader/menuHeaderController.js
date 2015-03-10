(function(){
    angular.module('menuHeaderController', ['menuHeaderService'])

    .controller('menuHeaderController', ['$scope', '$mdSidenav', 'menuHeaderFactory', '$rootScope',
    function ($scope, $mdSidenav, menuHeaderFactory, $rootScope) {

        $scope.toggleRight = function() {
            $mdSidenav('right').toggle();
        };

        $scope.tabs = menuHeaderFactory.tabs;
        
        $scope.onClickTab = function(tab){
            menuHeaderFactory.onClickTab(tab);
            $rootScope.$emit('_change');
        };
        
        $scope.isActiveTab = menuHeaderFactory.isActiveTab;
    }]);

})();