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
