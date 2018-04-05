$(document).ready(function() {
    $('#parking').on('input',function() {
        var o = {};
        var a = $('#customer_form').serializeArray();
        $.each(a, function() {
            if (o[this.name]) {
                if (!o[this.name].push) {
                    o[this.name] = [o[this.name]];
                }
                o[this.name].push(this.value || '');
            } else {
                o[this.name] = this.value || '';
            }
        });
        var data = o;
        temp = Number(data.Carpet_Area);
        data.Carpet_Area = temp;
        temp = Number(data.Floor_Number);
        data.Floor_Number = temp;
        temp = Number(data.Parking);
        data.Parking = temp;
        temp = Number(data.Furnishing);
        data.Furnishing = temp;
        temp = Number(data.Bathrooms);
        data.Bathrooms = temp;
        temp = Number(data.Bedrooms);
        data.Bedrooms = temp;
        var param = JSON.stringify(data);
        var param1 = "["+param+"]";
        console.log(param1);
        $.ajax({
            type: 'POST',
            url: 'http://realestateprice.pythonanywhere.com/',
            dataType: 'json',
            data: param1,
            contentType : 'application/json'
        });
    });
});