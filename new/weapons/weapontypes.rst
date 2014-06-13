:captiontag:`[WeaponTypes]` Section
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This new section allows you to declare new weapons without having to declare a
dummy unit to parse them (like the official "WEEDGUY" hack). This works in the
same way as the existing ``[Warheads]`` section. Any :type:`WeaponType` listed
under the :tag:`[WeaponTypes]` section will be parsed by the game and can be
used as a shrapnel weapon or a new weapon in a game mode, etc.

.. versionadded:: 0.1
