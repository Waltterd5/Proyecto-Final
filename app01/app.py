import web
        
urls = (
    '/', 'hello',
    '/adios', 'bye',
    '/buenosdias', 'morning'
)
app = web.application(urls, globals())

class hello:        
    def GET(self):
        return 'Hello'

class bye:
    def GET(self):
        raise web.seeother('https://www.google.com')

class morning:
    def GET(self):
        return 'Buenos Dias'

if __name__ == "__main__":
    app.run()
