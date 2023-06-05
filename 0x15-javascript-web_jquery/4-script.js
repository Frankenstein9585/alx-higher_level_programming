// This script changes the header color to red
$(document).ready(function () {
  $('div#toggle_header').click(function () {
    $('header').toggleClass('red green');
  });
});
