from __future__ import with_statement
from Maschine_Jam.JamModes import JamModes, MG_PAD, MG_CLIP
from Maschine_Jam.MidiMap import find_drum_device
from PushPadMode import PushPadMode
from _Framework.SubjectSlot import subject_slot

class JamEvoModes(JamModes):
    __pad_down = False
    
    def __init__(self, note_repeat = None, *a, **k):
        super(JamEvoModes, self).__init__(note_repeat, *a, **k)
        self._push_pad_mode = PushPadMode(1)
        self._push_pad_mode.enter_action = self.enter_push_pad_mode
        self._is_push_mode = False

    # Override
    def bind_modify_component(self, modifier_component):
        super(JamEvoModes, self).bind_modify_component(modifier_component)
        self._push_pad_mode.set_modifier_component(modifier_component)

    # Override
    def notify_shift(self, shift_value):
        if self._mode == self._push_pad_mode:
            self._push_pad_mode.handle_shift(shift_value)
        super(JamEvoModes, self).notify_shift(shift_value)

    # Override
    @subject_slot('value')
    def _do_pad_mode(self, value):
        if self.__pad_down and value == 0:
            if self._mode_group != MG_PAD:
                self._is_push_mode = self.is_shift_down()
                if self._is_push_mode:
                    self.enter_push_pad_mode()
                else:
                    self.enter_pad_mode()
            else:
                self.enter_clip_mode()
                self._mode_group = MG_CLIP
        self.__pad_down = value != 0

    # Override
    def selected_mode(self, value):
        if value == 'push_pad_mode':
            self.enter_push_pad_mode(False)
        else:
            super(JamEvoModes, self).selected_mode(value)

    # Override
    def __handle_possible_instrument_change(self):
        drum_device = find_drum_device(self.song().view.selected_track)
        if drum_device:
            if self._mode == self._pad_mode:
                self.enter_pad_mode()
            elif self._mode == self._push_pad_mode:
                self.enter_push_pad_mode()
            elif self._mode == self._step_mode:
                self.enter_step_mode(False, True)
        elif self._mode == self._drum_pad_mode:
            if self._is_push_mode:
                self.enter_push_pad_mode()
            else:
                self.enter_pad_mode()
        elif self._mode == self._drum_step_mode:
            self.enter_step_mode(False, True)

    def enter_push_pad_mode(self, show_info = True, check_drum_device = 0):
        if show_info:
            self._show_msg_callback('Push Style PAD Mode')
        selected_track = self.song().view.selected_track
        if not selected_track or not selected_track.has_midi_input:
            return
        drum_device = find_drum_device(selected_track)
        if drum_device:
            with self.rebuild():
                self._mode.exit()
                self._mode.spec_unbind()
                self._mode = self._drum_pad_mode
                self._light_button(1)
                self._mode.enter()
        else:
            with self.rebuild():
                self._mode.exit()
                self._mode.spec_unbind()
                self._mode = self._push_pad_mode
                self._light_button(1)
                self._mode.enter()
        self._mode_group = MG_PAD
