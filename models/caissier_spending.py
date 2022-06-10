from odoo import fields, models
from datetime import datetime,date

doors=[('option1', 'Label 1'), ('option2', 'Label 2')]
entrances=[('option1', 'Label 1'), ('option2', 'Label 2')]
class Openning(models.Model):
 _name = "caissier.spending"
 _description = "Caissier Spending"
 time = fields.Char(string="ساعة الافتتاح",default=datetime.now().strftime("%H:%M:%S"))


 date = fields.Date("تاريخ الافتتاح")



 door= fields.Char(string='الباب')
 entrance= fields.Char(string='المدخل')
 section= fields.Char(string='القسم')

 concerned= fields.Char( string='المعني')
 taxpayer= fields.Char(string='المكلف')
 
 description=fields.Char(string='الملاحضة')
 
 sold=fields.Integer(string='الرصيد')
 
 def button_check_isbn(self):
    print("Hi  Hi HI")