const hdfiles = $('header');
const dvrdhead = $('div#red_header');

dvrdhead.on('click', function () {
  hdfiles.addClass('red');
});
