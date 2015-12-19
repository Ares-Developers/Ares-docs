.. index:: Maps; Player @ X support for map events

===========================================================
:captiontag:`Player @ X` Support for Multiplayer Map Events
===========================================================

Map events have been expanded to support :value:`Player @ X` numeric constants
:value:`4475` to :value:`4482` for the multiplayer participants 1 to 8. If a
constant does not resolve to a valid player (that is, the player slot is not
empty and the player has not been defeated yet), the game will not crash any
more like before. Instead, the event will just not fire.

.. note:: \ :type:`ScriptTypes`, :type:`TeamTypes`, and :type:`TriggerTypes`
  still do not support ownership using :value:`Player @ X` logic.

.. versionadded:: 0.A
