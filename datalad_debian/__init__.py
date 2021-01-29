"""DataLad Debian extension"""

__docformat__ = 'restructuredtext'

import logging
lgr = logging.getLogger('datalad.debian')

# Defines a datalad command suite.
# This variable must be bound as a setuptools entrypoint
# to be found by datalad
command_suite = (
    # description of the command suite, displayed in cmdline help
    "DataLad for working with Debian packages",
    []
)

from datalad import setup_package
from datalad import teardown_package

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

