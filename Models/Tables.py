from Utils.db import db


class Estado(db.Model):
    __tablename__ = "Estado"
    c_estado = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    D_estado = db.Column(db.String(100), nullable=False)


#    def c_dic(self):
#       diccionario = {}
#        for column in self.__table__.colums:
#            diccionario[column.name] = getattr(self, column.name)
#        return diccionario


class Municipio(db.Model):
    __tablename__ = "Municipio"
    c_mnpio = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    D_MNPIO = db.Column(db.String(100), nullable=False)
    c_cve_ciudad = db.Column(db.Integer, nullable=False)
    c_estado = db.Column(db.Integer, db.ForeignKey("Estado.c_estado"))


#    def c_dic(self):
#        diccionario = {}
#        for column in self.__table__.colums:
#            diccionario[column.name] = getattr(self, column.name)
#        return diccionario


class Colonia(db.Model):
    __tablename__ = "Colonia"
    id_asenta_cpcons = db.Column(
        db.Integer, primary_key=True, unique=True, nullable=False
    )
    d_codigo = db.Column(db.String(100), nullable=False)
    d_asenta = db.Column(db.String(100), nullable=False)
    d_zona = db.Column(db.String(100), nullable=False)
    d_ciudad = db.Column(db.Integer, nullable=False)
    c_tipo_asenta = db.Column(db.Integer, nullable=False)
    c_mnpio = db.Column(db.Integer, db.ForeignKey("Municipio.c_mnpio"))


#    def c_dic(self):
#        diccionario = {}
#        for column in self.__table__.colums:
#            diccionario[column.name] = getattr(self, column.name)
#        return diccionario
