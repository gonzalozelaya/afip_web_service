# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import datetime, timedelta
from afip import Afip
from odoo.exceptions import UserError

class AfipPadron(models.Model):
  _inherit='res.partner'
  
  afip_company_id=fields.Many2one(
        comodel_name='res.company',
        string="Compania",)
  
  def connectToAfip(self):
      private_key, certificate = self.afip_company_id.sudo()._get_key_and_certificate()
      afip = Afip({
          "CUIT": 20401498819,
          "cert": certificate,
          "key": private_key
      })
      customer_vat = self.vat
      taxpayer_details = afip.RegisterInscriptionProof.getTaxpayerDetails(customer_vat)
      raise UserError(str(taxpayer_details))