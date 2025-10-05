

lead_form_crm_patch = {
    "key": "partner_form_base_enhancement",
    "name": "Partner Form - Base Enhancement",
    "model": "base.partner",
    "view_type": "form",
    "priority": 10,  # Higher priority (applied earlier)
    "inherit_mode": "extension",
    "inherit_id": "base_partner_form_view",  # THIS IS THE KEY - points to target view
    "module": "crm",
    "inheritance_operations": [
        {
            "operation": "before",
            "target": "field[name=country_id]",
            "content": {
                    "name": "responsible_user",
                    "string": "Responsible User",
                    "widget": "relation",
                    "help": "Responsible User",
                    "placeholder": "choose Responsible User",
            }
        },
    ]
}

