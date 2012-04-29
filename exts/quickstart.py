def setup(app):
    app.add_node(quickstart,
                 html=(visit_quickstart_node, depart_quickstart_node),
                 latex=(visit_quickstart_node, depart_quickstart_node),
                text=(visit_quickstart_node, depart_quickstart_node))

    app.add_directive('quickstart', QuickstartDirective)

from docutils import nodes

class quickstart(nodes.Admonition, nodes.Element):
    pass

def visit_quickstart_node(self, node):
    self.visit_admonition(node)

def depart_quickstart_node(self, node):
    self.depart_admonition(node)


from sphinx.util.compat import Directive
from sphinx.util.compat import make_admonition

class QuickstartDirective(Directive):

    # this enables content in the directive
    has_content = True

    def run(self):
        env = self.state.document.settings.env

        targetid = "quickstart-%d" % env.new_serialno('quickstart')
        targetnode = nodes.target('', '', ids=[targetid])
        
        self.options['class'] = [str('quickstart')]
        self.options['id'] = None

        ad = make_admonition(quickstart, self.name, ['Quickstart'], self.options,
                             self.content, self.lineno, self.content_offset,
                             self.block_text, self.state, self.state_machine)

        return [targetnode] + ad
