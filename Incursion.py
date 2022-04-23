from telegram.ext import (Updater , CommandHandler , MessageHandler ,
						 Filters  , InlineQueryHandler , CallbackQueryHandler)

from telegram import (InlineKeyboardMarkup , InlineKeyboardButton ,
					Bot,InlineQueryResultArticle  ,
					InputTextMessageContent , Bot)

from random import getrandbits , choice
import  datetime , time  , sqlite3 , pymysql

import pytz



	
def CREARBD ():
	
	con , cur = conn()
	
	cur.execute("CREATE TABLE IF NOT EXISTS go (id BIGINT , timestamp BIGINT,status INT )")
	con.commit()
	
	cur.execute("CREATE TABLE IF NOT EXISTS chanel (id BIGINT , message BIGINT)")
	con.commit()
	
	cur.execute("CREATE TABLE IF NOT EXISTS stat(id BIGINT PRIMARY KEY , fe INT , ff INT , oro INT , exp INT , orol INT , t1p INT , t2p INT , t3p INT , t4p INT , t5p INT , t1r INT , t2r INT , t3r INT , t4r INT , t5r INT , hamster INT , cheese INT , hay INT , corn INT , coke INT , Am INT , Di INT , At INT , Noc INT , pAm INT, pDi INT,pAt INT,pNoc INT , timestamp TEXT )")	
	con.commit()
	
	cur.execute("CREATE TABLE IF NOT EXISTS timezone (id BIGINT , timezone TEXT )")
	con.commit()	
	
	con.close()
	
	print("BD CREADA")



