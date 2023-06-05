// This script changes the header color to red
$(document).ready(function () {
  $.getJSON('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
	  const characterName = data.name;
	  $('div#character').text(characterName);
  });
});
