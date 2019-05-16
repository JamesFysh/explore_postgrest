from IPython.display import Image
from pygraphviz import AGraph
from eralchemy.cst import GRAPH_BEGINNING
from eralchemy.sqla import database_to_intermediary


def render_er_inline(db_conn_str):
    tables, relationships = database_to_intermediary(db_conn_str)
    t = '\n'.join(t.to_dot() for t in tables)
    r = '\n'.join(r.to_dot() for r in relationships)
    the_dot = '{}\n{}\n{}\n}}'.format(GRAPH_BEGINNING, t, r)
    return Image(AGraph(the_dot).draw(format='png', prog='dot'))