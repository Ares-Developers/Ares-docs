.. index::
  Radial Indicators; Customizable for structures and units
  Units; Radial Indicator support

Radial Indicators
~~~~~~~~~~~~~~~~~

Radial Indicators were a feature for buildings that could visualize the range of
its weapons or of some ranged effect it provided like a Stealh Generator. The
radius was determined automatically by checking certain functions the building
had, and it could only be turned on or off using a setting.

With :game:`Ares` it is possible to customize the range with a setting, which
could be used to override the automatically picked radius, or to give a Radial
Indicator to a building that by default would not have one. Radial Indicators
can now also be enabled for units.

:tagdef:`[TechnoType]RadialIndicatorRadius=integer - cells`
  Overrides the radius of the radial indicator for this unit or structure.
  Requires :tag:`HasRadialIndicator=yes`. The default is determined by the game.

  .. note:: Units only support non-sweeping, non-concentric radial indicators.

.. versionadded:: 3.0
