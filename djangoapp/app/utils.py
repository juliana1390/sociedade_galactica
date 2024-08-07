from django.db import connection

# SCIENTIST FUNCTIONS ==================================================================

# create star ----------------------------------------------------------
def create_star(id_estrela, nome, classificacao, massa, x, y, z):
    cursor = connection.cursor()
    try:
        cursor.callproc('create_star', [id_estrela, nome, classificacao, massa, x, y, z])
        connection.commit()
        cursor.close()
    except Exception as e:
        raise e
    
# read star data ----------------------------------------------------------
def read_star_data(id_estrela):
    try:
        with connection.cursor() as cursor:
            # stored function call
            cursor.callproc('read_star_data', [id_estrela])
            
            # fetch all rows from cursor
            result = cursor.fetchall()
            
            return result
            
    except Exception as e:
        raise e
    
# update star ----------------------------------------------------------
def update_star(id_estrela, nome, classificacao, massa, x, y, z):
    cursor = connection.cursor()
    try:
        cursor.callproc('update_star', [id_estrela, nome, classificacao, massa, x, y, z])
        connection.commit()
        cursor.close()
    except Exception as e:
        raise e

# delete star ----------------------------------------------------------
def delete_star(id_estrela):
    cursor = connection.cursor()
    try:
        cursor.callproc('delete_star', [id_estrela]),
        connection.commit()
        cursor.close()
    except Exception as e:
        raise e