function routesConfig($routeProvider) {
  $routeProvider
    .when("/", {
      templateUrl: _urlPrefixes.TEMPLATES + "components/home/home.html",
      controller: "HomeController"
    })
    .when("/students/:id", {
      templateUrl: _urlPrefixes.TEMPLATES + "components/home/detail.html",
      controller: "DetailController"
    })
    .otherwise({
      templateUrl: _urlPrefixes.TEMPLATES + "404.html"
    });
}

routesConfig.$inject = ["$routeProvider"];

module.exports = routesConfig;