def inline (Update , context) :   
	query_id = Update.inline_query.id
	query = Update.inline_query.query

	if not query :
		return

	texto_inline = query
	resultados = list()			    	        

	if texto_inline[0] == "🛡" :
		
		cas1 = '🛡Defender🛡\n<a href="https://t.me/share/url?url=/use_p04">/use_p04</a>\n<a href="https://t.me/share/url?url=/use_p05">/use_p05</a>\n<a href="https://t.me/share/url?url=/use_p06">/use_p06</a>' + texto_inline.replace("🛡" , "\n")		
		
		cas11 = InlineQueryResultArticle(
			id=query_id, 
			title ='🛡Defender🛡' , 
			input_message_content = InputTextMessageContent(message_text=cas1,parse_mode='html') , 
			parse_mode='html',
			reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(text="🛡Defend" , url = "https://t.me/share/url?url=🛡Defend")] , [InlineKeyboardButton(text="🛡Defend" , url = "https://t.me/share/url?url=🛡Defend") ]    ]))			
		
		
		resultados.append(cas11)		
		context.bot.answer_inline_query(Update.inline_query.id , results = resultados)		
				
	elif texto_inline[0] == "🐉" :		
		cas1 = "⚔🐉" + texto_inline.replace("🐉" , "\n")		
		cas11 = InlineQueryResultArticle(id=query_id , title = cas1 , input_message_content = InputTextMessageContent(cas1) , reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(text="⚔🐉" , url = "https://t.me/share/url?url=🐉")] , [InlineKeyboardButton(text="🛡Defend" , url = "https://t.me/share/url?url=🛡Defend") ]    ]))			
		resultados.append(cas11)		
		context.bot.answer_inline_query(Update.inline_query.id , results = resultados)		
	
	
	elif texto_inline[0] == "🦈" :		
		cas1 = "⚔🦈" + texto_inline.replace("🦈" , "\n")
		cas11 = InlineQueryResultArticle(id= query_id , title = cas1 , input_message_content = InputTextMessageContent(cas1) , reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(text="⚔🦈" , url = "https://t.me/share/url?url=🦈")] , [InlineKeyboardButton(text="🛡Defend" , url = "https://t.me/share/url?url=🛡Defend") ]    ]))			
		resultados.append(cas11)
		context.bot.answer_inline_query(Update.inline_query.id , results = resultados)			
	
	elif texto_inline[0] == "🦌" :		
		cas1 = "⚔🦌" + texto_inline.replace("🦌" , "\n")		
		cas11 = InlineQueryResultArticle(id= query_id , title = cas1 , input_message_content = InputTextMessageContent(cas1) , reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(text="⚔🦌" , url = "https://t.me/share/url?url=🦌")] , [InlineKeyboardButton(text="🛡Defend" , url = "https://t.me/share/url?url=🛡Defend") ]    ]))			
		resultados.append(cas11)		
		context.bot.answer_inline_query(Update.inline_query.id , results = resultados)			
				
	
	elif texto_inline[0] == "🦅" :		
		cas1 = "⚔🦅" + texto_inline.replace("🦅" , "\n")
		cas11 = InlineQueryResultArticle(id=query_id , title = cas1 , input_message_content = InputTextMessageContent(cas1) , reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(text="⚔🦅" , url = "https://t.me/share/url?url=🦅")] , [InlineKeyboardButton(text="🛡Defend" , url = "https://t.me/share/url?url=🛡Defend") ]    ]))			
		resultados.append(cas11)		
		context.bot.answer_inline_query(Update.inline_query.id , results = resultados)								
	

	elif texto_inline[0] == "🥔" :		
		cas1 = "⚔🥔" + texto_inline.replace("🥔" , "\n")		
		cas11 = InlineQueryResultArticle(id=query_id , title = cas1 , input_message_content = InputTextMessageContent(cas1) , reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(text="⚔🥔" , url = "https://t.me/share/url?url=🥔")] , [InlineKeyboardButton(text="🛡Defend" , url = "https://t.me/share/url?url=🛡Defend") ]    ]))			
		resultados.append(cas11)
		context.bot.answer_inline_query(Update.inline_query.id , results = resultados)							
		
	elif texto_inline[0] == "🐺" :		
		cas1 = "⚔🐺" + texto_inline.replace("🐺" , "\n")		
		cas11 = InlineQueryResultArticle(id=query_id , title = cas1 , input_message_content = InputTextMessageContent(cas1) , reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(text="⚔🐺" , url = "https://t.me/share/url?url=🐺")] , [InlineKeyboardButton(text="🛡Defend" , url = "https://t.me/share/url?url=🛡Defend") ]    ]))			
		resultados.append(cas11)
		context.bot.answer_inline_query(Update.inline_query.id , results = resultados)					
	
	
	elif texto_inline[0] == "🌑" :		
		cas1 = "⚔🌑" + texto_inline.replace("🌑" , "\n")
		cas11 = InlineQueryResultArticle(id= query_id , title = cas1 , input_message_content = InputTextMessageContent(cas1) , reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(text="⚔🌑" , url = "https://t.me/share/url?url=🌑")] , [InlineKeyboardButton(text="🛡Defend" , url = "https://t.me/share/url?url=🛡Defend") ]    ]))	
		resultados.append(cas11)
		context.bot.answer_inline_query(Update.inline_query.id , results = resultados)				
	
	
	elif texto_inline == "t" :
		cas1 = "🎲Play some dice"
		cas2 = "🍺Have a pint"
		cas3 = "🕵️Talk with Stranger"	
	
		cas11 = InlineQueryResultArticle(id=hex(getrandbits(64))[2:] , title = cas1 , input_message_content = InputTextMessageContent(cas1))
		cas22 = InlineQueryResultArticle(id=hex(getrandbits(64))[2:] , title = cas2 , input_message_content = InputTextMessageContent(cas2))
		cas33 = InlineQueryResultArticle(id=hex(getrandbits(64))[2:] , title = cas3 , input_message_content = InputTextMessageContent(cas3))
	
		resultados.append(cas11)
		resultados.append(cas22)
		resultados.append(cas33)
		context.bot.answer_inline_query(Update.inline_query.id , results = resultados)
			
	
	
	elif texto_inline == "i" :
		
		cas1 = "📦Resources"
		cas2 = "⚒Crafting"
		cas3 = "🗃Misc"
		cas4 = "🏷Equipment"
		cas5 = "⚗️Alchemy"

		cas11 = InlineQueryResultArticle(id=hex(getrandbits(64))[2:] , title = cas1 , input_message_content = InputTextMessageContent(cas1))

		cas22 = InlineQueryResultArticle(id=hex(getrandbits(64))[2:] , title = cas2 , input_message_content = InputTextMessageContent(cas2))
		cas33 = InlineQueryResultArticle(id=hex(getrandbits(64))[2:] , title = cas3 , input_message_content = InputTextMessageContent(cas3))
		cas44 = InlineQueryResultArticle(id=hex(getrandbits(64))[2:] , title = cas4, input_message_content = InputTextMessageContent(cas4))

		cas55 = InlineQueryResultArticle(id=hex(getrandbits(64))[2:] , title = cas5 ,  input_message_content = InputTextMessageContent(cas5))
		


		resultados.append(cas11)
		resultados.append(cas22)
		resultados.append(cas33)
		resultados.append(cas44)
		resultados.append(cas55)
		context.bot.answer_inline_query(Update.inline_query.id , results = resultados)
		

	elif texto_inline == "s" :
		shop = "/myshop_open"
		shop1 = InlineQueryResultArticle(id=hex(getrandbits(64))[2:] , title = shop ,  input_message_content = InputTextMessageContent(shop))
		resultados.append(shop1)


		context.bot.answer_inline_query(Update.inline_query.id , results = resultados)

	elif texto_inline == "du" :
		du1 = "▶️Fast fight"
		du2 = "🔎Fight!"
		du3 = "🤺Challenge"

		du11 = InlineQueryResultArticle(id=hex(getrandbits(64))[2:] , title = du1 ,  input_message_content = InputTextMessageContent(du1))
		du22 = InlineQueryResultArticle(id=hex(getrandbits(64))[2:] , title = du2 ,  input_message_content = InputTextMessageContent(du2))

		du33 = InlineQueryResultArticle(id=hex(getrandbits(64))[2:] , title = du3 ,  input_message_content = InputTextMessageContent(du3))
		resultados.append(du11)
		resultados.append(du22)
		resultados.append(du33)
		context.bot.answer_inline_query(Update.inline_query.id , results = resultados)




	elif texto_inline == "c" :
		cas1 = "⚖Exchange"
		cas2 = "⚒Workbench"
		cas3 = "📖Recipes"
		cas4 = "🛎Auction"
		cas5 = "🏷Wrap"
		cas7 = "⚗️Laboratory"

		cas11 = InlineQueryResultArticle(id=hex(getrandbits(64))[2:] , title = cas1 , input_message_content = InputTextMessageContent(cas1))

		cas22 = InlineQueryResultArticle(id=hex(getrandbits(64))[2:] , title = cas2 , input_message_content = InputTextMessageContent(cas2))
		cas33 = InlineQueryResultArticle(id=hex(getrandbits(64))[2:] , title = cas3 , input_message_content = InputTextMessageContent(cas3))
		cas44 = InlineQueryResultArticle(id=hex(getrandbits(64))[2:] , title = cas4, input_message_content = InputTextMessageContent(cas4))

		cas55 = InlineQueryResultArticle(id=hex(getrandbits(64))[2:] , title = cas5 ,  input_message_content = InputTextMessageContent(cas5))
		#cas66 = InlineQueryResultArticle(id=hex(getrandbits(64))[2:] , title = cas6 , input_message_content = InputTextMessageContent(cas6))

		cas77 = InlineQueryResultArticle(id=hex(getrandbits(64))[2:] , title = cas7 , input_message_content = InputTextMessageContent(cas7))


		resultados.append(cas11)
		resultados.append(cas44)
		resultados.append(cas77)
		resultados.append(cas22)
		resultados.append(cas55)
		#resultados.append(cas66)
		resultados.append(cas33)
		
		context.bot.answer_inline_query(Update.inline_query.id , results = resultados)

	else:
		alt1 = '/g_withdraw ' + texto_inline
		alt2 = '/g_invite ' + texto_inline
		alt3 = '/g_kick ' + texto_inline		
		alt4 = '/g_atk ' + texto_inline		
		alt5 = '/g_def ' + texto_inline						
		alt6 = '/g_lobby ' + texto_inline				
		alt7 = '/g_stock ' + texto_inline										
		
		
		alt11 = InlineQueryResultArticle(id=hex(getrandbits(64))[2:],title= alt1,  input_message_content=InputTextMessageContent(alt1))		
		alt22 = InlineQueryResultArticle(id=hex(getrandbits(64))[2:],title=  alt2,        input_message_content=InputTextMessageContent(alt2))	
		alt33 = InlineQueryResultArticle(id=hex(getrandbits(64))[2:],title= alt3,       input_message_content=InputTextMessageContent(alt3))
		alt44 = InlineQueryResultArticle(id=hex(getrandbits(64))[2:],title= alt4,       input_message_content=InputTextMessageContent(alt4))
		alt55 = InlineQueryResultArticle(id=hex(getrandbits(64))[2:],title= alt5,       input_message_content=InputTextMessageContent(alt5))
		alt66 = InlineQueryResultArticle(id=hex(getrandbits(64))[2:],title= alt6,       input_message_content=InputTextMessageContent(alt6))				
		alt77 = InlineQueryResultArticle(id=hex(getrandbits(64))[2:],title= alt7,       input_message_content=InputTextMessageContent(alt7))
				
		resultados.append(alt11)
		resultados.append(alt77)
		resultados.append(alt22)
		resultados.append(alt33)
		resultados.append(alt44)
		resultados.append(alt55)
		resultados.append(alt66)
								
		context.bot.answer_inline_query(Update.inline_query.id, results=resultados)
	

