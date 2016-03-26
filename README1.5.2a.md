# Thorpy-1.5.2a

ThorPy is a free GUI library intended for use with pygame. Extract thorpy folder for use, or see installation explanations on http://www.thorpy.org.

Changelog for ThorPy 1.5.2a:
-bar have been removed, as they were not consistent with the concepts of the library.
-set_active(value) and set_visible(value) methods have been added to elements.
-checker's get_text method has been fixed.
-stick_to method now handle rects as target argument.
-metada structure for storing data on the application. Metadata is now py27-proof for exceptions handling.
-get_application() function added to ThorPy.
-get_current_menu() function added to ThorPy.
-drawgrid.py added to gamestools.
-get_launcher() function added.
-fixed slider bug in make's method that did not correctly handled 'value' argument.
-added TogglablePool and RadioPool for managing logical dynamics of array of mutual-exclusive elements.
-lift rank is infinite by default so no element is drawn behind it
-fixed a bug on jailing system (new prisons overhided old ones)