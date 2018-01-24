.. index::
  Prism; Prism support modifier fixed for game modes/maps
  Prism; Lost prism supports no longer contribute to the firing beam
  Prism; Constructing/selling towers are no longer eligible to be support towers
  Bugs; Prism Tower support fixed
  Bugs; Prism Support Modifier corruption

==================
Prism Support Bugs
==================
+ Whenever a game mode or map declared the :tag:`[General]` section without
  re-stating the :tag:`PrismSupportModifier`, the :tag:`PrismSupportModifier`
  from :file:`rulesmd.ini` would get multiplied by 100, thus causing supported
  Prism Towers to deal extremely high damage. This bug is now fixed. It should
  be noted that several official maps which used to exhibit this bug were
  already 'fixed' by the UMP by re-stating :tag:`PrismSupportModifier=150%` in
  each affected map. As a result of the UMP fixes, these maps are now set at the
  original 150%, regardless of what your mod may set it to. If you want to
  change this then you should manually override the global modifier via
  :game:`Ares`' new Prism Forwarding logic. This can be done simply by adding a
  single flag to the Prism Tower:
  :tag:`[ATESLA]PrismForwarding.SupportModifier=whatever`
+ Once a Prism Tower had decided to support another, the firing tower gained
  that tower's benefit. If the supporting tower was destroyed or otherwise
  incapacitated, the firing tower would still get the full benefit of that
  tower, even though there are no visual effects drawn (and the supporting tower
  may even have started supporting another). :game:`Ares` fixes this so that
  incapacitated supporting towers do not contribute to the firing tower.
+ Prism Towers could be made to support another during their construction or
  selling phases. This caused graphical glitches with the tower. :game:`Ares`
  prevents these towers from supporting others.

.. versionadded:: 0.2
