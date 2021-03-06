import requests
import json

def test_get(url):
    r = requests.get(url)
    return r

def test_post(url, payload, header):
    r = requests.post(url, data=json.dumps(payload), headers= header)
    return r

def sing_file_post(url, filename, header):
    with open(filename, 'rb') as f:
        print(f)
        r = requests.post(url, data={filename: f})
    return r

def mult_file_post(url, filenames, header):
    tosend = dict()
    for fname in filenames:
        tosend[fname] = open(fname, 'rb')

    r = requests.post(url, files = tosend, headers = header)
    print(r.text)
    return r





if __name__ == "__main__":
    BASE = 'https://09ed5657.ngrok.io'
    url = 'https://09ed5657.ngrok.io/senddata'
    url2 = 'https://httpbin.org/post'
    payload = {'tests'}
    header = dict()
    # a = test_post(url, payload, header)
    # print(a.status_code)
    # print(a.content)


    PREFIX = 'test_files/'
    b = sing_file_post(url, PREFIX + 'post_test5.csv', header)
    print(b.status_code)
    print(b.content)

    # tf = [PREFIX + x for x in ['post_test.csv', 'post_test2.csv']]    
    # c = mult_file_post(url, tf, header)
    # print(c.status_code)
    # print(c.content)

    # tf = [PREFIX + x for x in ['post_test{}.csv'.format(y) for y in range(1,9)]]
    # d = mult_file_post(url, tf, header)
    # print(d.status_code)
    # print(d.content)

    # temp_r = test_get(BASE + 'testget')
    # print(temp_r.status_code)
    # print(temp_r.text)