frappe.ui.form.on('Lead', {
    refresh(frm) {
        frm.set_query('custom_sub_industry', () => {
            return {
                filters: {
                    industry: frm.doc.industry
                }
            }
        })
    },
})