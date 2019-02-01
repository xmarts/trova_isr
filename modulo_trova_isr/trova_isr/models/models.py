# -*- coding: utf-8 -*-

from odoo import models, fields, api

class InheritInfonavi(models.Model):
	_inherit = 'res.partner'
	infonavit = fields.Boolean(string = "Tienes infonavit",default=False)
	monto_infonavit = fields.Float( string = "Monto infonavit")

class InheritCamposnu(models.Model):
	_inherit = 'sales.commission'

	monto_info = fields.Float(string = "Monto infonavit", compute = "compute_info")
	monto_isr = fields.Float(string = "Monto ISR", compute="compute_isr")
	total_comi = fields.Float(string = "Total a pagar", compute = "compute_total_pagar")

	@api.multi
	def compute_info(self):
		if self.commission_user_id.partner_id.infonavit == True:
			self.monto_info = self.commission_user_id.partner_id.monto_infonavit

	@api.multi
	@api.depends("amount")
	def compute_isr(self):
		for invoice in self:
			li = self.env['sales.commission.isr'].search([("limite_inferior", "<=",invoice.amount),("limite_superior", ">=",invoice.amount)])
			if not li:
				self.monto_isr = (self.amount / 100) * 1.92
			else:
				self.monto_isr = (self.amount / 100) * li['porcentaje_isr']

	@api.multi
	@api.depends("amount","monto_info","monto_isr")
	def compute_total_pagar(self):
		comision_descuento = self.monto_info + self.monto_isr
		self.total_comi = self.amount - comision_descuento