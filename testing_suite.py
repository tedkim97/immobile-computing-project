import requests
import json

def test_post(url, payload, header):
    return requests.post(url, data = json.dumps(payload), headers = header)

def file_post(url, filename, header):
    with open(filename, 'rb') as f:
        print(f)
        r = requests.post(url, files={filename: f})
    return r

def mult_file_post(url, filenames, header):
    tosend = dict()
    for fname in filenames:
        tosend[fname] = open(fname, 'rb')

    r = requests.post(url, files = tosend, headers = header)
    return r
if __name__ == "__main__":
    url = 'https://49263074.ngrok.io/sendData'
    payload = {'test':1}
    header = dict()
    # a = test_post(url, payload, header)
    # print(a.status_code)
    # print(a.content)


    PREFIX = 'test_files/'
    # b = file_post(url, PREFIX + 'post_test.csv', header)
    # print(b.status_code)
    # print(b.content)

    # tf = [PREFIX + x for x in ['post_test.csv', 'post_test2.csv']]    
    # c = mult_file_post(url, tf, header)
    # print(c.status_code)
    # print(c.content)

    tf = [PREFIX + x for x in ['post_test{}.csv'.format(y) for y in range(1,9)]]
    d = mult_file_post(url, tf, header)
    print(d.status_code)
    print(d.content)