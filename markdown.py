# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 09:46:34 2019

@author: ycwei982
"""

from bs4 import BeautifulSoup 
import re

def main():
    htmlpath = input()
    html = open(htmlpath,"r",encoding='utf-8')
    html = BeautifulSoup(html, "html.parser")
    new_html = html.article
    
    print("# " + html.title.get_text() + '\n')
    
    # Desc, input and output
    i = 0
    for p in new_html.select("p"):
        if i == 0:
            print("## Description: \n")
        if i == 1:
            print("### Input: \n")
        if i == 2:
            print("### Output: \n")
        
        current_article = str(p.get_text()).replace("\n","") # Replace existing \n for beauty!
        print(current_article + '\n')
        
        # Here's another way to do it:
        # print(p.get_text().replace("\n", ""))
        
        i += 1
    
    sample_data_parse = new_html.get_text()
    
    # Sample input parsing
    sample_input = re.search(r'Sample Input(.*?)Sample Output', sample_data_parse, re.DOTALL) # Extract the real sample input data from the messed raw text
    
    print("\n## Sample Input: \n```")
    print(sample_input.group(1)) # Raw "Sample Input" stored at list's index 1
    print("```")
    # Sample output parsing
    sample_output = re.search(r'Sample Output(.*?)Hint', sample_data_parse, re.DOTALL) # Extract the real sample output data from the messed raw text
    
    print("\n## Sample Output: \n```")
    print(sample_output.group(1))
    print("```")
    
main()
