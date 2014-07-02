# -*- coding: utf-8 -*-

class Monster:
    """A class for the monster.

    Attributes:
        name: A string indicating the name of the monster.
        uuid: A string containing a UUID associated with the monster.
        type_name: A string indicating what elemental type the monster is.
        moves: A list of instances of the Move class that can be used.
    """

    def __init__(self, name, uuid, type_name, moves):
        """Inits Monster with name, uuid, type_name, moves."""
        self.name = name
        self.uuid = uuid
        self.type_name = type_name
        self.moves = moves

class Move:
    """A class for moves.

    Moves can be used by monsters in battle.

    Attributes:
        name: A string indicating the name of the move.
        type_name: A string indicating what elemental type the move is.
        effect: A string indicating what the move does.
        dmg: An integer indicating how powerful the move is
    """

    def __init__(self, name, type_name, effect, dmg):
        """Inits Move with name, type_name, effect, dmg."""
        self.name = name
        self.type_name = type_name
        self.effect = effect
        self.dmg = dmg
