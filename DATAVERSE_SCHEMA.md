# Dataverse Schema

This schema outlines tables for a Power Apps or Power Pages solution. The design stays drag-and-drop friendly so you can build forms and views without custom code.

## SalesOrder Table
| Column | Type | Description |
|---|---|---|
| **sales_order_id** | Text | Unique order number (primary column). |
| **customer_name** | Text | Name of the customer. |
| **po_number** | Text | Purchase order reference. |
| **first_date** | Date | First requested date. |
| **orig_ship_date** | Date | Original ship date. |
| **est_ship_date** | Date | Estimated ship date. |
| **status** | Choice | On Time, Late, Planning, etc. |
| **notes** | Multiline Text | Manual overrides or comments. |

## Item Table
| Column | Type | Description |
|---|---|---|
| **item_id** | Text | Calculated as `sales_order_id`-`item_number`. |
| **item_number** | Text | Item line number. |
| **material** | Text | Material code. |
| **description** | Text | Item description. |
| **quantity** | Number | Ordered quantity. |
| **net_price** | Currency | Price per unit. |
| **open_sales_value** | Currency | Total open value. |
| **order_status** | Text | Manufacturing, Planning, etc. |
| **pushout_comments** | Multiline Text | Reason for ship date changes. |
| **production_order** | Text | Internal production order number. |
| **item_category** | Text | Type of item (e.g., Spare Part). |
| **late** | Yes/No (calculated) | True if `est_ship_date` is past today and not shipped. |
| **audit_notes** | Multiline Text | Notes for manual changes or exceptions. |
| **sales_order** | Lookup (SalesOrder) | Parent order relationship. |

## ChangeHistory Table
Tracks updates between imports for auditing.

| Column | Type | Description |
|---|---|---|
| **change_history_id** | GUID (primary) | Unique row. |
| **item** | Lookup (Item) | Related item. |
| **field_changed** | Text | Column that changed. |
| **old_value** | Text | Previous value. |
| **new_value** | Text | Updated value. |
| **change_date** | DateTime | When the change occurred. |
| **changed_by** | Text | User or system. |

Use these tables to build views and forms in Power Apps. The default relationships let you drag table columns onto forms, and you can enable change tracking by creating a simple Power Automate flow that writes rows to **ChangeHistory** whenever records are updated.
