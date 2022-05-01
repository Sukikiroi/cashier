from odoo import fields, models
from datetime import datetime,date


class Openning(models.Model):
 _name = "caissier.income"
 _description = "Caissier Income"
 time = fields.Char(string="ساعة الافتتاح",default=datetime.now().strftime("%H:%M:%S"))
 date = fields.Date("تاريخ الافتتاح")
 
 
 balance=fields.Integer(string="الرصيد", readonly=True,default=0)
 
 
 first=fields.Integer(string="الرصيد", readonly=True,default=0)
 first_qty=fields.Integer(string="الرصيد", readonly=True,default=0) 
 
 
 
 seconde_qty=fields.Integer(string="الرصيد", readonly=True,default=0)
 seconde=fields.Integer(string="الرصيد", readonly=True,default=0)
 
 
 
 tree_qty=fields.Integer(string="الرصيد", readonly=True,default=0) 
 tree=fields.Integer(string="الرصيد", readonly=True,default=0)
 

 four_qty=fields.Integer(string="الرصيد", readonly=True,default=0)
 four=fields.Integer(string="الرصيد", readonly=True,default=0)
 
 
 
 
 operation_code=fields.Char(string="")
 client_code=fields.Integer(string="")




 def button_check_isbn(self):
    print("Hi  Hi HI")