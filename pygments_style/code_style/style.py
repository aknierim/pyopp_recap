from pygments.style import Style
from pygments.token import (
    Keyword,
    Name,
    Comment,
    String,
    Error,
    Literal,
    Number,
    Operator,
    Other,
    Punctuation,
    Text,
    Generic,
    Whitespace,
)

__all__ = ["CodeStyle"]

background = "#222436"
foreground = "#f2f2f2"
selection = "#515160"
comment = "#adacaf"
cyan = "#00d7e9"
green = "#56f576"
orange = "#ffb183"
pink = "#ff508c"
purple = "#817ad4"
red = "#ff3a52"
yellow = "#ffe648"

deletion = "#8f0035"


class CodeStyle(Style):
    name = "code"

    foreground_color = foreground
    background_color = background
    highlight_color = selection
    line_number_color = yellow
    line_number_background_color = selection
    line_number_special_color = green
    line_number_special_background_color = comment

    styles = {
        Whitespace: foreground,
        Comment: comment,
        Comment.Preproc: pink,
        Generic: foreground,
        Generic.Deleted: deletion,
        Generic.Emph: "underline " + foreground,
        Generic.Heading: "bold " + foreground,
        Generic.Inserted: "bold " + foreground,
        Generic.Output: selection,
        Generic.EmphStrong: "underline " + foreground,
        Generic.Subheading: "bold " + foreground,
        Generic.Prompt: "bold " + pink,
        Error: foreground,
        Keyword: pink,
        Keyword.Constant: pink,
        Keyword.Declaration: green + " italic",
        Keyword.Type: green,
        Literal: foreground,
        Name: foreground,
        Name.Attribute: cyan,
        Name.Builtin: green + " italic",
        Name.Builtin.Pseudo: yellow,
        Name.Class: cyan,
        Name.Function: cyan + " bold",
        Name.Label: green + " italic",
        Name.Tag: pink,
        Name.Variable: green + " italic",
        Number: orange,
        Operator: pink,
        Other: foreground,
        Punctuation: foreground,
        String: yellow,
        Text: foreground,
    }
