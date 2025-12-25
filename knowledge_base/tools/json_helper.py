import re

class JsonHelper:

	def remove_comments(json_str):
		# Regular expression to match strings, single-line comments (//), or multi-line comments (/* */)
		# We match strings first so we don't accidentally remove content inside them
		pattern = r'("(?:\\.|[^"\\])*")|//.*|/\*[\s\S]*?\*/'
		
		def replace(match):
			if match.group(1):
				return match.group(1) # Return the string as is
			return "" # Remove the comment
			
		return re.sub(pattern, replace, json_str)
	
	def fix_trailing_commas(json_str):
		# Match strings first to avoid modifying content inside them
		# Then match trailing commas: a comma followed by whitespace and a closing bracket/brace
		pattern = r'("(?:\\.|[^"\\])*")|,\s*([}\]])'
		
		def replace(match):
			if match.group(1):
				return match.group(1) # Return the string as is
			return match.group(2) # Return only the closing bracket/brace, removing the comma
			
		return re.sub(pattern, replace, json_str)
