
from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    gender = fields.Selection(
        selection=[('male', 'Male'), ('female', 'Female')],
        string='Gender', default='male')
