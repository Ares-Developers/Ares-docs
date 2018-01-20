:captiontag:`CanPassiveAquire` Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following tags refine the way :tag:`CanPassiveAquire` works when a
human-controlled unit is in guard mode. It does not affect AI-controlled units.
Units can be made to effectively hold fire when in guard mode (and optionally
cloakable), yet pick their own targets when in area guard mode.

In :game:`Tiberian Sun`, this was the default for any unit, and it made Stealth
Tanks (or any other self-cloaking unit) not give away their position when an
enemy unit came into range.

Both tags require :tag:`CanPassiveAquire=yes` and do not work on buildings.
Units count as cloakable if they have :tag:`Cloakable=yes` set or were awarded
cloak ability through crates or as veteran or elite ability. The unit does not
have to be actually cloaked; also, passive mechanisms like Cloak Generators will
not be considered.

:tagdef:`[TechnoType]CanPassiveAquire.Guard=boolean`
  Whether this unit can acquire targets on their own when in guard mode. If set
  to :value:`no`, the unit will hold fire, but can be made to acquire own
  targets by putting it in area guard mode. Defaults to :value:`yes`.

:tagdef:`[TechnoType]CanPassiveAquire.Cloak=boolean`
  Whether this unit can acquire targets on their own when the unit is cloakable
  and in guard mode. If set to :value:`no`, the unit will hold fire if cloakable
  and in guard mode, but can be made to acquire own targets by putting it in
  area guard mode. :tag:`CanPassiveAquire.Guard=no` overrides this tag. Defaults
  to :value:`yes`.

Note that the second tag is more specific than the first as it means cloakable
*and* in guard mode. :tag:`CanPassiveAquire.Guard` is the tag that makes units
always hold their fire in guard mode, :tag:`CanPassiveAquire.Cloak` can be used
for units that should hold fire only if they gained the veteran or elite
ability or picked up a cloak crate.

.. note:: If :tag:`OpportunityFire=yes`, units will select targets while on the
  move, and start firing automatically. They will not lose the target again when
  reaching their destination and thus not stop firing.

.. note:: Also note the spelling of both tags. :game:`Ares` keeps the spelling
  error of :tag:`CanPassiveAquire` to stay consistent.

.. index:: CanPassiveAquire; Units hold fire in guard mode

.. versionadded:: 0.A
