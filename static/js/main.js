const btnDelete = document.querySelectorAll('.btn-delete');

if (btnDelete.length > 0) { // Mejora: Verificar si hay elementos encontrados
    const btnArray = Array.from(btnDelete);
    btnArray.forEach((btn) => {
        btn.addEventListener('click', (e) => {
            if (!confirm('¿Estás seguro de que quieres eliminar el contacto?')) {
                e.preventDefault();
            }
        });
    });
}
