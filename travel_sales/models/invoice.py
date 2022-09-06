from odoo import fields, models, api


class Invoice(models.Model):

    _inherit = 'account.invoice'
    payment_count = fields.Integer(compute='count_payments')

    def count_payments(self):
        print(self.number)
        self.payment_count =self.env['account.payment'].search_count([('communication','like',self.number)])


    def get_payments(self):

        return {
            'type': 'ir.actions.act_window',
            'name': 'payments',
            'view_mode': 'tree,form',
            'res_model': 'account.payment',
            'domain': [('communication','like',self.number)],
        }
