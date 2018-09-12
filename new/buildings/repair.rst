.. index:: Buildings; Pause repair on insufficient funds

Repair and Insufficient Funds
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This global tag can be used to change how the repair mode works. By default, all
repairing is stopped once a player no longer has enough credits to afford it.
After gaining some credits, the buildings have to be ordered to repair again.
With this tag, repairing will pause, but not stop.

:tagdef:`[General]RepairStopOnInsufficientFunds=boolean`
  Whether repairing will automatically be stopped when the owning player has
  insufficient funds. If :value:`no`, repairing mode will not be turned off. The
  wrench will still be visible, even though the building is no longer actively
  repaired. Repairing will resume when the player gains more funds. This only
  affects human players. Defaults to :value:`yes`.

.. versionadded:: 0.D


.. index::
  Buildings; Not repairable by Engineers
  Engineer; Disallow instantly repairing a building

Buildings not repairable by Engineers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:tagdef:`[BuildingType]EngineerRepairable=boolean`
  Whether engineers can repair this building. If :value:`no`, the building might
  still be repaired by the normal building repair (:tag:`ClickRepairable=yes`),
  but Engineers cannot be used to restore full health instantly. Defaults to
  :tag:`Repairable`.

.. versionadded:: 2.0
