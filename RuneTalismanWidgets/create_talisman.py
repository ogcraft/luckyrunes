#!/usr/bin/python
#android create project --target 3 --name RuneTalisman_t --path ./RuneTalisman_t --activity RuneWidgetProvider --package com.luckyrune.RuneWidget_t

import os, sys, shutil, re

tmpl_files = ['AndroidManifest.xml', 'chid_icon.png', 'chid.png', 'res/xml/talisman_widget_info.xml', 'res/layout/main.xml', 'res/layout/widget.xml', 'assets/ondevice_luckyrune.css', 'assets/info.html', 'src/com/luckyrune/RuneWidget/RuneInfo.java', 'src/com/luckyrune/RuneWidget/RuneWidgetProvider.java' ]

widget_names = {
    'ch0013':'WelthRuneTalisman', 
    'ch0025':'GamerRuneTalisman', 
    'ch0035':'AUJARuneTalisman', 
}

defs = {}

def create_project(chid, defs):
    cmd="android create project --target %(target)d --name %(name)s --path %(path)s --activity %(activity)s --package %(package)s" % defs
    print "Doing:", cmd
    os.system(cmd)

def process_file(chid, f, defs):
    print "process_file:", f
    if f in 'AndroidManifest.xml':
        newfn = defs['path'] + os.sep + f 
        ll = open(defs['tmpl_dir'] + os.sep + f).readlines()
        content = "".join(ll)
        content = re.sub("ch0035",  chid, content)
        content = re.sub("com\.luckyrune\.RuneWidget",  defs['package'], content)
        content = re.sub("RuneTalismanName",  widget_names[chid], content)
        content = re.sub("RuneWidgetProvider",  widget_names[chid], content)
        write_file(newfn, content)
    elif f.endswith('icon.png'):
        fl = chid + os.sep + chid + '_icon.png'
        if os.path.exists(fl):
            dstbase = defs['path'] + os.sep + "res/drawable"
            dsts = (dstbase+ "-mdpi/", dstbase+ "-ldpi/", dstbase+ "-hdpi/",  defs['path'] + '/assets/')
            copy_file_to_dirs(fl, dsts)
    elif f.endswith('chid.png'):
        fl = chid + os.sep + chid + '.png'
        if os.path.exists(fl):
            dstbase = defs['path'] + os.sep + "res/drawable"
            dsts = (dstbase+ "-mdpi/", dstbase+ "-ldpi/", dstbase+ "-hdpi/",  defs['path'] + '/assets/')
            copy_file_to_dirs(fl, dsts)
    elif f.endswith('main.xml'):
        copy_file_to_same_path_in_dir(f, defs)
    elif f.endswith('info.xml'):
        copy_file_to_same_path_in_dir(f, defs)
    elif f.endswith('widget.xml'):
        fl = defs['tmpl_dir'] + os.sep + f 
        newfn = defs['path'] + os.sep + f  
        ll = open(fl).readlines()
        content = "".join(ll)
        content = re.sub("ch0035",  chid, content)
        write_file(newfn, content)
    elif f.endswith('ondevice_luckyrune.css'):
        copy_file_to_same_path_in_dir(f, defs)
    elif f.endswith('info.html'):
        fl = chid + '/info.html'
        copy_file_to_dirs(fl, [ defs['path'] + '/assets'])
    elif f.endswith('RuneInfo.java'):
        fl = defs['tmpl_dir'] + os.sep + f 
        newfn = defs['path'] + os.sep + 'src' + os.sep + defs['package_path'] + os.sep + 'RuneInfo.java'  
        ll = open(fl).readlines()
        content = "".join(ll)
        content = re.sub("com\.luckyrune\.RuneWidget",  defs['package'], content)
        content = re.sub("RuneWidgetProvider",  widget_names[chid], content)
        write_file(newfn, content)
    elif f.endswith('RuneWidgetProvider.java'):
        fl = defs['tmpl_dir'] + os.sep + f 
        newfn = defs['path'] + os.sep + 'src' + os.sep + defs['package_path'] + os.sep +  widget_names[chid] + '.java' 
        ll = open(fl).readlines()
        content = "".join(ll)
        content = re.sub("com\.luckyrune\.RuneWidget",  defs['package'], content)
        content = re.sub("RuneWidgetProvider",  widget_names[chid], content)
        write_file(newfn, content)

    else:
        print "Unknown file:", f
        

def copy_file_to_dirs(fn, dirs):
    for d in dirs:
        if not os.path.exists(d):
            print "Creating dir:", d
            os.makedirs(d)  
        print "Copy %s -> %s" % (fn, d)
        shutil.copy(fn, d)

def copy_file_to_same_path_in_dir(fn, defs):
    src = defs['tmpl_dir'] + os.sep + fn
    dst = defs['path'] + os.sep + fn 
    print "Copy %s -> %s" % (src, dst)
    fdir = os.path.dirname(dst)
    if not os.path.exists(fdir):
        print "Creating dir:", fdir
        os.makedirs(fdir) 
    shutil.copy(src, dst)

def write_file(fn,content):
    print "write_file: ", fn
    if os.path.exists(fn):
        os.remove(fn)
    fdir = os.path.dirname(fn)
    if not os.path.exists(fdir):
        print "Creating dir:", fdir
        os.makedirs(fdir) 
    print "Write %d butes >> %s" % (len(content), fn)
    open(fn, "w").write(content)    

def main(argv):
    print "argv:", argv
    chid = argv[1]
    defs['target'] = 3
    defs['name'] = "RuneTalisman_%s" % chid
    defs['path'] = "./RuneTalisman_%s" % chid
    defs['activity'] = widget_names[chid] #"RuneWidgetProvider"
    defs['package'] = "com.luckyrune.RuneTalisman_%s" % chid
    defs['package_path'] = defs['package'].replace('.', '/')
    defs['tmpl_dir'] = "./RuneWidget"
    create_project(chid, defs)
    # copy files from template
    for f in tmpl_files:
         process_file(chid, f, defs)

if __name__ == "__main__":
    main(sys.argv)


