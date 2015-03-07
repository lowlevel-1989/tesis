(function(){
    angular.module('bookController', ['bookService'])

    .controller('bookController', [ 
    '$scope', 'bookFactory',
    function ($scope, bookFactory) {
        

        //Scrolling
        
        $scope.scrollVisible = false;
        var change = false;
        var books;
        $scope.scrollActive = function(){
            $scope.scrollVisible = true;
            bookFactory.next().then(function(data){
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


    }]);

})();
