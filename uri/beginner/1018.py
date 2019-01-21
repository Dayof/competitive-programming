notes = [100, 50, 20, 10, 5, 2, 1]
aux_notes = list(notes)
notes_res = {k:0 for k in notes}

n = int(input())

aux, f_note = n, notes.pop(0)
while aux != 0:
    if aux-f_note >= 0:
        aux -= f_note
        notes_res[f_note] += 1
    elif len(notes) != 0:
        f_note = notes.pop(0)

print(n)
for k in aux_notes:
    print(notes_res[k], 'nota(s) de R$ %d,00' % k)