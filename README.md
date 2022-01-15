# Vultr

[![build status](https://travis-ci.org/spry-group/python-vultr.svg?branch=master)](https://travis-ci.org/spry-group/python-vultr)

Vultr provides a client library to the [Vultr.com](https://www.vultr.com/?ref=8914701) API.
This repo is a fork of an original library written for Vultr APIv1. 
I am re-doing this repo for APIv2.

## Usage

```python3
api_key = 'XXXXXXXXX'
vultr = Vultr(api_key)
plans_json = vultr.plans.list()
```
## Support

Python Vultr is supported on a volunteer basis.

* [Open an Issue](https://github.com/spry-group/python-vultr/issues/new)
* [![Gitter.im](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/spry-group/python-vultr)

## FUNCTIONS, IMPLEMENTATION AND TESTING (updated 13-Jan-2022)
*Keep checking this repo for updates as I add more APIv2 Functionality.
|API Module|Implementation|Tested|
|:-------:|:-------:|:------:|
|Account|Y|Y|
|Applications|Y|Y|
|Backup|Y|Y|
|Bare Metal|N|N|
|Billing|N|N|
|Block Storage|Y|N|
|DNS|Y|Y|
|Firewall|N|N|
|Instances|N|N|
|ISO|N|N|
|Kubernetes|N|N|
|Load Balancers|N|N|
|Object Storage|N|N|
|Operating Systems|N|N|
|Plans|N|N|
|Private Networks|N|N|
|Reserved IPs|N|N|
|Regions|N|N|
|Snapshots|N|N|
|SSH Keys|N|N|
|Startup Scripts|N|N|
|Users|N|N|
