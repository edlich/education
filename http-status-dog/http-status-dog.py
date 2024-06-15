#!/usr/bin/python3
import argparse
import webbrowser

def get_http_status_code(code: str):
	http_status_dog_host = 'https://http.dog'

	if int(code) in range(100, 999):
		code_path = '/' + code + '.jpg'
		webbrowser.open(http_status_dog_host + code_path)
	else:
		print(code + ' is not a valid HTTP status code')
	

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Funny HTTP Status Dog', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.set_defaults(func=get_http_status_code)
	parser.add_argument('-c', '--code', default='200', help='HTTP status code', type=str)

	args = parser.parse_args()
	args.func(args.code)