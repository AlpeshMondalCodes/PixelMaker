"""
One Dark Theme definitions for the Pixelator application.
Inspired by Atom's iconic One Dark & One Light syntax theme.
"""

COLORS = {
    "dark": {
        "bg_main": "#21252b",           # Dark background
        "bg_card": "#1e2227",           # Deeper slate background
        "bg_inset": "#282c34",          # One Dark editor background
        "text_primary": "#abb2bf",      # Primary light text
        "text_secondary": "#5c6370",    # Comment gray
        "accent_primary": "#61afef",    # Atom Blue
        "accent_primary_hover": "#4fa3e3",
        "accent_secondary": "#98c379",  # Atom Green
        "accent_secondary_hover": "#84b065",
        "accent_muted": "#e06c75",      # Atom Red / Coral
        "accent_muted_hover": "#be5046",
        "border": "#3b4048",            # Border gray
    },
    "light": {
        "bg_main": "#fafafa",           # One Light background
        "bg_card": "#ffffff",           # Pure white card
        "bg_inset": "#f0f0f0",          # Light inset
        "text_primary": "#383a42",      # Primary dark text
        "text_secondary": "#a0a1a7",    # Secondary muted text
        "accent_primary": "#4078f2",    # Deep Atom Blue
        "accent_primary_hover": "#285ed9",
        "accent_secondary": "#50a14f",  # Deep Atom Green
        "accent_secondary_hover": "#3b823a",
        "accent_muted": "#a0a1a7",      # Neutral gray utility
        "accent_muted_hover": "#696c77",
        "border": "#e5e5e6",            # Light border
    }
}

def get_color(color_key: str):
    """Returns a tuple of (light_color, dark_color) suitable for CustomTkinter."""
    return (COLORS["light"][color_key], COLORS["dark"][color_key])