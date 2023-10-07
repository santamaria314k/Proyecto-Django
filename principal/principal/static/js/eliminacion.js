


function eliminar(id_val) {




    swal({
        title: "¡Eliminar un Registro!",
        text:       "¿Estas seguro?",
        icon: "warning",
        buttons: true,
        dangerMode: true,
      })
      .then((willDelete) => {
        if (willDelete) {
         window.location.href="eliminarvaloracion/"+id_val+"/";
        }

        if (willDelete) {
          window.location.href = '/HomeLoc/admin/listarvaloracion/';  
        } 


      });

    


}

function eliminaremplo(id_val) {




  swal({
      title: "¡Eliminar un Registro!",
      text:       "¿Estas seguro?",
      icon: "warning",
      buttons: true,
      dangerMode: true,
    })
    .then((willDelete) => {
      if (willDelete) {
       window.location.href="eliminarvaloracionemplo/"+id_val+"/";


      }
      
      if (willDelete) {
        window.location.href = '/HomeLoc/employee/listarvaloracionemplo/';  
      } 
    });

  


}