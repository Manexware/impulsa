from openerp import models, fields, api


class ImSeller(models.Model):
    _name = 'im.seller'
    _description = 'Seller'

    name = fields.Char(required=True)

    _order = 'name'

    _sql_constraints = [
        ('name_uk', 'unique(name)', 'Concept must be unique'),
    ]

    @api.one
    def copy(self, default=None):
        default = dict(default or {})
        copied_count = self.search_count(
            [('name', '=like', u"Copy of {}%".format(self.name))])
        if not copied_count:
            new_name = u"Copy of {}".format(self.name)
        else:
            new_name = u"Copy of {} ({})".format(self.name, copied_count)
        default['name'] = new_name
        return super(ImSeller, self).copy(default)

