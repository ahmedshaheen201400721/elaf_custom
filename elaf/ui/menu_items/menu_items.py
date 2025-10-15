


menu_dict = {
    "set_default_filter_for_contacts": {
        "_inherit": "contacts_main_menu_partner",
        "inheritance_operations": [
           {
                "operation": "merge",
                "target": "context",
                "content": {
                    "default_filter": 'my_not_contacted_filter'
                }
            },
        ]
    }
}