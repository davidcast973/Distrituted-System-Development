var a = "";
var b = "";
var c = "";
var d = "";

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
            //console.log(data);
            
            var horaFormat = "";
            var horaR1 = data.description.tiempo;
            horaFormat = horaR1.hora+":"+horaR1.mins+":"+horaR1.segs;
            document.getElementById('reloj1').innerHTML = horaFormat;

        })
        .fail(function(data) {
        console.log( "error" );
        console.log(data);
        });
    }, 100);
    b = setInterval(function(){
        $.ajax({
            type: "GET",
            url: '/relojes/getTime/1/',
            //data: JSON.stringify({'auditoria':idAuditoria , 'preguntas':misCambios}),
            contentType:'application/json;charset=UTF-8',    
        })
        .done(function(data) {
            console.log( "exito R2" );
            //console.log(data);
            
            var horaFormat = "";
            var horaR2 = data.description.tiempo;
            horaFormat = horaR2.hora+":"+horaR2.mins+":"+horaR2.segs;
            document.getElementById('reloj2').innerHTML = horaFormat;

        })
        .fail(function(data) {
        console.log( "error" );
        console.log(data);
        });
    }, 100);
    c = setInterval(function(){
        $.ajax({
            type: "GET",
            url: '/relojes/getTime/2/',
            //data: JSON.stringify({'auditoria':idAuditoria , 'preguntas':misCambios}),
            contentType:'application/json;charset=UTF-8',    
        })
        .done(function(data) {
            console.log( "exito R3" );
            //console.log(data);
            
            var horaFormat = "";
            var horaR3 = data.description.tiempo;
            horaFormat = horaR3.hora+":"+horaR3.mins+":"+horaR3.segs;
            document.getElementById('reloj3').innerHTML = horaFormat;

        })
        .fail(function(data) {
        console.log( "error" );
        console.log(data);
        });
    }, 100);
    d = setInterval(function(){
        $.ajax({
            type: "GET",
            url: '/relojes/getTime/3/',
            //data: JSON.stringify({'auditoria':idAuditoria , 'preguntas':misCambios}),
            contentType:'application/json;charset=UTF-8',    
        })
        .done(function(data) {
            console.log( "exito R4" );
            //console.log(data);
            
            var horaFormat = "";
            var horaR4 = data.description.tiempo;
            horaFormat = horaR4.hora+":"+horaR4.mins+":"+horaR4.segs;
            document.getElementById('reloj4').innerHTML = horaFormat;

        })
        .fail(function(data) {
        console.log( "error" );
        console.log(data);
        });
    }, 100);


    $("#edit1").click(function(){
        clearInterval(a);
        swal({
            text: 'Dame la nueva hora en formato HH:MM:SS',
            content: "input",
            button: {
              text: "Editar!",
              closeModal: true,
            },
          })
          .then(name => {
            if (!name) throw null;
            tiempo=name.split(":");
            $.ajax({
                type: "GET",
                url: `/relojes/edit/${0}/${tiempo[0]}/${tiempo[1]}/${tiempo[2]}`,
                //data: JSON.stringify({'auditoria':idAuditoria , 'preguntas':misCambios}),
                contentType:'application/json;charset=UTF-8',    
            })
            .done(function(data) {
                a = setInterval(function(){
                    $.ajax({
                        type: "GET",
                        url: '/relojes/getTime/0/',
                        //data: JSON.stringify({'auditoria':idAuditoria , 'preguntas':misCambios}),
                        contentType:'application/json;charset=UTF-8',    
                    })
                    .done(function(data) {
                        console.log( "exito R1" );
                        //console.log(data);
                        
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
            })
            .fail(function(data) {
            console.log( "error" );
            console.log(data);
            });
          })
    });
    $("#edit2").click(function(){
        clearInterval(b);
        swal({
            text: 'Dame la nueva hora en formato HH:MM:SS',
            content: "input",
            button: {
              text: "Editar!",
              closeModal: true,
            },
          })
          .then(name => {
            if (!name) throw null;
            tiempo=name.split(":");
            $.ajax({
                type: "GET",
                url: `/relojes/edit/${1}/${tiempo[0]}/${tiempo[1]}/${tiempo[2]}`,
                //data: JSON.stringify({'auditoria':idAuditoria , 'preguntas':misCambios}),
                contentType:'application/json;charset=UTF-8',    
            })
            .done(function(data) {
                a = setInterval(function(){
                    $.ajax({
                        type: "GET",
                        url: '/relojes/getTime/1/',
                        //data: JSON.stringify({'auditoria':idAuditoria , 'preguntas':misCambios}),
                        contentType:'application/json;charset=UTF-8',    
                    })
                    .done(function(data) {
                        console.log( "exito R2" );
                        //console.log(data);
                        
                        var horaFormat = "";
                        var horaR1 = data.description.tiempo;
                        horaFormat = horaR1.hora+":"+horaR1.mins+":"+horaR1.segs;
                        document.getElementById('reloj2').innerHTML = horaFormat;
            
                    })
                    .fail(function(data) {
                    console.log( "error" );
                    console.log(data);
                    });
                }, 1000);
            })
            .fail(function(data) {
            console.log( "error" );
            console.log(data);
            });
          })
    });

    $("#edit3").click(function(){
        clearInterval(c);
        swal({
            text: 'Dame la nueva hora en formato HH:MM:SS',
            content: "input",
            button: {
              text: "Editar!",
              closeModal: true,
            },
          })
          .then(name => {
            if (!name) throw null;
            tiempo=name.split(":");
            $.ajax({
                type: "GET",
                url: `/relojes/edit/${2}/${tiempo[0]}/${tiempo[1]}/${tiempo[2]}`,
                //data: JSON.stringify({'auditoria':idAuditoria , 'preguntas':misCambios}),
                contentType:'application/json;charset=UTF-8',    
            })
            .done(function(data) {
                c = setInterval(function(){
                    $.ajax({
                        type: "GET",
                        url: '/relojes/getTime/2/',
                        //data: JSON.stringify({'auditoria':idAuditoria , 'preguntas':misCambios}),
                        contentType:'application/json;charset=UTF-8',    
                    })
                    .done(function(data) {
                        console.log( "exito R3" );
                        //console.log(data);
                        
                        var horaFormat = "";
                        var horaR1 = data.description.tiempo;
                        horaFormat = horaR1.hora+":"+horaR1.mins+":"+horaR1.segs;
                        document.getElementById('reloj3').innerHTML = horaFormat;
            
                    })
                    .fail(function(data) {
                    console.log( "error" );
                    console.log(data);
                    });
                }, 1000);
            })
            .fail(function(data) {
            console.log( "error" );
            console.log(data);
            });
          })
    });
    $("#edit4").click(function(){
        clearInterval(d);
        swal({
            text: 'Dame la nueva hora en formato HH:MM:SS',
            content: "input",
            button: {
              text: "Editar!",
              closeModal: true,
            },
          })
          .then(name => {
            if (!name) throw null;
            tiempo=name.split(":");
            $.ajax({
                type: "GET",
                url: `/relojes/edit/${3}/${tiempo[0]}/${tiempo[1]}/${tiempo[2]}`,
                //data: JSON.stringify({'auditoria':idAuditoria , 'preguntas':misCambios}),
                contentType:'application/json;charset=UTF-8',    
            })
            .done(function(data) {
                d = setInterval(function(){
                    $.ajax({
                        type: "GET",
                        url: '/relojes/getTime/3/',
                        //data: JSON.stringify({'auditoria':idAuditoria , 'preguntas':misCambios}),
                        contentType:'application/json;charset=UTF-8',    
                    })
                    .done(function(data) {
                        console.log( "exito R4" );
                        //console.log(data);
                        
                        var horaFormat = "";
                        var horaR1 = data.description.tiempo;
                        horaFormat = horaR1.hora+":"+horaR1.mins+":"+horaR1.segs;
                        document.getElementById('reloj4').innerHTML = horaFormat;
            
                    })
                    .fail(function(data) {
                    console.log( "error" );
                    console.log(data);
                    });
                }, 1000);
            })
            .fail(function(data) {
            console.log( "error" );
            console.log(data);
            });
          })
    });

    /*b = setInterval(function(){

    })
    c = setInterval(function(){

    })
    d = setInterval(function(){

    })*/

});