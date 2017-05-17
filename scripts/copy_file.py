import shutil
import os

copy_pair=[
    (r'D:\coblan\webcode\front_lib\css\fonts','../src/static/css/fonts'),
    (r'D:\coblan\webcode\front_lib\css\lib','../src/static/css/lib'),
    (r'D:\coblan\webcode\front_lib\js\lib','../src/static/js/lib'),
]

for src,dst in copy_pair:
    print('%s=>%s'%(src,dst))
    if os.path.exists(dst):
        shutil.rmtree(dst)
    # print('--start copy----')
    shutil.copytree(src,dst)