import sys, os , time 
import requests 
import json 


count = 0

while True:
    count +=1 
    api_key = 'acc_781af1b59b1fe08'
    api_secret = '6fd9e104945f5d3dc973ec1bcaca0fa6'

    with open('tags.txt', 'a') as outfile:
        # try:
        #     for root, dirs, files in os.walk("./images/canon"):
        #         for files in files:
        #             path = root + '/' + file
    #take pic
        # cmd = 'imagesnap /Users/user/Desktop/PZI/1/PYTHON/imagga-py-master/tests/images/{0:06d}.jpg'.format(count)
        # os.system(cmd)
        # upload pic to server
        # os.system("scp /Users/user/Desktop/PZI/1/PYTHON/imagga-py-master/tests/images/1.jpg max@headroom.pzwart.wdka.hro.nl:public_html/images/")

        r = requests.get('https://api.imagga.com/v1/tagging?url=http://headroom.pzwart.wdka.hro.nl/~max/images/canon/IMG_0048.JPG', auth=(api_key, api_secret))


        data = json.loads(r.text)

        listy = data['results'][0]['tags']
        print listy 
        for i in listy:
            word = i['tag']
            confidence = i['confidence']
            if word == "man":
                
                outfile.write(word)
                outfile.write( '{}'.format(confidence))
                outfile.writelines("\n")
        outfile.close()
        print 'pause'
        time.sleep(25)
