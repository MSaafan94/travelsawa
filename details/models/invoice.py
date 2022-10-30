from odoo import models, fields, api, _
from datetime import *


class DueDate(models.Model):
    _inherit = 'account.invoice'

    date_due = fields.Date(compute="date_due_method")

    @api.one
    @api.depends('sale_order_template_id')
    def date_due_method(self):
        # print(self.sale_order_template_id.endtimeee)
        if self.sale_order_template_id:
            self.date_due = self.sale_order_template_id.starttime.date()
        # self.date_due = self.sale_order_template_id.endtimeee
        # print(self.date_due)