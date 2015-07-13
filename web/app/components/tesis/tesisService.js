(function(){

    angular.module('tesisService', [])

        .factory('tesisFactory', ['$http', '$q', 'api', function ($http, $q, api){

            var paginador = api.url + 'thesis/';

            function next(arg, change){
                var page = paginador;
                var flag;
                var search = '';
                if(page === null && arg === undefined)
                    flag = true;

                if (change){
                    flag = false;
                    page   = api.url + 'thesis/';
                }

                var deferred = $q.defer();
                
                if (!flag){
                    if (arg){
                        search = arg;
                        page   = api.url + 'thesis/';
                    }else if (arg === '')
                        page   = api.url + 'thesis/';

                    var request = {
                        method: 'get',
                        url: page
                    };

                    if (search){
                        request.params = {
                            search: search
                        };
                    }

                    $http(request)

                    .success(function(data) {
                        paginador = data.next;
                        deferred.resolve(data);
                    });
                }

                return deferred.promise;
            }

            return {
                next: next
            };

        }]);
    
})();