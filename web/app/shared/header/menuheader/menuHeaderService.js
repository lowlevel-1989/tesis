(function(){

    angular.module('menuHeaderService', [])

        .factory('menuHeaderFactory', ['$location', function ($location){

            tabs=[
                {
                    'title': 'INICIO',
                    'url': '/home'
                },
                {
                    'title':'LIBROS',
                    'url': '/books'
                },
                {
                    'title':'TESIS',
                    'url': '/tesis'
                },
                {
                    'title':'LEYES',
                    'url': '/leyes'
                },
                {
                    'title':'REVISTAS',
                    'url': '/revistas'
                }
            ];


            var currentTab = $location.path();

            function onClickTab(url) {
                currentTab = url;
            }

            function isActiveTab(url) {
                return url == currentTab;
            }

            return {
                tabs: tabs,
                onClickTab: onClickTab,
                isActiveTab: isActiveTab

            };

        }]);
    
})();