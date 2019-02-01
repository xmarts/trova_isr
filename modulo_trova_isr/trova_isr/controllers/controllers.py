# -*- coding: utf-8 -*-
from odoo import http

# class TrovaIsr(http.Controller):
#     @http.route('/trova_isr/trova_isr/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/trova_isr/trova_isr/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('trova_isr.listing', {
#             'root': '/trova_isr/trova_isr',
#             'objects': http.request.env['trova_isr.trova_isr'].search([]),
#         })

#     @http.route('/trova_isr/trova_isr/objects/<model("trova_isr.trova_isr"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('trova_isr.object', {
#             'object': obj
#         })