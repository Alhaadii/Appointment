# Copyright (c) 2024, himadwise and contributors
# For license information, please see license.txt

# import frappe
from frappe.utils import format_time
from frappe.model.document import Document


class SchedualShifts(Document):
    def before_save(self):
        self.validate_shifts()

    def validate_shifts(self):
        self.title= format_time(self.start_time,"HH:mm")+ " - " +format_time(self.end_time,"HH:mm")
