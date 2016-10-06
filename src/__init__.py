from MaschineJamEvo import MaschineJamEvo

def create_instance(c_instance):
    return MaschineJamEvo(c_instance)


from _Framework.Capabilities import *

def get_capabilities():
    return {
        CONTROLLER_ID_KEY: controller_id(vendor_id=9000, product_ids=[2], model_name='Maschine JAM'),
        PORTS_KEY: [
            inport(props=[HIDDEN, NOTES_CC, SCRIPT]),
            inport(props=[]),
            outport(props=[HIDDEN, NOTES_CC, SYNC, SCRIPT]),
            outport(props=[])
        ]
    }
