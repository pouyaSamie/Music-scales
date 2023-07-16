class CircleOfFifths:
    def __init__(self):
        self.sharps = ['C', 'G', 'D', 'A', 'E', 'B', 'F#', 'C#']
        self.flats = ['F', 'Bb', 'Eb', 'Ab', 'Db', 'Gb', 'Cb', 'Fb']
        self.sharp_orders = ['F', 'C', 'G', 'D', 'A', 'E', 'B']
        self.flat_orders = ['B', 'E', 'A', 'D', 'G', 'C', 'F']
        self.notes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    def get_accidentals(self, key):
        if key in self.sharps:
            index = self.sharps.index(key)
            return [note + '#' for note in self.sharp_orders[:index]]
        elif key in self.flats:
            index = self.flats.index(key)
            return [note + 'b' for note in self.flat_orders[:index + 1]]
        else:
            return []

    def get_natural_scale(self, key):
        key_index = self.notes.index(key)
        return self.notes[key_index:] + self.notes[:key_index]

    def generate_major_scale(self, root):

        accidentals = self.get_accidentals(root)
        scale_notes = self.get_natural_scale(root[0])
        scale_notes = [next((accidental for accidental in accidentals if note[0] == accidental[0]), note) for note in self.get_natural_scale(root[0])]
        return scale_notes

    def transpose(self,note, interval):
        note_equivalents = {
                            'C': {'Natural': 'C', 'Flat': 'Cb', 'Sharp': 'C#'},
                            'C#': {'Natural': 'C#', 'Flat': 'C', 'Sharp': 'Cx'},
                            'Db': {'Natural': 'Db', 'Flat': 'C#', 'Sharp': 'D'},
                            'D': {'Natural': 'D', 'Flat': 'Db', 'Sharp': 'D#'},
                            'D#': {'Natural': 'D#', 'Flat': 'D', 'Sharp': 'Dx'},
                            'Eb': {'Natural': 'Eb', 'Flat': 'D#', 'Sharp': 'E'},
                            'E': {'Natural': 'E', 'Flat': 'Eb', 'Sharp': 'E#'},
                            'F': {'Natural': 'F', 'Flat': 'Fb', 'Sharp': 'F#'},
                            'F#': {'Natural': 'F#', 'Flat': 'F', 'Sharp': 'Fx'},
                            'Gb': {'Natural': 'Gb', 'Flat': 'F#', 'Sharp': 'G'},
                            'G': {'Natural': 'G', 'Flat': 'Gb', 'Sharp': 'G#'},
                            'G#': {'Natural': 'G#', 'Flat': 'G', 'Sharp': 'Gx'},
                            'Ab': {'Natural': 'Ab', 'Flat': 'G#', 'Sharp': 'A'},
                            'A': {'Natural': 'A', 'Flat': 'Ab', 'Sharp': 'A#'},
                            'A#': {'Natural': 'A#', 'Flat': 'A', 'Sharp': 'Ax'},
                            'Bb': {'Natural': 'Bb', 'Flat': 'A#', 'Sharp': 'B'},
                            'B': {'Natural': 'B', 'Flat': 'Bb', 'Sharp': 'B#'},
                            'E#': {'Natural': 'E#', 'Flat': 'E', 'Sharp': 'Ex'},
                            'B#': {'Natural': 'B#', 'Flat': 'B', 'Sharp': 'Bx'}
                        }
        if note not in note_equivalents:
            return None

        if interval == -1:
            return note_equivalents[note]['Flat']
        elif interval == 1:
            return note_equivalents[note]['Sharp']
        else:
            return note_equivalents[note]['Natural']

    def create_scale(self,key, intervals):
        major_scale = self.generate_major_scale(key)
        
        minor_scale = []

        for i, note in enumerate(major_scale):
            transposed_note = self.transpose(note, intervals[i])
            minor_scale.append(transposed_note)

        return minor_scale
