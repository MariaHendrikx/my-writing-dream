from markdown_it import MarkdownIt
from graphviz import Digraph

# Sample Markdown text
markdown_text = """
# This is a heading

This is a paragraph with **bold** and *italic* text.

- Item 1
- Item 2
"""

# Initialize the Markdown parser
md = MarkdownIt()

# Parse the Markdown text into tokens
tokens = md.parse(markdown_text)

######################################
#          Render normally           #
######################################

def test_render_normal():
    # Render the Markdown text to HTML
    html_output = md.render(markdown_text)

    # Print tokens and HTML output
    print("Tokens:")
    for token in tokens:
        print(token)
    print("\nHTML Output:")
    print(html_output)


######################################
#          Visualize AST             #
######################################

# Function to build the AST
def build_ast(tokens):
    root = {'name': 'Document', 'children': []}
    stack = [root]
    
    for token in tokens:
        node = {'name': f"{token.type} ({token.tag})", 'children': []}
        
        if token.nesting == 1:
            stack[-1]['children'].append(node)
            stack.append(node)
        elif token.nesting == 0:
            stack[-1]['children'].append(node)
        elif token.nesting == -1:
            stack.pop()
            stack[-1]['children'].append(node)
    
    return root

# Function to visualize the AST using graphviz
def visualize_ast(node, graph, parent=None):
    graph.node(node['name'])
    
    if parent:
        graph.edge(parent, node['name'])
    
    for child in node['children']:
        visualize_ast(child, graph, node['name'])

def test_visualizeAST():
    # Build the AST
    ast = build_ast(tokens)

    # Create a graphviz Digraph
    graph = Digraph(comment='Markdown AST')

    # Visualize the AST
    visualize_ast(ast, graph)

    # Render and display the graph
    graph.render('markdown_ast', format='png', view=True)




######################################
#        Custom Rendering            #
######################################

class CustomRenderer(RendererHTML):
    def render_heading_open(self, token, options, env):
        return f"<h{token.tag[1]} style='color: blue;'>"

    def render_heading_close(self, token, options, env):
        return f"</h{token.tag[1]}>"


def test_custom_renderer():
    # Initialize the Markdown parser with custom renderer
    md = MarkdownIt(renderer_cls=CustomRenderer)

    # Render the Markdown text to HTML with custom styles
    html_output = md.render(markdown_text)

    # Print HTML output with custom rendering
    print("Custom HTML Output:")
    print(html_output)