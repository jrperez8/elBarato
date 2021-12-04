const btnDelete = document.querySelector('.btn-delete')

if(btnDelete) {
   const btnArray =  Array.from(btnDelete);
   btnArray.forEach((btn) =>{
       btn.addEventListener('click', (e) => {
        if (!confirm('Desea Eliminiar este Elemento?')){
            e.preventDefaul();
        }
       });
    });
}