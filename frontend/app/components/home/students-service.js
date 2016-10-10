function StudentsService($resource) {
  var that = this;
  that.StudentsResource = $resource(_urlPrefixes.API + "students/:id/", {id:"@id"});

  that.getStudents = function(params) {
    return that.StudentsResource.query(params).$promise;
  };

  that.getStudentDetail = function(params) {
    return that.StudentsResource.get(params).$promise;
  };
}

angular.module("Home")
  .service("StudentsService", ["$resource", StudentsService]);