const hdfiles = $('header');
const divrdhd = $('DIV#toggle_header');

divrdhd.on('click', () => {
  const cclass = hdfiles.attr('class');

  if (cclass === 'green' {
    hdfiles.toggleClass('${cclass} red');
  }
  if (cclass === 'red') {
    hdfiles.toggleClass('${cclass} green');
  }
});
