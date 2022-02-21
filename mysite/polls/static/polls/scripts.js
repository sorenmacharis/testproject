$(document).ready(function(){
    
    
    $.ajax({
        type: 'GET',
        url: 'http://sorenmacharis.eu.pythonanywhere.com/numberofpolls',
        dataType: 'text',
        success: function(res){
                  //answer of api call.
                  $("#numberofpolls").html(res);
                },
        error: function(error) {
            $("#numberofpolls").html("0");
        }
    });

    $.ajax({
        type: 'GET',
        url: 'http://sorenmacharis.eu.pythonanywhere.com/numberofvotes',
        dataType: 'text',
        success: function(res){
                  //answer of api call.
                  $("#numberofvotes").html(res);
                },
        error: function(error) {
            $("#numberofvotes").html("0");
        }
    });
      
        
    });
    