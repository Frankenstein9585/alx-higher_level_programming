// This script changes the header color to red
$(document).ready(function () {
  $.getJSON('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
    const translate = data.hello;
    $('div#hello').text(translate);
  });
});
