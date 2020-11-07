from processors.priority_queue import priority_queue


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


def dequeue(priority_queue):
    queue_with_pacients = []
    for items in priority_queue.items():
        if len(items[1]) > 0:
            queue_with_pacients.append(items)

    
    for index in range(len(queue_with_pacients) -1, -1 , -1):
        priority = queue_with_pacients[index]
        if priority[0] == 'emergency':
            pacient = priority[1][0]
            priority[1].pop(0)
            priority_queue.update({priority[0]: priority[1]})
            
            return (priority_queue, pacient)
        if priority[0] == 'high_urgency':
            pacient = priority[1][0]
            priority[1].pop(0)
            priority_queue.update({priority[0]: priority[1]})
            return priority_queue
        if priority[0] == 'urgency':
            pacient = priority[1][0]
            priority[1].pop(0)
            priority_queue.update({priority[0]: priority[1]})
            return priority_queue
        if priority[0] == 'low_urgency':
            pacient = priority[1][0]
            priority[1].pop(0)
            priority_queue.update({priority[0]: priority[1]})
            return priority_queue
        if priority[0] == 'no_urgency':
            pacient = priority[1][0]
            priority[1].pop(0)
            priority_queue.update({priority[0]: priority[1]})
            return priority_queue
    
    return None

