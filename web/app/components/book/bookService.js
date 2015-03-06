(function(){

    angular.module('bookService', [])

        .factory('bookFactory', ['$http', '$q', 'api', function ($http, $q, api){

            var paginador = api.url + 'books/';

            function next(){
                
                var page = paginador;
                
                if(page === null){
                    return;
                }

                var deferred = $q.defer();

                $http({
                    method: 'get',
                    url: page
                })

                .success(function(data) {
                    if (data.count !== 0)
                        paginador = data.next;
                    deferred.resolve(data.results);
                });

                return deferred.promise;
            }

            return {
                next: next
            };

        }]);
    
})();