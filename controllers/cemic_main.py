from odoo import http
from odoo.http import request

class HelloWorldController(http.Controller):

    @http.route('/hello', type='http', auth='public', website=True)
    def hello_page(self, **kwargs):
        return request.render('cemic_website_portal.hello_template', {
            'visitor_name': request.env.user.name if request.env.user.id else 'Visitante'
        })
