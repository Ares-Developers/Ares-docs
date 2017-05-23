:captiontag:`Type=PsychicDominator`
```````````````````````````````````

Default values for general tags:

:tagdef:`[SuperWeapon]SW.Range=float,integer`
  Area around the target location the Psychic Dominator captures. This does not
  affect the damage. Defaults to :tag:`[General]DominatorCaptureRange`.
:tagdef:`[SuperWeapon]SW.Damage=integer`
  The damage the Psychic Dominator delivers right before capturing. No damage is
  dealt if this value is 0 or negative. Defaults to
  :tag:`[General]DominatorDamage`.
:tagdef:`[SuperWeapon]SW.Warhead=Warhead`
  The warhead used to deal the damage. Defaults to
  :tag:`[General]DominatorWarhead`.
:tagdef:`[SuperWeapon]SW.Deferment=integer - frames`
  Defaults to :value:`0`.
:tagdef:`[SuperWeapon]SW.ActivationSound=Sound`
  Defaults to :tag:`[AudioVisual]PsychicDominatorActivateSound`.
:tagdef:`[SuperWeapon]SW.AITargeting=enum`
  Defaults to :value:`PsychicDominator`.
:tagdef:`[SuperWeapon]SW.AffectsHouse=enum`
  Specifies the houses affected by the capture. Defaults to :value:`all`.
:tagdef:`[SuperWeapon]SW.AffectsTarget=enum`
  Specifies which types the capture affects. Defaults to
  :value:`infantry,units`.
:tagdef:`[SuperWeapon]Light.*=integer`
  Default to the scenario's :tag:`[Lighting]Dominator*`.
:tagdef:`[SuperWeapon]Cursor=mouse cursor`
  Defaults to :value:`PsychicDominator`.


Psychic Dominator specific tags:

:tagdef:`[SuperWeapon]Dominator.FirstAnim=Animation`
  The Animation hovering above the target for some time before the Psychic
  Dominator strikes. Defaults to :tag:`[General]DominatorFirstAnim`.
:tagdef:`[SuperWeapon]Dominator.FirstAnimHeight=integer - leptons`
  The height the :tag:`Dominator.FirstAnim` is played above the ground. Defaults
  to :value:`750`.
:tagdef:`[SuperWeapon]Dominator.SecondAnim=Animation`
  The Animation hovering above the target when the Psychic Dominator strikes.
  Defaults to :tag:`[General]DominatorSecondAnim`.
:tagdef:`[SuperWeapon]Dominator.SecondAnimHeight=integer - leptons`
  The height the :tag:`Dominator.SecondAnim` is played above the ground.
  Defaults to :value:`0`.
:tagdef:`[SuperWeapon]Dominator.FireAtPercentage=integer`
  After this percentage of the :tag:`Dominator.FirstAnim`'s frames have been
  played, the Dominator is fired. This is the actual percentage, :value:`20` is
  20%. Don't use decimal numbers. Defaults to
  :tag:`[General]DominatorFireAtPercentage`.
:tagdef:`[SuperWeapon]Dominator.ControlAnim=Animation`
  The Animation displayed above units being mind-controlled by the Dominator
  permanently. Defaults to :tag:`[CombatDamage]PermaControlledAnimationType`.
:tagdef:`[SuperWeapon]Dominator.Capture=boolean`
  Defines whether this Psychic Dominator captures units in its range. Otherwise
  only the damage is dealt. Defaults to :value:`yes`.
:tagdef:`[SuperWeapon]Dominator.Ripple=boolean`
  Defines whether this Psychic Dominator creates a ripple effect when the
  Psychic Dominator strikes. Defaults to :value:`yes`.
:tagdef:`[SuperWeapon]Dominator.CaptureMindControlled=boolean`
  Defines whether this Psychic Dominator can capture units that are
  mind-controlled already. Otherwise already mind-controlled units are ignored.
  Defaults to :value:`yes`.
:tagdef:`[SuperWeapon]Dominator.CapturePermaMindControlled=boolean`
  Defines whether this Psychic Dominator can capture units that are permanently
  mind-controlled already. Otherwise already permanently mind-controlled units
  are ignored. Defaults to :value:`yes`.
:tagdef:`[SuperWeapon]Dominator.CaptureImmuneToPsionics=boolean`
  Defines whether this Psychic Dominator can capture units that usually aren't
  mind-controllable. Setting this to :value:`yes` ignores the
  :tag:`ImmuneToPsionics` tag on its victims. Defaults to :value:`no`.
:tagdef:`[SuperWeapon]Dominator.PermanentCapture=boolean`
  Defines whether the victims are permanently mind-controlled. Setting this to
  :value:`no` allows other mind-controllers to re-capture the victim, otherwise
  it will be uncapturable. Defaults to :value:`yes`.


.. versionadded:: 0.2
