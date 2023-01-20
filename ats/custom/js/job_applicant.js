
frappe.ui.form.on("Job Applicant", {
	refresh: function(frm) {
		frm.set_query("job_title", function() {
			let des = cur_frm.doc.designation;
			return {
				filters: {
					'designation': ["in", des],
					'status': 'Open',
				},
			};
		});
	}
});
