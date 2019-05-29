@auth.requires_membership('Administrador')
def cupo():
	
	set_cupo=db(db.cupo).select().first()
	
	fecha1=set_cupo.cupo1
	
	
	form=SQLFORM.factory(
		Field('cupo1','integer',label='DEFINIR EL CUPO'),
		
			)
	if form.accepts(request,session):
				

				set_cupo.update_record(cupo1=form.vars.cupo1)
				
				redirect(URL(c='cupo',f='aceptado',args=[form.vars.cupo1]))

    				response.flash = 'formulario aceptado'
	elif form.errors:
        		response.flash = 'el formulario tiene errores'
    	else:
        		response.flash = 'por favor complete el formulario' 

	return dict(form=form,fecha1=fecha1)
def aceptado():
	cupo1=request.args[0]
	
	return dict(cupo1=cupo1)

