# def transpose(note, interval):
#     # Define a dictionary to map notes to their integer representation
#     note_map = {'C': 0, 'C#': 1, 'Db': 1, 'D': 2, 'D#': 3, 'Eb': 3, 'E': 4, 'Fb': 4,
#                 'E#': 5, 'F': 5, 'F#': 6, 'Gb': 6, 'G': 7, 'G#': 8, 'Ab': 8, 'A': 9,
#                 'A#': 10, 'Bb': 10, 'B': 11, 'Cb': 11, 'B#': 0}

#     # Get the integer representation of the note
#     note_value = note_map[note]

#     # Calculate the transposed note value
#     transposed_value = (note_value + interval) % 12

#     # Find the note name corresponding to the transposed value
#     transposed_note = [k for k, v in note_map.items() if v == transposed_value][0]

#     return transposed_note
