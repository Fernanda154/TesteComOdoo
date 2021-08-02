# -*- coding: utf-8 -*-

from odoo import models, fields, api

class tarefa(models.Model):
    _name = 'tarefa.tarefa'

    responsavel = fields.Char()
    description = fields.Text()

    @api.depends('description')
    def _tarefa_description(self):
        for record in self:
            record.description = "Record with description %s" % record.description