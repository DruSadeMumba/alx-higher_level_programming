$(document).ready(() => {
  const languageCodeInput = $('#language_code');
  $('#btn_translate').click(() => {
    translateHello();
  });
  languageCodeInput.keyup((event) => {
    if (event.keyCode === 13) {
      translateHello();
    }
  });
  function translateHello() {
    const languageCode = languageCodeInput.val();
    $.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`, (data) => {
      $('#hello').text(data.hello);
    });
  }
});
