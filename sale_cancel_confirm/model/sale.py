# Copyright 2020 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import models


class SaleOrder(models.Model):
    _name = "sale.order"
    _inherit = ["sale.order", "base.cancel.confirm"]

    _has_cancel_reason = "optional"  # ["no", "optional", "required"]

    def action_cancel(self):
        return (
            super().action_cancel()
            if self.filtered("cancel_confirm")
            else self.open_cancel_confirm_wizard()
        )

    def action_draft(self):
        self.clear_cancel_confirm_data()
        return super().action_draft()
