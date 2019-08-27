$(function(){

    a = setInterval(function(){
        $.ajax({
            type: "GET",
            url: '/relojes/getTime/0/',
            //data: JSON.stringify({'auditoria':idAuditoria , 'preguntas':misCambios}),
            contentType:'application/json;charset=UTF-8',    
        })
        .done(function(data) {
            console.log( "exito R1" );
            console.log(data);
            
            var horaFormat = "";
            var horaR1 = data.description.tiempo;
            horaFormat = horaR1.hora+":"+horaR1.mins+":"+horaR1.segs;
            document.getElementById('reloj1').innerHTML = horaFormat;

        })
        .fail(function(data) {
        console.log( "error" );
        console.log(data);
        });
    }, 1000);
    b = setInterval(function(){
        $.ajax({
            type: "GET",
            url: '/relojes/getTime/1/',
            //data: JSON.stringify({'auditoria':idAuditoria , 'preguntas':misCambios}),
            contentType:'application/json;charset=UTF-8',    
        })
        .done(function(data) {
            console.log( "exito R2" );
            console.log(data);
            
            var horaFormat = "";
            var horaR2 = data.description.tiempo;
            horaFormat = horaR2.hora+":"+horaR2.mins+":"+horaR2.segs;
            document.getElementById('reloj2').innerHTML = horaFormat;

        })
        .fail(function(data) {
        console.log( "error" );
        console.log(data);
        });
    }, 1000);
    c = setInterval(function(){
        $.ajax({
            type: "GET",
            url: '/relojes/getTime/2/',
            //data: JSON.stringify({'auditoria':idAuditoria , 'preguntas':misCambios}),
            contentType:'application/json;charset=UTF-8',    
        })
        .done(function(data) {
            console.log( "exito R3" );
            console.log(data);
            
            var horaFormat = "";
            var horaR3 = data.description.tiempo;
            horaFormat = horaR3.hora+":"+horaR3.mins+":"+horaR3.segs;
            document.getElementById('reloj3').innerHTML = horaFormat;

        })
        .fail(function(data) {
        console.log( "error" );
        console.log(data);
        });
    }, 1000);
    d = setInterval(function(){
        $.ajax({
            type: "GET",
            url: '/relojes/getTime/3/',
            //data: JSON.stringify({'auditoria':idAuditoria , 'preguntas':misCambios}),
            contentType:'application/json;charset=UTF-8',    
        })
        .done(function(data) {
            console.log( "exito R4" );
            console.log(data);
            
            var horaFormat = "";
            var horaR4 = data.description.tiempo;
            horaFormat = horaR4.hora+":"+horaR4.mins+":"+horaR4.segs;
            document.getElementById('reloj4').innerHTML = horaFormat;

        })
        .fail(function(data) {
        console.log( "error" );
        console.log(data);
        });
    }, 1000);
    /*b = setInterval(function(){

    })
    c = setInterval(function(){

    })
    d = setInterval(function(){

    })*/

});