from docutils import nodes, utils
from docutils.parsers.rst.roles import set_classes

def setup(app):
    app.add_role('tag', tag_role)
    app.add_role('game', game_role)
    app.add_role('file', file_role)
    app.add_role('type', type_role)
    app.add_role('value', value_role)
    app.add_role('captiontag', tag_role)

def game_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    set_classes(options)
    node = nodes.inline(text, text, classes=['game', 'docutils', 'literal'])
    return [node], []

def file_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    set_classes(options)
    node = nodes.literal(text, text, classes=['file', 'docutils', 'literal'])
    return [node], []

def type_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    set_classes(options)
    node = nodes.inline(text, text, classes=['type', 'docutils', 'literal'])
    return [node], []

def game_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    set_classes(options)
    node = nodes.inline(text, text, classes=['game', 'docutils', 'literal'])
    return [node], []

def value_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    set_classes(options)
    node = nodes.title_reference(text, text)
    return [node], []

def tag_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    try:
        data = split_tag_data(text)
        scope = data[0]
        tag = data[1]
        value = data[2]
    except ValueError as ex:
        msg = inliner.reporter.error(str(ex), line=lineno)
        prb = inliner.problematic(rawtext, rawtext, msg)
        return [prb], [msg]

    set_classes(options)
        
    node = nodes.inline("", "")
    if 0:
        if scope:
            node.append(nodes.literal(scope, scope))
            if tag:
                 node.append(nodes.Text(u"\u25BA"))
        node.append(nodes.literal(tag, tag))
        if value:
            node.append(nodes.literal(value, value))
    else:
        string = tag + value;
        if scope:
            if tag:
                string = u"\u25BA" + string
            string = scope + string
            
        if name == "captiontag":
            node.append(nodes.inline(string, string, classes=['type']))
        else:
            node.append(nodes.literal(string, string))

    return [node], []

def split_tag_data(data):
    pos = -1
    scope = ''
    tag = ''
    value = ''
    
    if data.find('[') == 0:
        pos = data.find(']')
        if pos == -1:
            raise ValueError('Tag contains a section that isn\'t '
                             'closed. Tag is "%s".' % data)

        scope = data[:pos+1]

    pos2 = data.find('=', pos+1)
    if pos2 > -1:
        value = data[pos2+1:]
    else:
        pos2 = len(data)
    
    tag = data[pos+1:pos2+1]

    return [scope, tag, value]
