app_name = "creative_custom_crm"
app_title = "Creative Custom Crm"
app_publisher = "CAT"
app_description = "Custom CRM"
app_email = "info@creativeadvtech.com"
app_license = "mit"

fixtures = [
    {
        "doctype": "Market Segment",
        "filters": [
            ["name", "in", ["Sister company", "Large / Corporate", "SMB", "Government"]]
        ]
    },
     {
        "doctype": "Property Setter",
        "filters": [
            ["name", "in", ["Lead-type-options","Lead-status-options","Lead-request_type-hidden"]]
        ]
    },
    {
        "doctype": "Custom Field",
        "filters": [
            ["name", "in", ["Lead-custom_sub_industry","Opportunity-custom_request_type","Lead-custom_lead_actions_table","Opportunity-custom_product_type","Opportunity-custom_deal_type"]]
        ]
    },
    {
        "doctype": "Industry Type",
        "filters": [
            ["name", "in", [
                "E-commerce and Retail", "Education", "Finance and Banking", "Government and Public Sector",
                "Telecommunications", "Transportation and Logistics","Media and Entertainment","Energy and Utilities"
            ]]
        ]
    },
    {
        "doctype": "Industry Type",
        "filters": [
            ["industry", "in", ["Government and Public Sector"]]
        ]
    },
    {
        "doctype": "Sub Industry"
    },
    {
        "doctype": "Lead Source",
        "filters": [
            ["source_name", "in", [
                "Name of the person",
                "Aexus",
                "Company website",
                "Social media",
                "LinkedIn"
            ]]
        ]
    },
    {
        "doctype": "Campaign",
        "filters": [
            ["campaign_name", "in", ["Internal referral","Lead generation partner","Inbound"]]
        ]
    },
]


# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/creative_custom_crm/css/creative_custom_crm.css"
# app_include_js = "/assets/creative_custom_crm/js/creative_custom_crm.js"

# include js, css files in header of web template
# web_include_css = "/assets/creative_custom_crm/css/creative_custom_crm.css"
# web_include_js = "/assets/creative_custom_crm/js/creative_custom_crm.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "creative_custom_crm/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
    "Lead" : "public/js/lead.js",
    "Opportunity" : "public/js/opportunity.js",
    
}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "creative_custom_crm/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "creative_custom_crm.utils.jinja_methods",
# 	"filters": "creative_custom_crm.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "creative_custom_crm.install.before_install"
# after_install = "creative_custom_crm.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "creative_custom_crm.uninstall.before_uninstall"
# after_uninstall = "creative_custom_crm.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "creative_custom_crm.utils.before_app_install"
# after_app_install = "creative_custom_crm.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "creative_custom_crm.utils.before_app_uninstall"
# after_app_uninstall = "creative_custom_crm.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "creative_custom_crm.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
    "Lead": {
        "validate": [
            "creative_custom_crm.creative_custom_crm.events.validate_lead_status"
        ]
    },
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"creative_custom_crm.tasks.all"
# 	],
# 	"daily": [
# 		"creative_custom_crm.tasks.daily"
# 	],
# 	"hourly": [
# 		"creative_custom_crm.tasks.hourly"
# 	],
# 	"weekly": [
# 		"creative_custom_crm.tasks.weekly"
# 	],
# 	"monthly": [
# 		"creative_custom_crm.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "creative_custom_crm.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "creative_custom_crm.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "creative_custom_crm.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["creative_custom_crm.utils.before_request"]
# after_request = ["creative_custom_crm.utils.after_request"]

# Job Events
# ----------
# before_job = ["creative_custom_crm.utils.before_job"]
# after_job = ["creative_custom_crm.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"creative_custom_crm.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

