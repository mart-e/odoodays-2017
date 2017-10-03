# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class Plants(models.Model):
    _name = 'nursery.plant'

    name = fields.Char("Plant Name")
    price = fields.Float()
    order_ids = fields.One2many("nursery.order", "plant_id", string="Orders")
    order_count = fields.Integer(compute='_get_total_sold',
                                 store=True,
                                 string="Total sold")

    @api.depends('order_ids')
    def _get_total_sold(self):
        for plant in self:
            plant.order_count = len(plant.order_ids)
