import yaml
import xml.etree.ElementTree as xml_tree

with open('feed.yaml','r') as file:
    yaml_data = yaml.safe_load(file)

    rss_element = xml_tree.Element('rss',{'version':'2.0',
    'xmlns:itunes':'http://www.itunes.com/dtds/podcast-1.0.dtd',
    'xmlns:content':'http://purl.org/rss/1.0/modules/content/'})
    
channel_elemnt = xml_tree.SubElement(rss_element, 'channel')

Link_prefix = yaml_data['link']

xml_tree.SubElement(channel_elemnt, 'title').text = yaml_data['title']
xml_tree.SubElement(channel_elemnt, 'subtitle').text = yaml_data['subtitle']
xml_tree.SubElement(channel_elemnt, 'itunes:author').text = yaml_data['author']
xml_tree.SubElement(channel_elemnt, 'description').text = yaml_data['description']
xml_tree.SubElement(channel_elemnt, 'itunes:image'),{'href': Link_prefix + yaml_data['image']}
xml_tree.SubElement(channel_elemnt, 'language').text = yaml_data['language']
xml_tree.SubElement(channel_elemnt, 'link').text = Link_prefix

xml_tree.SubElement(channel_elemnt, 'itunes:category'),{'text': yaml_data['category']}


for item in yaml_data['item']:
    item_element = xml_tree.SubElement(channel_elemnt, 'item')
    xml_tree.SubElement(item_element, 'itunes:title').text = item['title']
    xml_tree.SubElement(item_element, 'description').text = item['description']
    xml_tree.SubElement(item_element, 'pubDate').text = item['published']
    xml_tree.SubElement(item_element, 'enclosure'),{'url': Link_prefix + item['file']}, {'length': item['length']}, {'type': 'audio/mpeg'}

    xml_tree.SubElement(item_element, 'itunes:duration').text = item['duration']







output_tree = xml_tree.ElementTree(rss_element)

output_tree.write('podcast.xml', encoding='UTF-8', xml_declaration=True)
    