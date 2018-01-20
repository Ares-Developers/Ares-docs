Toggle Power
~~~~~~~~~~~~

The power toggling feature has been removed from :game:`Red Alert 2`, and thus
neither the sidebar button nor the power off building overlay were available.
A workaround using a fake super weapon was possible, but it did not work well.
:game:`Ares` adds this feature back (though not the sidebar button).

.. versionadded:: 0.8


Keyboard Command
----------------

Toggle Power is now available as a proper keyboard command, which functions like
clicking the corresponding button in the :game:`Tiberian Sun` sidebar. You can
find it in the category :value:`Interface`.

By default, this keyboard command is disabled: Even though it is shown and can
be configured, it will not do anything. This is to maintain compatibility with
the original :game:`Yuri's Revenge`, which didn't have this command available.

:tagdef:`[General]TogglePowerAllowed=boolean`
  Whether Toggle Power can be used. Defaults to :value:`no`.

.. index:: Toggle Power; Keyboard command


Cursors
-------

The two mouse cursors this feature uses can be customized with the following
:doc:`Mouse Cursor </new/mousecursors>` definitions:

:value:`TogglePower`: Shown if the building's power status can be toggled. Only
buildings owned by the player can toggle the power, if :tag:`TogglePower=yes`
and either :tag:`Power` is less than :value:`0` or :tag:`Powered=yes`.

:value:`NoTogglePower`: Shown if the building's power cannot be toggled.

.. index:: Toggle Power; Customizable cursors


Power Off Overlay Animation
---------------------------

If a building is powered down, :file:`poweroff.shp` is shown as overlay like the
repair wrench. Only the player owning this building as well as observers can see
this overlay, and other players will just see a building without power.

If a powered down building is repaired at the same time, both overlay animations
are moved to be shown simultaneously.

:file:`poweroff.shp` is drawn using the :file:`mousepal.pal` palette.

.. index:: Toggle Power; Overlay image for powered down buildings


AI Support
----------

If Toggle Power is enabled, the AI can also make use of it. The AI will try to
cope with power outages because of insufficient power output. AI players being
drained or suffering from a power blackout triggered by a spy or Force Shield
are exempt and will not try to turn off the base.

Base defenses are tried to be held online if possible. Super weapons are turned
off earlier than power consuming buildings that are not base defenses.

.. note:: Assume the order is unpredictable. Do not rely on the order in which
  the AI turns buildings off or back on. The implementation can change any time.

:tagdef:`[IQ]TogglePower=integer`
  Defines the IQ rating with which an AI player will toggle power of buildings
  in low power situations. Values less than :value:`0` deactivate this logic.
  Defaults to :value:`-1`.

:tagdef:`[General]TogglePowerDelay=integer - frames`
  Defines the delay between power checks. This makes AI players not respond
  immediately to power level changes. Values less than :value:`0` deactivate
  this logic. Defaults to :value:`45`.

.. index:: Toggle Power; AI can cope with low power
