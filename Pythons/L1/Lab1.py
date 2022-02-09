#####1
n, s, f = 'Dima', 'Liashko', 'Anatoliyovich'
print(n,s,f,'\n',sep=' ')
#####2
buff = ''
for i in ('Input your name: ', 'Surname: ', 'Group_№: '):
    buff+= str(input(i))
print(buff, '\n')
#####3,4
s = 1
for i in ('Height', 'Width'):
    s*= int(input(i))
p = int(input('Price'))
print(s, p*s*0.0001, s*0.0001, '\n', sep=' ')
###5
m = 1
for i in range(1,21):
    m*=i
print(m, '\n')
###6-7
print('A'*100, 'Python'*100,'\n', sep='\n')
###8
print(int(str(179)*50)**2, '\n')
###9
print(f'Hello, {input("Name: ")}!\n')
####10
print('103, 25, 724\n')
####11
print(round(156.1245983,2),'\n')
###12
print(' '*5, 1.24, ' '*4, 13.52, '\n', ' '*4, 3.567, ' '*3, -355.1, '\n', ' '*6, 8.2, ' '*5, 9.18)
###14
def is_bigger(a,b):
    return a>b
print(is_bigger(1,2))

x = 1 and 0 or 11
print(x)
