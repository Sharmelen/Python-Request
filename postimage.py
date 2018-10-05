import requests as rq
from skimage import io
from requests_toolbelt.multipart.encoder import MultipartEncoder


def uploadPromo(url, image_name):

    # url = "http://188.166.237.89:8880/ace/api/device/img"

    multipart_data = MultipartEncoder(
        fields={
            # a file upload field
            'uploadPromo': (image_name, open(image_name, 'rb'), 'image/png')
        }
    )
    headers = {
        'content-type': multipart_data.content_type,
        'authorization': 'jh5tvufrppbeov6j8d8objq3jp'
    }

    response = rq.request("POST", url, data=multipart_data, headers=headers)
    print(response.text)
    return (response.text)


# Getting Flower Image from ImageNet
url = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n03368352'
response = rq.get(url)
imgurls = response.text
imgurls = [s.strip() for s in imgurls.splitlines()]
promo_name = ['UNIFI', 'UNIFIPRO', 'TURBO', 'STUDENT', 'BIZ', 'UNIFILITE',
              'TESTUNIFI', 'TMRND', 'ACE', 'SMARTHELMAT']


for each in range(10):
    url = 'http://94.237.64.189:8880/ace/api/target/promo?title='+promo_name[each] +\
        '&company=TSSSB'
    image = io.imread(imgurls[each])
    image_name = promo_name[each]+'.png'
    io.imsave(image_name, image)
    uploadPromo(url, image_name)
