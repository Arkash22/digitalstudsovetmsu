#!/usr/bin/env python3
import vk,time,json

# Здесь нужно вставить ПОЛЬЗОВАТЕЛЬСКИЙ токен
vkToken= ""

# Имя файла, где указаны группы для дампа
inp_fname="groups.txt"

# Имя файла, куда записать результат работы (таблица) NAME ID
out_fname="users.dat"

# Имя файла, куда записать результат работы (словарь JSON) ID: NAME
outjson_fname="users.json"

# Выводить/скрыть подробно все запросы к VK API
vk.silence=False

try: # Для отладки на своём ПК
	import getpass
	if(getpass.getuser()=='dolgikh'):
		import subprocess
		def bashExec(q):
			return subprocess.check_output(q,shell=True).decode("UTF-8")

		vkToken=bashExec("cat ~/bin/.token").replace("\n","")
		vk.silence=True
		print("Debug mode enabled")
except:pass

vk.auth(vkToken)

def domain2ID(d):
	o=vk.Api("utils.resolveScreenName",screen_name=d)
	return o.content["object_id"],o.content["type"]

def getUsersByUser(uid):
	o=None
	try:
		o=vk.Api("friends.get",user_id=uid,offset=0,count=1000,
			fields="nickname,bdate",
			name_case="nom")
		usrs=o.content['items']
		count=o.content['count']
		offset=0
		while(len(usrs)<0.9*count):
			offset+=1000
			time.sleep(0.4)
			try:
				o=vk.Api("friends.get",user_id=uid,offset=offset,count=1000,
					fields="nickname",
					name_case="nom")
				usrs+=o.content['items']
			except KeyError:
				time.sleep(60)
				offset-=1000
			except NewConnectionError:
				time.sleep(60)
				offset-=1000
		return usrs
	except KeyError: # Private profile
		try:
			if("Rate limit reached" in o.content['error_msg']):
				print("Исчерпан лимит запросов. Смените токен или подождите сутки")
				print("Ждём...")
				time.sleep(86400)
				return getUsersByUser(uid)
			if(not "profile is private" in o.content['error_msg']): # Другая ошибка, записываем пользователя как бесполезняк исследовать
				return []
		except Exception as e:
			raise(e)
		time.sleep(0.3)
		o=vk.Api("friends.getMutual",target_uid=uid,count=1000,offset=0)
		if(len(o.content)==0): # Общих друзей так и не нашлось
			return []
		time.sleep(0.3)
		o=vk.Api("users.get",user_ids=",".join([str(i) for i in o.content]),
			fields="nickname,bdate",
			name_case="nom")
		usrs=o.content
		return usrs

def getUsersByGroup(g):
	o=vk.Api("groups.getMembers",group_id=g,offset=0,count=1000,
			fields="nickname,bdate",
			name_case="nom")
	usrs=o.content['items']
	count=o.content['count']
	offset=0
	while(len(usrs)<0.9*count):
		offset+=1000
		time.sleep(0.4)
		try:
			o=vk.Api("groups.getMembers",group_id=g,offset=offset,count=1000,
				fields="nickname,bdate",
				name_case="nom")
			usrs+=o.content['items']
		except KeyError:
			time.sleep(60)
			offset-=1000
	return usrs

def getUsersByChat(g):
	o=vk.Api("messages.getConversationMembers",peer_id=g,offset=0,count=200,v="5.144",
			fields="nickname,bdate",
			name_case="nom")
	usrs=o.content['profiles']
	count=o.content['count']
	offset=0
	while(len(usrs)<0.9*count):
		offset+=200
		time.sleep(0.4)
		try:
			o=vk.Api("messages.getConversationMembers",peer_id=g,offset=offset,count=200,v="5.144",
				fields="nickname,bdate",
				name_case="nom")
			usrs+=o.content['profiles']
		except KeyError:
			time.sleep(60)
			offset-=200
		except NewConnectionError:
			time.sleep(60)
			offset-=200
	return usrs

print("Loading...")
sources=open(inp_fname,"r").readlines()

outfl=open(out_fname,"w", encoding="utf-8")

outjson=dict()

foundIds=[]

for source in sources:
	# preprocessing
	source=source.replace("\n","").replace("\r","")
	if(len(source)<3 or "#" in source[:2]): # This line is comment
		print(source)
		continue
	print("\rSource: "+source,end='')
	owner_id=None
	isUser=False
	if("/wall" in source):
		owner_id=source[source.index("/wall")+5:]
		if("_" in owner_id):
			owner_id=owner_id[:owner_id.index("_")]
		if("?" in owner_id):
			owner_id=owner_id[:owner_id.index("?")]
		isUser=not owner_id[0]=="-"
		owner_id=owner_id.replace("-","")
	else:
		if("/" in source):
			source=source[source.rindex("/")+1:]
		if("?" in source):
			source=source[:source.rindex("?")]
		owner_id,t=domain2ID(source)
		isUser=(t=='user')
		owner_id=str(owner_id)
	print("Found ID "+owner_id+"\tisUser: "+str(isUser),end='')
	# processing:
	users=None
	if(isUser):
		users=getUsersByUser(owner_id)
	else:
		users=getUsersByGroup(owner_id)
	time.sleep(0.3)
	for u in users:
		uid=u['id']
		if(uid in foundIds):continue
		foundIds.append(uid)
		name=u["first_name"]+" "+u["last_name"]
		if(not 'bdate' in u):
#			u['bdate']="02.02.1970" # STUB!
			continue # Пропуск пользователя без указания даты рождения, не записываем вообще
		if(u['bdate'].count(".")==1):
			continue # Пропуск пользователей, у которых только месяц и день рождения
		byear=int(u['bdate'].split(".")[-1])
		if(byear<1998 or byear>2004):
			continue # Пропуск по причине слишком молодой/слишком старый
		outfl.write(name+";"+str(uid)+";"+str(u['bdate'])+"\n")
		outjson[uid]=name
	print("\rOK                                                "+"  "*len(source),end='')

outfl.close()
json.dump(outjson, open(outjson_fname,"w"))
print("Done!")
