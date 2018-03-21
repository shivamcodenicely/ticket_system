
                $(document).ready(function(){
                    alert('hi there');
                    $.ajax({
        url: '/ticket/adminload/',
        type: 'GET',
        dataType: 'json',
        success: function (contxt) {
            {
                console.log(contxt.ticket_list)
            }
         }

    });
});