def start (Update , context):
	
	if Update.effective_chat.id >0:
			
		name = Update.effective_user.first_name
		
		Update.message.reply_text(
			text=f'Bienvenido <b>{name}</b> reenvíe las 2 '
				  'intervensiones más recientes desde <b><a href="https://t.me/chtwrsbot">Chat Wars</a></b> '
				  'y de paso te invito a unirte a nuestro canal <b><a href="https://t.me/forknight">For Knight</a></b>',					
			parse_mode="html",
			disable_web_page_preview=True,
			reply_markup=InlineKeyboardMarkup([
			[InlineKeyboardButton(text='🏖Atajos',callback_data='atajos'),
			InlineKeyboardButton(text="ℹ️",callback_data="look_info")]
			]))
	
def SAVE_INFO (Update,context):
	
	user_id = Update.effective_user.id		
	timestamp =datetime.datetime.timestamp(Update.message.forward_date)
	text = Update.message.text
	
	if 'We hope you feel terrible.' in text:
		status = 0
	else :
		status = 1
		
	con , cur = conn()
	cur.execute(f"SELECT * FROM go WHERE id={user_id} AND timestamp={timestamp}")   
	
	if cur.fetchone() == None:

		cur.execute(f"INSERT INTO go (id,timestamp,status)VALUES({user_id},{timestamp},{status})")
		con.commit()		
		cur.execute(f"SELECT * FROM go WHERE id ={user_id}")			
			
		if len(cur.fetchall()) <= 1:
			Update.message.reply_text("Envíame otro mensaje para calcular la diferencia de horas.")
							

		else :
			
			cur.execute(f"SELECT timestamp FROM go WHERE id={user_id}")							
			tiempos = cur.fetchall()				
			tiempos.sort(key=lambda tiempos:tiempos[0] , reverse = True)
			
			cur.execute(f"SELECT timezone FROM timezone WHERE id={user_id}")
			try :
				tzn = cur.fetchone()[0]
			except :
				tzn = "etc/GMT+5"
			
			
			tz = pytz.timezone(tzn)			
			
			
			t1 = datetime.datetime.fromtimestamp(tiempos[0][0],tz=tz)
			t2 = datetime.datetime.fromtimestamp(tiempos[1][0],tz=tz)
			
			tforay = datetime.datetime.fromtimestamp(timestamp,tz=tz)
			
			tactual = datetime.datetime.now(tz=tz)
			tlimite = tactual - datetime.timedelta(hours=72)
			
			
							
			tf = t1 - t2
			
			
			if t1 > tforay :
				
				hp = t1 - tforay
			
			elif t1 == tforay:
				
				hp = tf
							
			segundos = tf.total_seconds()
			horas=int(segundos/3600)
			segundos-=horas*3600
			minutos=int(segundos/60)	
			
			lista = ['🍌','🍑','🥑','🐍','🧀','🍕','🍼','🍻','🥕','❄','✈','💎','⚱','🐣','💰','🎭','🦄','🍀','🌈','🦠','🚀','🦊','☀','☂','🕊','🏰']
			emoji = choice(lista)
			
			texto_go = (f"{emoji}<b>Nuevo Intervalo</b>\n\nDiferencia del anterior /go: <b>{horas}</b> horas , <b>{minutos}</b> minutos")	
			


			if tf == hp and  t1 >= tlimite :
				Update.message.reply_text(
					text=texto_go,
					parse_mode="html")
			else :
				Update.message.reply_text(
					text='/go <b>Guardado</b>',
					parse_mode='html')
					
				
				
			if tf==hp and t1 >= tlimite and 60 > horas > 36:
				SENDER_CHANNEL (Update,context,texto_go)
				
					
			if len(tiempos) > 7 :
			    cur.execute(f"DELETE FROM go WHERE id={user_id} AND timestamp={tiempos[-1][0]}")
			    con.commit()		
		
	else :
		Update.message.reply_text(
            text="Ya ha sido <b>guardado</b>",
			parse_mode="html")
			
	con.close()

