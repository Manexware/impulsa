from openerp import models, fields, api
from openerp.addons.base_geoengine import geo_model
from openerp.addons.base_geoengine import fields as geo_fields


class ImSchedule(geo_model.GeoModel):
    _name = 'im.schedule'
    _description = 'Schedule'

    name = fields.Char()
    customer_id = fields.Many2one('res.partner')
    seller_id = fields.Many2one('hr.employee')
    latitude = fields.Float()
    longitude = fields.Float()
    date = fields.Date()
    the_point = geo_fields.GeoPoint('Coordinate Customer',compute='_get_geo_point',store=True)

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

    @api.one
    @api.depends('latitude', 'longitude')
    def _get_geo_point(self):
        if not self.latitude or not self.longitude:
            self.the_point = False
        else:
            self.the_point = geo_fields.GeoPoint.from_latlon(self.env.cr, self.latitude, self.longitude)
