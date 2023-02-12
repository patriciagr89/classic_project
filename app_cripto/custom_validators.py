from wtforms.validators import ValidationError
from app_cripto.models.models_DB import *

#aqui me he basado en la validacion EqualTo de la libreria de validaciones de wtforms para controlar que no se introduzcan dos monedas iguales
class NotEqualTo:

    def __init__(self, fieldname, message=None):
        self.fieldname = fieldname
        self.message = message

    def __call__(self, form, field):
        try:
            other = form[self.fieldname]
        except KeyError as exc:
            raise ValidationError(
                field.gettext("Invalid field name '%s'.") % self.fieldname
            ) from exc
        if field.data != other.data:
            return

        d = {
            "other_label": hasattr(other, "label")
            and other.label.text
            or self.fieldname,
            "other_name": self.fieldname,
        }
        message = self.message
        if message is None:
            message = field.gettext("Field must be equal to %(other_name)s.")

        raise ValidationError(message % d)