def SENDER_CHANNEL(Update,context,texto_go):
				
	sms = context.bot.send_message(
		chat_id=-1001310125115,
		#chat_id=-1001529634997,
		text=texto_go,
		parse_mode='html')
				
	message_id=sms.message_id
	chanel_id=sms.sender_chat.id
	
	con , cur = conn()
	cur.execute(f"INSERT INTO chanel(id,message)VALUES({chanel_id},{message_id})")
	con.commit()
	
	cur.execute(f"SELECT * FROM chanel")
	info = cur.fetchall()
	
	if len(info) > 15 :
		info.sort(key=lambda info:info[1] , reverse = True)
		sms = info[-1]
		
		try :			
			context.bot.delete_message(chat_id=sms[0],message_id=sms[1])				
		except Exception as Error:
			context.bot.send_message(chat_id=1190666125,text=f"{Error} :{sms[1]}")
					
			
		cur.execute(f"DELETE FROM chanel WHERE message={sms[1]}")
		con.commit()
		

	con.close()

def intervine (Update,context):
	
	if Update.effective_chat.id > 0:
				
	    con , cur = conn()
		
	    user_id = Update.effective_user.id	
		
	    cur.execute(f"SELECT timestamp FROM go WHERE id={user_id}")
	    tiempos = cur.fetchall()
	    if len(tiempos) > 1:
			
		    tiempos.sort(key=lambda tiempos:tiempos[0] , reverse = True)
		    
		    cur.execute(f"SELECT timezone FROM timezone WHERE id={user_id}")
		    try :
		    	tzn = cur.fetchone()[0]
		    except :
		    	tzn = "etc/GMT+5"
		    con.close()

		    tz = pytz.timezone(tzn)
			
		    t1 = datetime.datetime.fromtimestamp(tiempos[0][0],tz=tz)
		    t2 = datetime.datetime.fromtimestamp(tiempos[1][0],tz=tz)
		    t3 = datetime.datetime.now(tz=tz)
			
		    tf = t3 - t1
			
		    segundos = tf.total_seconds()
		    horas=int(segundos/3600)
		    segundos-=horas*3600
		    minutos=int(segundos/60)
			
			#Prox
			
		    tp = t1 - t2
		    fp = tp + t1
		    
		    dp = fp.strftime("<b>%d/%m a las %I:%M %p</b>")
		    		    
		    
		    segundosp = tp.total_seconds()
		    horasp=int(segundosp/3600)
		    segundosp-=horasp*3600
		    minutosp=int(segundosp/60)	
			
			
		    Update.message.reply_text(
				text=f"Tiempo pasado desde la última incursión <b>{horas}</b> horas y <b>{minutos}</b> minutos.\n\n"
					 f"Próxima incursión estimada para el {dp}\n\n"
					 f"Intervalo reciente <b>{horasp}</b> horas , <b>{minutosp}</b> minutos\n\nZona Horaria {tzn[4:]}"
					 ,
				parse_mode="html",
				reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="🔔 Canal",url="https://t.me/forknight")]]))
						
	    else :
	    	start(Update,context)
	
