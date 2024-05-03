$(document).ready(function () {
  const saluteurl = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  const gret = $('div#hello');

  function getgret () {
    return $.get({
      url: saluteurl,
      dataType: 'json'
    });
  }

  getgret().then(res) => {
    gret.text(es.hello);
  });
});
