from django.urls import path
from app.views import *
from app.scientist_views import *


app_name = 'app'

urlpatterns = [
    # app:index
    path('', index, name='index'),
    path('login_page/', login, name='login'),

    path('login_check/', login_check, name='login_check'),
    path('logout/', logout, name='logout'),

    # SCIENTIST URLS ----------------------------------------------------------------------

    #  create star
    path('create_star/', view_create_star, name='view_create_star'),
    path('pagina_erro/', view_create_star, name='pagina_erro'),
    path('pagina_sucesso/', view_create_star, name='pagina_sucesso'),

    # read star data
    path('read_star_data/', view_read_star_data, name='view_read_star_data'),
    path('pagina_erro/', view_read_star_data, name='pagina_erro'),
    path('pagina_sucesso/', view_read_star_data, name='pagina_sucesso'),

    # update star
    path('update_star/', view_update_star, name='view_update_star'),
    path('pagina_erro/', view_update_star, name='pagina_erro'),
    path('pagina_sucesso/', view_update_star, name='pagina_sucesso'),

    # delete star
    path('delete_star/', view_delete_star, name='view_delete_star'),
    path('pagina_erro/', view_delete_star, name='pagina_erro'),
    path('pagina_sucesso/', view_delete_star, name='pagina_sucesso'),

]
