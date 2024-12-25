# Copyright (c) 2024, himadwise and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class AppointmentDoc(Document):
    def after_insert(self):
        # After inserting the appointment, get the queue number
        queue_number = self.add_to_appointment_queue()

        # Manually render the HTML template with the queue number
        context = {
            'queue_number': queue_number  # Pass the queue number here
        }

        # Render the HTML template
        html_content = frappe.render_template("www/success_with_q_number.html", context)

        # Return or do something with the rendered HTML
        return html_content

    def add_to_appointment_queue(self):
        # Add the appointment to the queue and return the queue number
        q = frappe.get_all("Appointment Queue", filters={
            "date": self.date,
            "shift": self.shift,
            "clinic": self.clinic
        })

        if not q:
            q = frappe.get_doc({
                "doctype": "Appointment Queue",
                "date": self.date,
                "shift": self.shift,
                "clinic": self.clinic,
            })
        else:
            q = frappe.get_doc("Appointment Queue", q[0]["name"])

        # Add the appointment to the queue
        q.append("queue", {
            "appointment": self.name,
        })

        q.save(ignore_permissions=True)

        # Return the queue number
        return len(q.queue)
