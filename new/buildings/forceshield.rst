.. index::
  Force Shield; Effect duration per building
  Buildings; Force Shield effect duration

Force Shield
~~~~~~~~~~~~

Like the Iron Curtain the Force Shield duration can be customized for each
:type:`BuildingType`.

:tagdef:`[BuildingType]ForceShield.Modifier=float - multiplier`
  The number of seconds of Force Shield duration is multiplied by this value.
  Valid values are :value:`0%` (Force Shield disallowed) or higher. Defaults to
  :value:`100%`.

  .. note:: Buildings with a :tag:`ForceShield.Modifier` value of :value:`0.0`
    or less are not eligible to fire a Force Shield super weapon on.

.. versionadded:: 0.6
.. versionchanged:: 0.8
