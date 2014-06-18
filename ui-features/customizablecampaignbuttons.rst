Customizable Campaign Buttons
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With :game:`Ares` you can have up to four campaign buttons on :game:`Yuri's
Revenge`'s campaign selection menu and customize all of them in
:file:`uimd.ini`.

.. image:: /images/ui_campaignbuttons.jpg
  :alt: Campaign menu showing four campaign buttons
  :align: center

.. index:: Interface; Third Button / Campaign Button Customization.


You can customize all campaign buttons using these :file:`uimd.ini` tags by
replacing :tag:`X` by the numbers from :tag:`1` to :tag:`4`:

:tagdef:`[UISettings]CampaignX=battle`
  The mission from :file:`battle.ini` started by clicking the image button. To
  hide a button set :tag:`CampaignX=no`. Defaults to :value:`ALL1`,
  :value:`SOV1`, :value:`TUT1` or :value:`no` respectively.
:tagdef:`[UISettings]CampaignX.Image=filename, *including* the .shp extension`
  The 260x136 image shown on the campaign selection menu. Have a look at
  :file:`fsalg.shp` to see an example. Defaults to :value:`fsalg.shp` or
  :value:`fsslg.shp` respectively.
:tagdef:`[UISettings]CampaignX.Palette=filename, *including* the .pal extension`
  The palette used to render the image. Defaults to :value:`fsalg.pal`,
  :value:`fsslg.pal` or :value:`fsbclg.pal` respectively.
:tagdef:`[UISettings]CampaignX.Subline=CSF label`
  The subline displayed beneath the campaign image. To override the default
  value set this to a label containing no text. Defaults to
  :value:`STT:AlliedCampaignIcon`, :value:`STT:SovietCampaignIcon` or
  :value:`STT:CampaignAnimTutorial` respectively.
:tagdef:`[UISettings]CampaignX.Tooltip=CSF label`
  The text displayed as tooltip when the player hovers over the image. To
  override the default value set this to a label containing no text. Defaults to
  :tag:`CampaignX.Subline`.

:game:`Ares` defaults to the original game's values so you don't have to change
anything. To display a third button just add the above tags for
:tag:`Campaign3`.

Three buttons are arranged in a triangle formation: one centered in the upper
row, two in the lower one. If you want to have an upside-down triangle, skip
:tag:`Campaign3` and use :tag:`Campaign4` instead. Four campaigns are always
ordered left to right, top to bottom.

To control the sound that is played when the player hovers over the image see
:tag:`HoverSound=` on :doc:`/ui-features/campaignlist`.

.. quickstart:: If you want to have a third campaign button to start the
  tutorial mission, set :tag:`[UISettings]Campaign3.Image=fsbclg.shp`. You will
  have to rework that image, as there is no :game:`Yuri's Revenge` style version
  of it.

.. versionadded:: 0.2
