.. index:: AI; Team retaliates if a member is attacked

Team Retaliate
~~~~~~~~~~~~~~

If a unit attacked a member of an idling team in :game:`Tiberian Sun` and didn't
kill it right away, the team would collectively retaliate against the offender.
This logic has been removed from :game:`Red Alert 2` and :game:`Ares` brings it
back as an optional feature.

While the original logic just ignored :type:`AircraftTypes`, the restored logic
also excludes :tag:`ConsideredAircraft=yes` units and parasites. Another
difference is that the team members' current targets are no longer reset when a
second offender attacks the team, which might prevent target juggling in case of
multiple attackers.

This feature can only be enabled globally using a tag to not change the original
game's behavior. Also, :game:`Ares` does not extend :type:`TeamTypes` yet to
allow custom tags per team.

:tagdef:`[General]TeamRetaliate=boolean`
  Whether teams are allowed to retaliate if a member is attacked and not killed
  immediately. Defaults to :value:`no`.

.. versionadded:: 0.7
