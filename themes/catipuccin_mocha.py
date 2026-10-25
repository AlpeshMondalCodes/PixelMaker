# How to Change THEME
""" Rename this file with "theme.py and move it to the root folder removing the original theme.py"""

COLORS = {
    "dark": {
        "bg_main": "#1e1e2e",           # Base: Deep rich dark blue-gray
        "bg_card": "#181825",           # Mantle: Darker container background
        "bg_inset": "#313244",          # Surface0: Inset fields (entry boxes, text area)
        "text_primary": "#cdd6f4",      # Text: High-contrast soft lavender-white
        "text_secondary": "#a6adc8",    # Subtext1: Muted secondary text
        "accent_primary": "#b4befe",    # Lavender: Primary action buttons (Browse / Main)
        "accent_primary_hover": "#cba6f7", # Mauve for hover state
        "accent_secondary": "#f5c2e7",  # Pink: Secondary / Save button accent
        "accent_secondary_hover": "#eba0ac", # Flamingo for hover state
        "accent_muted": "#585b70",      # Surface2: Utility buttons (Tips / ASCII)
        "accent_muted_hover": "#45475a",    # Surface1 for hover state
        "border": "#45475a",            # Surface1: Clean subtle borders
    },
    "light": {
        "bg_main": "#FDF4F5",           # Very soft blush-tinted white background
        "bg_card": "#FFFFFF",           # Pure white container cards
        "bg_inset": "#F7E8EC",          # Muted warm pinkish-gray for inset fields/entries
        "text_primary": "#2D1E2F",      # Deep dark plum for ultra-sharp reading text
        "text_secondary": "#8A6D8C",    # Soft muted mauve-gray for labels
        "accent_primary": "#7C3AED",    # Electric Violet (Primary action / Browse / Slider)
        "accent_primary_hover": "#6D28D9", # Richer violet hover
        "accent_secondary": "#DB2777",  # Vivid Magenta / Hot Pink (Save button - pops brilliantly)
        "accent_secondary_hover": "#BE185D", # Deep pink hover
        "accent_muted": "#4B5563",      # Cool charcoal gray (Tips & ASCII utility buttons)
        "accent_muted_hover": "#374151", # Darker charcoal hover
        "border": "#E5D1D7",            # Soft dusty-rose subtle card borders
    }
}

def get_color(color_key: str):
    """
    Returns a tuple of (light_color, dark_color) suitable for CustomTkinter
    color arguments.
    """
    return (COLORS["light"][color_key], COLORS["dark"][color_key])