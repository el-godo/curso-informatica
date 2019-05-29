def form():

	return dict()
def consulta():
	Fields=db.evento.apellido,db.evento.nombre,db.evento.dni,db.evento.dependencia
	set_evento=db(db.evento)
	grid=SQLFORM.grid(set_evento,fields=Fields,csv=False,paginate=20,deletable=False,editable=True,searchable=True,search_widget='default',create=False,)
	

	return dict(grid=grid)
