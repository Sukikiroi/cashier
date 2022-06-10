from odoo import api,fields, models
from datetime import datetime,date


class Openning(models.Model):
 _name = "caissier.income"
 _description = "Caissier Income"
 time = fields.Char(string="ساعة المدخول",default=datetime.now().strftime("%H:%M:%S"))
 date = fields.Date("تاريخ المدخول")
 
 
 balance=fields.Integer(string="الرصيد", readonly=True,default=0,compute="calulate_total")
 company_id = fields.Many2one('res.company', 'Company', required=True, index=True,default=lambda self: self.env.company)
 first=fields.Integer(string=" أوراق 2000", readonly=True,compute="_compute_first")
 first_qty=fields.Integer(string="الكمية",default=0) 
 
 
 
 seconde=fields.Integer(string="أوراق 1000",default=0 ,compute="_compute_seconde")
 seconde_qty=fields.Integer(string="الكمية",default=0)
 
 
 
 tree=fields.Integer(string="أوراق 500",default=0 ,compute="_compute_tree") 
 tree_qty=fields.Integer(string="الكمية",default=0)
 

 four=fields.Integer(string="أوراق  200  ",default=0,compute="_compute_four")
 four_qty=fields.Integer(string="الكمية",default=0)
 

 coin_one=fields.Integer(string="الكمية",default=0)
 
 coin_two=fields.Integer(string="الكمية",default=0)

 coin_tree=fields.Integer(string="الكمية",default=0)

 coin_four=fields.Integer(string="الكمية",default=0)

 coin_five=fields.Integer(string="الكمية",default=0)

 coin_six=fields.Integer(string="الكمية",default=0)

 operation_code=fields.Char(string=" رمز العملية")
 client_code=fields.Integer(string=" رمز العميل")
 isOpen =fields.Boolean(default=False)




 @api.depends("first_qty")
 def _compute_first(self):
        for record in self:
            record.first = 2000.0 * record.first_qty


 @api.depends("seconde_qty")
 def _compute_seconde(self):
        for record in self:
            record.seconde = 1000.0 * record.seconde_qty      
 


 @api.depends("tree_qty")
 def _compute_tree(self):
        for record in self:
            record.tree = 500.0 * record.tree_qty

 @api.depends("four_qty")
 def _compute_four(self):
        for record in self:
            record.four = 200.0 * record.four_qty 





 @api.onchange("first","seconde","tree","four")    
 def calulate_total(self):
    for record in self:
            record.balance = record.first +record.seconde+record.tree+record.four