(function(){

    angular.module('otrosService', [])

        .factory('otrosFactory', ['$http', '$q', 'api', function ($http, $q, api){

            var actual = 'magazines/';
            var paginador = api.url + actual;

            function set(tipe){
            	switch(tipe) {
				    case 'Folletos':
				    	actual = 'brochures/';
				        break;
				    case 'Leyes':
				    	actual = 'laws/';
				        break;
				    default:
				    	actual = 'magazines/';
				}
				paginador = api.url + actual;
            }

            function next(arg, change){
                var page = paginador;
                var flag;
                var search = '';
                if(page === null && arg === undefined)
                    flag = true;

                if (change){
                    flag = false;
                    page   = api.url + actual;
                }

                var deferred = $q.defer();
                
                if (!flag){
                    if (arg){
                        search = arg;
                        page   = api.url + actual;
                    }else if (arg === '')
                        page   = api.url + actual;

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
                next: next,
                set: set 
            };

        }]);
    
})();