from django.contrib.auth.models import Group

def navbar_context(request):
    """
    Determina qué navbar debe mostrarse según el tipo de usuario autenticado.
    """
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return {
                'navbar_template': 'layouts/navbar_logeado.html',
                'navbar_template_calendario': 'layouts/navbar_logeado_cal.html'
            }
        elif request.user.groups.filter(name="Administrador Dueño").exists():
            return {
                'navbar_template': 'layouts/navbar_logeado.html',
                'navbar_template_calendario': 'layouts/navbar_logeado_cal.html'
            }
        elif request.user.groups.filter(name="Vendedor").exists():
            return {
                'navbar_template': 'layouts/navbar_logeado.html',
                'navbar_template_calendario': 'layouts/navbar_logeado_cal.html'
            }
        else:
            return {
                'navbar_template': 'layouts/navbar_logeado.html',
                'navbar_template_calendario': 'layouts/navbar_logeado_cal.html'
            } 
    return {
            'navbar_template': 'layouts/navbar.html',
            'navbar_template_calendario': 'layouts/navbar_logeado_cal.html'
    } # Si el usuario no está autenticado, no carga nada
