#!/usr/bin/python3


from flask import Blueprint

# Create an instance of Blueprint with the URL prefix /api/v1
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Import everything from `api.v1.views.index` to avoid circular imports later
# PEP8 may flag this, but it's necessary to avoid circular import issues
from api.v1.views.index import *