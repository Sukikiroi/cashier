from odoo import fields, models
from datetime import datetime,date


class Openning(models.Model):
 _name = "caissier.openning"
 _description = "Caissier Openning"
 time = fields.Char(string="ساعة الافتتاح",default=datetime.now().strftime("%H:%M:%S"))
 date = fields.Date("تاريخ الافتتاح")
 balance=fields.Integer(string="الرصيد", readonly=True,default=0)
 


 def button_check_isbn(self):
    print("Hi  Hi HI")