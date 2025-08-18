//Esperar hasta que esté todo cargado para mostrarse

document.addEventListener('DOMContentLoaded', function() {

    const avisoCookies = document.getElementById('aviso-cookies')
    const aceptarCookiesBtn = document.getElementById('aceptar-cookies')
    const rechazarCookiesBtn = document.getElementById('rechazar-cookies')

    //Comprobar si se ha aceptado antes las cookies usando localStorage


    if (!localStorage.getItem('cookies_aceptadas')){
        avisoCookies.classList.add('activo');
    }

    //poner botones a escuchar

    aceptarCookiesBtn.addEventListener('click', function() {
        avisoCookies.classList.remove('activo');
        localStorage.setItem('cookies_aceptadas', 'true');
    });

        rechazarCookiesBtn.addEventListener('click', function() {
        avisoCookies.classList.remove('activo');
    });



    //menu hamburguesa nav

    const botonnav = document.getElementById('boton-nav');
    const navPrincipal = document.getElementById('nav-principal');

        //boton existe?
    if (botonnav && navPrincipal) {
        //esperar click 
        botonnav.addEventListener('click', function() {
            navPrincipal.classList.toggle('nav-visible');
            const esVisible = navPrincipal.classList.contains('nav-visible');
            botonnav.setAttribute('aria-expanded', esVisible)
        })
    }
});