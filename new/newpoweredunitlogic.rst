New Powered Unit Logic
~~~~~~~~~~~~~~~~~~~~~~

In original Yuri's Revenge, the `PowersUnit=` tag logic dictated that
there could only be one powered unit, and one building providing
power, per side. Ares replaces this tag with `PoweredBy=`, which
allows each side to have multiple buildings power multiple units.

:[UnitType]PoweredBy=: Allows multiple powered units to exist, as well
  as allowing multiple buildings to provide power.


.. versionadded:: 0.2

NB: Be advised, if a powered unit is being built when the powers.units
building is destroyed, the immobile unit will jam up that WarFactory
until destruction or powers.units building is rebuilt.

NB: `PowersUnit=` is usable but obsolete in Ares. Therefore features
using `PowersUnit=` won't be supported by the BugTracker or RenProj in
general.

NB: `PoweredBy=` can use multiple buildings, but be advised, using a
comma to separate multiple buildings will be parsed as "or" rather
than "and". There is no "and" capacity.
