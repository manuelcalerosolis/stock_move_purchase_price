# -*- coding: utf-8 -*-

import logging

from odoo import models, fields, api, _
from odoo.addons import decimal_precision as dp

_logger = logging.getLogger(__name__)


class StockMove(models.Model):
    _inherit = "stock.move"
    _description = "Stock Move"

    purchase_price_unit = fields.Float(
        'Purchase price unit', compute='_compute_purchase_price_unit',
        digits=dp.get_precision('Product Price'),
        readonly=True, help='Price that has already been assigned for this move')

    @api.multi
    def _compute_purchase_price_unit(self):
        """ Fill the `purchase price` field on a stock move
        """

        for record in self:
            for order_line in record.picking_id.purchase_id.order_line:
                if order_line.product_id == record.product_id:
                    record.purchase_price_unit = order_line.price_total

    sale_price_unit = fields.Float(
        'Purchase price unit', compute='_compute_sale_price_unit',
        digits=dp.get_precision('Product Price'),
        readonly=True, help='Price that has already been assigned for this move')

    @api.multi
    def _compute_sale_price_unit(self):
        """ Fill the `sale price` field on a stock move
        """

        for record in self:
            for order_line in record.picking_id.sale_id.order_line:
                if order_line.product_id == record.product_id:
                    record.purchase_price_unit = order_line.price_total
