from fastapi import HTTPException, status

from app.v1.schema import jurisdiccion_schema
from app.v1.schema import juicio_schema
from app.v1.schema import user_schema
from app.v1.model.user_model import User
from app.v1.model.jurisdiccion_model import Jurisdiccion
from app.v1.model.juicio_model import Juicio as JuicioModel
from app.v1.model.juicio_model import Juicio_Abogado as JuicioAbogado

def get_jurisdiccion(id: int):
    jurisdiccion = Jurisdiccion.get_by_id(id)

    if not jurisdiccion:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Jurisdicción no encontrada"
        )

    return jurisdiccion_schema.Jurisdiccion(
        id=id,
        provincia=jurisdiccion.provincia,
        sede=jurisdiccion.sede
    )

def add_abogados(juicio: juicio_schema.Juicio, abogados: list[int] | int):
    if type(abogados) is list:
        juicio.abogados = list()
        for abogado_id in abogados:
            db_user = User.get_by_id(abogado_id)
            if db_user:
                db_rel = JuicioAbogado(juicio_id=juicio.id, abogado_id=db_user.id)
                db_rel.save()
                juicio.abogados.append(user_schema.User(email=db_user.email,usuario=db_user.usuario, id=db_user.id, tipo=db_user.tipo))
            else:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Abogado inexistente"
                )
    else:
        db_user = User.get_by_id(abogados)
        if db_user:
            db_rel = JuicioAbogado(juicio_id=juicio.id, abogado_id=db_user.id)
            db_rel.save()
            juicio.abogados = user_schema.User(email=db_user.email,usuario=db_user.usuario, id=db_user.id, tipo=db_user.tipo)
        else:
            raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Abogado inexistente"
                )

    return juicio 

def create_juicio(juicio: juicio_schema.JuicioCreate):
    jurisdiccion = get_jurisdiccion(juicio.juris_id)
    
    db_juicio = JuicioModel(
        jurisdicion_id = jurisdiccion.id,
        caratula = juicio.caratula,
        nexpediente = juicio.nexpediente,
        materia = juicio.materia,
        estado_procesal = juicio.estado_procesal,
        situacion_tramite = juicio.situacion_tramite,
        tipo_reclamo = juicio.tipo_reclamo,
        siniestro = juicio.siniestro,
        poliza = juicio.poliza,
        suma_asegurada = juicio.suma_asegurada,
        monto_demanda = juicio.monto_demanda,
        fecha_hecho = juicio.fecha_hecho,
        fecha_notificacion = juicio.fecha_notificacion,
        fecha_contestacion = juicio.fecha_contestacion,
        fecha_mora = juicio.fecha_mora,
        hechos_demanda = juicio.hechos_demanda,
        hechos_contestacion = juicio.hechos_contestacion,
        evaluacion = juicio.evaluacion,
        transabilidad = juicio.transabilidad,
        defensas_opuestas = juicio.defensas_opuestas,
        observaciones = juicio.observaciones,
        informe_medico = juicio.informe_medico
    )

    db_juicio.save()

    return add_abogados(
        juicio_schema.Juicio(
        id = db_juicio.id,
        jurisdicion=jurisdiccion,
        abogados=[],
        caratula   = db_juicio.caratula,
        nexpediente = db_juicio.nexpediente,
        materia = db_juicio.materia,
        estado_procesal = db_juicio.estado_procesal,
        situacion_tramite = db_juicio.situacion_tramite,
        tipo_reclamo = db_juicio.tipo_reclamo,
        siniestro = db_juicio.siniestro,
        poliza = db_juicio.poliza,
        suma_asegurada = db_juicio.suma_asegurada,
        monto_demanda = db_juicio.monto_demanda,
        fecha_hecho = db_juicio.fecha_hecho,
        fecha_notificacion = db_juicio.fecha_notificacion,
        fecha_contestacion = db_juicio.fecha_contestacion,
        fecha_mora = db_juicio.fecha_mora,
        hechos_demanda = db_juicio.hechos_demanda,
        hechos_contestacion = db_juicio.hechos_contestacion,
        evaluacion = db_juicio.evaluacion,
        transabilidad = db_juicio.transabilidad,
        defensas_opuestas = db_juicio.defensas_opuestas,
        observaciones = db_juicio.observaciones,
        informe_medico = db_juicio.informe_medico
    ),
    juicio.abogados)

