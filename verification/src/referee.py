from checkio_referee import RefereeRank, ENV_NAME



import settings_env
from tests import TESTS


class Referee(RefereeRank):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "good_radix"
    FUNCTION_NAMES = {
        "python_3": "good_radix",
        "js_node": "goodRadix"
    }
    ENV_COVERCODE = {
        
    }