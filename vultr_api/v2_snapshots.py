'''Partial class to handle Vultr App API calls'''
from .utils import VultrBase, update_params


class VultrSnapshots(VultrBase):
    '''Handles Vultr App API calls'''
    def __init__(self, api_key):
        VultrBase.__init__(self, api_key)
