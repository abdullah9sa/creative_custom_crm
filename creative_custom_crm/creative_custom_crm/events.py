import frappe
from frappe import _, msgprint

def validate_lead_status(self, args):
    
    self.set_full_name()
    self.set_lead_name()
    self.set_title()
    self.set_status()
    self.check_email_id_is_unique()
    self.validate_email_id()
    
    if (self.status not in ["Meeting and Demo", "Follow up confirmed", "Interested/Qualified", "Lead", "MQL", "SQL"]):
        frappe.throw(
            _(
                "Please Update Lead Status to be one of the following Options " + '"Meeting and Demo", "Follow up confirmed", "Interested/Qualified", "Lead", "MQL" or "SQL"'
            )
        )