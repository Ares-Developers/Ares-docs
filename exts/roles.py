from docutils import nodes, utils
from docutils.parsers.rst.roles import set_classes

def setup(app):
    app.add_role('game', game_role)
    app.add_role('file', file_role)
    app.add_role('type', type_role)
    app.add_role('value', value_role)

    app.add_role('tag', tag_role)
    app.add_role('captiontag', tag_role)
    app.add_role('tagdef', tag_role)
    
    app.add_config_value('ares_tag_defexpanded', False, 'env')
    app.add_config_value('ares_tag_separator', u"\u25BA", 'env')
    app.add_config_value('ares_tag_captionclass', 'type', 'env')
    app.add_config_value('ares_tag_typeclass', 'type', 'env')

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

    config = inliner.document.settings.env.app.config
    separator = config.ares_tag_separator
    captionclass = config.ares_tag_captionclass
    typeclass = config.ares_tag_typeclass
    

    node = nodes.inline("", "")
    if name == "tagdef":
        # tag definition item
        # value describes the data type
        if config.ares_tag_defexpanded:
            if scope:
                node.append(nodes.literal(scope, scope))
                if tag:
                     node.append(nodes.Text(" " + separator + " "))
            node.append(nodes.literal(tag, tag))
        else:
            string = scope + separator + tag
            node.append(nodes.literal(string, string))
        
        if value:
            #node.append(nodes.Text(" ("))
            node.append(nodes.inline(value, " (" + value.strip() + ")", classes=[typeclass]))
            #node.append(nodes.Text(")"))
    else:
        # tags in captions and other text
        string = tag + value;
        if scope:
            if tag:
                string = separator + string
            string = scope + string

        # tags in captions use monospace without <pre>
        if name == "captiontag":
            node.append(nodes.inline(string, string, classes=[captionclass]))
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
