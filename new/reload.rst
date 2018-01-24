.. index::
  Ammo; Reload and empty reload amounts
  TechnoTypes; Reload and empty reload amounts

:captiontag:`ReloadAmount` and :captiontag:`EmptyReloadAmount`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The game has options for :tag:`Reload` and :tag:`EmptyReload` to define how long
it takes to reload one round of ammunition, depending on whether the unit still
has ammo left. :game:`Ares` adds two new tags to define how many rounds of
ammunition are restored.

This logic is not supported on :type:`AircraftTypes`.

:tagdef:`[TechnoType]ReloadAmount=integer`
  The number of rounds restored after each reload interval. Negative values are
  supported. Defaults to :value:`1`.

:tagdef:`[TechnoType]EmptyReloadAmount=integer`
  The number of rounds restored after reload interval when there is no ammo
  left. If :value:`0` or negative, the unit will not reload. This does not
  require :tag:`EmptyReload` to be set. Defaults to :tag:`ReloadAmount`.

.. versionadded:: 0.B
