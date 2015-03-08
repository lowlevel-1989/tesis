(function(){

    angular.module('menuHeaderService', [])

        .factory('menuHeaderFactory', function (){

           tabs=[
                {
                    'title':'INICIO'
                },
                {
                    'title':'TESIS'
                },
                {
                    'title':'LIBROS'
                }
           ];

            return {
                tabs: tabs
            };

        });
    
})();