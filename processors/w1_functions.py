

def enqueue(priority_queue, patient):
    patient_urgency = patient[1]
    patient_name = patient[0]

    if patient_urgency == 1:
        no_urgency_list = priority_queue.get('no_urgency')
        no_urgency_list.append(patient_name)
    if patient_urgency == 2:
        low_urgency_list = priority_queue.get('low_urgency')
        low_urgency_list.append(patient_name)
    if patient_urgency == 3:
        urgency_list = priority_queue.get('urgency')
        urgency_list.append(patient_name)
    if patient_urgency == 4:
        high_urgency_list = priority_queue.get('high_urgency')
        high_urgency_list.append(patient_name)
    if patient_urgency == 5:
        emergency_list = priority_queue.get('emergency')
        emergency_list.append(patient_name)

    return priority_queue