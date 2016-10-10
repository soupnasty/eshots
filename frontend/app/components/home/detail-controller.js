function DetailController($routeParams, StudentsService) {
  var that = this;
  that.currentId = $routeParams.id;
  that.student = {};

  that.init = function() {
    return StudentsService.getStudentDetail({id: that.currentId}).then(function(student) {
      that.student = student;
    });
  };
}

angular.module("Home")
  .controller("DetailController", [
    "$routeParams",
    "StudentsService",
    DetailController
  ]);