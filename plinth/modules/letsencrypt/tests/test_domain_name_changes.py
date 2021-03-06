#
# This file is part of Plinth.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
"""
Tests for letsencrypt module.
"""

import os
import os.path
import unittest

from .. import on_domain_added, on_domain_removed

euid = os.geteuid()
sudo_available = os.path.isfile("/usr/bin/sudo")


@unittest.skipUnless(sudo_available, 'Requires sudo')
class TestDomainNameChanges(unittest.TestCase):
    """Test for automatically obtaining and revoking Let's Encrypt certs"""

    @unittest.skipUnless(euid == 0, 'Needs to be root')
    def test_add_onion_domain(self):
        self.assertFalse(
            on_domain_added('test', 'hiddenservice', 'ddddd.onion'))

    @unittest.skipUnless(euid == 0, 'Needs to be root')
    def test_add_valid_domain(self):
        self.assertTrue(
            on_domain_added('test', 'domainname', 'subdomain.domain.tld'))

    @unittest.skipUnless(euid == 0, 'Needs to be root')
    def test_remove_domain(self):
        self.assertTrue(on_domain_removed('test', '', 'somedomain.tld'))
