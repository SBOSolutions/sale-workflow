# Copyright 2018 Tecnativa - Carlos Dauden
# Copyright 2021 Tecnativa - Víctor Martínez
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    picking_note = fields.Text(string="Picking Internal Note")
    picking_customer_note = fields.Text(string="Picking Customer Comments")


class StockMove(models.Model):
    _inherit = "stock.move"

    def _get_new_picking_values(self):
        vals = super()._get_new_picking_values()
        if sale_note := self.sale_line_id.order_id.picking_note:
            vals.update({"note": sale_note})
        vals.update({"customer_note": self.sale_line_id.order_id.picking_customer_note})
        return vals
