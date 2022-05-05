import os;
import xml.etree.ElementTree as ET

def getChildren(child , childrens ):
    childrens[child.tag] = child.text
    for c in child:
        getChildren(c , childrens);
        

def parseXML(xmlfile):
    info = {}
    # create element tree object
    tree = ET.parse(xmlfile)
  
    # get root element
    root = tree.getroot();
    root_children = {};
    need = ["path" , "width" , "height" , "name" , "xmin" , "ymin" , "xmax" , "ymax"];
    getChildren(root , root_children);
    result = "";

    for el in need:
            
        result += f'{root_children[el]},'
    return result[0: len(result)-1] + "\n";



def get_all_xml_files(filename):
    abs_path =  os.path.abspath(filename);
    return [file for file in os.listdir(abs_path) if file.split(".")[1] =="xml"]


# print(get_all_xml_files("Dataset/Images/Knife/train"));    
OUT_FILE= "test_annotation.csv";

def write_to_file(output , data):
    f=  open(output , "a")
    f.write(data);    
    f.close()

def process(dir):   
    files = get_all_xml_files(dir);
    write_to_file(OUT_FILE , "filename,width,height,class,xmin,ymin,xmax,ymax\n");
    for file in  files:
        result = parseXML(dir+file);
        write_to_file(OUT_FILE , result);
        
process("WorkSpace/training/images/test/");    


