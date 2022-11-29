"""Root `__init__` of the gymnasium module setting the `__all__` of gymnasium modules."""
# isort: skip_file

from gymnasium.core import (
    Env,
    Wrapper,
    ObservationWrapper,
    ActionWrapper,
    RewardWrapper,
)
from gymnasium.spaces.space import Space
from gymnasium.envs.registration import make, spec, register, registry, pprint_registry
from gymnasium import envs, spaces, utils, vector, wrappers, error, logger

import os
import sys

__all__ = [
    # core classes
    "Env",
    "Wrapper",
    "ObservationWrapper",
    "ActionWrapper",
    "RewardWrapper",
    "Space",
    # registration
    "make",
    "spec",
    "register",
    "registry",
    "pprint_registry",
    # root files
    "envs",
    "spaces",
    "utils",
    "vector",
    "wrappers",
    "error",
    "logger",
]
__version__ = "0.26.3"

# Initializing pygame initializes audio connections through SDL. SDL uses alsa by default on all Linux systems
# SDL connecting to alsa frequently create these giant lists of warnings every time you import an environment using
#   pygame
# DSP is far more benign (and should probably be the default in SDL anyways)

if sys.platform.startswith("linux"):
    os.environ["SDL_AUDIODRIVER"] = "dsp"

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

try:
    import gym_notices.notices as notices

    # print version warning if necessary
    notice = notices.notices.get(__version__)
    if notice:
        print(notice, file=sys.stderr)
except Exception:  # nosec
    pass