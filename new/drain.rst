Drain Weapon Options
~~~~~~~~~~~~~~~~~~~~

Unlike defensive structures or refineries, draining power plants always affects
the player's entire power, not just what is produced locally. :game:`Ares` adds
some tags to make this customizable.

:tagdef:`[TechnoType]Drain.Local=boolean`
  Whether this unit drains only the local power from its target building, or
  whether this building does not bring down the entire power grid of the owning
  player when drained. If any of the draining unit or the building drained have
  this set to :value:`yes`, only the local power is drained. If both have this
  set to :value:`no`, then the victim's entire power is drained. Defaults to
  :value:`no`.

:tagdef:`[TechnoType]Drain.Amount=integer`
  The amount of power drained from a power plant of the victim player. Requires
  :tag:`Drain.Local=yes` on either the draining unit or the drained building. If
  positive, this is the maximum amount of power drained. If negative, this is
  the minimum amount of power drained. Defaults to :value:`0`.

  The start value is the victim building's :tag:`Power`, then the draining
  unit's :tag:`Drain.Amount` is applied, and finally the drained building's
  :tag:`Drain.Amount`.

For example: draining a Power Plant with :tag:`Power=500` and
:tag:`Drain.Amount=0` using a Floating Disk.

With :tag:`Drain.Amount=-1000` on the disk, it will drain 1000, with
:tag:`Drain.Amount=0` it will drain the 500 the building produces, and with
:tag:`Drain.Amount=200` on the disk it will drain 200.

If the building would have :value:`Drain.Amount=-600`, it would never drain less
than 600. If the building had :tag:`Drain.Amount=800`, it would never drain more
than 800.

.. index:: Drain; Drain only the local power plant.
.. index:: Drain; Drain a customizable amount of power.

.. versionadded:: 0.6
