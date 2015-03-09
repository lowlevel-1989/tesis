(function(){

    angular.module('menuHeaderService', [])

        .factory('menuHeaderFactory', function (){

           tabs=[
                {
                    'title': 'INICIO',
                    'url': '#!/'
                },
                {
                    'title':'TESIS',
                    'url': '#!/tesis'
                },
                {
                    'title':'LIBROS',
                    'url': '#!/books'
                }
           ];

            return {
                tabs: tabs
            };

        });
    
})();