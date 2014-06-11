Score Screens and Themes
~~~~~~~~~~~~~~~~~~~~~~~~

Campaign
--------

The campaign score screen consists of four elements, a background, a transition
piece, an animation, and a palette file for all three.

:tagdef:`[Side]CampaignScore.Background=filename, *including* the .shp extension`
  A 632x568 image used as the background. Uses the palette defined as
  :tag:`CampaignScore.Palette`. Defaults to :value:`ASCRBKMD.SHP`,
  :value:`SSCRBKMD.SHP` or :value:`SYCRBKMD.SHP` for sides 1, 2 and all others
  respectively.

:tagdef:`[Side]CampaignScore.Transition=filename, *including* the .shp extension`
  An image used as a transition from the looping animation to the statc
  background image. Played backwards for the opposite case. Uses the palette
  defined as :tag:`CampaignScore.Palette`. Defaults to :value:`ASCRTMD.SHP`,
  :value:`SSCRTMD.SHP` or :value:`SYCRTMD.SHP` for sides 1, 2 and all others
  respectively.

:tagdef:`[Side]CampaignScore.Animation=filename, *including* the .shp extension`
  An image played as a loop after the introductory transition until the dialog
  is closed. The exact looping point is not known. Uses the palette defined as
  :tag:`CampaignScore.Palette`. Defaults to :value:`ASCRAMD.SHP`,
  :value:`SSCRAMD.SHP` or :value:`SYCRAMD.SHP` for sides 1, 2 and all others
  respectively.

:tagdef:`[Side]CampaignScore.Palette=filename, *including* the .pal extension`
  The palette to draw all animations on the campaign score screen. Defaults to
  :value:`ASCORE.PAL`, :value:`SSCORE.PAL` or :value:`YSCORE.PAL` for sides 1, 2
  and all others respectively.

The music piece played on the campaign score screen can be customized with the
following tags. :game:`Ares` can differentiate themes on whether the player
finished the mission in under par time.

:tagdef:`[Side]CampaignScore.UnderParTheme=theme id`
  The theme playing for this side when a player finishes a campaign mission
  quicker than the defined par time. Defaults to :value:`SCORE`.

:tagdef:`[Side]CampaignScore.OverParTheme=theme id`
  The theme playing for this side when a player finishes a campaign mission
  slower than the defined par time. Defaults to :value:`SCORE`.

.. versionadded:: 0.7


Multiplayer
-----------

The multiplayer score screen consists of a background drawn with a special
palette, and ten pcx bar images.

:tagdef:`[Side]MultiplayerScore.Background=filename, *including* the .shp extension`
  A 632x568 image used as the background. Uses the palette defined as
  :tag:`MultiplayerScore.Palette`. Defaults to :value:`MPASCRNL.SHP`,
  :value:`MPSSCRNL.SHP` or :value:`MPYSCRNL.SHP` for sides 1, 2 and all others
  respectively.

:tagdef:`[Side]MultiplayerScore.Palette=filename, *including* the .pal extension`
  The palette to draw the background of the multiplay score screen. Defaults to
  :value:`MPASCRN.PAL`, :value:`MPSSCRN.PAL` or :value:`MPYSCRN.PAL` for sides
  1, 2 and all others respectively.

:tagdef:`[Side]MultiplayerScore.Bars=filename, *including* the .pcx extension`
  The filename used as a pattern for the ten bars of 440x36 on the multiplayer
  score screen, two captions and up to eight players. Can contain :value:`~~`,
  which are replaced with a number from 01 to 10. Defaults to
  :value:`mpascrnlbar~~.pcx`, :value:`mpsscrnlbar~~.pcx` or
  :value:`mpyscrnlbar~~.pcx` for sides 1, 2 and all others respectively.

Depending on whether the player won or lost an alternative music theme can be
played.

:tagdef:`[Side]MultiplayerScore.WinTheme=theme id`
  The theme playing for this side when a player is victorious in a multiplayer
  match. Defaults to :value:`SCORE`.

:tagdef:`[Side]MultiplayerScore.LoseTheme=theme id`
  The theme playing for this side when a player is defeated in a multiplayer
  match. Defaults to :value:`SCORE`.

.. versionadded:: 0.7


Graphical Text Banner
---------------------

Instead of rendering a plain text on the screen as previous titles did,
:game:`Red Alert 2` used a graphic. Here this graphic can be customized for each
side.

The shp should have at least 4 frames: campaign won and lost, and multiplayer
won and lost.

:tagdef:`[Side]GraphicalText.Image=filename, *including* the .shp extension`
  The graphic file used as overlay to show whether a mission or match has been
  won or lost. The image is centered in the viewport and rendered in the palette
  defined as :tag:`GraphicalText.Palette`. Defaults to :value:`GRFXTXT.SHP`.

:tagdef:`[Side]GraphicalText.Palette=filename, *including* the .pal extension`
  The palette the graphical text image uses. The banner is actually rendered in
  the theater's palette and this palette is used to find the best match for the
  colors. Defaults to :value:`GRFXTXT.PAL`.

.. versionadded:: 0.7
