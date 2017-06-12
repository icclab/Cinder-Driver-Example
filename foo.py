__author__ = 'anke'

from oslo_config import cfg
from oslo_log import log as logging
from cinder import interface
from cinder.volume import driver

LOG = logging.getLogger(__name__)
CONF = cfg.CONF
ENABLE_TRACE = False

volume_opts = []

CONF = cfg.CONF
CONF.register_opts(volume_opts)

@interface.volumedriver
class FooDriver(driver.VolumeDriver):

    VERSION = '3.0.0'

    def __init__(self, *args, **kwargs):
        super(FooDriver, self).__init__(*args, **kwargs)
        self.configuration.append_config_values(volume_opts)

    def logmsg(self, string):
        LOG.debug(string)

    def create_volume(self, volume):
        self.logmsg('create/n')

    def update_volume(self, volume):
        self.logmsg('update/n')

    def delete_volume(self, volume):
        self.logmsg('delete/n')

    def get_vol_by_id(self, volume):
        self.logmsg('get vol by id/n')

    def get_vols(self):
        self.logmsg('get vols/n')

    def attach_volume(self):
        self.logmsg('attach/n')

    def check_for_setup_error(self):
        self.logmsg('check for setup error/n')

    def clone_image(self):
        self.logmsg('clone/n')

    def copy_image_to_volume(self):
        self.logmsg('img to vol/n')

    def copy_volume_to_image(self):
        self.logmsg('vol to img/n')

    def detach_volume(self):
        self.logmsg('detach vol /n')

    def do_setup(self, context):
        self.logmsg('do setup /n')

    def extend_volume(self):
        self.logmsg('extend vol /n')

    def get_volume_stats(self, refresh=False):
         ret = {
             'volume_backend_name': 'foo',
             'vendor_name': 'bar',
             'driver_version': '3.0.0',
             'storage_protocol': 'foobar',
             'total_capacity_gb': 42,
             'free_capacity_gb': 42
         }
         self.logmsg('updating backend stats')
         return ret

    def initialize_connection(self):
        self.logmsg('init con /n')

    def terminate_connection(self):
        self.logmsg('terminate con /n')

