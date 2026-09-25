# logic_manager.py


def determine_priority(ai_result):

    severity = ai_result["severity_score"]
    hazard = ai_result["common_area_hazard"]

    if severity >= 8 and hazard:
        return "EMERGENCY"

    elif severity >= 6:
        return "HIGH"

    elif severity >= 3:
        return "MEDIUM"

    else:
        return "LOW"

def assign_contractor(ai_result):

    category = ai_result["fault_category"]

    contractors = {
        "Water Leakage": "Plumbing Contractor",
        "Electrical": "Electrical Contractor",
        "Lift": "Lift Maintenance Contractor",
        "Air Conditioning": "HVAC Contractor"
    }

    return contractors.get(
        category,
        "General Maintenance Contractor"
    )


def calculate_sla(priority):

    if priority == "EMERGENCY":
        return "1 hour"

    elif priority == "HIGH":
        return "4 hours"

    elif priority == "MEDIUM":
        return "24 hours"

    else:
        return "72 hours"


def create_alert(ai_result, priority, contractor, sla):

    return (
        f"Priority: {priority}\n"
        f"Contractor: {contractor}\n"
        f"Response SLA: {sla}\n"
        f"Issue: {ai_result['issue_summary']}"
    )


def process_fault(ai_result):

    priority = determine_priority(ai_result)

    contractor = assign_contractor(ai_result)

    sla = calculate_sla(priority)

    alert = create_alert(
        ai_result,
        priority,
        contractor,
        sla
    )

    return {
        "fault_category": ai_result["fault_category"],
        "severity_score": ai_result["severity_score"],
        "common_area_hazard": ai_result["common_area_hazard"],
        "issue_summary": ai_result["issue_summary"],
        "priority": priority,
        "contractor": contractor,
        "response_sla": sla,
        "alert": alert
    }