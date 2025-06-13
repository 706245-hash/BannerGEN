import random

def generate_ascii_banner(text, style="block", width=80):
    """
    Generate a custom ASCII art banner with multiple style options
    Returns a list of lines for the banner
    """
    # Define character sets for different styles
    styles = {
        "block": ["█", "▓", "▒", "░", " "],
        "line": ["║", "═", "╔", "╗", "╚", "╝"],  # 6 elements (0-5)
        "star": ["★", "☆", "✶", "✦", " "],
        "simple": ["#", "=", "+", "|", " "],
        "matrix": ["0", "1", " ", " "]
    }
    
    # Select character set based on style
    chars = styles.get(style.lower(), styles["block"])
    
    # Define banner templates
    templates = [
        # Top-heavy block style (uses indices 0, 4)
        lambda t: [
            f" {chars[0]*(len(t)+4)} ",
            f"{chars[0]}{chars[4]*(len(t)+4)}{chars[0]}",
            f"{chars[0]}{chars[4]} {t.upper()} {chars[4]}{chars[0]}",
            f"{chars[0]}{chars[4]*(len(t)+4)}{chars[0]}",
            f" {chars[0]*(len(t)+4)} "
        ],
        
        # Side-bar style (uses indices 0, 1, 2, 3, 4, 5)
        lambda t: [
            f"{chars[2]}{chars[1]*(len(t)+6)}{chars[3]}",
            f"{chars[0]}  {t.upper()}  {chars[0]}",
            f"{chars[4]}{chars[1]*(len(t)+6)}{chars[5]}"
        ] if len(chars) > 5 else [
            f"{chars[0]}{chars[1]*(len(t)+6)}{chars[0]}",
            f"{chars[0]}  {t.upper()}  {chars[0]}",
            f"{chars[0]}{chars[1]*(len(t)+6)}{chars[0]}"
        ],
        
        # Centered with decoration (uses indices 0)
        lambda t: [
            f"{' '*((width-len(t))//2-2)}{chars[0]*4} {t.upper()} {chars[0]*4}",
            f"{' '*((width-len(t))//2-2)}{chars[0]}{' '*(len(t)+6)}{chars[0]}"
        ],
        
        # Matrix style (uses indices 0, 1)
        lambda t: [
            f"{''.join(random.choice(chars[0:2]) for _ in range(width))}",
            f"{''.join(random.choice(chars[0:2]) for _ in range((width-len(t))//2-1))} {t.upper()} {''.join(random.choice(chars[0:2]) for _ in range((width-len(t))//2-1))}",
            f"{''.join(random.choice(chars[0:2]) for _ in range(width))}"
        ] if len(chars) > 1 else [
            f"{chars[0]*width}",
            f"{chars[0]*((width-len(t))//2-1)} {t.upper()} {chars[0]*((width-len(t))//2-1)}",
            f"{chars[0]*width}"
        ]
    ]
    
    # Select a random template
    try:
        banner = random.choice(templates)(text)
    except IndexError:
        # Fallback to simple style if there's an index error
        chars = styles["simple"]
        banner = templates[0](text)
    
    # Center align the banner
    centered = []
    for line in banner:
        padding = (width - len(line)) // 2
        centered.append((" " * padding) + line)
    
    return centered

# Example usage
if __name__ == "__main__":
    # ANSI color codes
    colors = {
        "HEADER": "\033[95m",
        "BLUE": "\033[94m",
        "CYAN": "\033[96m",
        "GREEN": "\033[92m",
        "YELLOW": "\033[93m",
        "RED": "\033[91m",
        "BOLD": "\033[1m",
        "UNDERLINE": "\033[4m",
        "END": "\033[0m",
    }
    
    # Generate and display different banners
    texts = ["Hello World", "Vault", "Access Control", "Crypto Lock"]
    styles = ["block", "line", "star", "simple", "matrix"]
    
    for i, text in enumerate(texts):
        # Select random color and style
        color = random.choice(list(colors.values())[0:6])
        style = styles[i % len(styles)]
        
        # Generate banner
        banner = generate_ascii_banner(text, style=style)
        
        # Print with color
        print(f"\n{color}{'='*80}{colors['END']}")
        for line in banner:
            print(f"{color}{line}{colors['END']}")
        print(f"{color}{'='*80}{colors['END']}")