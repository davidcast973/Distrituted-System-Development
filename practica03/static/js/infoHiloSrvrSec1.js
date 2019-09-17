

$(function(){
    var a = "";
    
    a = setInterval(function(){
        $.ajax({
            type: "GET",
            url: '/relojes/getTime/0/',
            //data: JSON.stringify({'auditoria':idAuditoria , 'preguntas':misCambios}),
            contentType:'application/json;charset=UTF-8',    
        })
        .done(function(data) {
            //console.log( "exito R1" );
            //console.log(data);
            
            var horaFormat = "";
            var horaR1 = data.description.tiempo;
            if( horaR1.hora < 10){
                horaR1.hora = "0"+horaR1.hora;
            }
            if( horaR1.mins < 10){
                horaR1.mins = "0"+horaR1.mins;
            }
            if( horaR1.segs < 10){
                horaR1.segs = "0"+horaR1.segs;
            }
            horaFormat = horaR1.hora+":"+horaR1.mins+":"+horaR1.segs;
            document.getElementById('reloj1').innerHTML = horaFormat;

        })
        .fail(function(data) {
        console.log( "error" );
        console.log(data);
        });
    }, 500);
    
});