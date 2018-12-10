function validacion(opcion){
     if(opcion=="comprar"){
      var id_moneda_a_comprar = $("#id_moneda_a_comprar").val();
      var id_cantidad = $("#id_cantidad").val();
      var id_pagara_con = $("#id_pagara_con").val();

      if(id_moneda_a_comprar == "" || id_cantidad == "" || id_pagara_con == ""){
        alert("Existen campos no rellenados. Es necesario rellenar todos los campos.");
      }

      else if(id_moneda_a_comprar == id_pagara_con && !(id_moneda_a_comprar == "" || id_cantidad == "" || id_pagara_con == "") ){
        alert("La moneda a comprar debe ser distinta a la moneda con la que se debe pagar.");
       }

      else if(isNaN(id_cantidad)){
        alert("La cantidad ingresada debe ser un numero.");
      }

      else if(id_cantidad<=0){
        alert("La cantidad ingresada debe ser mayor a cero.");
      }
      else{
        $("#boton_comprar").click();
      }

     }

    if(opcion=="vender"){
      var id_moneda_a_vender = $("#id_moneda_a_vender").val();
      var id_cantidad = $("#id_cantidad").val();
      var id_desea_recibir = $("#id_desea_recibir").val();

      if(id_moneda_a_vender == "" || id_cantidad == "" || id_desea_recibir == ""){
        alert("Existen campos no rellenados. Es necesario rellenar todos los campos.");
      }

      else if(id_moneda_a_vender == id_desea_recibir && !(id_moneda_a_vender == "" || id_cantidad == "" || id_desea_recibir == "") ){
        alert("La moneda a vender debe ser distinta a la moneda que se desea recibir.");
      }

      else if(isNaN(id_cantidad)){
        alert("La cantidad ingresada debe ser un numero.");
      }

      else if(id_cantidad<=0){
        alert("La cantidad ingresada debe ser mayor a cero.");
      }

      else{
        $("#boton_vender").click();
      }
     }
    }