def go (Update,context):
	
	if Update.effective_chat.id > 0 :
		
		con , cur = conn()
		
		user_id = Update.message.from_user.id	
		
		cur.execute(f"SELECT timestamp , status FROM go WHERE id={user_id}")
		tiempos = cur.fetchall()
		
		if tiempos != []:
			
			tiempos.sort(key=lambda tiempos:tiempos[0] , reverse = True)
			
			cur.execute(f"SELECT timezone FROM timezone WHERE id={user_id}")
			try :
				tzn = cur.fetchone()[0]
				#print(tzn)
			except :
				tzn = "etc/GMT+5"
				
			con.close()
				
			tz = pytz.timezone(tzn)
			
			
			tl = []
			n = 1
			for t in tiempos :
				xt = datetime.datetime.fromtimestamp(t[0],tz=tz)				
				status = t[1]
				if status == 0 :
					emoj = '🔥'
				elif status == 1 :
					emoj = '🛡'
				else :
					emoj = '❔'
				tl.append(f'{xt.strftime("%I : %M  %p %d/%m/%Y ")} {emoj} #{n}')
				n += 1
				
			tl = "\n".join(tl)
			Update.message.reply_text(
				text=f"🧹Tiempos registrados de tus últimos /go:\n\n{tl}\n\nZona Horaria {tzn[4:]}\n\n/intervine")
	
		else :
			start(Update,context)	
	
def MENSAJE (Update,context):
	
	text = Update.message.text[9:]	
	con , cur = conn()
		
	cur.execute(f"SELECT id FROM go")
	info = cur.fetchall()
	users = set(info)
	Update.message.reply_text(f'Usuarios Registrados : {len(users)}')
	
	for i in users :
		try :
			bot.send_message(chat_id=i[0],text=text)
			time.sleep(5)
		except :
			pass

def RESTORE_CH(Update,context):
	
	con , cur = conn()
	cur.execute("DELETE FROM chanel")
	con.commit()
	con.close()
	Update.message.reply_text("ok")	

def porcen(p,t):
	
	try :
		por = 100 * ( p / t )
	except ZeroDivisionError :
		por = 0
	return round(por,1)


		

def conn ():		
	con = pymysql.connect(
		host='containers-us-west-42.railway.app',
		user='root',
		password='qzNJ5WZvOxsZK8Pm8g7d',
		db='railway'
	)
	print("se conectooooooo")
				
	cur = con.cursor()	
	return con , cur
	
def SAVE_STAT_FORAY_SUCCES(Update,context):
	
	text = Update.message.text.splitlines()
	
	id = Update.effective_user.id
	
	#Foray
	fe = 1
	
	oro = int(text[1][9:text[1].find(' gold')])
	
	exp = int(text[1][text[1].find('and ')+4:text[1].find(' exp.')])
	
	if len(text) == 3 :
		
		obj = text[2][8:]
		
		#Coke
		if 'Coke' in obj :
			coke = 1
		elif 'Coke' not in obj :
			coke = 0
		#Corn
		if 'Corn' in obj :
			corn = 1
		elif 'Corn' not in obj :
			corn = 0
		#Hay
		if 'Hay' in obj :
			hay = 1
		elif 'Hay' not in obj :
			hay = 0
		#Hamsters
		if 'Hamsters' in obj :
			hamsters = 1
		elif 'Hamsters' not in obj :
			hamsters = 0						
		#Cheese
		if 'Cheese' in obj :
			cheese = 1
		elif 'Cheese' not in obj :
			cheese = 0
			
		#Scrolls
		#t1
		if '📕' in obj :
			if 'Peace' in obj :
				t1r = 0
				t1p = 1
			elif 'Rage' in obj:
				t1r = 1
				t1p = 0		
		elif '📕' not in obj:
			t1r = 0
			t1p = 0
								
		#t2
		if '📗' in obj :
			if 'Peace' in obj :
				t2r = 0
				t2p = 1
			elif 'Rage' in obj:
				t2r = 1
				t2p = 0		
		elif '📗' not in obj:
			t2r = 0
			t2p = 0				
	
		#t3
		if '📘' in obj :
			if 'Peace' in obj :
				t3r = 0
				t3p = 1
			elif 'Rage' in obj:
				t3r = 1
				t3p = 0		
		elif '📘' not in obj:
			t3r = 0
			t3p = 0		
		#t4
		if '📙' in obj :
			if 'Peace' in obj :
				t4r = 0
				t4p = 1
			elif 'Rage' in obj:
				t4r = 1
				t4p = 0		
		elif '📙' not in obj:
			t4r = 0
			t4p = 0	
		
		#t5
		if '📒' in obj :
			if 'Peace' in obj :
				t5r = 0
				t5p = 1
			elif 'Rage' in obj:
				t5r = 1
				t5p = 0		
		elif '📒' not in obj:
			t5r = 0
			t5p = 0	
		
	
	
	elif len(text) == 2 :
		
		coke = 0
		corn = 0
		hay = 0
		hamsters = 0
		cheese = 0
		t1r = 0
		t1p = 0
		t2r = 0
		t2p = 0
		t3r = 0
		t3p = 0
		t4r = 0
		t4p = 0
		t5r = 0
		t5p = 0
		
	
	con , cur = conn()	
	cur.execute(f"SELECT timezone FROM timezone WHERE id={Update.effective_user.id}")
	try :
		tzn = cur.fetchone()[0]
		#print(tzn)
	except :
		tzn = "etc/GMT+5"
								
	tz = pytz.timezone(tzn)
					
	
	
	
	timestamp = datetime.datetime.timestamp(Update.message.forward_date)
	date = datetime.datetime.fromtimestamp(timestamp,tz=tz)
	hora = int(date.strftime('%H'))
	
	if hora == 0 :
		hora = 24
	

	if 2 <= hora < 4 or 10 <= hora < 12 or 18 <= hora < 20 :
		Am = 1
		Di = 0
		At = 0
		Noc= 0	
	
	elif 4 <= hora < 6 or 12 <= hora < 14 or 20 <= hora < 22 :
		Am = 0
		Di = 1
		At = 0
		Noc= 0				
	
	elif 6 <= hora < 8 or 14 <= hora < 16 or 22 <= hora < 24 :
		Am = 0
		Di = 0
		At = 1
		Noc= 0		
	
	else :
		Am = 0
		Di = 0
		At = 0
		Noc= 1
		
	cur.execute(f"SELECT * FROM stat WHERE id={id}")
	datos = cur.fetchall()
	
	if len(datos) == 0 :
		cur.execute(f"INSERT INTO stat (id,fe,ff,oro,exp,orol,t1p,t2p,t3p,t4p,t5p,t1r,t2r,t3r,t4r,t5r,hamster,cheese,hay,corn,coke,Am,Di,At,Noc,pAm,pDi,pAt,pNoc,timestamp)VALUES({id},0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'inicio')")
		con.commit()
	
	
	cur.execute(f"SELECT timestamp FROM stat WHERE id={id}")
	info = cur.fetchone()
	
	if f"{timestamp}" not in info[0].split():
	
		
		cur.execute(f"SELECT * FROM stat WHERE id={id}")
		info = cur.fetchone()
		
		bfe  = info[1] + fe
		boro = info[3] + oro
		bexp = info[4] + exp
		#scroll
		bt1p = info[6] + t1p
		bt2p = info[7] + t2p
		bt3p = info[8] + t3p
		bt4p = info[9] + t4p
		bt5p = info[10]+ t5p
		bt1r = info[11]+ t1r
		bt2r = info[12]+ t2r
		bt3r = info[13]+ t3r
		bt4r = info[14]+ t4r
		bt5r = info[15]+ t5r
		#comida y etc
		bh   = info[16]+ hamsters
		bc   = info[17]+ cheese
		bha  = info[18]+ hay
		bco  = info[19]+ corn
		bcok = info[20]+ coke
		#tiempo
		bam  = info[21]+ Am
		bd   = info[22]+ Di
		bat  = info[23]+ At
		bn   = info[24]+ Noc
		tmp  = info[29] + f" {timestamp}"
		
		cur.execute(
			f"UPDATE stat SET fe={bfe} , oro={boro} , exp={bexp},"
			f"t1p={bt1p},t2p={bt2p},t3p={bt3p},t4p={bt4p},t5p={bt5p},"
			f"t1r={bt1r},t2r={bt2r},t3r={bt3r},t4r={bt4r},t5r={bt5r},"
			f"hamster={bh},cheese={bc},hay={bha},corn={bco},coke={bcok},"
			f"Am={bam},Di={bd},At={bat},Noc={bn},timestamp='{tmp}' WHERE id ={id}"						
			)
		
		con.commit()
		con.close()
		
		Update.message.reply_text("OK")
	
	elif f"{timestamp}" in info[0].split():
		Update.message.reply_text("Ya ha sido <b>guardado</b>",'html')
		con.close()

