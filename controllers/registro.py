def hay():
    set_cupo=db(db.cupo.id==1).select().first() 
    cupo1=set_cupo.cupo1    
  
    
    if (cupo1==0):
        redirect(URL(c='registro',f='curso_cerrado'))       
    else:
        redirect(URL(c='registro',f='form',args=[cupo1]))     
     
    return dict(cupo1=cupo1)
def form():
	cupo1=request.args[0] 
	cupo1=int(cupo1)
	form=SQLFORM.factory(
    Field('dni','integer',label='INGRESE SU DNI',requires=[IS_LENGTH(8,error_message='NO ES UN DNI VALIDO'),IS_UPPER(),IS_NOT_EMPTY(error_message='LLENE EL CAMPO'),IS_INT_IN_RANGE(9999900,99999999,error_message='NO ES UN DNI VALIDO')]),
    Field('fecha',requires=IS_IN_SET(["30-05-2019"],error_message='LLENE EL CAMPO'),label=" FECHA A ASISTIR",default="30-05-2019")
            )
	if form.accepts(request,session):
		response.flash = 'formulario aceptado'
       		redirect(URL(c='registro',f='validacion',args=[form.vars.dni,form.vars.fecha]))
    	elif form.errors:
        	response.flash = 'el formulario tiene errores'        
   	else:
        	response.flash = 'por favor complete el formulario' 

	return dict(form=form,cupo1=cupo1)
def validacion():
	dni=request.args[0]
    	fecha=request.args[1]
    	set_evento=db(db.evento.dni==dni).select() 
    	tiene=len(set_evento)
    	if tiene==0:
        #print"si"
        	redirect(URL(c='registro',f='formulario',args=[dni,fecha]))# redirecciona      

    	elif tiene!=0:
        	redirect(URL(c='registro',f='registrado',args=[dni]))

   

	return dict(fecha=fecha,dni=dni)
def formulario():
    dni=request.args[0]
    fecha=request.args[1]
    set_cupo=db(db.cupo.id==1).select().first()
    fecha1=set_cupo.cupo1
    fecha1=int(fecha1)
    form=SQLFORM.factory(
    	Field('apellido',label='APELLIDO ',requires=[IS_LENGTH(40), IS_UPPER(),IS_NOT_EMPTY(error_message='LLENE EL CAMPO')]),
    	Field('nombre',label='NOMBRE',requires=[IS_LENGTH(40), IS_UPPER(),IS_NOT_EMPTY(error_message='LLENE EL CAMPO')]),    	
    	Field('telefono',"integer",label='TELEFONO'),
    	Field('mail',label='E-MAIL',requires=[IS_EMAIL(error_message='INGRESE UN E-MAIL VALIDO'),IS_UPPER(),IS_NOT_EMPTY(error_message='LLENE EL CAMPO')]),
    	Field('dependencia',label='DEPENDENCIA POLICIAL',requires=[IS_LENGTH(80),IS_UPPER(),IS_NOT_EMPTY(error_message='LLENE EL CAMPO')]),    	
    	)
    if form.accepts(request,session):
    	resto=fecha1-1
    	set_cupo.update_record(cupo1=resto)
    	db.evento.insert(apellido=form.vars.apellido,nombre=form.vars.nombre,dni=dni,mail=form.vars.mail,fecha=fecha,telefono=form.vars.telefono,
                dependencia=form.vars.dependencia) 
    	redirect(URL(c='registro',f='aceptado',args=[dni,form.vars.nombre,form.vars.apellido,form.vars.mail,fecha]))
    elif form.errors:
        response.flash = 'el formulario tiene errores'        
    else:
        response.flash = 'por favor complete el formulario'        

    return dict(form=form)
def aceptado(): 
    dni=request.args[0]
    nom_ape=request.args[1]
    fecha=request.args[3]
  
   
    return dict(fecha=fecha)
def registrado():
    dni=request.args[0]
    set_evento=db(db.evento.dni==dni).select().first() 
    nom=set_evento.nombre
    ape=set_evento.apellido
    fecha=set_evento.fecha
    dependencia=set_evento.dependencia
    return dict(dni=dni,set_evento=set_evento,nom=nom,ape=ape,fecha=fecha,dependencia=dependencia)
def lleno():
    fecha=request.args[0]
    return dict(fecha=fecha)

def curso_cerrado():
    return dict()#
