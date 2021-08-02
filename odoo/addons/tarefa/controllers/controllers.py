# -*- coding: utf-8 -*-
from odoo import http

class Tarefa(http.Controller):
    @http.route('/tarefa/tarefa/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/tarefa/tarefa/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('tarefa.listing', {
            'root': '/tarefa/tarefa',
            'objects': http.request.env['tarefa.tarefa'].search([]),
        })

    @http.route('/tarefa/tarefa/objects/<model("tarefa.tarefa"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('tarefa.object', {
            'object': obj
        })