def SAVE_STAT_FORAY_FAIL (Update,context):
	
	text = Update.message.text.splitlines()
	id = Update.effective_user.id
	
	if len(text)==2:
		orol = int(text[1][7:text[1].find(" gold")])
	elif len(text)==1:
		orol = 0
	
	ff = 1
				
	con , cur = conn()	
	cur.execute(f"SELECT timezone FROM timezone WHERE id={Update.effective_user.id}")
	try :
		tzn = cur.fetchone()[0]
		#print(tzn)
	except :
		tzn = "etc/GMT+5"
								
	tz = pytz.timezone(tzn)
		
	
	
	timestamp = datetime.datetime.timestamp(Update.message.forward_date)
	date = datetime.datetime.fromtimestamp(timestamp,tz=tz)
	hora = int(date.strftime('%H'))
	
	if hora == 0 :
		hora = 24
	

	if 2 <= hora < 4 or 10 <= hora < 12 or 18 <= hora < 20 :
		Am = 1
		Di = 0
		At = 0
		Noc= 0	
	
	elif 4 <= hora < 6 or 12 <= hora < 14 or 20 <= hora < 22 :
		Am = 0
		Di = 1
		At = 0
		Noc= 0				
	
	elif 6 <= hora < 8 or 14 <= hora < 16 or 22 <= hora < 24 :
		Am = 0
		Di = 0
		At = 1
		Noc= 0		
	
	else :
		Am = 0
		Di = 0
		At = 0
		Noc= 1			
		
	cur.execute(f"SELECT * FROM stat WHERE id={id}")
	datos = cur.fetchall()
	
	if len(datos) == 0 :
		cur.execute(f"INSERT INTO stat (id,fe,ff,oro,exp,orol,t1p,t2p,t3p,t4p,t5p,t1r,t2r,t3r,t4r,t5r,hamster,cheese,hay,corn,coke,Am,Di,At,Noc,pAm,pDi,pAt,pNoc)VALUES({id},0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)")
		con.commit()				

	
	cur.execute(f"SELECT timestamp FROM stat WHERE id={id}")
	info = cur.fetchone()
	
	if f"{timestamp}" not in info[0].split():		
		
		cur.execute(f"SELECT * FROM stat WHERE id={id}")
		info = cur.fetchone()
		
		bff  = info[2] + ff
		boro = info[5] + orol
		bpAm = info[25]+ Am
		bpDi = info[26]+ Di
		bpAt = info[27]+ At
		bpNoc= info[28]+ Noc
		tmp  = info[29]+ f" {timestamp}"
			
		
		
		cur.execute(f"UPDATE stat SET ff={bff},orol={boro},pAm={bpAm},pDi={bpDi},pAt={bpAt},pNoc={bpNoc},timestamp='{tmp}' WHERE id={id}")
		con.commit()
		con.close()
		
		Update.message.reply_text("OK")	
	
	elif f"{timestamp}" in info[0].split():
		Update.message.reply_text("Ya ha sido <b>guardado</b>",'html')
		con.close()
	

