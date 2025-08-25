from models.bill import Bill

def split_bill(bill: Bill) -> dict:
    totals = {}

    # Subtotal per person
    subtotal = 0
    for item in bill.items:
        subtotal += item.price
        share = item.price / len(item.participants)
        for person in item.participants:
            totals[person] = totals.get(person, 0) + share

    # Adding tax and tip proportionally
    if subtotal > 0:
        for person, amount in totals.items():
            fraction = amount / subtotal 
            totals[person] = amount + (bill.tax * fraction) + (bill.tip * fraction)

    return totals