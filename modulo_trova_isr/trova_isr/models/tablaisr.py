from odoo import models, fields, api, _

class tablaIsr(models.Model):
	_name = 'sales.commission.isr'
	#_inherit = 'sales.commission'
	_description = 'Tabla de ISR'
	limite_inferior = fields.Float(string ='Límite inferior')
	limite_superior = fields.Float(string = 'Límite superior')
	porcentaje_isr = fields.Float(string = 'Porcentaje ISR')

