from saxonche import *
import os


def main():
    cwd = os.getcwd()
    print("Working directory: " + cwd)
    proc = PySaxonProcessor()
    xml_file = os.path.join(cwd, "xml/books.xml")
    books_xsl = os.path.join(cwd, "stylesheets/books.xsl")

    xml_doc = proc.parse_xml(xml_file_name=xml_file)
    xslt_proc = proc.new_xslt30_processor()
    author_value = proc.make_string_value('Jane Austen')

    executable = xslt_proc.compile_stylesheet(stylesheet_file=books_xsl)
    executable.set_initial_match_selection(xdm_value=xml_doc)
    executable.set_global_context_item(xdm_item=xml_doc) # This line is needed to avoid error
    result = executable.apply_templates_returning_value(xdm_value=xml_doc)
    print(result.head.children[0].children[2])

if __name__ == "__main__":
    main()
    print("Done")



