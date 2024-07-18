frappe.ui.form.on('Opportunity', {
    refresh(frm) {

        frm.set_value("sales_stage",null);
        frm.set_query('sales_stage', () => {
            return {
                filters: {
                    stage_name: ["in", ["Interested/Qualified", "Meeting and Demo", "Follow up confirmed", "Proposal to be sent",
                        "Proposal sent", "Contract and budget discussion", "Closed won", "Closed lost"
                    ]]
                }
            }
        });

    },
});