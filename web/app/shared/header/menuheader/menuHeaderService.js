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

            var currentTab = tabs[0].url;

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

        });
    
})();