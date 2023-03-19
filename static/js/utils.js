$(document).ready(function () {
  $("#alertParameter").hide();
});

function showAlertError() {
  $("#alertParameter").css("visibility", "visible");
  $("#alertParameter")
    .fadeTo(2000, 500)
    .slideUp(500, function () {
      $("#alertParameter").slideUp(500);
    });
}
