# -*- coding:utf-8 -*-

from flask import current_app, g, request


class FlaskReplicated(object):
    READONLY_METHODS = set(['GET', 'HEAD'])

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        assert hasattr(app, 'extensions')
        assert 'sqlalchemy' in app.extensions
        if 'replicated' not in app.extensions:
            app.extensions['replicated'] = self
            binds = app.config.get('SQLALCHEMY_BINDS') or {}
            if 'slave' in binds:
                app.before_request(self._pick_database_replica)
                db = app.extensions['sqlalchemy'].db
                get_engine_vanilla = db.get_engine

                def get_replicated_engine(app=app, bind=None):
                    if bind is None:
                        use_slave = getattr(g, 'use_slave', False)
                        use_master = getattr(g, 'use_master', False)
                        if use_slave and not use_master:
                            bind = 'slave'
                    return get_engine_vanilla(app, bind)

                db.get_engine = get_replicated_engine

    def _pick_database_replica(self):
        func = current_app.view_functions.get(request.endpoint)
        if getattr(func, 'use_master_database', False):
            g.use_master = True
        g.use_slave = request.method in self.READONLY_METHODS


def changes_database(func):
    func.use_master_database = True
    return func
