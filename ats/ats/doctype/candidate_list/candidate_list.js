// Copyright (c) 2022, sanaa and contributors
// For license information, please see license.txt

frappe.ui.form.on("Candidate list", {
    onload: function(frm) {
		var dialog_box = new frappe.ui.Dialog({
			title: __('Upload Your Resume'),
			fields: [
				{
					"label" : "Resume",
					"fieldname": "resume",
					"fieldtype": "Attach",

				}
			],
            primary_action_label: 'Submit',
            primary_action(values) {
                cur_frm.doc.upload_cv_resume = values['resume']
                cur_frm.refresh()
                dialog_box.hide();
            }
        });

        dialog_box.show();
    }
})


