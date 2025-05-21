# import the necessary libraries
import xml.dom.minidom
import os
import datetime
import xml.sax

# change the path to the directory where the XML file is located
os.chdir('Practical14')

# use DOM
# get the start time
start_time_DOM = datetime.datetime.now()
# parse the xml file into a DOM object
DOMTree = xml.dom.minidom.parse('go_obo.xml')
# get the root element of the DOM tree
root = DOMTree.documentElement
# get the list of all the terms in the XML file
terms = root.getElementsByTagName('term')
# divide the terms into three ontologies
def term_divider(terms):
    # create three lists to store the terms in each ontology
    cellular_component = []
    molecular_function = []
    biological_process = []
    # iterate through the terms and add them to the appropriate list
    for term in terms:
        # get the <namespace> elements
        namespace = term.getElementsByTagName('namespace')[0].firstChild.nodeValue
        # check the namespace and add the term to the appropriate list
        if namespace == 'cellular_component':
            cellular_component.append(term)
        elif namespace == 'molecular_function':
            molecular_function.append(term)
        elif namespace == 'biological_process':
            biological_process.append(term)
    # return the three lists
    return cellular_component, molecular_function, biological_process

# def a function to get the number of <is_a> in each term
def most_is_a(list_of_terms_in_ontology, ontology_name):

    # create a dictionary to store the term names and the number of <is_a> elements in each term
    term_dict = {}
    # get all the <is_a> elements in the XML file
    for term in list_of_terms_in_ontology:
        is_a = term.getElementsByTagName('is_a')
        # count the number of <is_a> elements
        length = len(is_a)
        # get the name of the term
        term_id = term.getElementsByTagName('id')[0].firstChild.nodeValue
        term_name = term.getElementsByTagName('name')[0].firstChild.nodeValue
        term_info = term_id + "_" + term_name
        # add the term name and the number of <is_a> elements to the dictionary
        term_dict[term_info] = length

    # find the term with the maximum number of <is_a> elements
    max_term = max(term_dict.values())
    term_with_max_is_a = [term for term, count in term_dict.items()
                        if count == max_term]

    # count the number of <is_a> elements
    length = len(term_with_max_is_a)
    # print the term with the maximum number of <is_a> elements
    print(f'The term with the maximum number of <is_a> elements in {ontology_name} is: {term_with_max_is_a}')
    print(f'The number of <is_a> elements in this term is: {max_term}')


cellular_component, molecular_function, biological_process = term_divider(terms)
most_is_a(cellular_component, 'cellular_component')
most_is_a(molecular_function, 'molecular_function')
most_is_a(biological_process, 'biological_process')
# get the end time
end_time_DOM = datetime.datetime.now()
# calculate the time taken to run the program
time_taken_DOM = end_time_DOM - start_time_DOM
print(f'Time taken to run the program using DOM: {time_taken_DOM}')


# use SAX
# define a custom ContentHandler called GoHandler
class GoHandler (xml.sax.ContentHandler):
    # initialize the handler
    def __init__(self):
        self.id = ''
        self.name = ''
        self.info = ''
        self.namespace = ''
        self.is_a_list = []
        self.current_element = ''
        self.in_a_term = False
        self.length = 0
        self.count_dict_c = {}
        self.count_dict_m = {}
        self.count_dict_b = {}
    # startElement method is called when an opening tag is encountered
    def startElement(self, tag, attributes):
        self.current_data = tag
        # check if the current element is <term>
        if tag == "term":
            self.id = ''
            self.name = ''
            self.namespace = ''
            self.is_a_list = []
    # define the characters method to handle the text content of the elements
    def characters(self, content):
        # check if the current element is <id>, <namespace>, or <is_a>
        if self.current_data == "id":
            self.id += content
        if self.current_data == "namespace":
            self.namespace += content
        if self.current_data == "is_a":
            self.is_a_list.append(content)
        if self.current_data == "name":
            self.name += content
    # define the endElement method to handle the closing tags
    def endElement(self, tag):
        if tag == "term":
            self.in_a_term = False
            # calculate the number of <is_a> elements
            self.length = len(self.is_a_list)
            # add the term name and the number of <is_a> elements to the dictionary
            self.info = self.id + "_" + self.name
            if self.namespace == 'cellular_component':
                self.count_dict_c[self.info] = self.length
            elif self.namespace == 'molecular_function':
                self.count_dict_m[self.info] = self.length
            elif self.namespace == 'biological_process':
                self.count_dict_b[self.info] = self.length
        self.current_data = ''
            

# define a function to get the maximum number of <is_a> elements in each ontology
def max_is_a_count(count_dict, ontology_name):
    # find the term with the maximum number of <is_a> elements
    max_term = max(count_dict.values())
    term_with_max_is_a = [term for term, count in count_dict.items()
                        if count == max_term]
    # print the term with the maximum number of <is_a> elements
    print(f'The term with the maximum number of <is_a> elements in {ontology_name} is: {term_with_max_is_a}')
    print(f'The number of <is_a> elements in this term is: {max_term}')

# get the start time
start_time_SAX = datetime.datetime.now()
# create an XMLReader object
parser = xml.sax.make_parser()
# assign the handler to the parser
handler = GoHandler()
# set the content handler to the parser
parser.setContentHandler(handler)
# parse the XML file
parser.parse('go_obo.xml')
# get the end time
end_time_SAX = datetime.datetime.now()
# compare the number of <is_a> elements in each ontology
max_is_a_count(handler.count_dict_c, 'cellular_component')
max_is_a_count(handler.count_dict_m, 'molecular_function')
max_is_a_count(handler.count_dict_b, 'biological_process')
# calculate the time taken to run the program
time_taken_SAX = end_time_SAX - start_time_SAX
print(f'Time taken to run the program using SAX: {time_taken_SAX}')

# compare the time taken to run the program using DOM and SAX
if time_taken_DOM < time_taken_SAX:
    print(f'The DOM method is faster than the SAX method by: {time_taken_SAX - time_taken_DOM}')
else:
    print(f'The SAX method is faster than the DOM method by: {time_taken_DOM - time_taken_SAX}')

# time_taken_DOM = 8.526424 s
# time_taken_SAX = 1.440686 s
# The SAX is faster than the DOM.


