from Maschine_Jam.PadScale import PadScale, BASE_NOTE_FIX_COLOR

class PushPadScale(PadScale, object):
    def __init__(self, name, notevalues, colorconverter = None):
        super(PushPadScale, self).__init__(name, notevalues, colorconverter)

    # Override
    def convert_color(self, midi_note, base_note, color = (36, 39)):
        if self._colorconverter:
            return self._colorconverter(midi_note, base_note, color)
        elif midi_note % 12 != base_note:
            return BASE_NOTE_FIX_COLOR
        else:
            return color[1]

    # Override
    def set_grid_map(self, base_note, start_pitch, next_pitch_direction = 0):
        self._note_to_grid_map = {}
        base_grid_pitch = start_pitch
        start_pitch_index = (base_grid_pitch - base_note) % 12
        if start_pitch_index not in self._map:
            base_grid_pitch = self._next_scale_index(start_pitch, base_note, next_pitch_direction)
        pitch = base_grid_pitch
        count = 0
        while count < 8:
            index = (pitch - base_note) % 12
            if index in self._map:
                self._note_to_grid_map[pitch] = 7 - count
                self._grid_to_note_map[7 - count] = pitch
                count += 1
            pitch += 1

        return base_grid_pitch
