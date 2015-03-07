(function(){

    angular.module('bookService', [])

        .factory('bookFactory', ['$http', '$q', 'api', function ($http, $q, api){

            var paginador = api.url + 'books/';

            function next(arg){
                
                var page = paginador;
                var flag;
                var search = '';

                if(page === null)
                    flag = true;

                var deferred = $q.defer();
                
                if (!flag){

                    if (arg)
                        search = arg;

                    $http({
                        method: 'get',
                        url: page,
                        params: {
                            "search": search
                        }
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