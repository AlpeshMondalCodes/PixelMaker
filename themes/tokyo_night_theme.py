"""
Tokyo Night Theme definitions for the Pixelator application.
A clean, dark theme that celebrates the lights of Tokyo at night, with a crisp Day alternative.
"""

COLORS = {
    "dark": {
        "bg_main": "#1a1b26",           # Tokyo Night background
        "bg_card": "#16161e",           # Darker card background
        "bg_inset": "#24283b",          # Inset background
        "text_primary": "#c0caf5",      # Bright text
        "text_secondary": "#565f89",    # Muted text / comments
        "accent_primary": "#7aa2f7",    # Neon Blue
        "accent_primary_hover": "#5d8bf6",
        "accent_secondary": "#bb9af7",  # Neon Purple / Violet
        "accent_secondary_hover": "#a378f5",
        "accent_muted": "#414868",      # Muted slate
        "accent_muted_hover": "#333a56",
        "border": "#292e42",            # Border slate
    },
    "light": {
        "bg_main": "#e1e2e7",           # Tokyo Day background
        "bg_card": "#ffffff",           # Pure white card
        "bg_inset": "#d5d6db",          # Day inset
        "text_primary": "#3760bf",      # Deep blue primary text
        "text_secondary": "#6172b0",    # Secondary text
        "accent_primary": "#2e7de9",    # Bright blue
        "accent_primary_hover": "#1a65d3",
        "accent_secondary": "#9854f6",  # Violet accent
        "accent_secondary_hover": "#7e33e3",
        "accent_muted": "#8990b3",      # Muted slate
        "accent_muted_hover": "#6c7399",
        "border": "#c4c8d4",            # Soft border
    }
}

def get_color(color_key: str):
    """Returns a tuple of (light_color, dark_color) suitable for CustomTkinter."""
    return (COLORS["light"][color_key], COLORS["dark"][color_key])