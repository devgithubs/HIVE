$(document).ready(function() {
  $(".datepicker").datepicker({
    format: "dd-M-yyyy",
    yearRange: 3,
    showClearBtn: true,
    i18n: {
        done: "Select"
    }})
  $(".btn-link").click(function(){
      $(".collapse").collapse('toggle');
    });
});