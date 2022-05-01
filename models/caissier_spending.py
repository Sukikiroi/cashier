from odoo import fields, models
from datetime import datetime,date

doors=[('option1', 'Label 1'), ('option2', 'Label 2')]
entrances=[('option1', 'Label 1'), ('option2', 'Label 2')]
class Openning(models.Model):
 _name = "caissier.spending"
 _description = "Caissier Spending"
 time = fields.Char(string="ساعة الافتتاح",default=datetime.now().strftime("%H:%M:%S"))
 date = fields.Date("تاريخ الافتتاح")



 door= fields.Selection(doors, string='My Selection Field')


 entrance= fields.Selection(entrances, string='My Selection Field')

 def button_check_isbn(self):
    print("Hi  Hi HI")