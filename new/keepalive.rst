.. index:: Players; Keep alive in Short Games

Keep Alive
~~~~~~~~~~

Originally, all :tag:`Insignificant=no` and :tag:`DontScore=no` buildings keep
players alive in Short Games, excluding fake vehicles like Slave Miners and
deployable tanks and artilleries, and only these, aside from vehicles in the
:tag:`BaseUnit` list.

Using :game:`Ares` you can customize this set by including insignificant
buildings, fake as well as actual vehicles and even infantry or aircraft, or by
removing certain buildings that should not keep players alive despite being
significant.

As long as a player owns at least one object that keeps alive, a Short Game will
not count as lost.

:tagdef:`[TechnoType]KeepAlive=boolean`
  Whether an object of this type will keep the owning player alive, independent
  of :tag:`DontScore=` and :tag:`Insignificant=`. Defaults to :value:`yes` for
  :tag:`Insignificant=no` and :tag:`DontScore=no` buildings, to :value:`no`
  otherwise (including all units, infantry and aircraft).

  .. note:: No matter this setting, :type:`VehicleType`\ s contained in the
    \ :tag:`[General]BaseUnit=` list will always keep the player alive during
    Short Games. This might change in the future.

.. versionadded:: 3.0
