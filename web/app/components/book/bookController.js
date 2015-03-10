(function(){
    angular.module('bookController', ['bookService','bookIndividualDirective'])

    .controller('bookController', [ 
    '$scope', 'bookFactory',
    function ($scope, bookFactory) {
        
        //BookSingle
        $scope.bookShow = false;

        $scope.showBookInfo = function(book){
           $scope.bookShow = true;
           $scope.bookShowInfo = book;
        };
        //BookSingle

        //Scrolling
        
        $scope.scrollVisible = false;
        var change = false;
        var books;
        var none = false;
        $scope.scrollActive = function(arg){
            if (!none){
                $scope.scrollVisible = true;
                bookFactory.next(arg).then(function(data){
                    if (!change)
                        books = data.results;
                    else
                        books = books.concat(data.results);
                    change = true;
                    $scope.books = books;                
                    $scope.scrollVisible = false;
                    if (data.next === null)
                        none = true;
                });
            }
        };

        //Scrolling


        //Search

            var search;

            $scope.search = function () {
                if (search !== $scope.data){
                    search = $scope.data;
                    change = false;
                    none   = false;
                    $scope.scrollActive(search);
                }
            };

        //Search
    }]);

})();
