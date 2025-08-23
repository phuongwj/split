from models.bill import Bill

def split_bill(bill: Bill) -> dict:
    totals = {}

    for item in bill.item:
        share = item.price / len(item.participants)
        for person in item.participants:
            totals[person] = totals.get(person, 0) + share

    return totals