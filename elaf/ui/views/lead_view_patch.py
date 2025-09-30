lead_form_crm_patch = {
    "key": "lead_form_crm_enhancement",
    "name": "Lead Form - CRM Enhancement",
    "model": "crm.lead",
    "view_type": "form",
    "priority": 10,  # Higher priority (applied earlier)
    "inherit_mode": "extension",
    "inherit_id": "crm_lead_form_view",  # THIS IS THE KEY - points to target view
    "module": "crm",
    "inheritance_operations": [
        {
            "operation": "before",
            "target": "field[name=partner]",
            "content": {
                    "name": "category",
                    "string": "Category",
                    "widget": "select",
                    "help": "Category",
                    "placeholder": "choose Category",
            }
        },
        {
            "operation": "before",
            "target": "field[name=probability]",
            "content": {
                    "name": "area",
                    "string": "Area",
                    "widget": "text",
                    "help": "Area",
                    "placeholder": "Area",
            }
        },
        {
            "operation": "after",
            "target": "field[name=probability]",
            "content": {
                    "name": "number_of_floors",
                    "string": "Number of Floors",
                    "widget": "number",
                    "help": "Number of Floors",
                    "placeholder": "Number of Floors",
            }
        },
    ]
}

