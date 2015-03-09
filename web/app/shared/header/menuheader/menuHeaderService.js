(function(){

    angular.module('menuHeaderService', [])

        .factory('menuHeaderFactory', ['$location', function ($location){

            tabs=[
                {
                    'title': 'INICIO',
                    'url': '/home'
                },
                {
                    'title':'TESIS',
                    'url': '/tesis'
                },
                {
                    'title':'LIBROS',
                    'url': '/books'
                }
            ];

            var currentTab = $location.path();

            function onClickTab(tab) {
                currentTab = tab.url;
            }

            function isActiveTab(urlTab) {
                return urlTab == currentTab;
            }

            return {
                tabs: tabs,
                onClickTab: onClickTab,
                isActiveTab: isActiveTab

            };

        }]);
    
})();