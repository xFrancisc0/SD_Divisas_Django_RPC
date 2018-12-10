//Este es el metodo para validar si los datos de ingreso en las funcionalidades de compra y venta
//son validos.
function validacion(opcion){
     //Si se esta comprando alguna compra, se ejecutara este if
     if(opcion=="comprar"){
      //Se obtienen los valores de los 3 campos
      var id_moneda_a_comprar = $("#id_moneda_a_comprar").val();
      var id_cantidad = $("#id_cantidad").val();
      var id_pagara_con = $("#id_pagara_con").val();
      //Se valida que no sean nulos
      if(id_moneda_a_comprar == "" || id_cantidad == "" || id_pagara_con == ""){
        alert("Existen campos no rellenados. Es necesario rellenar todos los campos.");
      }
      //Se valida que la moneda a comprar no sea la misma con la que se paga
      else if(id_moneda_a_comprar == id_pagara_con && !(id_moneda_a_comprar == "" || id_cantidad == "" || id_pagara_con == "") ){
        alert("La moneda a comprar debe ser distinta a la moneda con la que se debe pagar.");
       }
      //Se valida que id_cantidad es numero
      else if(isNaN(id_cantidad)){
        alert("La cantidad ingresada debe ser un numero.");
      }
      //Se valida que id_cantidad no sea menor a 0
      else if(id_cantidad<=0){
        alert("La cantidad ingresada debe ser mayor a cero.");
      }
      //Si la validacion fue exitosa, se activa el boton de compra (el cual es
      //invisible )
      else{
        $("#boton_comprar").click();
      }
     }

    //Si se esta vendiendo alguna divisa, se ejecuta este if
    if(opcion=="vender"){
      //Se obtienen los valores de los 3 campos
      var id_moneda_a_vender = $("#id_moneda_a_vender").val();
      var id_cantidad = $("#id_cantidad").val();
      var id_desea_recibir = $("#id_desea_recibir").val();
      //Se valida que no sean nulos
      if(id_moneda_a_vender == "" || id_cantidad == "" || id_desea_recibir == ""){
        alert("Existen campos no rellenados. Es necesario rellenar todos los campos.");
      }
      //Se valida que la moneda a vender no sea la misma a la que se va a recibir
      else if(id_moneda_a_vender == id_desea_recibir && !(id_moneda_a_vender == "" || id_cantidad == "" || id_desea_recibir == "") ){
        alert("La moneda a vender debe ser distinta a la moneda que se desea recibir.");
      }
      //Se valida que id_cantidad es numero
      else if(isNaN(id_cantidad)){
        alert("La cantidad ingresada debe ser un numero.");
      }
      //Se valida que id_cantidad no sea menor a 0
      else if(id_cantidad<=0){
        alert("La cantidad ingresada debe ser mayor a cero.");
      }
      //Si la validacion fue exitosa, se activa el boton de venta (el cual es
      //invisible )
      else{
        $("#boton_vender").click();
      }
     }
    }