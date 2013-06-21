---------------
Migration Guide
---------------

If you are upgrading from previous versions of :game:`Ares`, you may have to
account for the following changes.

From Ares 0.1
~~~~~~~~~~~~~

Changed tags:

  :tag:`[Superweapon]SW.Deliver` --> :tag:`[Superweapon]Deliver.Types`.
    Replace the old tag name by the new tag name.
  
  :tag:`[Superweapon]SW.DeliverBuildups` --> :tag:`[Superweapon]Deliver.Buildups`.
    Replace the old tag name by the new tag name.
  
  :tag:`[Superweapon]SonarPulse.Range` --> :tag:`[Superweapon]SW.Range`.
    Replace the old tag name by the new tag name.
  
  :tag:`[Superweapon]GenericWarhead.Warhead` --> :tag:`[Superweapon]SW.Warhead`.
    Replace the old tag name by the new tag name.
  
  :tag:`[Superweapon]GenericWarhead.Damage` --> :tag:`[Superweapon]SW.Damage`.
    Replace the old tag name by the new tag name.
  
  :tag:`[Superweapon]Nuke.Sound` --> :tag:`[Superweapon]SW.ActivationSound`.
    Replace the old tag name by the new tag name.

Other changes:

  :game:`Ares` 0.1 supported options in :file:`ares.ini` to configure how
  graphics surfaces were allocated. The tags :tag:`Surface.*.Memory` and
  :tag:`Surface.*.Force3D` are obsolete now and have no effect any more.

From Ares 0.2 and below
~~~~~~~~~~~~~~~~~~~~~~~

Changed tags:

  No changes required.

Other changes:

  The ini file reader has been updated for :game:`Ares` 0.3. Values that were
  invalid previously might now be valid, and previously valid notations might
  have become invalid. If values cannot be parsed correctly, :game:`Ares`
  puts a message to the debug log.

  For example, it was possible to supply only one or two numbers when three
  comma separated numbers were expected. In that case, the value became
  inconsistent. This is no longer allowed and will result in a message in the
  debug log.
