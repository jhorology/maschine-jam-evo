import Live
from Maschine_Jam.MaschineJam import MaschineJam
from Maschine_Jam.MidiMap import debug_out, register_sender, PAD_TRANSLATIONS, FEEDBACK_CHANNELS
from Maschine_Jam.EncoderComponent import EncoderComponent
from Maschine_Jam.ModifierComponent import ModifierComponent
from JamEvoModes import JamEvoModes

# supported NI script version
NI_SCRIPT_VERSION = '########## LIVE 9 Maschine JAM V 1.00 #############'

class MaschineJamEvo(MaschineJam):
    def __init__(self, c_instance):
        super(MaschineJam, self).__init__(c_instance)
        with self.component_guard():
            self._suppress_send_midi = True
            register_sender(self)
            self._challenge = Live.Application.get_random_int(0, 400000000) & 2139062143
            self._set_suppress_rebuild_requests(True)
            self._c_ref = c_instance
            self.request_rebuild_midi_map()
            self._main_mode_container = JamEvoModes(c_instance.note_repeat)
            self._set_suppress_rebuild_requests(False)
            self._active = True
            self._display_device_param = False
            self._setup_transport()
            self._setup_session()
            self._encoder_modes = EncoderComponent(self._session)
            self._encoder_modes.connect()
            self._encoder_modes.set_state_listener(self)
            self._modifier = ModifierComponent(self._session)
            self._connect_session()
            self._main_mode_container.bind_session()
            self._main_mode_container.bind_modify_component(self._modifier)
            self._setup_mainjogwheel()
            self._init_m4l()
            self.set_pad_translations(PAD_TRANSLATIONS)
            self.set_feedback_channels(FEEDBACK_CHANNELS)
            self._suppress_send_midi = False
            self._main_mode_container._step_mode.set_mode_elements(self._modifier, self._encoder_modes)
            self._main_mode_container._drum_step_mode.set_mode_elements(self._modifier)
            self._final_init()
        
    # Override
    def _final_init(self):
        super(MaschineJamEvo, self)._final_init()
        assert self._last_message and self._last_message == NI_SCRIPT_VERSION, "Unsupported NI script version. %s" % self._last_message
        debug_out('########## LIVE 9 Maschine JAM Evoluzione 0.01 #############')
        
    # Override
    def log_message(self, message):
        self._last_message = message
        super(MaschineJamEvo, self).log_message(message)
