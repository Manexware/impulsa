from openerp import models, fields, api


class ImSchedule(models.Model):
    _name = 'im.schedule'
    _description = 'Schedule'

    name = fields.Char(required=True)
    customer_id = fields.Many2one('im.customer')
    seller_id = fields.Many2one('im.seller')
    latitude = fields.Char()
    longitude = fields.Char()

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
        return super(ImSchedule, self).copy(default)

