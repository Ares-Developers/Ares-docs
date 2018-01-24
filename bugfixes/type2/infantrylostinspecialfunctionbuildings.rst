.. index::
  Armory; Infantry still inside a Hospital or Armory may go into limbo
  Hospital; Infantry still inside a Hospital or Armory may go into limbo
  Tech Structures; Infantry still inside a Hospital or Armory may go into limbo

===========================================
Infantry Lost In Special Function Buildings
===========================================

Infantry sent into an Armory or old-style Tech Hospital emerge a few moments
later, having had the relevant benefit applied (e.g. promotion or healing).
However, if the building were destroyed, sold or undeployed whilst the
:type:`InfantryType` were still inside then that :tag:`InfantryType` would
remain in 'limbo' whilst still counting towards the owning player's units (e.g.
defeat conditions, build limit, etc). :game:`Ares` will make sure that such
:type:`InfantryTypes` are ejected from the building in those situations.

.. versionadded:: 0.1
