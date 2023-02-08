from odoo import fields, models

class EditViewsWizard(models.TransientModel):
    _name = "edit.views.wizard"
    _description = "Edit Views Wizard"
    
    name = fields.Char(string='New Name')
    book_id = fields.Many2one('books.management', string='Book')
    type = fields.Selection(string='Type', selection=[('anime', 'Anime'),('others', 'Others')], default='others')

    def action_edit_name(self):
        book_id = self.book_id
        book_type = self.type
        book_name = self.env['books.management'].browse(book_id)
        new_name = {}
        new_name["name"] = self.name + " - Category: " + book_type
        book_name.write(new_name)
        return self.name
