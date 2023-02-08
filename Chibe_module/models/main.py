from odoo import models,fields

import sys
import os

class BooksManagement(models.Model):
    _name = 'books.management'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'image.mixin']
    _description = 'Books Management'
    
    name = fields.Char(string='Name')
    # author = fields.Many2many('')
    publishing_year = fields.Date(string='Publishing year')
    type = fields.Selection(string="Type", selection=[('anime', 'Anime'),('others', 'Others')], default='others')
    # image_1920 = fields.Image(string="Image", max_width=1920, max_height=1920)
    price = fields.Float(string='Price')
    partner_id = fields.Many2one('res.partner', 'Responsible')
    guest_ids = fields.Many2many('res.partner', 'Participants')
    
    # resized fields stored (as attachment) for performance
    # image_1024 = fields.Image("Image 1024", related="image_1920", max_width=1024, max_height=1024, store=True)
    # image_512 = fields.Image("Image 512", related="image_1920", max_width=512, max_height=512, store=True)
    # image_256 = fields.Image("Image 256", related="image_1920", max_width=256, max_height=256, store=True)
    # image_128 = fields.Image("Image 128", related="image_1920", max_width=128, max_height=128, store=True)

    def action_wizard(self):
        # action = self.env['ir.actions.act_window']._for_xml_id('books_management.action_edit_name')
        # return action
        self.ensure_one()
        view_wizard = self.env.ref('books_management.view_edit_name_form')
        return {
            'name': "Edit Name",
            'type': 'ir.actions.act_window',
            'res_model': 'edit.views.wizard',
            'views': [(view_wizard.id, 'form')],
            'target': 'new',
            'context': {
                'default_book_id': self.id,
                'default_name': self.name,
                'default_type': self.type
            }
        }