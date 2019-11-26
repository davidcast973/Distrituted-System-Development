

$(function(){
    var a = "";
    
    a = setInterval(function(){
        $.ajax({
            type: "GET",
            url: '/numeros/getTime/0/',
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

    play = setInterval(function(){
        url_freqs = `/numeros/get-frequency-numbers/${0}`;
        $.ajax({
            type: "GET",
            url: url_freqs,
            //data: JSON.stringify({'auditoria':idAuditoria , 'preguntas':misCambios}),
            contentType:'application/json;charset=UTF-8',    
        })
        .done(function(data) {
            if(data.ok == true){
                var datos = data.description; // data.description;
                var index = 0;
                for(index=1; index <= 30; index++){
                    var idFormado = `n_${index}`;
                    try{
                        if( datos[index] != undefined){
                            document.getElementById( idFormado ).innerHTML = datos[index];
                        }
                        else{
                            document.getElementById( idFormado ).innerHTML = "-";
                        }
                    }catch(error){
                        //console.log("Hubo un error");
                        //console.log(error);
                    }
                }
            }else{
                console.log("Ocurrió un error:");
                console.log(data);
                console.log("---------------------------");
            }    
        })
        .fail(function(data) {
            console.log( "error" );
            console.log(data);
        });
    }, 1000);
    
    
    $("#edit1").click(function(){
        clearInterval(a);

        $.ajax({
            type: "GET",
            url: `/numeros/pausa/${0}/pausa`,
            //data: JSON.stringify({'auditoria':idAuditoria , 'preguntas':misCambios}),
            contentType:'application/json;charset=UTF-8',    
        });
        
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
            console.log(`/numeros/edit/${0}/${tiempo[0]}/${tiempo[1]}`);
            $.ajax({
                type: "POST",
                async: false,
                url: `/numeros/edit/${0}/${tiempo[0]}/${tiempo[1]}`,
                //data: JSON.stringify({'auditoria':idAuditoria , 'preguntas':misCambios}),
                contentType:'application/json;charset=UTF-8',    
            })
            .done(function(data) {
              console.log(data);
                $.ajax({
                    type: "GET",
                    async: false,
                    url: `/numeros/pausa/${0}/retoma`,
                    //data: JSON.stringify({'auditoria':idAuditoria , 'preguntas':misCambios}),
                    contentType:'application/json;charset=UTF-8',    
                });
                a = setInterval(function(){
                    $.ajax({
                        type: "GET",
                        url: '/numeros/getTime/0/',
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
                }, 200);
            })
            .fail(function(data) {
            console.log( "error" );
            console.log(data);
            });
          })
    });
    $("#send").click(function(){
        swal("Actualizando...", "Todo se está actualizando", "info");
        $.ajax({
            type: "POST",
            url: `/numeros/sendUpdate`,
            //data: JSON.stringify({'auditoria':idAuditoria , 'preguntas':misCambios}),
            contentType:'application/json;charset=UTF-8',    
        }).done(function(data){
            if(data.ok == true){
                console.log("Actualización terminada...");
                console.log(data);
                swal("Listo!", "Todo se actualizó...", "success");
                setTimeout(function () {
                    location.reload();
                }, 2000);
            }else{
                console.log("ERROR");
                console.log(data);
                console.log("------");
                swal("Oh!", "Ha ocurrido un error...", "error");
                /*setTimeout(function () {
                    location.reload();
                }, 2000);*/
            }
        });
    });

});



/////////////////////
function add1(){
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      console.log("ACELERA");
      console.log(this.responseText);
    }
  };
  xhttp.open("GET", "/numeros/0/A", true);
  xhttp.send();
}

function sub1(){
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      console.log("DESACELERA");
      console.log(this.responseText);
    }
  };
  xhttp.open("GET", "/numeros/0/D", true);
  xhttp.send();
}

////////////////////