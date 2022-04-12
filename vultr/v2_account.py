'''Partial class to handle Vultr DNS API calls'''
from .utils import VultrBase, update_params


class VultrAcc(VultrBase):
    '''Handles Vultr DNS API calls'''
    def __init__(self, api_key):
        VultrBase.__init__(self, api_key)

    def account_info(self, params=None):
        params = params if params else dict()
        return self.request('/v2/account', params, 'GET')

