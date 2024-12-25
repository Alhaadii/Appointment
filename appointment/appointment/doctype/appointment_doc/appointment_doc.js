// Copyright (c) 2024, himadwise and contributors
// For license information, please see license.txt

frappe.ui.form.on("Appointment Doc", {
	refresh(frm) {
        frm.set_query("shift", (doc)=>{
            return {
                filters:{
                    "clinic": doc.clinic
                }
            }
        })
	},
});
