@auth.requires_login()
def imprimir():

	return dict()
def print_fecha1():
	
	import json
	

    	ordenar=db(db.evento.apellido).select()
	set_evento=db(db.evento.fecha=="30-05-2019").select(orderby=db.evento.apellido)
	evento=set_evento.first() 	

    	
    	
	return dict(set_evento=set_evento,evento=evento)

   	
    	

def todo():
	

    	ordenar=db(db.evento.apellido).select()
	set_evento=db(db.evento.fecha).select(orderby=db.evento.apellido)
	evento=set_evento.first() 
		

    	
    	
	return dict(set_evento=set_evento,evento=evento)

	