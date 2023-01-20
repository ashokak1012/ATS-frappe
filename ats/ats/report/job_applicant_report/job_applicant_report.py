# Copyright (c) 2022, sanaa and contributors
# For license information, please see license.txt

import frappe


def execute(filters):
	columns, data = [], []
	columns = get_columns()
	data = get_data(filters)
	return columns, data

def get_columns():
	return [
		{
			"label": "Applicant",
			"fieldname": "applicant_name",
			"fieldtype": "Link",
			"options": "Job Applicant",
			"width": 200,
		},
	]
def get_data(filters):
	filt={}
	if(filters.get('job_title')):
		filt['job_title'] = filters.get('job_title')
	applicant= frappe.get_all("Job Applicant",filters=filt, fields=['applicant_name'])
	return applicant