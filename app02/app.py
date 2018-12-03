import web
        
urls = (
    '/', 'Index',
    '/acercade', 'Acercade',
)

render = web.template.render('templates/')

class Index:        
    def GET(self):
        return render.index()

class Acercade:
    def GET(self):
        return render.acercade()

if __name__ == "__main__":
    web.config.debug = False
    app = web.application(urls, globals())
    app.run()
