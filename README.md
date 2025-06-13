# ASCII Banner Generator

A Python script that generates customizable ASCII art banners with multiple styles and colors, perfect for command-line applications, security tools, or terminal-based projects.

## Features

- 🎨 Multiple banner styles: block, line, star, simple, and matrix
- 🌈 ANSI color support for vibrant terminal output
- 📏 Adjustable width for different terminal sizes
- 🎲 Random style selection or explicit style choice
- ✨ Special pre-designed "Password Generator" banner included

## Installation

1. Ensure you have Python 3.x installed
2. Clone this repository or download the `main.py` file

```bash
git clone https://github.com/yourusername/banner-generator.git
cd banner-generator
```

## Usage

### Basic Usage

Run the script directly to see example banners:
```bash
python main.py
```

### Programmatic Usage

Import the generator function in your Pyhon code:
```python
from main import generate_ascii_banner

# Generate a banner
banner = generate_ascii_banner("Hello World", style="star", width=60)

# Print the banner
for line in banner:
    print(line)
```
### Parameters
| Parameter | Description                                         | Default  |
|-----------|-----------------------------------------------------|----------|
| `text`      | Text to display in the banner                       | Required |
| `style`     | Style of banner (`block`, `line`, `star`, `simple`, `matrix`) |`block`    |
| `width`     | Total width of the banner in characters             | `80`       |

## Examples
### Block Style
```text
 ███████████████ 
█               █
█  HELLO WORLD  █
█               █
 ███████████████
```
### Line style
```text
╔══════════════════════╗
║  HELLO WORLD         ║
╚══════════════════════╝
```
### Matrix style
```text
0101010101010101010101010101010101010101
0101010101 HELLO WORLD 01010101010101010
0101010101010101010101010101010101010101
```
## Customisation
### Adding new styles
1. Add a new character set to the `styles` dictionary
2. Create a corresponding template function in the `templates` list


### Changing Colours
Modify the `colors` dictionary to use different ANSI colour codes:
```python
colors = {
    "PURPLE": "\033[95m",
    "ORANGE": "\033[33m",
    # Add more colors as needed
}
```

## Troubleshooting
- **Invalid escape sequence warnings**: Ensure backslashes in pre-designed banners are properly escaped
- **IndexError**: Verify all style definitions have enough characters for their templates
- **Color not working**: Check if your terminal supports ANSI colour codes






