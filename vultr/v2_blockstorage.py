'''Partial class to handle Vultr App API calls'''
from .utils import VultrBase, update_params


class VultrBlockStorage(VultrBase):
    '''Handles Vultr App API calls'''
    def __init__(self, api_key):
        VultrBase.__init__(self, api_key)

    def list_blockstorages(self, params=None):
        params = params if params else dict()
        return self.request('/v2/blocks', params, 'GET')

    def create_blockstorage(self, region, size, params=None):
        params = update_params(params, {'region':region,'size_gb':size})
        return self.request('/v2/blocks', params, 'POST')

    def get_blockstorage(self, blockid, params=None):
        params = params if params else dict()
        return self.request('/v2/blocks/'+blockid, params, 'GET')

    def delete_blockstorage(self, blockid, params=None):
        params = params if params else dict()
        return self.request('/v2/blocks/'+blockid, params, 'DELETE')

    def update_blockstorage(self, blockid, params=None):
        params = params if params else dict()
        return self.request('/v2/blocks'+blockid, params, 'PATCH')

    def attach_blockstorage(self, blockid, instanceid, params=None):
        params = update_params(params, {'instance_id':instanceid})
        return self.request('/v2/blocks/'+blockid+'/attach', params, 'POST')

    def detach_blockstorage(self, blockid, params=None):
        params = params if params else dict()
        return self.request('/v2/blocks/'+blockid+'/detach', params, 'POST')


