from backend.core.utils.collections import deep_update
from backend.core.utils.settings import get_settings_from_environment


# globals() is a dictionary of global variables

deep_update(globals(), get_settings_from_environment(ENVVAR_SETTINGS_PREFIX))
