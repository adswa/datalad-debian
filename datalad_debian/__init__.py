"""DataLad Debian extension"""

__docformat__ = 'restructuredtext'

# defines a datalad command suite
# this symbold must be indentified as a setuptools entrypoint
# to be found by datalad
command_suite = (
    # description of the command suite, displayed in cmdline help
    "DataLad for working with Debian packages",
    [
        (
            'datalad_debian.new_distribution',
            'NewDistribution',
            'deb-new-distribution',
            'deb_new_distribution',
        ),
        (
            'datalad_debian.new_package',
            'NewPackage',
            'deb-new-package',
            'deb_new_package',
        ),
    ]
)

from datalad import setup_package
from datalad import teardown_package

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
