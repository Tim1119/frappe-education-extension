import frappe
from frappe import _

def validate_assessment_criteria(doc, method):
    """Validate that Assessment Criteria exists in School Settings"""
    
    # Get School Settings
    try:
        settings = frappe.get_doc('School Settings', 'School Settings')
    except frappe.DoesNotExistError:
        # If School Settings doesn't exist, skip validation
        return
    
    # Build list of valid criteria names
    valid_criteria = [item.criteria_name for item in settings.get('assessment_criteria_item', [])]
    
    # If no criteria defined in settings, allow anything
    if not valid_criteria:
        return
    
    # Check if current criteria name is in valid list
    if doc.assessment_criteria not in valid_criteria:
        frappe.throw(_('Assessment Criteria "{0}" is not configured in School Settings. Please add it first.').format(doc.assessment_criteria))


