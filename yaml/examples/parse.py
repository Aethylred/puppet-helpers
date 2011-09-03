#!/usr/bin/python -u
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
# Simple example to print package updates

import sys
import puppet_yaml

def main(argv):
    f = file(argv[1])
    report = puppet_yaml.load(f.read())

    print report.host
    for resource in report.resource_statuses.values():
        if resource.get_type() == "Package":
            for event in resource.events:
                print ("Changed %s from %s to %s, status: %s" 
                       % (resource.get_name(),
                          event.previous_value,
                          event.desired_value,
                          event.status))

if __name__ == '__main__':
    sys.exit(main(sys.argv))

# vim:et:ts=4:sw=4:et:sts=4:ai:set list listchars=tab\:»·,trail\:·:
