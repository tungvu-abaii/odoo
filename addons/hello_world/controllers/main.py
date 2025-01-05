from odoo import http

class HelloWorldController(http.Controller):
    @http.route('/hello_world', auth='public', website=True)
    def index(self, **kwargs):
        return http.request.render('hello_world.index', {})