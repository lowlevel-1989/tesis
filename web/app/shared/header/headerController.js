(function(){
    angular.module('headerController', [])

    .controller('headerController', [ '$scope', '$mdSidenav', 
    function ($scope, $mdSidenav) {

        $scope.toggleRight = function() {
    		$mdSidenav('right').toggle();
  		};
  		
    }]);

})();