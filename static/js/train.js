$(document).ready(function() {
  $('#train').click(function() {
    $('#model').show();
    var temp = "Done"
    $.ajax({
      type: 'GET',
      url: 'http://realestateprice.pythonanywhere.com/train',
    });
  });
});
