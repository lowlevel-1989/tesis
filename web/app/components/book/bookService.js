(function(){

    angular.module('bookService', [])

        .factory('bookFactory', ['$http', '$q', 'api', function ($http, $q, api){

            var paginador = api.url + 'books/';

            function next(arg){
                var page = paginador;
                var flag;
                var search = '';

                if(page === null && arg === undefined)
                    flag = true;

                var deferred = $q.defer();
                
                if (!flag){
                    if (arg){
                        search = arg;
                        page   = api.url + 'books/';
                    }else if (arg === '')
                        page   = api.url + 'books/';

                    $http({
                        method: 'get',
                        url: page,
                        params: {
                            "search": search
                        }
                    })

                    .success(function(data) {
                        paginador = data.next;
                        console.log(data.results);
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