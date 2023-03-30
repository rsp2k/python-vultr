'''Partial class to handle Vultr DNS API calls'''
from .utils import VultrBase, update_params


class VultrBackup(VultrBase):
    '''Handles Vultr DNS API calls'''
    def __init__(self, api_key):
        VultrBase.__init__(self, api_key)

    def list_backups(self, params=None):
        params = params if params else dict()
        return self.request('/v2/backups', params, 'GET')

    def get_backup(self, backupid, params=None):
        params = params if params else dict()
        return self.request('/v2/backups/'+backupid, params, 'GET')

