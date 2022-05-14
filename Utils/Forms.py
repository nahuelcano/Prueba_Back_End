from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class EstadoF(FlaskForm):
    c_estado = IntegerField("codigo estado", validators=[DataRequired()])
    estado = StringField("estado", validators=[DataRequired()])
    submit = SubmitField("Agregar estado")


class MunicipioF(FlaskForm):
    c_mnpio = IntegerField("Codigo municipio", validators=[DataRequired()])
    D_MNPIO = StopIteration("Municipio", validators=[DataRequired()])
    c_cve_ciudad = IntegerField("Codigo Clave Ciudad", validators=[DataRequired()])
    c_estado = IntegerField("Codigo Estado", validators=[DataRequired()])
    submit = SubmitField("Agregar municipio")


class ColoniaF(FlaskForm):
    id_asenta_cpcons = IntegerField("Id asentamiento", validators=[DataRequired()])
    d_codigo = IntegerField("Codigo postal", validators=[DataRequired()])
    d_asenta = StringField("Tipo asentamiento", validators=[DataRequired()])
    d_zona = StringField("Descripcion zona", validators=[DataRequired()])
    d_ciudad = StringField("Colonia", validators=[DataRequired()])
    c_tipo_asenta = IntegerField(
        "Codigo tipo asentamiento", validators=[DataRequired()]
    )
    c_mnpio = IntegerField("Codigo municipio", validators=[DataRequired()])
    submit = SubmitField("Agregar colonia")
