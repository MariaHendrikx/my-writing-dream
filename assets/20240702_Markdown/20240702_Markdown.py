import re
from graphviz import Digraph

# Tokenize the markdown text
def tokenize_markdown(text):
    tokens = []
    lines = text.split('\n')
    
    for line in lines:
        line = line.strip()
        
        if not line:
            continue
        
        # Match headings
        if line.startswith('#'):
            heading_level = len(re.match(r'^#+', line).group(0))
            heading_text = line[heading_level:].strip()
            tokens.append(('HEADING', heading_level, heading_text))
        
        # Match list items
        elif line.startswith('- '):
            item_text = line[2:].strip()
            tokens.append(('LIST_ITEM', item_text))
        
        # Match bold and italic text within paragraphs
        else:
            # Match links
            line = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'LINK(\1, \2)', line)
            
            # Match bold text
            line = re.sub(r'\*\*([^\*]+)\*\*', r'BOLD(\1)', line)
            
            # Match italic text
            line = re.sub(r'\*([^\*]+)\*', r'ITALIC(\1)', line)
            
            tokens.append(('PARAGRAPH', line))
    
    return tokens

# Visualize the AST
def visualize_ast(node):
    def add_nodes_edges(node, dot=None):
        if dot is None:
            dot = Digraph()
            dot.node(name=str(id(node)), label=node.type)
        
        for child in node.children:
            dot.node(name=str(id(child)), label=child.type)
            dot.edge(str(id(node)), str(id(child)))
            add_nodes_edges(child, dot=dot)
        
        return dot

    dot = add_nodes_edges(node)
    return dot

# Define the AST node class
class ASTNode:
    def __init__(self, type, value=None, children=None):
        self.type = type
        self.value = value
        self.children = children if children is not None else []

    def __repr__(self):
        return f'ASTNode(type={self.type}, value={self.value}, children={self.children})'


# Build the AST from the tokens
def build_ast(tokens):
    root = ASTNode('DOCUMENT')
    current_parent = root

    for token in tokens:
        type = token[0]

        if type == 'HEADING':
            level, text = token[1], token[2]
            node = ASTNode('HEADING', value={'level': level, 'text': text})
            current_parent.children.append(node)
        
        elif type == 'LIST_ITEM':
            item_text = token[1]
            node = ASTNode('LIST_ITEM', value=item_text)
            current_parent.children.append(node)
        
        elif type == 'PARAGRAPH':
            text = token[1]
            node = ASTNode('PARAGRAPH', value=text)
            current_parent.children.append(node)
    
    return root



# Example usage
markdown_text = """# This is a heading

This is a paragraph with **bold** and *italic* text.

- Item 1
- Item 2

[OpenAI](https://www.openai.com)"""

tokens = tokenize_markdown(markdown_text) # Previous step
ast = build_ast(tokens) # Current step



dot = visualize_ast(ast)



dot.render('ast', format='png', view=True)

# Define the AST node class (same as before)
class ASTNode:
    def __init__(self, type, value=None, children=None):
        self.type = type
        self.value = value
        self.children = children if children is not None else []

# Function to perform tree traversal and generate HTML
def render_ast_to_html(node):
    if node.type == 'DOCUMENT':
        return ''.join(render_ast_to_html(child) for child in node.children)
    
    elif node.type == 'HEADING':
        level = node.value['level']
        text = node.value['text']
        return f'<h{level}>{text}</h{level}>\n'
    
    elif node.type == 'LIST_ITEM':
        text = node.value
        return f'<li>{text}</li>\n'
    
    elif node.type == 'PARAGRAPH':
        text = node.value
        return f'<p>{text}</p>\n'
    
    elif node.type == 'IMAGE':
        alt_text = node.value['alt']
        image_url = node.value['url']
        return f'<img src="{image_url}" alt="{alt_text}">\n'
    
    # Handle any other node types gracefully
    return ''

# Function to generate complete HTML from markdown text
def markdown_to_html(markdown_text):
    tokens = tokenize_markdown(markdown_text)
    ast = build_ast(tokens)
    html_content = render_ast_to_html(ast)
    return html_content

# Example usage
markdown_text = """# This is a heading

This is a paragraph with **bold** and *italic* text.

- Item 1
- Item 2

![OpenAI Logo](https://www.openai.com/assets/img/logo.svg)
"""

html_output = markdown_to_html(markdown_text)
print(html_output)

