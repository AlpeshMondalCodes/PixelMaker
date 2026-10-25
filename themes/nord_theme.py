"""
Nord Theme definitions for the Pixelator application.
An arctic, north-bluish color palette for calm, clean UI elements.
"""

COLORS = {
    "dark": {
        "bg_main": "#2e3440",           # nord0 - Polar Night dark
        "bg_card": "#242933",           # Deeper Polar Night
        "bg_inset": "#3b4252",          # nord1 - Polar Night inset
        "text_primary": "#eceff4",      # nord6 - Snow Storm light
        "text_secondary": "#d8dee9",    # nord4 - Snow Storm muted
        "accent_primary": "#88c0d0",    # nord8 - Frost Ice Blue
        "accent_primary_hover": "#81a1c1", # nord9 - Frost Blue
        "accent_secondary": "#a3be8c",  # nord14 - Aurora Green
        "accent_secondary_hover": "#8fbcbb", # nord7 - Frost Turquoise
        "accent_muted": "#4c566a",      # nord3 - Muted Slate
        "accent_muted_hover": "#434c5e",
        "border": "#434c5e",            # nord2 - Boundary
    },
    "light": {
        "bg_main": "#eceff4",           # nord6 - Snow Storm background
        "bg_card": "#ffffff",           # Pure white card
        "bg_inset": "#e5e9f0",          # nord5 - Snow Storm inset
        "text_primary": "#2e3440",      # nord0 - Polar Night dark text
        "text_secondary": "#4c566a",    # nord3 - Muted label text
        "accent_primary": "#5e81ac",    # nord10 - Deep Frost Blue
        "accent_primary_hover": "#4c566a",
        "accent_secondary": "#a3be8c",  # nord14 - Aurora Green
        "accent_secondary_hover": "#8fbcbb",
        "accent_muted": "#4c566a",      # Muted slate
        "accent_muted_hover": "#3b4252",
        "border": "#d8dee9",            # nord4 - Light border
    }
}

def get_color(color_key: str):
    """Returns a tuple of (light_color, dark_color) suitable for CustomTkinter."""
    return (COLORS["light"][color_key], COLORS["dark"][color_key])