# -*- coding: UTF-8 -*-
from utils import load_data, output_to_file

if __name__ == '__main__':
    output_to_file(
        data=load_data(), 
        template_file='README.md',
        output_file='README.md', 
        template_dir='template_dir'
    )
    
    
    
