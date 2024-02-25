from bottle import *
class Bottle(Bottle):
    import os
    @property
    def roles(_): return os.listdir('roles')
    def _render_file(_, path):
        from pypugjs import process
        with open(path) as f:
            s = ''.join(f.readlines())
        return [ process(s), '\n' ]
    def render_file(_, path):
        for role in _.roles:
            try: return _._render_file(role+path)
            except FileNotFoundError: pass
        raise HTTPError(404)
    def static_file(_, path):
        for role in _.roles:
            try: return static_file(role+path, '.')
            except HTTPError: pass
            pass
        raise HTTPError(404)
    pass
with Bottle() as app:
    default_headers = {
        'Cache-Control': 'no-store, must-revalidate',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
    }
    @app.hook('before_request')
    def handle_options():
        if request.method == 'OPTIONS':
            # Bypass request routing and immediately return a response
            raise HTTPResponse(headers=cors_headers)
        return
    @app.hook('after_request')
    def add_default_headers():
        for key, value in default_headers.items():
            response.set_header(key, value)
            pass
        return
    @app.get(r'/')
    @app.get(r'<branch:path>/')
    @app.get(r'<branch:path><leaf><ext:re:\.html>')
    def _(branch='/', leaf='index', ext='.html'):
        try:
            return app.render_file(branch+'/'+leaf+'.pug')
        except HTTPError:
            return app.static_file(branch+'/'+leaf+  ext )
    @app.get(r'<branch:path>')
    def _(branch):
        return app.static_file(branch)
    if __name__=='__main__': run()