def SHOW_STAT(Update,context):
	
	id = Update.effective_user.id

	con , cur = conn()
	cur.execute(f"SELECT * FROM stat WHERE id={id}")
	info = cur.fetchone()
	if info != None :
	
		fe  = info[1]
		ff  = info[2] 
		oro = info[3] 
		exp = info[4]
		orol = info[5] 
		#scroll
		t1p = info[6] 
		t2p = info[7] 
		t3p = info[8] 
		t4p = info[9] 
		t5p = info[10]
		t1r = info[11]
		t2r = info[12]
		t3r = info[13]
		t4r = info[14]
		t5r = info[15]
		#comida y etc
		hamster = info[16]
		cheese  = info[17]
		hay     = info[18]
		corn    = info[19]
		coke    = info[20]
		#tiempo
		Am  = info[21]
		Di  = info[22]
		At  = info[23]
		Noc = info[24]
		fAm = info[25]
		fDi = info[26]
		fAt = info[27]
		fNoc= info[28]		
		
		pe = porcen(fe,(fe+ff))
		pf = porcen(ff,(fe+ff))
		
		pAm = porcen(Am,(Am+fAm))
		pDi = porcen(Di,(Di+fDi))
		pAt = porcen(At,(At+fAt))
		pNoc = porcen(Noc,(Noc+fNoc))
		
		sms = f"<i>Total de incursiones {fe+ff}</i>\n\n"\
			  f"<i>{pe}% 😈Exitosas {fe}</i>\n"\
			  f"<i>Oro {oro}💰</i>\n"\
			  f"<i>Exp {exp}🔥</i>\n\n"\
			  f"<i>{pf}% 🤕Fracasadas {ff}</i>\n"\
			  f"<i>Oro -{orol}💰</i>\n\n"\
			  f"<i>{hamster} - 🐹Hamsters</i>\n"\
			  f"<i>{cheese} - 🧀 Cheese</i>\n"\
			  f"<i>{corn} - 🌽 Corn</i>\n"\
			  f"<i>{coke} - 🌿Coke</i>\n"\
			  f"<i>{hay} - 🌾Hay</i>\n\n"\
			  f"<code>📚    🧘Peace    😡Rage  \n"\
			  f"📕        {t1p}        {t1r}\n"\
			  f"📗        {t2p}        {t2r}\n"\
			  f"📘        {t3p}        {t3r}\n"\
			  f"📙        {t4p}        {t4r}\n"\
			  f"📒        {t5p}        {t5r}</code>\n\n"\
			  f"<i>Effectividad por horario /luck</i>\n"\
			  f"<i>🌄 Amanecer {pAm}%</i>\n"\
			  f"<i>🏙 Día {pDi}%</i>\n"\
			  f"<i>🌇 Atardecer {pAt}%</i>\n"\
			  f"<i>🌃 Noche {pNoc}%</i>"		
		
		Update.message.reply_text(sms,"html")		
	
	else :
		Update.message.reply_text("No hay datos.")
	con.close()

