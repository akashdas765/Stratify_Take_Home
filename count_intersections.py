def count_intersections(radians, identifiers):
    chords = {}
    for r, id in zip(radians, identifiers):
        pre, i = id.split('_')
        if i not in chords:
            chords[i] = [None, None]  
        if pre == 's':
            chords[i][0] = r  
        else:
            chords[i][1] = r  

    events = []
    for i, (s, e) in chords.items():
        start = ('start', s, i)
        events.append(start)
        
        end = ('end', e, i)
        events.append(end)
    
    events.sort(key=lambda x: (x[1], x[0] == 'end'))

    chords_Act = set() 
    count_intersect = 0

    for etype, i, chord_id in events:
        if etype == 'start':
            s, e = chords[chord_id]
            for active_id in chords_Act:
                start_a, end_a = chords[active_id]

                if (start_a < s < end_a) != (start_a < e < end_a):
                    count_intersect += 1
            chords_Act.add(chord_id)
        else:
            chords_Act.remove(chord_id)

    return count_intersect