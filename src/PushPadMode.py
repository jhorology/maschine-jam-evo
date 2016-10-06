from Maschine_Jam.PadMode import PadMode
from Maschine_Jam.PadScale import PadScale
from Maschine_Jam.MidiMap import ND_KEYBOARD1, BASE_NOTE
from Maschine_Jam.MaschineMode import MaschineMode
from const import PUSH_SCALES, PUSH_PAD_MODE
from _Framework.InputControlElement import *
from _Framework.SubjectSlot import subject_slot

class PushPadMode(PadMode):

    def __init__(self, button_index, monochrome = False, *a, **k):
        super(PushPadMode, self).__init__(button_index, monochrome, *a, **k)
        self._note_display_mode = ND_KEYBOARD1
        self._base_note = 0
        self._octave = 2
        self.current_scale_index = 0
        self._is_monochrome = monochrome
        self._scale = PUSH_SCALES[self.current_scale_index]
        self.assign_transpose(PUSH_SCALES[self.current_scale_index])
        self._focus_track = None
        return

    # Override
    @property
    def get_scale(self):
        """
        :rtype : PadScale
        """
        return PUSH_SCALES[self.current_scale_index]

    # Override
    def get_color(self, value, column, row):
        color = self._get_ref_color()
        button = self.canonical_parent.get_button_matrix().get_button(column, row)
        if button is not None:
            if button.state == 0:
                return 0
            scale = PUSH_SCALES[self.current_scale_index]
            return scale.convert_color(button.get_identifier(), self._base_note, color)
        else:
            return

    # Override
    def get_mode_id(self):
        return PUSH_PAD_MODE

    # Override
    def ext_name(self):
        return 'push_pad_mode'

    # Override
    def inc_base_note(self, inc):
        new_value = self._base_note + inc
        if new_value < 0:
            new_value = 11
            self._octave = max(0, self._octave - 1)
        elif new_value > 11:
            new_value = 0
            self._octave = self._octave + 1
        self._base_note = new_value
        scale = PUSH_SCALES[self.current_scale_index]
        self.canonical_parent.show_message(" PAD Mode Scale: %s %s%s" % (scale.name, BASE_NOTE[self._base_note], str(self._octave - 2)))
        self.update_transpose()

    # Override
    def inc_octave(self, inc):
        new_value = self._octave + inc
        if new_value >= 0 and new_value < 8:
            self._octave = new_value
            scale = PUSH_SCALES[self.current_scale_index]
            self.update_transpose()
            self.canonical_parent.show_message(" PAD Mode Scale: %s %s%s"  % (scale.name, BASE_NOTE[self._base_note], str(self._octave - 2)))

    # Override
    def inc_scale(self, inc, update = True):
        nr_of_scales = len(PUSH_SCALES) - 1
        prev_value = self.current_scale_index
        self.current_scale_index = min(nr_of_scales, max(0, self.current_scale_index + inc))
        if prev_value != self.current_scale_index:
            newscale = PUSH_SCALES[self.current_scale_index]
            self.canonical_parent.show_message(" PAD Mode Scale: %s %s%s"  % (newscale.name, BASE_NOTE[self._base_note], str(self._octave - 2)))
            if update:
                self.update_transpose()

    # Override
    def get_octave(self):
        return PUSH_SCALES[self.current_scale_index].to_octave(self._octave)

    # Override
    def update_transpose(self):
        if self._active:
            self.clear_transpose()
            self.assign_transpose(PUSH_SCALES[self.current_scale_index])
            self.canonical_parent._set_suppress_rebuild_requests(True)
            self.canonical_parent.request_rebuild_midi_map()
            self.canonical_parent._set_suppress_rebuild_requests(False)

    def assign_transpose(self, scale):
        assert isinstance(scale, PadScale)
        self._scale = scale
        scale_len = len(scale.notevalues)
        octave = self._octave
        if self._active:
            for button, (column, row) in self.canonical_parent.get_button_matrix().iterbuttons():
                if button:
                    if button.state == 0:
                        button.remove_value_listener(self._dummy_lister)
                    note_index = (7 - row) * 3 + column
                    scale_index = note_index % scale_len
                    octave_offset = note_index / scale_len
                    note_value = scale.notevalues[scale_index] + self._base_note + octave * 12 + octave_offset * 12
                    if note_value < 128:
                        button.set_to_notemode(True)
                        button.set_send_note(note_value)
                        button.state = 1
                        button.send_value(0, True)
                    else:
                        button.set_send_note(button.get_identifier())
                        button.set_to_notemode(False)
                        button.state = 0
                        button.add_value_listener(self._dummy_lister)
                        button.send_color_direct(0)

