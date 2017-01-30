# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2017 CERN.
#
# Invenio is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

"""Invenio module that adds PID relations to the Invenio-PIDStore module."""

PIDRELATION_RELATION_TYPE_TITLES = {
    'ORDERED': 'Ordered',
    'UNORDERED': 'Unordered',
    'VERSION': 'Version',
}

PIDRELATIONS_RELATION_TYPES = {
    'ORDERED': 0,
    'UNORDERED': 1,
    'VERSION': 2,
}
"""Relation types definition."""

# TODO: Remove after refactorinf
# PIDRELATIONS_RELATION_TYPES = dict(
#     VERSION=0,
#     COLLECTION=1,
#     RECORD_DRAFT=2,
# )

PIDRELATIONS_DEFAULT_VALUE = 'foobar'
"""Default value for the application."""

PIDRELATIONS_INDEXED_RELATIONS = dict(
    recid=dict(
        field='version',
        api='invenio_pidrelations.versions_api:PIDVersioning',
        # FIXME: for now the API does not provide any way to know if a relation
        # is ordered or not. Thus we write it here.
        ordered=True,
    )
)
"""Default PID fetcher."""
