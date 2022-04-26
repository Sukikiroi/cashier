{
    "name": "الصندوق",
    "summary": "Manage Caissier.",
    "author": "kaddour Abdelaziz",
    "category": "Services/caissier",
    "license": "AGPL-3",
    "website": "https://github.com/Sukikiroi/treasury-module",
    "version": "15.0.1.0.0",
    "depends": ["base","web"],
    "application": True,
    
    "data": [
         "security/caissier_security.xml",
         "security/ir.model.access.csv",
          "views/caissier_closing_view.xml",
           "views/caissier_spending_view.xml",
            "views/caissier_income_view.xml",
             "views/caissier_openning_view.xml",
             "views/caissier_menu.xml",
    ],
      "qweb": [
        # 'static/src/xml/qweb_template.xml',
    ],
    # "css": ["static/src/css/test.css"],
    "assets": {
        # "web.assets_backend": [
        #     "khazina/static/src/css/test.css",
        # ],
    },
}
