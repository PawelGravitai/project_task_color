# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProjectTask(models.Model):
     _inherit = "project.task"

color = fields.Integer()