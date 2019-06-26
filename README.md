This project is intended as a testbed for bringing support for the Redfish (https://redfish.dmtf.org/) hardware management API to Salt (https://github.com/saltstack/salt).

## How to use

You just copy the grains module into your Salt Master's _grains directory (usually "/srv/salt/_grains") and the execution module into _modules (usually "/srv/salt/_modules").

Then you sync to a minion:

    salt "my_minion" saltutil.sync_all

You also need to provide the Redfish credentials either via a Pillar (not tested yet) or by adding the following to your minion's config (in "/etc/minion" or by adding a separate config file, e.g. "redfish.conf", into "/etc/minion.d"). The configuration looks like this:

    redfish:
        host: host_name_or_ip
        user: username
        pwd: password

## Limitations of the current prototype code

### Almost no inline documentation and no error handling

If you enter stuff the Redfish server won't understand, forget to set the credentials, whatever, there is no error handling apart from what Salt provides for free.

### Not "proxyfied" yet

Both the grains module and the execution module need to be installed on an existing minion.

For the grains module this may make sense if the idea is to augment the existing grains by grains collected via Redfish for the same system. But in general, it's probably a very bad idea to assume that the Redfish connector is running on the OS that's installed on the very server you want to manage "out of band": If the OS is down, you can't reach your Redfish! And of course you can't do anything with Redfish _before_ the OS and minion are deployed.

The initial idea is to adapt those modules to become proxy-aware and use them from a **salt-proxy** instead.

### No certificate checking

To make initial development easier, SSL certificate checking is deactivated. This needs to be enabled for the shipping version, at least as the default option!

### Only works on tested hardware

Currently the code expects the system to be available as **redfish/v1/Chassis/System.Embedded.1**. In other server types there may be several server blades, which may have completely different names!

### No state module

At the moment you can only use this in Salt states via **module.run**. We'll need a proper state module if we want to support proper idempotency.

