

$(function(){
    var a = "";
    var b = "";
    var c = "";
    var d = "";
    
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

            if( horaR2.hora < 10){
                horaR2.hora = "0"+horaR2.hora;
            }
            if( horaR2.mins < 10){
                horaR2.mins = "0"+horaR2.mins;
            }
            if( horaR2.segs < 10){
                horaR2.segs = "0"+horaR2.segs;
            }

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

            horaR3.hora = horaR3.hora < 10 ? "0"+horaR3.hora : horaR3.hora;
            horaR3.mins = horaR3.mins < 10 ? "0"+horaR3.mins : horaR3.mins;
            horaR3.segs = horaR3.segs < 10 ? "0"+horaR3.segs : horaR3.segs;
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
            horaR4.hora = horaR4.hora < 10 ? "0"+horaR4.hora : horaR4.hora;
            horaR4.mins = horaR4.mins < 10 ? "0"+horaR4.mins : horaR4.mins;
            horaR4.segs = horaR4.segs < 10 ? "0"+horaR4.segs : horaR4.segs;
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
            text: 'Se supone que interrumpió a',
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
            $.ajax({
                type: "GET",
                url: `/relojes/edit/${0}/${tiempo[0]}/${tiempo[1]}`,
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
                url: `/relojes/edit/${1}/${tiempo[0]}/${tiempo[1]}`,
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
                url: `/relojes/edit/${2}/${tiempo[0]}/${tiempo[1]}`,
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
                        var horaR3 = data.description.tiempo;
                        horaR3.hora = horaR3.hora < 10 ? "0"+horaR3.hora : horaR3.hora;
                        horaR3.mins = horaR3.mins < 10 ? "0"+horaR3.mins : horaR3.mins;
                        horaR3.segs = horaR3.segs < 10 ? "0"+horaR3.segs : horaR3.segs;
                        horaFormat = horaR3.hora+":"+horaR3.mins+":"+horaR3.segs;
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
                url: `/relojes/edit/${3}/${tiempo[0]}/${tiempo[1]}`,
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
                        var horaR4 = data.description.tiempo;
                        horaR4.hora = horaR4.hora < 10 ? "0"+horaR4.hora : horaR4.hora;
                        horaR4.mins = horaR4.mins < 10 ? "0"+horaR4.mins : horaR4.mins;
                        horaR4.segs = horaR4.segs < 10 ? "0"+horaR4.segs : horaR4.segs;
                        horaFormat = horaR4.hora+":"+horaR4.mins+":"+horaR4.segs;
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

/////////////////////
function add1(){
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      console.log("ACELERA");
      console.log(this.responseText);
    }
  };
  xhttp.open("GET", "/relojes/0/A", true);
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
  xhttp.open("GET", "/relojes/0/D", true);
  xhttp.send();
}

////////////////////

function add2(){
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      console.log("ACELERA");
      console.log(this.responseText);
    }
  };
  xhttp.open("GET", "/relojes/1/A", true);
  xhttp.send();
}

function sub2(){
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      console.log("DESACELERA");
      console.log(this.responseText);
    }
  };
  xhttp.open("GET", "/relojes/1/D", true);
  xhttp.send();
}

////////////////

function add3(){
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      console.log("ACELERA");
      console.log(this.responseText);
    }
  };
  xhttp.open("GET", "/relojes/2/A", true);
  xhttp.send();
}

function sub3(){
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      console.log("DESACELERA");
      console.log(this.responseText);
    }
  };
  xhttp.open("GET", "/relojes/2/D", true);
  xhttp.send();
}
////////////////////

function add4(){
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      console.log("ACELERA");
      console.log(this.responseText);
    }
  };
  xhttp.open("GET", "/relojes/3/A", true);
  xhttp.send();
}

function sub4(){
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      console.log("DESACELERA");
      console.log(this.responseText);
    }
  };
  xhttp.open("GET", "/relojes/3/D", true);
  xhttp.send();
}

