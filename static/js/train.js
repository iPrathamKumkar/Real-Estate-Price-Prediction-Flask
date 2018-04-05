$(document).ready(function() {
    $('#train').click(function() {
        var temp = "Done"
    	$.ajax({
            type: 'GET',
            url: 'http://realestateprice.pythonanywhere.com/train',
        });
    });
});