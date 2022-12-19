from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class InventoryCustom(models.Model):
    _inherit = 'product.template'

    is_room = fields.Boolean()


class PurchaseCustom(models.Model):
    _inherit = 'purchase.order'

    @api.multi
    def unlink(self):
        raise ValidationError("Sorry you can not delete, you can archive it instead")


class SaleOrderTemplateCust(models.Model):
    _inherit = 'sale.order.template'

    total_rooms = fields.Float()
    stock_rooms = fields.Float(compute="_compute_stock")
    available_rooms = fields.Float(compute="_compute_available")

    @api.one
    # @api.depends('product_id', 'quantity')
    def _compute_stock(self):
        sale_order_domain = [('template_name', '=', self.name), ('is_room', '=', True), ('state', 'not in', (['draft', 'waiting', 'sent', 'expired']))]
        sale_order_line_ids = self.env['sale.order.line'].sudo().search(sale_order_domain)

        self.stock_rooms = sum(sale_order_line_ids.mapped('product_uom_qty'))
        print(self.stock_rooms)
        # if sale_order_template_option_id:
        #     self.stock_rooms = sale_order_template_option_id.stock

    @api.one
    def _compute_available(self):
        self.available_rooms = self.total_rooms - self.stock_rooms


class SaleOrderCust(models.Model):
    _inherit = 'sale.order'

    total_rooms = fields.Float(related='sale_order_template_id.total_rooms')


class SaleOrderOption(models.Model):
    _inherit = 'sale.order.option'

    transfer = fields.Boolean("Transfer", default=False)
    hotel = fields.Many2one('model.hotel', string="Hotel")
    inventory = fields.Float(string="Inventory")
    analytic_tag_id = fields.Many2one('account.analytic.tag', 'Analytic Tags')
    available = fields.Float(string="Available", compute="_compute_available")
    is_room = fields.Boolean()

    @api.one
    @api.depends('product_id', 'quantity')
    def _compute_available(self):
        for rec in self:
            if rec.product_id:
                rec.available = 0
                sale_order_template_option_id = self.env['sale.order.template.option'].sudo().search(
                    [('product_id', '=', rec.product_id.id),
                     ('template_name', '=', self.order_id.sale_order_template_id.name)], limit=1)
                if sale_order_template_option_id:
                    rec.available = sale_order_template_option_id.available


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    location_id = fields.Many2one('stock.location', "Location")
    cost = fields.Float('Cost', related="product_id.standard_price", store=True, readonly=False)
    available = fields.Float(string="Available", compute="_compute_available")
    reserved = fields.Float()
    is_room = fields.Boolean(compute='compute_is_room')
    template_name = fields.Char(related='order_id.sale_order_template_id.name')

    @api.one
    def compute_is_room(self):
        self.is_room = self.product_id.is_room

    @api.one
    @api.depends('product_id', 'product_uom_qty')
    def _compute_available(self):
        for rec in self:
            if rec.product_id:
                rec.available = 0
                if rec.product_id:
                    sale_order_template_option_id = self.env['sale.order.template.option'].sudo().search(
                        [('product_id', '=', rec.product_id.id),
                         ('template_name', '=', self.order_id.sale_order_template_id.name)], limit=1)
                    if sale_order_template_option_id:
                        rec.available = sale_order_template_option_id.available
