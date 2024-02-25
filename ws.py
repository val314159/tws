from bottle import *
def render_file(path):
    from pypugjs import process
    with open(path) as f:
        s = ''.join(f.readlines())
    return [ process(s), '\n' ]
class Bottle(Bottle):
    import os
    @property
    def roles(_): return list(os.walk('roles'))[0][1]
    def render_file(_, path):
        for role in _.roles:
            try:
                return render_file(role+path)
            except FileNotFoundError:
                pass
        raise HTTPError(404)
    def static_file(_, path):
        for role in _.roles:
            try:
                return static_file(role+path, '.')
            except HTTPError:
                pass
            pass
        raise HTTPError(404)
    pass
app = default_app.push(Bottle())
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
    return     app.static_file(branch)
if __name__=='__main__': run()
