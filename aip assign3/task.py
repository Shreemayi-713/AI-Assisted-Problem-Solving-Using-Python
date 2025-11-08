# TGNPDCL Electricity Bill Calculator

# Tariff rates for different customer types
tariff = {
    'domestic': {'slabs': [(0,100,1.50), (101,200,2.50), (201,500,3.50), (501,9999,4.50)], 'fc':50, 'cc':10},
    'commercial': {'slabs': [(0,100,3.00), (101,200,4.00), (201,500,5.00), (501,9999,6.00)], 'fc':150, 'cc':25},
    'industrial': {'slabs': [(0,100,4.50), (101,200,5.50), (201,500,6.50), (501,9999,7.50)], 'fc':300, 'cc':50},
    'agricultural': {'slabs': [(0,9999,1.00)], 'fc':0, 'cc':5}
}

def calc_ec(units, ct):
    """Calculate Energy Charges"""
    t = tariff[ct.lower()]
    ec = 0
    rem = units
    for min_u, max_u, rate in t['slabs']:
        if rem <= 0: break
        if max_u == 9999:
            ec += rem * rate
            break
        slab_lower = 1 if min_u == 0 else min_u
        if units >= slab_lower:
            slab_units = min(units, max_u) - slab_lower + 1
            slab_units = min(slab_units, rem)
            ec += slab_units * rate
            rem -= slab_units
    return round(ec, 2)

# Read inputs
pu = float(input("Enter Previous Units (PU): "))
cu = float(input("Enter Current Units (CU): "))
ct = input("Enter Customer Type (domestic/commercial/industrial/agricultural): ").strip().lower()

# Calculate
units = cu - pu
ec = calc_ec(units, ct)
fc = tariff[ct]['fc']
cc = tariff[ct]['cc']
ed = round(ec * 0.05, 2)  # 5% of EC
total = ec + fc + cc + ed

# Print bill
print("\n" + "="*60)
print("          TGNPDCL ELECTRICITY BILL")
print("="*60)
print(f"Customer Type          : {ct.upper()}")
print(f"Previous Units (PU)    : {pu} units")
print(f"Current Units (CU)     : {cu} units")
print(f"Units Consumed         : {units} units")
print("-"*60)
print(f"Energy Charges (EC)    : Rs. {ec:.2f}")
print(f"Fixed Charges (FC)     : Rs. {fc:.2f}")
print(f"Customer Charges (CC)   : Rs. {cc:.2f}")
print(f"Electricity Duty (ED)   : Rs. {ed:.2f}")
print("-"*60)
print(f"TOTAL BILL AMOUNT      : Rs. {total:.2f}")
print("="*60)
