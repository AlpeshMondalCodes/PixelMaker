"""
Dracula Theme definitions for the Pixelator application.
Includes high-contrast, rich purple-tinted dark mode and crisp Dracula-inspired light mode.
"""

COLORS = {
    "dark": {
        "bg_main": "#282a36",           # Background
        "bg_card": "#21222c",           # Darker Current Line / Selection
        "bg_inset": "#44475a",          # Current Line / Selection
        "text_primary": "#f8f8f2",      # Foreground
        "text_secondary": "#6272a4",    # Comment
        "accent_primary": "#bd93f9",    # Purple
        "accent_primary_hover": "#a87ff3",
        "accent_secondary": "#ff79c6",  # Pink
        "accent_secondary_hover": "#e052aa",
        "accent_muted": "#50fa7b",      # Green
        "accent_muted_hover": "#32d85d",
        "border": "#44475a",            # Selection boundary
    },
    "light": {
        "bg_main": "#f8f8f2",           # Crisp Dracula light background
        "bg_card": "#ffffff",           # Pure white cards
        "bg_inset": "#e2e2dc",          # Soft gray-tint inset
        "text_primary": "#282a36",      # Dracula dark foreground text
        "text_secondary": "#6272a4",    # Comment gray
        "accent_primary": "#9547f7",    # Deeper purple for light mode readability
        "accent_primary_hover": "#7c28e0",
        "accent_secondary": "#d62588",  # Deeper pink
        "accent_secondary_hover": "#b0136b",
        "accent_muted": "#282a36",      # Dark contrast utility buttons
        "accent_muted_hover": "#1e2029",
        "border": "#d0d0c8",            # Subtle card border
    }
}

def get_color(color_key: str):
    """Returns a tuple of (light_color, dark_color) suitable for CustomTkinter."""
    return (COLORS["light"][color_key], COLORS["dark"][color_key])