(function(){
    angular.module('otrosController', ['otrosService'])

    .controller('otrosController', [ 
    '$scope', 'otrosFactory', '$rootScope',
    function ($scope, otrosFactory, $rootScope) {
    	//BookSingle
        $scope.bookShow = false;

        $scope.showBookInfo = function(book){
           if (!$scope.bookShow){
                $scope.bookShow = true;
                $scope.bookShowInfo = book;
            }else
                $scope.bookShow = false;
        };
        //BookSingle

        $scope.cambio = function(){
        	otrosFactory.set($scope.select);
        	$scope.search();
        };

        //Scrolling

        $rootScope.$on('_change', function(event){ 
            $scope.change = false;
            $scope.none   = false;
        });

        $scope.scrollVisible = false;
        var books;
        $scope.scrollActive = function(arg){
            if (!$scope.none){
                $scope.scrollVisible = true;
                var change = !$scope.change;
                otrosFactory.next(arg, change).then(function(data){
                    if (!$scope.change)
                        books = data.results;
                    else
                        books = books.concat(data.results);
                    $scope.change = true;
                    $scope.books = books;                
                    $scope.scrollVisible = false;
                    if (data.next === null)
                        $scope.none = true;
                });
            }
        };

        //Scrolling


        //Search

            var search;

            $scope.search = function () {
                if (search !== $scope.data){
                    search = $scope.data;
                    $scope.bookShow = false;
                    $scope.change = false;
                    $scope.none   = false;
                    $scope.scrollActive(search);
                }
            };

        //Search
    }]);

})();
