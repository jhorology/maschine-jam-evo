from Maschine_Jam.MidiMap import USER_MODE
from PushPadScale import PushPadScale

# MODE Id
PUSH_PAD_MODE = USER_MODE + 1

# Ableton Push compatible scales + additional scales
PUSH_SCALES = (
    PushPadScale('Major',            (0, 2, 4, 5, 7, 9, 11)),
    PushPadScale('Minor',            (0, 2, 3, 5, 7, 8, 10)),
    PushPadScale('Dorian',           (0, 2, 3, 5, 7, 9, 10)),
    PushPadScale('Mixolydian',       (0, 2, 4, 5, 7, 9, 10)),
    PushPadScale('Lydian',           (0, 2, 4, 6, 7, 9, 11)),
    PushPadScale('Phrygian',         (0, 1, 3, 5, 7, 8, 10)),
    PushPadScale('Locrian',          (0, 1, 3, 5, 6, 8, 10)),
    PushPadScale('Diminished',       (0, 1, 3, 4, 6, 7,  9, 10)),
    PushPadScale('Whole-half',       (0, 2, 3, 5, 6, 8,  9, 11)),
    PushPadScale('Whole Tone',       (0, 2, 4, 6, 8, 10)),
    PushPadScale('Minor Blues',      (0, 3, 5, 6, 7,10)),
    PushPadScale('Minor Pentatonic', (0, 3, 5, 7, 10)),
    PushPadScale('Major Pentatonic', (0, 2, 4, 7, 9)),
    PushPadScale('Harmonic Minor',   (0, 2, 3, 5, 7, 8, 11)),
    PushPadScale('Melodic Minor',    (0, 2, 3, 5, 7, 9, 11)),
    PushPadScale('Super Locrian',    (0, 1, 3, 4, 6, 8, 10)),
    PushPadScale('Bhairav',          (0, 1, 4, 5, 7, 8, 11)),
    PushPadScale('Hungarian Minor',  (0, 2, 3, 6, 7, 8, 11)),
    PushPadScale('Minor Gypsy',      (0, 1, 4, 5, 7, 8, 10)),
    PushPadScale('Hirojoshi',        (0, 2, 3, 7, 8)),
    PushPadScale('In-Sen',           (0, 1, 5, 7, 10)),
    PushPadScale('Iwato',            (0, 1, 5, 6, 10)),
    PushPadScale('Kumoi',            (0, 2, 3, 7, 9)),
    PushPadScale('Pelog',            (0, 1, 3, 4, 7, 8)),
    PushPadScale('Spanish',          (0, 1, 3, 4, 5, 6, 8,10)),

    # additional scale
    PushPadScale('Okinawan Pentatonic', (0, 4, 5, 7, 11)),
    PushPadScale('Okinawan Hexatonic',  (0, 2, 4, 5, 7, 11))
)
