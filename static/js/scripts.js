$(document).ready(function() {
  $(".datepicker").datepicker({
    format: "dd-M-yyyy",
    yearRange: 3,
    showClearBtn: true,
    i18n: {
        done: "Select"
    }})
  $(".dropdown-toggle").dropdown();  
  $(".collapse").collapse('toggle');
});