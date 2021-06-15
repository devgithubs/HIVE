$(document).ready(function() {
  $('.datepicker').datepicker({
    format: 'dd mmmm,yyyy',
    yearRange: 3
});
  $(".btn-link").click(function(){
      $(".collapse").collapse('toggle');
    });
});

