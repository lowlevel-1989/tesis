(function(){
    angular.module('bookController', ['bookService'])

    .controller('bookController', [ 
    '$scope', 'bookFactory',
    function ($scope, bookFactory) {
        
        //Scrolling
        
        $scope.scrollVisible = false;
        var change = false;
        var books;
        $scope.scrollActive = function(arg){
            $scope.scrollVisible = true;
            bookFactory.next(arg).then(function(data){
                if (!change)
                    books = data;
                else
                    books = books.concat(data);
                change = true;
                $scope.books = books;                
                $scope.scrollVisible = false;
            });
        };

        //Scrolling


        //Search

            var search;

            $scope.search = function () {
                if (search !== $scope.data){
                    search = $scope.data;
                    change = false;
                    $scope.scrollActive(search);
                }
            };

        //Search
    }]);

})();
