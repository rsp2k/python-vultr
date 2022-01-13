'''Partial class to handle Vultr DNS API calls'''
from .utils import VultrBase, update_params


class VultrDNS(VultrBase):
    '''Handles Vultr DNS API calls'''
    def __init__(self, api_key):
        VultrBase.__init__(self, api_key)

    def list(self, params=None):
        params = params if params else dict()
        return self.request('/v2/domains', params, 'GET')

    def create_domain(self, domain, ipaddr, params=None):
        params = update_params(params, {'domain': domain,'ip': ipaddr})
        return self.request('/v2/domains', params, 'POST')

    def get_domain(self, domain, params=None):
        params = update_params(params, {'domain':domain})
        return self.request('/v2/domains/'+domain, 'GET')

    def delete_domain(self, domain, params=None):
        params = update_params(params, {'domain': domain})
        return self.request('/v2/domains/'+domain, params, 'DELETE')

    def update_domain():
        return self.request()

    def get_soa(self, domain, params=None):
        params = update_params(params, {'domain': domain})
        return self.request('/v2/domains/'+domain+'/soa', params, 'GET')

    def update_soa(self, domain, params=None):
        params = update_params(params, {'domain':domain})
        return self.request('/v2/domains/'+domain+'/soa',params,'PATCH')

    def get_dnssecinfo(self, domain, params=None):
        params = update_params(params, {'domain':domain})
        return self.request('/v2/domains/'+domain+'/dnssec',params,'GET')

    def create_record(self, domain, name, _type, data, params=None):
        params = update_params(params, {'name': name,'type': _type,'data': data})
        return self.request('/v2/domains/'+domain+'/records', params, 'POST')

    def list_records(self, domain, params=None):
        params = update_params(params, {'domain': domain})
        return self.request('v2/domains/'+domain+'/records', params, 'GET')

    def get_record(self, domain, recordid, params=None):
        params = update_params(params, {'domain': domain,'RECORDID': recordid})
        return self.request('/v2/domains/'+domain+'/records/'+recordid,params,'GET')

    def delete_record(self, domain, recordid, params=None):
        params = update_params(params, {'domain': domain,'RECORDID': recordid})
        return self.request('/v2/domains/'+domain+'/records/'+recordid, params, 'DELETE')

    def update_record(self, domain, recordid, params=None):
        params = update_params(params, {'domain': domain,'RECORDID': recordid})
        return self.request('/v2/domains/'+domain+'/records/'+recordid, params, 'PATCH')
