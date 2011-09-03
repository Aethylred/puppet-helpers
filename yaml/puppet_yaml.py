# vim: set fileencoding=utf-8 :
#
# (C) 2011 Guido Guenther <agx@sigxcpu.org>
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# Minimal set of classes to parse puppet reports
#
# Reports are usually stored in /var/lib/puppet/reports/ on the puppet server.
# To  enable sending reports put:
#
# [agent]
#  report = true
#
# in the client's /etc/puppet/puppet.conf

import yaml

class PuppetReport(yaml.YAMLObject):
    yaml_tag = u'!ruby/object:Puppet::Transaction::Report'

class PuppetLog(yaml.YAMLObject):
    yaml_tag = u'!ruby/object:Puppet::Util::Log'

class PuppetMetric(yaml.YAMLObject):
    yaml_tag = u'!ruby/object:Puppet::Util::Metric'

class PuppetResource(yaml.YAMLObject):
    yaml_tag = u'!ruby/object:Puppet::Resource::Status'

    def get_type(self):
        return self.resource.split('[')[0]

    def get_name(self):
        return self.resource.split('[')[1][:-1]

class PuppetTransaction(yaml.YAMLObject):
    yaml_tag = u'!ruby/object:Puppet::Transaction::Event'

# Treat ruby symbols as simple strings
def variable_constructor(loader, value):
    """Turn '!ruby/sym' into a simple strings"""
    return str(value.value)
yaml.add_constructor(u'!ruby/sym', variable_constructor)

def load(*args, **kwargs):
    return yaml.load(*args, **kwargs)

# vim:et:ts=4:sw=4:et:sts=4:ai:set list listchars=tab\:»·,trail\:·:
