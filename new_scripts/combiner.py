import json

with open('csb') as f:
    times = json.load(f)

with open('sublist') as f:
    descs = json.load(f)

with open('evaluations') as f:
    evals = json.load(f)

classes = {}

for c in times:
    classes[c] = {
        'no': c,
        'co': times[c]['course'],
        'cl': times[c]['class'],
        'f': times[c]['final'],
        
        's': times[c]['sections'],
        'l': times[c]['l'],
        'r': times[c]['r'],
        'b': times[c]['b']}

    if c in descs:
        classes[c]['hh'] = descs[c]['HASS-H']
        classes[c]['ha'] = descs[c]['HASS-A']
        classes[c]['hs'] = descs[c]['HASS-S']
        classes[c]['he'] = descs[c]['HASS-E']
        classes[c]['ci'] = descs[c]['CI-H']
        classes[c]['cw'] = descs[c]['CI-HW']
        classes[c]['re'] = descs[c]['REST']
        classes[c]['la'] = descs[c]['LAB']
        classes[c]['u1'] = descs[c]['units1']
        classes[c]['u2'] = descs[c]['units2']
        classes[c]['u3'] = descs[c]['units3']
        classes[c]['le'] = descs[c]['level']
        classes[c]['t'] = descs[c]['terms']
        classes[c]['d'] = descs[c]['desc']
        classes[c]['n'] = descs[c]['name']
    else:
        classes[c]['hh'] = False
        classes[c]['ha'] = False
        classes[c]['hs'] = False
        classes[c]['he'] = False
        classes[c]['ci'] = False
        classes[c]['cw'] = False
        classes[c]['re'] = False
        classes[c]['la'] = False
        classes[c]['u1'] = 0
        classes[c]['u2'] = 0
        classes[c]['u3'] = 0
        classes[c]['le'] = 'U'
        classes[c]['t'] = ['FA']
        classes[c]['d'] = 'New class- manual fill required.'
        classes[c]['n'] = 'New class'

    if c in evals:
        total_rating = 0
        total_hours = 0
        total_size = 0
        terms = 0
        
        for t in evals[c]:
            if t['resp'] > 0:
                total_rating += t['rating']
                total_hours += t['oc_hours'] + t['ic_hours']
                total_size += t['eligible']
                terms += 1
                
        if terms == 0:
            terms = 1
            
        classes[c]['ra'] = round(total_rating / terms, 1)
        classes[c]['h'] = round(total_hours / terms, 1)
        classes[c]['si'] = round(total_size / terms, 1)
    else:
        classes[c]['ra'] = 0
        classes[c]['h'] = 0
        classes[c]['si'] = 0

with open('full.json', 'w') as f:
    f.write('var classes = ')
    json.dump(classes, f)
    f.write(';')

        
        
        