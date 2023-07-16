from Music import CircleOfFifths
def test_circle_of_fifths():
    circle = CircleOfFifths()

    major_keys = {
        'C': [],
        'G': ['F#'],
        'D': ['F#', 'C#'],
        'A': ['F#', 'C#', 'G#'],
        'E': ['F#', 'C#', 'G#', 'D#'],
        'B': ['F#', 'C#', 'G#', 'D#', 'A#'],
        'F#': ['F#', 'C#', 'G#', 'D#', 'A#', 'E#'],
        'C#': ['F#', 'C#', 'G#', 'D#', 'A#', 'E#', 'B#'],
        'F': ['Bb'],
        'Bb': ['Bb', 'Eb'],
        'Eb': ['Bb', 'Eb', 'Ab'],
        'Ab': ['Bb', 'Eb', 'Ab', 'Db'],
        'Db': ['Bb', 'Eb', 'Ab', 'Db', 'Gb'],
        'Gb': ['Bb', 'Eb', 'Ab', 'Db', 'Gb', 'Cb'],
        'Cb': ['Bb', 'Eb', 'Ab', 'Db', 'Gb', 'Cb', 'Fb']
    }




    for key in major_keys:
        expected_accidentals = major_keys[key]
        accidentals = circle.get_accidentals(key)
        try:
            assert accidentals == expected_accidentals

        except AssertionError:
            print(f"Assertion failed for Key: {key}")
            print(f"Expected Accidentals: {expected_accidentals}")
            print(f"Actual Accidentals: {accidentals}")
            print("------")
    print('All tests Passed')

def test_all_major_scales():
    circle = CircleOfFifths()

    major_keys = ['C', 'G', 'D', 'A', 'E', 'B', 'F#', 'C#',
                  'F', 'Bb', 'Eb', 'Ab', 'Db', 'Gb', 'Cb']

    major_scales = [
        ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
        ['G', 'A', 'B', 'C', 'D', 'E', 'F#'],
        ['D', 'E', 'F#', 'G', 'A', 'B', 'C#'],
        ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'],
        ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#'],
        ['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#'],
        ['F#', 'G#', 'A#', 'B', 'C#', 'D#', 'E#'],
        ['C#', 'D#', 'E#', 'F#', 'G#', 'A#', 'B#'],
        ['F', 'G', 'A', 'Bb', 'C', 'D', 'E'],
        ['Bb', 'C', 'D', 'Eb', 'F', 'G', 'A'],
        ['Eb', 'F', 'G', 'Ab', 'Bb', 'C', 'D'],
        ['Ab', 'Bb', 'C', 'Db', 'Eb', 'F', 'G'],
        ['Db', 'Eb', 'F', 'Gb', 'Ab', 'Bb', 'C'],
        ['Gb', 'Ab', 'Bb', 'Cb', 'Db', 'Eb', 'F'],
        ['Cb', 'Db', 'Eb', 'Fb', 'Gb', 'Ab', 'Bb']
    ]


    all_tests_pass = True  # Variable to track test results
    for key, expected_scale in zip(major_keys, major_scales):
        scale = circle.generate_major_scale(key)
        try:
            assert scale == expected_scale
            print(f"{key} was Ok {scale}")
            print("------")
        except AssertionError:
            print(f"Assertion failed for Key: {key}")
            print(f"Expected Scale: {expected_scale}")
            print(f"Actual Scale: {scale}")
            print("------")
            all_tests_pass = False
            break
    if all_tests_pass:
        print("All tests pass")

def test_minor_scales():
    minor_scales = {
        'C': ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb'],
        'C#': ['C#', 'D#', 'E', 'F#', 'G#', 'A', 'B'],
        'D': ['D', 'E', 'F', 'G', 'A', 'Bb', 'C'],
        'Eb': ['Eb', 'F', 'Gb', 'Ab', 'Bb', 'Cb', 'Db'],
        'E': ['E', 'F#', 'G', 'A', 'B', 'C', 'D'],
        'F': ['F', 'G', 'Ab', 'Bb', 'C', 'Db', 'Eb'],
        'F#': ['F#', 'G#', 'A', 'B', 'C#', 'D', 'E'],
        'G': ['G', 'A', 'Bb', 'C', 'D', 'Eb', 'F'],
        'Ab': ['Ab', 'Bb', 'Cb', 'Db', 'Eb', 'Fb', 'Gb'],
        'A': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
        'Bb': ['Bb', 'C', 'Db', 'Eb', 'F', 'Gb', 'Ab'],
        'B': ['B', 'C#', 'D', 'E', 'F#', 'G', 'A']
    }
    minor_intervals = [0, 0, -1, 0, 0, -1, -1]
    for root_note, expected_scale in minor_scales.items():
        circle = CircleOfFifths()
        scale = circle.create_scale(root_note,minor_intervals)
        assert scale == expected_scale, f"Test failed for {root_note} minor scale. \r\n Expected: {expected_scale} \r\n output:{scale}"
    print('All test Passed')

def test_Harmonicminor_scales():
    harmonic_minor_scales = {
    'C': ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'B'],
    'C#': ['C#', 'D#', 'E', 'F#', 'G#', 'A', 'B#'],
    'D': ['D', 'E', 'F', 'G', 'A', 'Bb', 'C#'],
    'Eb': ['Eb', 'F', 'Gb', 'Ab', 'Bb', 'Cb', 'D'],
    'E': ['E', 'F#', 'G', 'A', 'B', 'C', 'D#'],
    'F': ['F', 'G', 'Ab', 'Bb', 'C', 'Db', 'E'],
    'F#': ['F#', 'G#', 'A', 'B', 'C#', 'D', 'E#'],
    'G': ['G', 'A', 'Bb', 'C', 'D', 'Eb', 'F#'],
    'Ab': ['Ab', 'Bb', 'Cb', 'Db', 'Eb', 'Fb', 'G'],
    'A': ['A', 'B', 'C', 'D', 'E', 'F', 'G#'],
    'Bb': ['Bb', 'C', 'Db', 'Eb', 'F', 'Gb', 'A'],
    'B': ['B', 'C#', 'D', 'E', 'F#', 'G', 'A#']
    }

    HarmonicMinor_intervals = [0, 0, -1, 0, 0, -1, 0]
    for root_note, expected_scale in harmonic_minor_scales.items():
        circle = CircleOfFifths()
        scale = circle.create_scale(root_note,HarmonicMinor_intervals)
        assert scale == expected_scale, f"Test failed for {root_note} Harmonic minor scale. \r\n Expected: {expected_scale} \r\n output:{scale}"
    print('All test Passed')

test_minor_scales()
test_Harmonicminor_scales()
#test_all_major_scales()
#test_circle_of_fifths()
# circle = CircleOfFifths()
# circle.get_accidentals('F')