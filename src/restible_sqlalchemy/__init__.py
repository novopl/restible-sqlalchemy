# -*- coding: utf-8 -*-
""" SQLAlchemy integration. """
from __future__ import absolute_import, unicode_literals

# package interface
from .resource import SqlAlchemyResource
from .util import db_query_from_params

__version__ = '0.2'
