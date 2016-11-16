# ================================================= #
# Global configuration settings for text processing #
# (enabled with the -c flag in the CLI commands)    #
# ================================================= #

# Enable or disable text processing operations
TO_LOWERCASE = True
TO_UPPERCASE = False
REMOVE_MULTIPLE_NEWLINES = True
REMOVE_URLS = True
ONLY_ASCII = True
REMOVE_SHORT_LINES = True

# If REMOVE_SHORT_LINES is enabled define the minimum number of words required
# to include a line in the final text
MINIMUM_WORDS = 5


# ============== #
# Other Settings #
# ============== #

# Define the beatifoulsoup parser for parsing html
BS4_PARSER = 'html.parser'
