User Interface Colors
~~~~~~~~~~~~~~~~~~~~~

To complement the graphical user interface elements :game:`Yuri's Revenge`
relies on a set of hardcoded colors. Customize the colors used to draw texts and
borders with these :game:`Ares` tags.

All these :file:`uimd.ini` tags are RGB colors, that is three comma separated
values from 0 to 255.

Please note the special combobox (dropdown list) state for dropdown lists in
Observer mode, that is it has its Observer entry selected.
:game:`Yuri's Revenge` uses grey colors and special graphical elements to denote
this state. Changing the global values will not change the Observer colors,
you'll have to define the specific :tag:`Color.Observer.*` tags.

:tagdef:`[UISettings]Color.Border1=R,G,B`
  The first color control borders are drawn in. Defaults to
  :value:`167,190,197`.
:tagdef:`[UISettings]Color.Border2=R,G,B`
  The second color control borders are drawn in. Defaults to
  :value:`104,122,128`.
:tagdef:`[UISettings]Color.Text=R,G,B`
  The default color all texts are drawn in. This does not affect Observer
  dropdown lists, see :tag:`Color.Observer.Text`. Defaults to :value:`255,255,0`
  (yellow).
:tagdef:`[UISettings]Color.X.Text=R,G,B`
  The text color for certain types of controls. :value:`X` can be one of
  :tag:`Button`, :tag:`Label` (descriptions), :tag:`List`, :tag:`Checkbox`,
  :tag:`Combobox` (dropdown lists), :tag:`Observer` (dropdown lists in with
  Observer selected), :tag:`Groupbox` (frames), :tag:`Slider`, or :tag:`Edit`
  (text boxes). Defaults to :value:`238,238,238` (light grey) for
  :tag:`Observer`, to :tag:`[UISettings]Color.Text` otherwise.
:tagdef:`[UISettings]Color.Selection=R,G,B`
  The default background color for selected items. This does not affect Observer
  dropdown lists, see :tag:`Color.Observer.Selection`. Defaults to
  :value:`255,0,0` (red).
:tagdef:`[UISettings]Color.X.Selection=R,G,B`
  The background color for selected items of certain types of controls.
  :value:`X` can be one of :tag:`List`, :tag:`Combobox` (dropdown lists) or
  :tag:`Observer` (dropdown lists in with Observer selected). Defaults to
  :value:`98,98,98` (dark grey) for :tag:`Observer`, to
  :tag:`[UISettings]Color.Selection` otherwise.
:tagdef:`[UISettings]Color.Disabled=R,G,B`
  The default color texts of disabled controls are drawn in. This does not
  affect the color of disabled buttons and Observer dropdown lists, see below.
  Defaults to :value:`159,0,0` (dark red).
:tagdef:`[UISettings]Color.X.Disabled=R,G,B`
  The text color of disabled controls of certain types. :value:`X` can be one of
  :tag:`Button`, :tag:`Label` (descriptions), :tag:`List`, :tag:`Checkbox`,
  :tag:`Combobox` (dropdown lists), :tag:`Observer` (dropdown lists in with
  Observer selected), or :tag:`Slider`. Defaults to :value:`167,0,0` (dark red)
  for :tag:`Button`, to :value:`143,143,143` (grey) for :tag:`Observer`, to
  :tag:`[UISettings]Color.Disabled` otherwise.

.. note:: This feature does not support recoloring the dialog prompting for the
  \ :game:`Yuri's Revenge` disk when starting the game.

.. index:: Interface; Custom User Interface Colors.

.. versionadded:: 0.2
