frappe.ui.form.on('Lead', {
    refresh(frm) {
        frm.set_query('custom_sub_industry', () => {
            return {
                filters: {
                    industry: frm.doc.industry
                }
            }
        });
        frm.set_query('industry', () => {
            return {
                filters: {
                    industry: ["in", ["E-commerce and Retail", "Education", "Finance and Banking", "Government and Public Sector",
                         "Telecommunications", "Health Care", "Manufacturing","Transportation and Logistics"
                         ,"Media and Entertainment","Real Estate","Energy and Utilities","Software"]] 
                }
            }
        });




        frm.set_query('campaign_name', () => {
            return {
                filters: {
                    industry: ["in", ["Internal referral", "Lead generation partner", "Inbound"]]
                }
            }
        });


        frm.set_query('market_segment', () => {
            return {
                filters: {
                    name: ["in", ["Government", "SMB", "Large / Corporate", "Sister company"]] 
                }
            }
        });
    },
})