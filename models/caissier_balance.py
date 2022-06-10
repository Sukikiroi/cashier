from odoo import fields, models
from datetime import datetime,date


class Openning(models.Model):
 _name = "caissier.balance"
 _description = "Caissier Balance"

 balance_today=fields.Integer(string=" الرصيد اليومي", readonly=True,default=0)
 balance_total=fields.Integer(string="الرصيد الكلي", readonly=True,default=0)


 def button_check_isbn(self):
    print("Hi  Hi HI")