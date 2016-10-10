function HomeController(StudentsService) {
  var that = this;
  that.students = [];

  that.init = function() {
    return StudentsService.getStudents().then(function(students) {
      that.students = students;
    });
  };

}

angular.module("Home")
  .controller("HomeController", [
    "StudentsService",
    HomeController
  ]);
