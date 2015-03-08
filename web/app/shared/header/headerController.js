(function(){
    angular.module('headerController', ['menuHeaderDirective'])

    .controller('headerController', [ '$scope', '$mdSidenav', 
    function ($scope, $mdSidenav) {

        $scope.toggleRight = function() {
            $mdSidenav('right').toggle();
        };

        console.log(1);

    }]);

})();