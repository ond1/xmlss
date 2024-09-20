from saxonche import *

proc = PySaxonProcessor()
xslt_proc = proc.new_xslt30_processor()

executable = xslt_proc.compile_stylesheet(stylesheet_file='stylesheets/producing-json.xsl')
executable.set_capture_result_documents(True, True)
executable.call_template_returning_value("a")
rdocs_map = executable.get_result_documents()
keyslist = [*rdocs_map.keys()]
print(keyslist)
print(rdocs_map[keyslist[0]].head)
print(type(rdocs_map[keyslist[0]].head))
