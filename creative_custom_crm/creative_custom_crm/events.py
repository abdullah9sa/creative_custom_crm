import frappe
from frappe import _, msgprint

def validate_lead_status(self, args):
    if (self.status not in ["Meeting and Demo", "Follow up confirmed", "Interested/Qualified", "Lead", "MQL", "SQL"]):
        frappe.throw(
            _(
                "Please Update Lead Status to be one of the following Options " + '"Meeting and Demo", "Follow up confirmed", "Interested/Qualified", "Lead", "MQL" or "SQL"'
            )
        )