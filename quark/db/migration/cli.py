# Copyright 2014 Openstack Foundation
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from neutron.db.migration import cli

import os


def main():
    config = cli.alembic_config.Config(
        os.path.join(os.path.dirname(__file__), 'alembic.ini')
    )
    config.set_main_option('script_location',
                           'quark.db.migration:alembic')
    # attach the Neutron conf to the Alembic conf
    config.neutron_config = cli.CONF

    cli.CONF()
    #TODO(gongysh) enable logging
    cli.legacy.modernize_quantum_config(cli.CONF)
    cli.CONF.command.func(config, cli.CONF.command.name)