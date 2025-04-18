ledger_data = {}

def add_entry(party_name, entry):
    if party_name not in ledger_data:
        ledger_data[party_name] = []
    ledger_data[party_name].append(entry)

def get_ledger(party_name):
    return ledger_data.get(party_name, [])
