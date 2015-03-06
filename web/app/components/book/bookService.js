(function(){

    angular.module('bookService', [])

        .factory('bookFactory', ['$http', '$q', 'api', function ($http, $q, api){

            var paginador = api.url + 'books/';

            function next(){
                
                var page = paginador;
                var flag;                


                if(page === null)
                    flag = true;

                var deferred = $q.defer();
                
                if (!flag){
                    $http({
                        method: 'get',
                        url: page
                    })

                    .success(function(data) {
                        paginador = data.next;
                        deferred.resolve(data.results);
                    });
                }

                return deferred.promise;
            }

            return {
                next: next
            };

        }]);
    
})();