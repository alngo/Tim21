import sys
import os

root_path = os.path.join(os.path.dirname(__file__), '..')
broker_path = os.path.join(root_path, 'tim21/brokers/')

sys.path.insert(0, os.path.abspath(root_path))
sys.path.insert(0, os.path.abspath(broker_path))

import tim21  # noqa # pylint: disable=unused-import, wrong-import-position
