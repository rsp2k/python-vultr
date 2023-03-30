'''Python library for the Vultr cloud API'''
from .utils import VultrBase
from .v2_account import VultrAcc
from .v2_applications import VultrApp
from .v2_backup import VultrBackup
from .v2_baremetal import VultrBareMetal
#from .v2_billing import VultrBilling
from .v2_blockstorage import VultrBlockStorage
from .v2_dns import VultrDNS
from .v2_firewall import VultrFirewall
from .v2_instances import VultrInstances
from .v2_iso import VultrISO
from .v2_kubernetes import VultrKubernetes
from .v2_loadbalancers import VultrLoadBalancers
from .v2_objectstorage import VultrObjectStorage
from .v2_operatingsystems import VultrOperatingSystems
from .v2_plans import VultrPlans
from .v2_privatenetworks import VultrPrivateNetworks
from .v2_regions import VultrRegions
from .v2_reservedips import VultrReservedIPs
from .v2_snapshots import VultrSnapshots
from .v2_sshkeys import VultrSSHKeys
from .v2_startupscripts import VultrStartupScripts
from .v2_users import VultrUsers

class Vultr(VultrBase):
	def __init__(self, api_key):
		VultrBase.__init__(self, api_key)
		self.account = VultrAcc(api_key)
		self.applications = VultrApp(api_key)
		self.backup = VultrBackup(api_key)
		self.baremetal = VultrBareMetal(api_key)
#		self.billing = VultrBilling(api_key)
		self.blockstorage = VultrBlockStorage(api_key)
		self.dns = VultrDNS(api_key)
		self.firewall = VultrFirewall(api_key)
		self.instances = VultrInstances(api_key)
		self.iso = VultrISO(api_key)
		self.kubernetes = VultrKubernetes(api_key)
		self.loadbalancers = VultrLoadBalancers(api_key)
		self.objectstorage = VultrObjectStorage(api_key)
		self.operatingsystems = VultrOperatingSystems(api_key)
		self.plans = VultrPlans(api_key)
		self.privatenetworks = VultrPrivateNetworks(api_key)
		self.regions = VultrRegions(api_key)
		self.reservedips = VultrReservedIPs(api_key)
		self.snapshots = VultrSnapshots(api_key)
		self.sshkeys = VultrSSHKeys(api_key)
		self.startupscripts = VultrStartupScripts(api_key)
		self.users = VultrUsers(api_key)
