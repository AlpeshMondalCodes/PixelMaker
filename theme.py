"""
Theme definitions for the Pixelator application.
Contains color palettes for both Dark and Light modes.
"""
COLORS = {
    "dark": {
        "bg_main": "#121013",           # Deep dark background with auburn undertone
        "bg_card": "#1D1619",           # Card & container background
        "bg_inset": "#2A1A1F",          # Inset elements (entry boxes, text area)
        "text_primary": "#FFFFFF",      # High contrast primary text
        "text_secondary": "#B3A5A8",    # Muted secondary text
        "accent_primary": "#3772FF",    # Electric Blue for primary action buttons
        "accent_primary_hover": "#2557D6",
        "accent_secondary": "#E3B505",  # Amber Gold for secondary action buttons
        "accent_secondary_hover": "#C69E00",
        "accent_muted": "#764134",      # Warm brown accent / borders
        "accent_muted_hover": "#8C4E3F",
        "border": "#3A262C",            # Subtle borders
    },
    "light": {
        "bg_main": "#F0F3F9",           # Soft grayish-blue clean background
        "bg_card": "#FFFFFF",           # Crisp white cards
        "bg_inset": "#E5EAF3",          # Slightly deeper gray-blue for entry fields/text areas
        "text_primary": "#1E293B",      # Dark slate for sharp, legible text
        "text_secondary": "#64748B",    # Medium slate for labels and secondary text
        "accent_primary": "#2563EB",    # Royal Blue (Primary action / Browse / Slider elements)
        "accent_primary_hover": "#1D4ED8", # Deeper blue for hover
        "accent_secondary": "#059669",  # Rich Emerald Green (Save button — makes it pop clearly against white/gray)
        "accent_secondary_hover": "#047857", # Darker emerald for hover
        "accent_muted": "#475569",      # Charcoal slate (Tips & ASCII utility buttons)
        "accent_muted_hover": "#334155", # Darker charcoal hover
        "border": "#CBD5E1",            # Clean, defined gray border for structural inputs/cards
    }
}

def get_color(color_key: str):
    """
    Returns a tuple of (light_color, dark_color) suitable for CustomTkinter
    color arguments.
    """
    return (COLORS["light"][color_key], COLORS["dark"][color_key])