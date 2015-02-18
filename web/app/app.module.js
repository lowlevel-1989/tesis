(function(){
	var app = angular.module('biblioteca', ['authService',
											'authController',
											'biblioteca.routes'])
	
	.factory('bibliotecaApi', function() {
		return {
			host: 'http://localhost:8000/api/'
		};
	})

	.config(['$httpProvider', function ($httpProvider) {
		$httpProvider.interceptors.push('tokenInterceptor');
	}])

	.run(['$rootScope', '$location', '$window', 'authService',
	function ($rootScope, $location, $window, authService) {
		authService.isAuthenticated = $window.sessionStorage.isAuthenticated;
		$rootScope.$on("$routeChangeStart", function (event, nextRoute, currentRoute) {
			try {
				if (($location.path() === '/' || $location.path() === '/login') && authService.isAuthenticated)
					$location.path('/home');
				if (nextRoute.access.requiredLogin && !authService.isAuthenticated)
					$location.path('/');
			}catch(err){
				console.log('Redirect: #/');
			}
		});
	}]);
})();
