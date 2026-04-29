from django import template
import re

register = template.Library()

@register.filter
def highlight_gold(text):
    """
    Wrap specific phrases with gold-text span.
    Only exact matches: 'Candidates fail in job' and 'what they know.'
    """
    if not text:
        return text

    # Phrases to highlight (order matters for overlapping)
    phrases = [
        ('Candidates fail in job', '<span class="gold-text">Candidates fail in job</span>'),
        ('what they know.', '<span class="gold-text">what they know.</span>'),
    ]

    result = text
    for phrase, replacement in phrases:
        if phrase in result:
            result = result.replace(phrase, replacement)

    return result
