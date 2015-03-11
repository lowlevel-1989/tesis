(function(){
    angular.module('tesisController', ['tesisService','bookIndividualDirective'])

    .controller('tesisController', [ 
    '$scope', 'tesisFactory', '$rootScope',
    function ($scope, tesisFactory, $rootScope) {
        
        //BookSingle
        $scope.bookShow = false;

        $scope.showBookInfo = function(book){
           if (!$scope.bookShow){
                $scope.bookShow = true;
                $scope.bookShowInfo = book;
                console.log($scope.bookShow);
            }else{
                $scope.bookShow = false;
                console.log($scope.bookShow);
            }
        };
        //BookSingle


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
                tesisFactory.next(arg, change).then(function(data){
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
