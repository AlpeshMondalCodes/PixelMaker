"""
Rosé Pine Theme definitions for the Pixelator application.
All natural pine, faux fur, and soft pastel shades for dark and light modes.
"""

COLORS = {
    "dark": {
        "bg_main": "#191724",           # Base
        "bg_card": "#1f1d2e",           # Surface
        "bg_inset": "#26233a",          # Overlay
        "text_primary": "#e0def4",      # Text
        "text_secondary": "#908caa",    # Subtle
        "accent_primary": "#ebbcba",    # Rose
        "accent_primary_hover": "#e2a5a3",
        "accent_secondary": "#c4a7e7",  # Iris
        "accent_secondary_hover": "#b18fea",
        "accent_muted": "#31748f",      # Pine
        "accent_muted_hover": "#255a70",
        "border": "#403d52",            # Highlight Med
    },
    "light": {
        "bg_main": "#faf4ed",           # Rosé Pine Dawn Base
        "bg_card": "#ffffff",           # Pure white card
        "bg_inset": "#f2e9e1",          # Dawn Surface
        "text_primary": "#575279",      # Dawn Text
        "text_secondary": "#797593",    # Dawn Subtle
        "accent_primary": "#d7827e",    # Dawn Rose
        "accent_primary_hover": "#c36a66",
        "accent_secondary": "#907aa9",  # Dawn Iris
        "accent_secondary_hover": "#786192",
        "accent_muted": "#286983",      # Dawn Pine
        "accent_muted_hover": "#1d5166",
        "border": "#dfdad9",            # Soft border
    }
}

def get_color(color_key: str):
    """Returns a tuple of (light_color, dark_color) suitable for CustomTkinter."""
    return (COLORS["light"][color_key], COLORS["dark"][color_key])