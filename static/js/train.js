$(document).ready(function() {
    $('#train').click(function() {
    	$.ajax({
            type: 'GET',
            url: '/train',
        });
    });
});