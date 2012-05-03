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

  :game:`Ares` 0.1 supported options in :file:`arda.ini` to configure how
  graphics surfaces were allocated. The tags :tag:`Surface.*.Memory` and
  :tag:`Surface.*.Force3D` are obsolete now and have no effect any more.
