# -*- coding: utf-8 -*-
'''
Created on Mar 11, 2012

@author: moloch

    Copyright 2012 Root the Box

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
'''


from uuid import uuid4
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.types import Unicode, Integer
from models import dbsession, Team, snapshot_team_to_flag, snapshot_team_to_game_level
from models.BaseGameObject import BaseObject


class SnapshotTeam(BaseObject):
    '''
    Used by game history; snapshot of a single team in history
    '''

    team_id = Column(Integer, ForeignKey("team.id"), nullable=False)
    money = Column(Integer, nullable=False)
    game_levels = relationship("GameLevel", secondary=snapshot_team_to_game_level, backref=backref("SnapshotTeam", lazy="joined"))
    flags = relationship("Flag", secondary=snapshot_team_to_flag, backref=backref("SnapshotTeam", lazy="joined"))

    @property
    def name(self):
        return dbsession.query(Team._name).filter_by(id=self.team_id).first()[0]