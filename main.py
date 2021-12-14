
import os
import re

def generate_navigation_including_all_md():
    L = [file_name for file_name in os.listdir('.') if re.match('^.*\.md$', file_name)]
    L2 = []
    for file_name in L:
        file_name_link = file_name.replace(" ", "%20")
        file_name_without_ext = re.sub("(.*)\.md", "\\1", file_name)
        i2 = f'[{file_name_without_ext}]({file_name})  '
        L2.append(i2)
        
    with open('README.md', 'w') as f:
        f.write('\n'.join(L2))


def main():
    generate_navigation_including_all_md()
    print('ok')

if __name__ == '__main__':
    main()

