import web
urls = (
'/', 'index'
)
class index:
    def GET(self):
        return "Welcome !!! Nguyen Manh Hung - 2175173"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
