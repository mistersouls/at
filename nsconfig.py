from pydantic import BaseModel, Field
from typing import Annotated, List

class NsConfig(BaseModel):
    force: Annotated[bool, Field(title="Force", description="Configurations will be cleared without prompting for confirmation.")]
    level: Annotated[str, Field(title="Level", description="Types of configurations to be cleared. Possible values: basic, extended, full")]
    rbaconfig: Annotated[str, Field(title="RBA Config", description="RBA configurations and TACACS policies bound to system global will not be cleared if RBA is set to NO. Default is YES, which will clear RBA configurations. Possible values: YES, NO")]
    ipaddress: Annotated[str, Field(title="IP Address", description="IP address of the Citrix ADC. Minimum length: 1")]
    netmask: Annotated[str, Field(title="Netmask", description="Netmask corresponding to the IP address.")]
    nsvlan: Annotated[float, Field(title="NSVLAN", description="VLAN for the subnet on which the IP address resides. Minimum value: 2, Maximum value: 4094")]
    ifnum: Annotated[List[str], Field(title="Interfaces", description="Interfaces of the appliances that must be bound to the NSVLAN. Minimum length: 1")]
    tagged: Annotated[str, Field(title="Tagged", description="Specifies that the interfaces will be added as 802.1q tagged interfaces. Possible values: YES, NO")]
    httpport: Annotated[List[int], Field(title="HTTP Ports", description="The HTTP ports on the Web server. Minimum value: 1")]
    maxconn: Annotated[float, Field(title="Max Connections", description="The maximum number of connections to the web server(s). Minimum value: 0, Maximum value: 4294967294")]
    maxreq: Annotated[float, Field(title="Max Requests", description="The maximum number of requests on a particular connection. Minimum value: 0, Maximum value: 65535")]
    cip: Annotated[str, Field(title="Client IP Insertion", description="Control the insertion of the actual client IP address into the HTTP header request. Possible values: ENABLED, DISABLED")]
    cipheader: Annotated[str, Field(title="Client IP Header", description="The text that will be used as the client IP header. Minimum length: 1")]
    cookieversion: Annotated[str, Field(title="Cookie Version", description="The version of the cookie inserted by the system. Possible values: 0, 1")]
    securecookie: Annotated[str, Field(title="Secure Cookie", description="Enable/disable secure flag for persistence cookie. Default: ENABLED, Possible values: ENABLED, DISABLED")]
    pmtumin: Annotated[float, Field(title="Minimum Path MTU", description="The minimum Path MTU. Default: 576, Minimum value: 168, Maximum value: 1500")]
    pmtutimeout: Annotated[float, Field(title="PMTU Timeout", description="The timeout value in minutes. Default: 10, Minimum value: 1, Maximum value: 1440")]
    ftpportrange: Annotated[str, Field(title="FTP Port Range", description="Port range configured for FTP services. Minimum length: 1024, Maximum length: 64000")]
    crportrange: Annotated[str, Field(title="Cache Redirection Port Range", description="Port range for cache redirection services. Minimum length: 1, Maximum length: 65535")]
    timezone: Annotated[str, Field(title="Timezone", description="Name of the timezone. Default: CoordinatedUniversalTime, Minimum length: 1, Maximum length: 64")]
    grantquotamaxclient: Annotated[float, Field(title="Grant Quota Max Client", description="The percentage of shared quota to be granted at a time for maxClient. Default: 10, Minimum value: 0, Maximum value: 100")]
    exclusivequotamaxclient: Annotated[float, Field(title="Exclusive Quota Max Client", description="The percentage of maxClient to be given to PEs. Default: 80, Minimum value: 0, Maximum value: 100")]
    grantquotaspillover: Annotated[float, Field(title="Grant Quota Spillover", description="The percentage of shared quota to be granted at a time for spillover. Default: 10, Minimum value: 0, Maximum value: 100")]
    exclusivequotaspillover: Annotated[float, Field(title="Exclusive Quota Spillover", description="The percentage of max limit to be given to PEs. Default: 80, Minimum value: 0, Maximum value: 100")]
    all: Annotated[bool, Field(title="All Partitions", description="Use this option to do saveconfig for all partitions.")]
    config1: Annotated[str, Field(title="Config 1", description="Location of the configurations.")]
    config2: Annotated[str, Field(title="Config 2", description="Location of the configurations.")]
    outtype: Annotated[str, Field(title="Output Type", description="Format to display the difference in configurations. Possible values: cli, xml")]
    template: Annotated[bool, Field(title="Template", description="File that contains the commands to be compared.")]
    ignoredevicespecific: Annotated[bool, Field(title="Ignore Device Specific", description="Suppress device specific differences.")]
    weakpassword: Annotated[bool, Field(title="Weak Password", description="Option to list all weak passwords (not adhering to strong password requirements).")]
    changedpassword: Annotated[bool, Field(title="Changed Password", description="Option to list all passwords changed which would not work when downgraded to older releases.")]
    config: Annotated[str, Field(title="Config File", description="Configuration File to be used to find weak passwords.")]
    message: Annotated[str, Field(title="Message", description=".")]
    mappedip: Annotated[str, Field(title="Mapped IP", description="Mapped IP Address of the System. Minimum length: 1")]
    range: Annotated[float, Field(title="Range", description="The range of Mapped IP addresses to be configured. Minimum value: 1")]
    svmcmd: Annotated[float, Field(title="SVM Command", description="Identifies the source of command. Default value: 0")]
    systemtype: Annotated[str, Field(title="System Type", description="The type of the System. Possible Values: Stand-alone, HA, Cluster.")]
    primaryip: Annotated[str, Field(title="Primary IP", description="HA Master Node IP address.")]
    primaryip6: Annotated[str, Field(title="Primary IP6", description=".")]
    flags: Annotated[float, Field(title="Flags", description="The flags for this entry.")]
    lastconfigchangedtime: Annotated[str, Field(title="Last Config Changed Time", description="Time when the configuration was last modified.")]
    lastconfigsavetime: Annotated[str, Field(title="Last Config Save Time", description="Time when the configuration was last saved.")]
    currentsytemtime: Annotated[str, Field(title="Current System Time", description="Current system time in date format.")]
    systemtime: Annotated[float, Field(title="System Time", description="Current system time.")]
    configchanged: Annotated[bool, Field(title="Config Changed", description="Returns True if configuration has changed since last saved config.")]
    response: Annotated[str, Field(title="Response", description=".")]

    class Config:
        schema_extra = {
            "example": {
                "force": True,
                "level": "basic",
                "rbaconfig": "YES",
                "ipaddress": "192.168.1.1",
                "netmask": "255.255.255.0",
                "nsvlan": 100,
                "ifnum": ["eth0", "eth1"],
                "tagged": "YES",
                "httpport": [80, 8080],
                "maxconn": 100,
                "maxreq": 1000,
                "cip": "ENABLED",
                "cipheader": "X-Client-IP",
                "cookieversion": "1",
                "securecookie": "ENABLED",
                "pmtumin": 576,
                "pmtutimeout": 10,
                "ftpportrange": "1024-2048",
                "crportrange": "1024-2048",
                "timezone": "CoordinatedUniversalTime",
                "grantquotamaxclient": 10,
                "exclusivequotamaxclient": 80,
                "grantquotaspillover": 10,
                "exclusivequotaspillover": 80,
                "all": True,
                "config1": "/etc/nsconfig/config1",
                "config2": "/etc/nsconfig/config2",
                "outtype": "cli",
                "template": True,
                "ignoredevicespecific": True,
                "weakpassword": False,
                "changedpassword": False,
                "config": "/etc/nsconfig/ns.conf",
                "message": "",
                "mappedip": "192.168.1.100",
                "range": 10,
                "svmcmd": 0,
                "systemtype": "Standalone",
                "primaryip": "192.168.1.1",
                "primaryip6": "::1",
                "flags": 1,
                "lastconfigchangedtime": "2025-02-26T18:00:00Z",
                "last
