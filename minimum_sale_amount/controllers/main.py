from odoo import http
from odoo.addons.website_sale.controllers.main import WebsiteSale


class MyWebsiteSale(WebsiteSale):

    @http.route(['/shop/cart/update'], type='json', auth="public", website=True)
    def cart_update(self, product_id, line_id=None, add_qty=None, set_qty=None, display=True):
        # Call the original method to update the cart and get the order total
        res = super().cart_update(product_id, line_id=line_id, add_qty=add_qty, set_qty=set_qty, display=display)
        order_total = res.get('order_total')

        # Check if the order total is less than the minimum sale amount
        min_sale_amt = float(self.env['ir.config_parameter'].sudo().get_param('sale.min_sale_amount', default=0))
        if order_total < min_sale_amt:
            # Redirect to the cart page if the order total is less than the minimum sale amount
            return http.request.redirect('/shop/cart')

        # Otherwise, call the original method to process the checkout and redirect to the checkout page
        return super().process_checkout()
