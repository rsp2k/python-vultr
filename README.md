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
|Function|Implementation|Tested|
|:-------:|:-------:|:------:|
|vultr.account.account_info|Y|Y|
