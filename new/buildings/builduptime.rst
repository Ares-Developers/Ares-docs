Buildup and Sell Time
~~~~~~~~~~~~~~~~~~~~~

The global setting :tag:`[General]BuildupTime` has been deglobalized and split
into two separate tags for construction and selling on :type:`BuildingTypes`.

Also, :game:`Ares` now supports make animations having more frames than the
buildup time without glitching. In case the buildup time is too short and it
would require skipping frames, the buildup time is automatically increased so
this does not happen anymore.

:tagdef:`[BuildingType]BuildupTime=double - minutes`
  The time the buildup animation plays regardless of the number of frames.
  Defaults to :tag:`[General]BuildupTime`.

  .. note:: Note that certain building functions still become available
    immediately after being placed, not only after being fully constructed.

:tagdef:`[BuildingType]SellTime=double - minutes`
  Analogous to :tag:`BuildTime` when a building is sold. Defaults to
  :tag:`BuildupTime`.

.. index:: Buildings; Deglobalized BuildupTime, separate SellTime

.. versionadded:: 0.D
