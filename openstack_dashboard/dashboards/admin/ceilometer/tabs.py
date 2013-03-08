# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2012 Canonical Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from django.utils.translation import ugettext_lazy as _

from horizon import tabs

from openstack_dashboard import api

from .tables import DiskUsageTable, NetworkUsageTable


class DiskUsageTab(tabs.TableTab):
    table_classes = (DiskUsageTable,)
    name = _("Global Disk Usage")
    slug = "global_disk_usage"
    template_name = ("admin/ceilometer/table_with_date_selectors.html")

    def get_global_disk_usage_data(self):
        request = self.tab_group.request
        result = api.ceilometer.global_disk_usage(request)
        return result


class NetworkUsageTab(tabs.TableTab):
    table_classes = (NetworkUsageTable,)
    name = _("Global Network Usage")
    slug = "global_network_usage"
    template_name = ("admin/ceilometer/table_with_date_selectors.html")

    def get_global_network_usage_data(self):
        request = self.tab_group.request
        result = api.ceilometer.global_network_usage(request)
        return result


class CeilometerOverviewTabs(tabs.TabGroup):
    slug = "ceilometer_overview"
    tabs = (DiskUsageTab, NetworkUsageTab,)
    sticky = True