def ATAJOS (Update,context):
	query = Update.callback_query
	
	query.edit_message_text(
		text='<b>Atajos enviar a @chtwrsbot</b>\ni , c , s , t , du\n<b>Wars enviar a grupo o canal</b>\n🛡,🐺 ,🦌,🦈, 🌑, 🐉,🦅,🥔',
		parse_mode='html',
		reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Ir a 🏰CW",switch_inline_query='du')]]))

def LUCK (Update,context):
	con , cur = conn()	
	cur.execute("SELECT Am , Di , At , Noc , pAm , pDi , pAt , pNoc FROM stat")
	info = cur.fetchall()	
	con.close()

	Am = []
	Di = []
	At = []
	Noc =[]
	pAm =[]
	pDi =[]
	pAt =[]
	pNoc =[]
	
	for i in info :
		Am.append(i[0])
		Di.append(i[1])
		At.append(i[2])
		Noc.append(i[3])
		pAm.append(i[4])
		pDi.append(i[5])
		pAt.append(i[6])
		pNoc.append(i[7])
		
	Am = sum(Am)
	Di = sum(Di)
	At = sum(At)
	Noc =sum(Noc)
	
	pAm =sum(pAm)
	pDi =sum(pDi)
	pAt =sum(pAt)
	pNoc =sum(pNoc)
	
	eAm= str(porcen (Am,(Am+pAm))) + "%"
	eDi= str(porcen (Di,(Di+pDi))) + "%"
	eAt= str(porcen (At,(At+pAt))) + "%"
	eNoc=str(porcen (Noc,(Noc+pNoc)))+"%"
	
	Update.message.reply_text(
		text="<i>Effectividad por horario</i>\n"
			 f"<i>🌄 Amanecer {eAm}</i>\n"
			 f"<i>🏙 Día {eDi}</i>\n"
			 f"<i>🌇 Atardecer {eAt}</i>\n"
			 f"<i>🌃 Noche {eNoc}</i>",
		parse_mode="html")


def set_timezone(Update , context):
	
	text = Update.message.text[10:]
	mensaje = "Para cambiar la zona horaria envíe el comando <code>/timezone +5</code> para "\
			  " establecer en <b>GMT+5</b>"
	try :
		if text[0]=="+" or text[0]=="-":
			
			signo = text[0]
			
			try :
				n = int(text[1:])
				if n <= 14 :
						
					btn = InlineKeyboardButton(text="✅Establecer",callback_data="timezone")
				
					Update.message.reply_text(
						text=f"Establecer Zona Horaria a <b>GMT{signo}{n}</b>",
						parse_mode="html",
						reply_markup=
							InlineKeyboardMarkup([[btn]]))
				elif n > 14 :
					Update.message.reply_text("El <b>rango permitido</b> es desde -14 hasta +14","html")			
			
			except :
				Update.message.reply_sticker("CAACAgIAAxkBAAIydmIqqBLgpaEesoh8cqZBq0A3B5uSAAIcDQACE4LASRiIytfduu32IwQ")
				Update.message.reply_text(mensaje,"html")
						
		
	except :
		Update.message.reply_sticker("CAACAgIAAxkBAAIydmIqqBLgpaEesoh8cqZBq0A3B5uSAAIcDQACE4LASRiIytfduu32IwQ")
		Update.message.reply_text(mensaje,"html")

def TIMEZ (Update,context):
	
	text = Update.callback_query.message.text[26:]
	query = Update.callback_query
	
	user_id = Update.effective_user.id
	tz = f"etc/{text}"
	
	con , cur = conn()
	
	cur.execute(f"SELECT * FROM timezone WHERE id={user_id}")
	info = cur.fetchall()
	if len(info) < 1:
		cur.execute(f"INSERT INTO timezone(id,timezone)VALUES({user_id},'{tz}')")
		con.commit()
		con.close()
		
		query.edit_message_text(f"Tu Zona Horaria cambió a <b>{text}</b>","html")
	else :
		cur.execute(f"UPDATE timezone SET timezone='{tz}' WHERE id={user_id}")
		con.commit()
		con.close()
		
		query.edit_message_text(f"Tu Zona Horaria cambió a <b>{text}</b>","html")



def LOOK_INFO(Update,context):
	
	
	query = Update.callback_query
	
	query.edit_message_text(
		text=f"<b>Creado por <a href='https://t.me/RaulCobiellas'>Raúl</a></b>"\
			  "\n\n¿Quieres ayudar a mantener el bot?"
			  "\n\n<b>BANDEC</b>:\n<code>9227 0699 9322 0782</code>\n"
			  "<b>Tron (trx)</b>:\n<code>TLypMUacELJJPDaTT1RTeCrgMkWE5eGwqD</code>\n"
			  "<b>Tether (trc20)</b>:\n<code>TLypMUacELJJPDaTT1RTeCrgMkWE5eGwqD</code>"		
		,
		parse_mode="html",
		disable_web_page_preview=True)





if __name__ == '__main__':
	
	CREARBD()	
	TOKEN ='2012546692:AAGawgNRfkSOofpMczhIHr6w0xWRBLTUHqE'
	bot = Bot(TOKEN)
	updater = Updater(TOKEN)	
	update = Updater	
	dp = updater.dispatcher

	dp.add_handler(CommandHandler('start' , start))
	dp.add_handler(CommandHandler('intervine', intervine))
	dp.add_handler(CommandHandler('go' , go))	
	dp.add_handler(CommandHandler('stat' , SHOW_STAT))
	dp.add_handler(CommandHandler('luck',LUCK))
	dp.add_handler(CommandHandler('timezone',set_timezone))
		
	dp.add_handler(CallbackQueryHandler(pattern='atajos',callback=ATAJOS))	
	dp.add_handler(CallbackQueryHandler(pattern='timezone',callback=TIMEZ))	
	dp.add_handler(CallbackQueryHandler(pattern='look_info',callback=LOOK_INFO))	


	dp.add_handler(MessageHandler(Filters.chat_type.private & Filters.forwarded_from(408101137) & Filters.regex("We hope you feel terrible.|You tried stopping|You successfully defeated") , SAVE_INFO ))
	dp.add_handler(MessageHandler(Filters.chat_type.private & Filters.forwarded_from(408101137) & Filters.regex("was completely clueless.") , SAVE_STAT_FORAY_SUCCES ))
	dp.add_handler(MessageHandler(Filters.chat_type.private & Filters.forwarded_from(408101137) & Filters.regex("noticed you and nearly beat you to death.") , SAVE_STAT_FORAY_FAIL ))
				
	#enviar mensaje masivo
	dp.add_handler(MessageHandler(Filters.user(1190666125) & Filters.regex('/mensaje') & Filters.chat_type.private,MENSAJE))	
	#BORRAR DATOS DE LA TABLA chanel
	dp.add_handler(MessageHandler(Filters.user(1190666125) & Filters.regex('^/restore_ch$') & Filters.chat_type.private,RESTORE_CH))		
	
	dp.add_handler(InlineQueryHandler(inline))
	updater.start_polling()
	print("running")
	updater.idle()    
