// Copyright (c) 2016, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.query_reports["Custom Lead Details"] = {
	filters: [
		{
			fieldname: "company",
			label: __("Company"),
			fieldtype: "Link",
			options: "Company",
			default: frappe.defaults.get_user_default("Company"),
			reqd: 1,
		},
		{
			fieldname: "from_date",
			label: __("From Date"),
			fieldtype: "Date",
			default: frappe.datetime.add_months(frappe.datetime.get_today(), -12),
			reqd: 1,
		},
		{
			fieldname: "to_date",
			label: __("To Date"),
			fieldtype: "Date",
			default: frappe.datetime.get_today(),
			reqd: 1,
		},
		{
			fieldname: "custom_lead_status",
			label: __("Status"),
			fieldtype: "Select",
			options: [
				{ value: "Meeting and Demo", label: __("Meeting and Demo") },
				{ value: "Follow up confirmed", label: __("Follow up confirmed") },
				{ value: "Interested/Qualified", label: __("Interested/Qualified") },
				{ value: "Lead", label: __("Lead") },
				{ value: "MQL", label: __("MQL") },
				{ value: "SQL", label: __("SQL") }
			],
		},
		{
			fieldname: "territory",
			label: __("Territory"),
			fieldtype: "Link",
			options: "Territory",
		},
	],
};
