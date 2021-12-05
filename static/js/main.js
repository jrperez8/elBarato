const btnDelete = document.querySelectorAll('.btn-delete');
if(btnDelete) {
   const btnArray =  Array.from(btnDelete);
   btnArray.forEach((btn) =>{
       btn.addEventListener('click', (e) => {
        if (!confirm('Desea Eliminar este Elemento?')){
            e.preventDefault();
        }
       });
    });
}

function removeCliente(){    
    let opcion = confirm ('Desea Eliminar este Elemento?');
    if (opcion == false){
        alert ("Operación Cancelada");
        return false
    }else {
        alert ("Inmueble Retirado");
        return true;
    }   

}

function registroClientes(){   

    let id = document.getElementById("id").value;
    let name = document.getElementById("name").value;
    let status = document.getElementById("status").value;
    let mobile = document.getElementById("mobile").value;


    var expresion = /^[a-z][\w.-]+@\w[\w.-]+\.[\w.-]*[a-z][a-z]$/i;
    
    if( id == null || id.length == 0){
        alert ("El Campo ID debe ser diligenciado");
        return false;
    }
    else {
        if( name == null || name.length == 0 || /^\s+$/.test(name) ) {
            alert ("El Campo Nombre debe ser Diligenciado");
            return false;
          }
          else {
            if( status == null || status.length == 0 ) {
                alert ("El Campo Status debe ser Diligenciado");
                return false;
              }
              else {
                if( mobile == null || mobile.length == 0){
                    alert ("El Campo Movil debe ser diligenciado");
                    return false;
                }
                else{
                    return true;
                }
              }
          }
    }  
   
}

function prueba(){
    alert ("Prueba JS")
}