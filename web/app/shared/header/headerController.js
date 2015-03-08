(function(){
    angular.module('headerController', ['menuHeaderService'])

    .controller('headerController', [ '$scope', '$mdSidenav', 'menuHeaderFactory',
    function ($scope, $mdSidenav, menuHeaderFactory) {

        $scope.toggleRight = function() {
    		$mdSidenav('right').toggle();
  		};
  		

  		$scope.tabs = menuHeaderFactory.tabs;
  		console.log($scope.tabs);

    }]);

})();