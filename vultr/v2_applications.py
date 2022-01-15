'''Partial class to handle Vultr DNS API calls'''
from .utils import VultrBase, update_params


class VultrApp(VultrBase):
    '''Handles Vultr DNS API calls'''
    def __init__(self, api_key):
        VultrBase.__init__(self, api_key)

    def list_applications(self, params=None):
        params = params if params else dict()
        return self.request('/v2/applications', params, 'GET')
