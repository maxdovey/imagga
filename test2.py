import sys, os , time 
import requests 
import json 




while True:

    api_key = 'acc_781af1b59b1fe08'
    api_secret = '6fd9e104945f5d3dc973ec1bcaca0fa6'

    outfile = open ('tags.txt', 'w')
    #take pic
    os.system('imagesnap -d DV-VCR /Users/user/Desktop/PZI/1/PYTHON/imagga-py-master/tests/images/1.jpg')
    #upload pic to server
    os.system("scp /Users/user/Desktop/PZI/1/PYTHON/imagga-py-master/tests/images/1.jpg max@headroom.pzwart.wdka.hro.nl:public_html/images/")

    r = requests.get('https://api.imagga.com/v1/tagging?url=http://headroom.pzwart.wdka.hro.nl/~max/images/1.jpg', auth=(api_key, api_secret))


    data = json.loads(r.text)


    listy = data['results'][0]['tags']

    for i in listy:
        word = i['tag']
        neword = word.replace('""',' ')
        outfile.write(neword)
        outfile.writelines("\n")
    outfile.close()
    os.system("scp /Users/user/Desktop/PZI/1/PYTHON/imagga-py-master/tests/tags.txt max@headroom.pzwart.wdka.hro.nl:public_html/images/")
    print "pause"
    time.sleep(15)
