// Copyright (c) 2022, sanaa and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["job applicant report"] = {
	"filters": [
		{
			"label": "Job Title",
			"fieldname": "job_title",
			"fieldtype": "Link",
			"options": "Job Opening",
			"width": 200,
		},
	]
};