def get_juicios():
    """
    Próximo feature Juicios filtrados por usuario.
    def get_juicios(user: user_schema.User):
        juicio_by_user = (JuicioModel
                          .select()
                          .join(JuicioAbogado)
                          .join(User)
                          .where(User.id == user.id))
    
    Filtros opcionales
        - Por actor
        - Por demandado
        - Por nexpediente

    """
    
    juicios = JuicioAbogado.select(JuicioAbogado, User, JuicioModel).join(JuicioModel).switch(JuicioAbogado).join(User)
        
    juicios_list = []
    for db_juicio in juicios:
        if juicios_list == []:
            juicios_list.append(
                juicio_schema.Juicio(
                    id = db_juicio.juicio_id,
                    jurisdicion=get_jurisdiccion(db_juicio.juicio.jurisdicion_id),
                    abogados=[user_schema.User(email=db_juicio.abogado.email,usuario=db_juicio.abogado.usuario, id=db_juicio.abogado.id, tipo=db_juicio.abogado.tipo)],
                    caratula   = db_juicio.juicio.caratula,
                    nexpediente = db_juicio.juicio.nexpediente,
                    materia = db_juicio.juicio.materia,
                    estado_procesal = db_juicio.juicio.estado_procesal,
                    situacion_tramite = db_juicio.juicio.situacion_tramite,
                    tipo_reclamo = db_juicio.juicio.tipo_reclamo,
                    siniestro = db_juicio.juicio.siniestro,
                    poliza = db_juicio.juicio.poliza,
                    suma_asegurada = db_juicio.juicio.suma_asegurada,
                    monto_demanda = db_juicio.juicio.monto_demanda,
                    fecha_hecho = db_juicio.juicio.fecha_hecho,
                    fecha_notificacion = db_juicio.juicio.fecha_notificacion,
                    fecha_contestacion = db_juicio.juicio.fecha_contestacion,
                    fecha_mora = db_juicio.juicio.fecha_mora,
                    hechos_demanda = db_juicio.juicio.hechos_demanda,
                    hechos_contestacion = db_juicio.juicio.hechos_contestacion,
                    evaluacion = db_juicio.juicio.evaluacion,
                    transabilidad = db_juicio.juicio.transabilidad,
                    defensas_opuestas = db_juicio.juicio.defensas_opuestas,
                    observaciones = db_juicio.juicio.observaciones,
                    informe_medico = db_juicio.juicio.informe_medico
                )
            )
        else:
            if not any(d.id == db_juicio.juicio_id for d in juicios_list):
                juicios_list.append(
                    juicio_schema.Juicio(
                        id = db_juicio.juicio_id,
                        jurisdicion=get_jurisdiccion(db_juicio.juicio.jurisdicion_id),
                        abogados=[user_schema.User(email=db_juicio.abogado.email,usuario=db_juicio.abogado.usuario, id=db_juicio.abogado.id, tipo=db_juicio.abogado.tipo)],
                        caratula   = db_juicio.juicio.caratula,
                        nexpediente = db_juicio.juicio.nexpediente,
                        materia = db_juicio.juicio.materia,
                        estado_procesal = db_juicio.juicio.estado_procesal,
                        situacion_tramite = db_juicio.juicio.situacion_tramite,
                        tipo_reclamo = db_juicio.juicio.tipo_reclamo,
                        siniestro = db_juicio.juicio.siniestro,
                        poliza = db_juicio.juicio.poliza,
                        suma_asegurada = db_juicio.juicio.suma_asegurada,
                        monto_demanda = db_juicio.juicio.monto_demanda,
                        fecha_hecho = db_juicio.juicio.fecha_hecho,
                        fecha_notificacion = db_juicio.juicio.fecha_notificacion,
                        fecha_contestacion = db_juicio.juicio.fecha_contestacion,
                        fecha_mora = db_juicio.juicio.fecha_mora,
                        hechos_demanda = db_juicio.juicio.hechos_demanda,
                        hechos_contestacion = db_juicio.juicio.hechos_contestacion,
                        evaluacion = db_juicio.juicio.evaluacion,
                        transabilidad = db_juicio.juicio.transabilidad,
                        defensas_opuestas = db_juicio.juicio.defensas_opuestas,
                        observaciones = db_juicio.juicio.observaciones,
                        informe_medico = db_juicio.juicio.informe_medico
                    )
                )
            else:
                for d in juicios_list:
                    if d.id == db_juicio.juicio_id:
                        d.abogados.append(user_schema.User(email=db_juicio.abogado.email,usuario=db_juicio.abogado.usuario, id=db_juicio.abogado.id, tipo=db_juicio.abogado.tipo))
                        break
            
    return juicios_list