(function(){
    angular.module('bookController', ['bookService','bookIndividualDirective'])

    .controller('bookController', [ 
    '$scope', 'bookFactory', '$rootScope',
    function ($scope, bookFactory, $rootScope) {
        
        //BookSingle
        $scope.bookShow = false;

        $scope.showBookInfo = function(book){
           if ($scope.bookShow !== true){
                $scope.bookShow = true;
                $scope.bookShowInfo = book;
                console.log($scope.bookShow);
            }else{
                $scope.bookShow = false;
                console.log($scope.bookShow);
            }
        };

        $scope.showPrueba = function(){
           console.log('hola');
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
            console.log('inicia la funcion');
            if (!$scope.none){
                $scope.scrollVisible = true;
                var change = !$scope.change;
                bookFactory.next(arg, change).then(function(data){
                    console.log('entre');
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
                    $scope.change = false;
                    $scope.none   = false;
                    $scope.scrollActive(search);
                }
            };

        //Search
    }]);

})();
