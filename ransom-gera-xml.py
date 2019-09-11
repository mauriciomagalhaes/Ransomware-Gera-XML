import xml.etree.ElementTree as ET
import requests, json, os, sys, subprocess

try:
    req = requests.get('https://fsrm.experiant.ca/api/v1/combined')
except:
    print('Problemas com acesso a página')
    exit()

dic = json.loads(req.text)
rans = (dic['filters'])

root = ET.Element("Root")
doc = ET.SubElement(root, 'Header', DatabaseVersion='2.0')
doc = ET.SubElement(root, 'QuotaTemplates')
doc = ET.SubElement(root, 'DatascreenTemplates')
doc = ET.SubElement(root, 'FileGroups')
fgp = ET.SubElement(doc, 'FileGroup', Name='Ransomware_Extensions', Id='{43230248-6303-4124-9596-e0240170b8b9}',  Description='')
Men = ET.SubElement(fgp, 'Members')

for patt in rans:
    pat = ET.SubElement(Men, 'Pattern', PatternValue=patt)

doc = ET.SubElement(fgp, "NonMembers")

tree = ET.ElementTree(root)
tree.write("rans2.xml", short_empty_elements=False, xml_declaration=True, encoding='utf16', method="xml")

# Descomentar abaixo para inserir no FILEGROUP do win2k8 ou 2k8r2

#os.system("C:\System32\filescrn.exe f i /FIle:C:\Temp\rans2.xml /Overwrite")