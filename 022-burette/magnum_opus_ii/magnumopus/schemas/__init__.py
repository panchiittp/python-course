from typing import Dict
from flask_marshmallow import Marshmallow

ma = Marshmallow()

def init_app(app):
    ma.init_app(app)
    return [configure_injector]

def configure_injector(binder):
    from .substance_schema import SubstanceSchema

    binder.bind(
        SubstanceSchema, to=SubstanceSchema()
    )

    binder.multibind(
        Dict[str, SubstanceSchema], to={
            'one': SubstanceSchema(),
            'many': SubstanceSchema(many=True)
        }
    )
