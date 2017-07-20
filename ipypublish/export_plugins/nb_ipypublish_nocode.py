"""original notebook with default metadata tags added (where not already present) to set
- code/error tags to False
- all output tags set to True
- a basic titlepage and table of contents
"""
from ipypublish.latex.create_tplx import create_tplx
from ipypublish.latex.standard import standard_definitions as defs
from ipypublish.latex.standard import standard_packages as package
from ipypublish.latex.ipypublish import doc_article as doc
from ipypublish.latex.ipypublish import biblio_natbib as bib
from ipypublish.latex.ipypublish import contents_output as output
from ipypublish.latex.ipypublish import contents_framed_code as code
from ipypublish.latex.ipypublish import front_pages as title
from ipypublish.filters.filters import remove_dollars, first_para, create_key, dict_to_kwds
from ipypublish.preprocessors.latex_doc import LatexDocLinks
from ipypublish.preprocessors.latex_doc_defaults import MetaDefaults


oformat = 'Notebook'
template = create_tplx([p.tplx_dict for p in 
            [package,defs,doc,title,bib,output,code]])

_filters = {'remove_dollars': remove_dollars,
            'first_para': first_para,
            'create_key': create_key,
        'dict_to_kwds':dict_to_kwds}
        
cell_defaults = {
  "latex_doc": {
    "figure": {
      "placement": "H"
    },
    "table": {
      "placement": "H"
    },
    "equation": True,
    "text": True,
    "code":False,
    "error":False
  }
}

nb_defaults={
"latex_doc": {
  "titlepage":{},
  "toc": True,
  "listfigures": False,
  "listtables": False,
  "listcode": False,
  }
}
            
config = {'TemplateExporter.filters':_filters,
          'Exporter.filters':_filters,
          'Exporter.preprocessors':[MetaDefaults],
          'MetaDefaults.cell_defaults':cell_defaults,
          'MetaDefaults.nb_defaults':nb_defaults}