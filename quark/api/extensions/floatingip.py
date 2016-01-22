# Copyright (c) 2013 OpenStack Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from neutron.api import extensions
from neutron.api.v2 import attributes


def _validate_single_or_list_of_unique_strings(data, valid_values):
    if not isinstance(data, list):
        return attributes.validators['type:uuid_or_none'](data)
    else:
        return attributes.validators['type:uuid_list'](data)

attributes.validators['type:single_or_list_of_unique_strings'] = (
    _validate_single_or_list_of_unique_strings)

RESOURCE_NAME = "floatingip"
RESOURCE_COLLECTION = RESOURCE_NAME + "s"

EXTENDED_ATTRIBUTES_2_0 = {
    RESOURCE_COLLECTION: {
        'port_id': {'allow_post': True, 'allow_put': True,
                    'validate': {
                        'type:single_or_list_of_unique_strings': None
                    },
                    'is_visible': True, 'default': None,
                    'required_by_policy': True}
    }
}


class Floatingip(extensions.ExtensionDescriptor):
    """Extends Networks for quark API purposes."""

    @classmethod
    def get_name(cls):
        return "floatingip"

    @classmethod
    def get_alias(cls):
        return "floatingip"

    @classmethod
    def get_description(cls):
        return "Floating IPs"

    @classmethod
    def get_namespace(cls):
        return ("http://docs.openstack.org/network/ext/"
                "networks_quark/api/v2.0")

    @classmethod
    def get_updated(cls):
        return "2013-03-25T19:00:00-00:00"

    @classmethod
    def get_required_extensions(cls):
        return ['router']

    def get_extended_resources(self, version):
        if version == "2.0":
            return EXTENDED_ATTRIBUTES_2_0
        else:
            return {}
