# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import datetime, timedelta
from afip import Afip
from odoo.exceptions import UserError

class AfipPadron(models.Model):
  _name='afip.web.services'
  
  name=fields.Char('Nombre')
  
  def connectToAfip(self):
      afip = Afip({ "CUIT": 20409378472 })
      tax_id = 20111111111
      taxpayer_details = afip.RegisterScopeThirteen.getTaxpayerDetails(tax_id)
      raise UserError(str(taxpayer_details))